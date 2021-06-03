from modules.universalFunctions import *
from modules.settingsWrapper import *
from genericpath import exists, getsize
from requests import post, Session, get
from urllib.request import urlopen, urlretrieve
from lxml.html import fromstring
from time import sleep
from pandas.core.common import flatten
import arcpy
from os import path, mkdir, walk, rename, remove
from datetime import datetime
from shutil import move, make_archive, rmtree, unpack_archive
from json import dumps, loads, load, dump


class CatalogueDataUpdate:
    def __init__(self, settingsClass, geoprocessingFunction):
        self.name = settingsClass.name
        self.dataCatalogueId = settingsClass.dataCatalogueId
        self.fileName = settingsClass.fileName
        self.downloadFolder = settingsClass.downloadFolder
        self.archiveFolder = settingsClass.archiveFolder
        self.currentPath = settingsClass.currentPath
        self.jsonPayload = settingsClass.jsonPayload
        self.geoprocessingFunction = geoprocessingFunction

    def archiving(self):
        """ Takes the path of a shape file, and archives all files in that shapefile into the given archive folder. If path is gdb feature class, archives that whole GDB"""
        try:
            currentPathType = arcpy.Describe(self.currentPath).dataType

            if currentPathType == "ShapeFile":
                folderPath, shapefileNameWithExtension = path.split(self.currentPath)
                shapefileNameWithoutExtension = path.splitext(
                    shapefileNameWithExtension
                )[0]

                # get date modified timestamp from tenures.shp
                tenuresModifiedTime = getFileCreatedDate(self.currentPath)

                # make a new directory in the name of the Shapefile with time added in archive folder
                newDirectoryPath = f"{self.archiveFolder}\\{shapefileNameWithoutExtension}{tenuresModifiedTime}"
                mkdir(newDirectoryPath)

                #TODO: couuld we use arcpy to really simplify this section??

                # iterate through current .shp directory, pull out files with the name of the shapefile, add the time to thoes file names, move the file to previously created directory
                count = 1
                for _, _, files in walk(folderPath):

                    numberofFiles = len(files)
                    for fileNameWExtension in files:
                        filename, extension = path.splitext(fileNameWExtension)
                        if filename == shapefileNameWithoutExtension:
                            rename(
                                path.join(folderPath, fileNameWExtension),
                                path.join(
                                    folderPath,
                                    f"{filename}{tenuresModifiedTime}{extension}",
                                ),
                            )
                            move(
                                f"{folderPath}\\{filename}{tenuresModifiedTime}{extension}",
                                f"{newDirectoryPath}\\{filename}{tenuresModifiedTime}{extension}",
                            )
                        count += 1

                    if count > numberofFiles:
                        break

                # make a .zip of the shapefile directory in detectory folder
                make_archive(newDirectoryPath, "zip", newDirectoryPath)

                # remove non zipped data
                rmtree(newDirectoryPath)

                self.archivedFile = f"{newDirectoryPath}"

            # NOTE, this needs to be refined
            elif currentPathType == "FeatureClass":
                currentGDB, fileName = (
                    path.split(self.currentPath)[0],
                    path.split(self.currentPath)[1],
                )
                make_archive(
                    f"{self.archiveFolder}\\{fileName}{getFileCreatedDate(self.currentPath)}",
                    "zip",
                    currentGDB,
                )
                arcpy.Delete_management(currentGDB)

            else:
                print("File not Recognizable type")

            print("Done Archiving!")

        except:
            print("Cannot archive, check file")
            self.archiveStatus = False

    def catalogueWarehouseDownload(self):
        """requests link to download raw download from data catalogue warehouse, and downloads and unzips file from that link"""

        with Session() as s:
            # instantiate session with BC data catalogue, save important cookies in variable
            s.get(
                "https://apps.gov.bc.ca/pub/dwds-ofi/jsp/dwds_pow_current_order.jsp?publicUrl=https%3A%2F%2Fapps.gov.bc.ca%2Fpub%2Fdwds-ofi%2Fpublic%2F&secureUrl=https%3A%2F%2Fapps.gov.bc.ca%2Fpub%2Fdwds-ofi%2Fsecure%2F&customAoiUrl=http%3A%2F%2Fmaps.gov.bc.ca%2Fess%2Fhm%2Faoi%2F&pastOrdersNbr=5&secureSite=false&orderSource=bcdc"
            )
            jsession = s.cookies.get_dict()["JSESSIONID"]
            cookie2 = s.cookies.get_dict()["4a63ae55e0a822631a47a8e865d4afa6"]

            # cookies sent to data catalogue for shapefile link request
            cookies = {
                "JSESSIONID": jsession,
                "_ga": "GA1.3.990723064.1619392484",
                "_gid": "GA1.3.847311570.1619392484",
                "4a63ae55e0a822631a47a8e865d4afa6": cookie2,
                "WT_FPC": "id=239981ddcf51d1babb01619389913272:lv=1619486491386:ss=1619485433432",
            }

            # headers sent to BC data catalogue for shapefile link request
            headers = {
                "Connection": "keep-alive",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache",
                "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                "Accept": "application/json",
                "X-Requested-With": "XMLHttpRequest",
                "sec-ch-ua-mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
                "Content-Type": "application/json",
                "Origin": "https://apps.gov.bc.ca",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://apps.gov.bc.ca/pub/dwds-ofi/jsp/dwds_pow_current_order.jsp?publicUrl=https%3A%2F%2Fapps.gov.bc.ca%2Fpub%2Fdwds-ofi%2Fpublic%2F&secureUrl=https%3A%2F%2Fapps.gov.bc.ca%2Fpub%2Fdwds-ofi%2Fsecure%2F&customAoiUrl=http%3A%2F%2Fmaps.gov.bc.ca%2Fess%2Fhm%2Faoi%2F&pastOrdersNbr=5&secureSite=false&orderSource=bcdc",
                "Accept-Language": "en-US,en;q=0.9",
            }

            # Send request
            print("sending request")
            response = post(
                "https://apps.gov.bc.ca/pub/dwds-ofi/public/order/createOrderFiltered/",
                headers=headers,
                cookies=cookies,
                json=self.jsonPayload,
            )

        # Check distribution.data.gov.bc.ca Every 15 seconds to see if order is available, Storre download link in variable when ready.

        # NOTE: this Folloowing section is the most fragile piece of the whole software. If anything about the way the BC data catalogue operates changes, thiis function is likely to go down And break every data catalogue download. If there are problems with the download, this is the likely culprit.
        orderNumber = response.json()["Value"]
        orderURL = f"https://apps.gov.bc.ca/pub/dwds-rasp/pickup/{orderNumber}"

        stopLoop = False

        while stopLoop == False:
            sleep(15)
            print("checking...")
            connection = urlopen(orderURL)
            dom = fromstring(connection.read())
            for link in dom.xpath("//a/@href"):
                if "distribution.data.gov.bc.ca/fme_temp.zip" in link:
                    stopLoop = False
                    break
                elif "distribution.data.gov.bc.ca" in link:
                    downloadURL = link
                    stopLoop = True
                    break

        # create folder for  raw data,remove it first if it already exists
        folderPath = f"{self.downloadFolder}\\raw{self.fileName}"
        if path.exists(folderPath):
            rmtree(folderPath)
        mkdir(folderPath)

        # retrieve info from URL
        urlretrieve(downloadURL, f"{folderPath}.zip")

        # unzipp the file and remove original zipped file
        unpack_archive(f"{folderPath}.zip", folderPath)
        remove(f"{folderPath}.zip")

        # hunt through unzipped folder for shapefiles and HTML
        rawShapefilePaths = []
        rawHtmlPaths = []

        for dirname, _, files in walk(folderPath):
            for i in files:
                if i[-4:] == ".shp":
                    rawShapefilePaths.append(f"{dirname}\\{i}")
                if i[-5:] == ".html":
                    rawHtmlPaths.append(f"{dirname}\\{i}")
        


        if len(rawShapefilePaths) > 1:
            self.rawShapefilePaths = rawShapefilePaths
        else:
            self.rawShapefilePaths = rawShapefilePaths[0]

        if len(rawHtmlPaths) > 1:
            self.rawHtmlPaths = rawHtmlPaths
        else:
            self.rawHtmlPaths = rawHtmlPaths[0]

        print("done downloading!")

    def geoprocessing(self):
        self.resultObject = self.geoprocessingFunction(self.rawShapefilePaths)
        self.processedFile = arcpyGetPath(self.resultObject)

    def writeDownloadInfo(self):
        """creates downnload info for metadata, text file, and log"""
        # gets List of original filenames If more than one data source, otherwise gets original filename
        if isinstance(self.rawShapefilePaths, list):
            originalName = str(
                [path.splitext(path.split(i)[1])[0] for i in self.rawShapefilePaths]
            )
        else:
            originalName = path.splitext(path.split(self.rawShapefilePaths)[1])[0]

        # gets List of original HTML files If more than one data source, otherwise gets original HTML file name
        if isinstance(self.rawHtmlPaths, list):
            originalHtml = str(
                [path.splitext(path.split(i)[1])[0] for i in self.rawHtmlPaths]
            )
        else:
            originalHtml = path.splitext(path.split(self.rawHtmlPaths)[1])[0]

        self.catalogueDownloadInfo = f"Date Downloaded: {datetime.today().strftime('%Y-%m-%d')} from BC's data catalogue\n URL: {self.jsonPayload['featureItems'][0]['layerMetadataUrl']}\n Original Catalogue downnload name(s): {originalName}\nSee {originalHtml} for licence information and metadata for  catalogue downnloads\n For more information about downloading data, email data@gov.bc.ca.\nTo report downloading errors email NRSApplications@gov.bc.ca."

    def writeTextAndMetadata(self):
        """writes download information from BC Data catalogue to File metadata"""
        with open(f"{self.downloadFolder}\\{self.fileName}.txt", "w") as textFile:
            textFile.write(self.catalogueDownloadInfo)

        newMetadata = arcpy.metadata.Metadata(self.processedFile)
        newMetadata.description = self.catalogueDownloadInfo
        newMetadata.save()

    def writeLog(self):

        logFolder = f"{UniversalSettingsWrapper.logFolder}"

        # make log directory if it doesn't exist
        if exists(logFolder) == False:
            mkdir(logFolder)

        # instantiate variables
        archivedFile = (
            "Archiving Error" if self.archiveStatus == False else self.archivedFile
        )
        updateStack = "placeholder"
        today = datetime.today()
        logPath = f'{logFolder}\\{today.strftime("%B-%Y")}.json'
        todayString = today.strftime("%Y-%m-%d")
        time = today.strftime("%H:%M:%S")

        # build log dictionary
        logDictionary = {
            "dates": {
                todayString: {
                    "times": {
                        time: {
                            "dataset": self.name,
                            "updateStack": updateStack,
                            "archivedFile": archivedFile,
                            "currentPath": self.processedFile,
                            "catalogueDownloadInfo": self.catalogueDownloadInfo,
                        }
                    }
                }
            }
        }

        # Create new empty JSON if log doesn't exist,Read JSON file if it does
        if exists(logPath) == False:
            with open(logPath, "w") as logFile:
                jsonIn = logDictionary
        else:
            with open(logPath) as logFile:
                jsonIn = load(logFile)

        # write JSON to file
        with open(logPath, "w") as logFile:
            # if there is no entry for today
            if todayString not in jsonIn["dates"].keys():
                jsonIn["dates"][todayString] = logDictionary[todayString]["dates"]
            # if today's entry already exists
            else:
                jsonIn["dates"][todayString]["times"][time] = logDictionary["dates"][
                    todayString
                ]["times"][time]
        # write JSON to file
        dump(jsonIn, logFile)

    def catalogueUpdateProcess(self):
        self.archiving()
        self.catalogueWarehouseDownload()
        self.geoprocessing()
        self.writeDownloadInfo()
        self.writeTextAndMetadata()
        self.writeLog()
