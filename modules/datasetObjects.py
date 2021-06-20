"""
datasetObjects.py- Module for Dataset object
"""
import arcpy
import logging
from genericpath import exists, getsize
from requests import post, Session
from urllib.parse import urlparse
from urllib.request import urlopen, urlretrieve
from lxml.html import fromstring
from time import sleep
from os import path, mkdir, walk, rename, remove
from datetime import datetime
from shutil import move, make_archive, rmtree, unpack_archive
from json import load, dump
import time
from traceback import print_exc
from io import StringIO

from modules.universalFunctions import *
from modules.settingsWrapper import *
from modules.catalogueFunctions import *
from modules.parksFunctions import *

class Dataset:
    """
    Primary object for handling datasets. 
    """    
    def __init__(self, datasetAlias):
        """
        Constructor method.

        :param datasetAlias: Dataset alias. Must match what is in configuration files.
        :type datasetAlias: str
        """        

        # Instantiate settings wrappers and assign attributes
        self.universalSettingsWrapper = UniversalSettingsWrapper()
        self.datasetSettingsWrapper = DatasetSettingsWrapper(datasetAlias)

        self.name = self.datasetSettingsWrapper.name
        self.dataCatalogueIdList = self.datasetSettingsWrapper.dataCatalogueIdList
        self.fileName = self.datasetSettingsWrapper.fileName
        self.downloadFolder = self.datasetSettingsWrapper.downloadFolder
        self.archiveFolder = self.datasetSettingsWrapper.archiveFolder
        self.currentPath = self.datasetSettingsWrapper.currentPath
        self.jsonPayload = self.datasetSettingsWrapper.jsonPayload
        self.updateFrequency = self.datasetSettingsWrapper.updateFrequency
        self.arcgisWorkspaceFolder = self.datasetSettingsWrapper.arcgisWorkspaceFolder
        self.urlList = self.datasetSettingsWrapper.urlList
        

        self.alias = datasetAlias
        self.geoprocessingFunction = eval(self.datasetSettingsWrapper.geoprocessingFunction)

    def archiving(self):
        """
        Archives shapefile or Geodatabase feature class.

        :raises ValueError: If object is not shapefile or Geodatabase feature class
        """
        try:
            currentPathType = arcpy.Describe(self.currentPath).dataType
            
            # if shapefile
            if currentPathType == "ShapeFile":
                folderPath, shapefileNameWithExtension = path.split(self.currentPath)

                # get date created timestamp
                createdTime = getFileCreatedDate(self.currentPath)

                # make a new directory in the name of the Shapefile with time added in archive folder
                newDirectoryPath = f"{self.archiveFolder}\\{shapefileNameWithExtension}{createdTime}"
                
                if exists(newDirectoryPath):
                    rmtree(newDirectoryPath)

                mkdir(newDirectoryPath)

                # iterate through current .shp directory, pull out files with the name of the shapefile, add the time to thoes file names, move the file to previously created directory
                count = 1
                for _, _, files in walk(folderPath):

                    numberofFiles = len(files)
                    for fileNameWExtension in files:
                        filename, extension = path.splitext(fileNameWExtension)
                        if filename  in  shapefileNameWithExtension:
                            rename(
                                path.join(folderPath, fileNameWExtension),
                                path.join(
                                    folderPath,
                                    f"{filename}{createdTime}{extension}",
                                ),
                            )
                            move(
                                f"{folderPath}\\{filename}{createdTime}{extension}",
                                f"{newDirectoryPath}\\{filename}{createdTime}{extension}",
                            )
                        count += 1

                    if count > numberofFiles:
                        break

                # make a .zip of the shapefile directory in detectory folder
                make_archive(newDirectoryPath, "zip", newDirectoryPath)

                # remove non zipped data
                rmtree(newDirectoryPath)

                self.archivedFile = f"{newDirectoryPath}"

            # if gbd
            elif currentPathType == "FeatureClass":
                currentGDB, fileName = (
                    path.split(self.currentPath)[0],
                    path.split(self.currentPath)[1],
                )

                self.archivedFile = f"{self.archiveFolder}\\{fileName}{getFileCreatedDate(arcpy.Describe(self.currentPath).path)}.gdb"
                make_archive(
                    self.archivedFile,
                    "zip",
                    currentGDB,
                )
                arcpy.Delete_management(currentGDB)

            else:
                raise ValueError("Incorrect file type")

            self.archiveStatus = True

        except:
            print_exc()
            print("Archiving error, check file path")
            self.logger.error("Archiving error")


            self.archiveStatus = False
        
        finally:
            self.logger.info("archiving()")

    def dataAcquisition(self):
        """
        Acquires all data associated with dataset from BC data catalogue and any other sources. Stores raw file paths in variable.
        """        

        with Session() as s:
            # self.datasetSettingsWrapper session with BC data catalogue, save important cookies in variable
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
            print(f"{self.alias}: Sending request")

            response = post(
                "https://apps.gov.bc.ca/pub/dwds-ofi/public/order/createOrderFiltered/",
                headers=headers,
                cookies=cookies,
                json=self.jsonPayload,
            )


        # NOTE: this following section is the most fragile piece of the whole software. If anything about the way the BC data catalogue operates changes, this function is likely to go down and break every data catalogue download. If there are problems with the download, this is the likely culprit.
        
        # get order number when responses ready, build template URL with it
        orderNumber = response.json()["Value"]
        orderURL = f"https://apps.gov.bc.ca/pub/dwds-rasp/pickup/{orderNumber}"

        # check order url every 15 seconds for the appropriate download link, break the loop when that link no longer includes "fme_temp.zip". This signifies that the temporary link has been replaced.
        stopLoop = False
        while stopLoop == False:
            sleep(15)
            print(f"{self.alias}: Checking...")
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
        
        print(f"{self.alias}: Found! Starting download...")

        # create folder for  raw data, remove it first if it already exists
        self.rawFolderPath = f"{self.downloadFolder}\\raw{self.fileName}"

        if path.exists(self.rawFolderPath) == True:
            rmtree(self.rawFolderPath)

        # retrieve info from URL
        urlretrieve(downloadURL, f"{self.rawFolderPath}.zip")

        # unzipp the file and remove original zipped file
        unpack_archive(f"{self.rawFolderPath}.zip", self.rawFolderPath)
        remove(f"{self.rawFolderPath}.zip")

        # hunt through unzipped folder for gbd feature clases, shapefiles and HTML File paths. Store as list.
        rawFilePaths = []
        rawHtmlPaths = []

        for dirname, _, files in walk(self.rawFolderPath):
            if dirname[-4:] == ".gdb":
                arcpy.env.workspace= dirname
                rawFilePaths.append(
                    arcpy.Describe(
                        arcpy.ListFeatureClasses()[0]
                    ).catalogPath
                )

            for i in files:
                if i[-4:] == ".shp":
                    rawFilePaths.append(f"{dirname}\\{i}")
                if i[-5:] == ".html":
                    rawHtmlPaths.append(f"{dirname}\\{i}")

        # download and unzip any auxiliary shape files, add their paths to list
        if len(self.urlList) > 0:
            print(f"{self.alias}: Downloading auxiliary datasets")
            for url in self.urlList:
                rawFilePaths.extend(
                    shapeFileDownloadUnzip(url, self.rawFolderPath, urlparse(url).netloc)
                )

        else:
            print(f"{self.alias}: This dataset has no auxiliary URLs")

        # unpack list if it's only one item
        if len(rawFilePaths) > 1:
            self.rawFilePaths = list(dict.fromkeys(rawFilePaths))
        else:
            self.rawFilePaths = rawFilePaths[0]

        self.rawHtmlPaths = list(dict.fromkeys(rawHtmlPaths))

        print(f"{self.alias}: Done downloading!")

        self.logger.info("dataAcquisition()")

    def geoprocessing(self):
        """
        Run geoprocessing chain associated with dataset
        """        
        self.resultObject = self.geoprocessingFunction(self.rawFilePaths, self)
        self.processedFile = arcpyGetPath(self.resultObject)
        
        #remove raw data
        rmtree(self.rawFolderPath)
        
        self.logger.info(f"{self.geoprocessingFunction.__name__}('{self.rawFilePaths}')")

    def createDownloadInfo(self):
        """
        Create download info text 
        """        

        # gets List of original filenames If more than one data source, otherwise gets original filename
        if isinstance(self.rawFilePaths, list):
            originalName = str(
                [path.splitext(path.split(i)[1])[0] for i in self.rawFilePaths]
            )
        else:
            originalName = path.splitext(path.split(self.rawFilePaths)[1])[0]

        # gets List of original HTML files If more than one data source, otherwise gets original HTML file name
        if isinstance(self.rawHtmlPaths, list):
            originalHtml = str([path.split(i)[1] for i in self.rawHtmlPaths])
        else:
            originalHtml = path.split(self.rawHtmlPaths)[1]

        auxiliaryDownloadInfo = (
            self.urlList
            if len(self.urlList) > 0
            else None
        )

        self.catalogueDownloadInfo = f"\n     Date Downloaded: {datetime.today().strftime('%Y-%m-%d')} from BC's data catalogue\n     URL: {self.jsonPayload['featureItems'][0]['layerMetadataUrl']}\n     Original Catalogue download name(s): {originalName}\n     See {originalHtml} for licence information and metadata for catalogue downloads\n     For more information about downloading data, email data@gov.bc.ca.\n     To report downloading errors email NRSApplications@gov.bc.ca. \n     Auxiliary download links: {auxiliaryDownloadInfo}"


    def writeTextAndMetadata(self):
        """
        Writes download information to processed file metadata
        """

        if arcpy.Describe(self.processedFile).dataType == "ShapeFile":
            with open(
                f"{self.downloadFolder}\\{path.splitext(self.fileName)[0]}.txt", "w"
            ) as textFile:
                textFile.write(self.catalogueDownloadInfo)

        newMetadata = arcpy.metadata.Metadata(self.processedFile)
        newMetadata.description = self.catalogueDownloadInfo
        newMetadata.save()

    def writeLog(self):
        """
        Builds JSON logs. Create a new log every month.
        """  
        logFolder = f"{self.universalSettingsWrapper.logFolder}"

        # make log directory if it doesn't exist
        if exists(logFolder) == False:
            mkdir(logFolder)

        # self.datasetSettingsWrapper variables
        archivedFile = (
            "Archiving Error" if self.archiveStatus == False else self.archivedFile
        )
        errors_updateStack = self.logCaptureString.getvalue()
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
                            "dataset": f"{self.name}\n",
                            "errors/updateStack": f"\n{errors_updateStack}",
                            "archivedFile": f"{archivedFile}\n",
                            "currentPath": f"{self.processedFile}\n",
                            "catalogueDownloadInfo": f"{self.catalogueDownloadInfo}\n",
                        }
                    }
                }
            }
        }

        # If log doesn't exist or is empty for some reason, create A new JSON file and populate with dictionary
        if exists(logPath) == False or getsize(logPath)==0:
            with open(logPath, "w")  as logFile:
                dump(logDictionary, logFile)

        # if log already exists
        else:
            with open(logPath, "r") as logFile:
                jsonIn = load(logFile)

            with open(logPath, "w") as logFile:
                # if there is no entry for today
                if todayString not in jsonIn["dates"].keys():
                    jsonIn["dates"][todayString]= logDictionary["dates"][todayString]
                # if today's entry already exists
                else:
                    jsonIn["dates"][todayString]["times"][time] = logDictionary["dates"][
                        todayString
                    ]["times"][time]

                # write JSON to file
                dump(jsonIn, logFile)
        

    def writeToSettings(self):
        """
        Write processed file path to settings.json
        """  
        dictToSettings = {"currentPath": self.processedFile}
        self.datasetSettingsWrapper.settingsWriter(dictToSettings)

    def updateProcess(self):
        """
        The  most important darn function in the whole kit and caboodle. The entire update process for a dataset. Called from the update button on the DatasetFrame widget.
        """ 
        # test to see if current file is open in ArcGIS
        schemaLockStatus=arcpy.TestSchemaLock(self.currentPath)
        
        try:
            spatialObjectStatus=  True if arcpy.Describe(self.currentPath).dataType in ("ShapeFile", "FeatureClass") else False
        except:
            spatialObjectStatus= False
            print_exc()
        
        # check to see if requisite paths in place
        fromSettings =self.universalSettingsWrapper
        requiredPaths =True
        requiredPathList = []

        # if path doesn't exist, is a blank string, and isn't a geodatabase feature class, flag the path as invalid
        for i in  (fromSettings.downloadFolder, fromSettings.archiveFolder, fromSettings.logFolder, fromSettings.htgLandsPath, fromSettings.soiPath):
            if (exists(i)== False or i == ""):
                try:
                    if arcpy.Describe(i).dataType != "FeatureClass":
                        requiredPaths=False
                        requiredPathList.append(i)
                except:
                    requiredPaths=False
                    requiredPathList.append(i)
                                
        if requiredPaths== False:
            print(f"Download folder, archive folder, log folder, HTG lands path, and SOI path required. The following paths are invalid: {requiredPathList}")
            return

        # If all is good, let 'er rip
        if (schemaLockStatus== True or spatialObjectStatus ==  False) and requiredPaths==True:            
            #insantiate logger
            self.logger = logging.getLogger('basic_logger')
            self.logger.setLevel(logging.DEBUG)
            self.logCaptureString = StringIO()
            self.ch = logging.StreamHandler(self.logCaptureString)
            self.ch.setLevel(logging.DEBUG)
            formatter = logging.Formatter('    %(levelname)s - %(message)s')
            self.ch.setFormatter(formatter)
            self.logger.addHandler(self.ch)

            self.logger.info("updateProcess()")

            print(f"{self.alias}: Starting update process!")
            
            # archive
            print(f"{self.alias}: Archiving…")
            self.archiving()

            # acquire data
            tic = time.perf_counter()
            print(f"{self.alias}: Starting data acquisition")
            self.dataAcquisition()
            toc = time.perf_counter()
            print(f"{self.alias}: Total acquisition time - {toc - tic:0.4f} seconds")
            
            # geoprocessing chain 
            print(f"{self.alias}: Starting geoprocessing")
            tic = time.perf_counter()
            self.geoprocessing()
            toc = time.perf_counter()
            print(f"{self.alias}: Geoprocessing time - {toc - tic:0.4f} seconds")           

            print(f"{self.alias}: Logging…")

            #write logs and metadata
            try:
                self.writeToSettings()
                self.createDownloadInfo()
                self.writeTextAndMetadata()
                self.writeLog()
            except:
                print("Logging error")
                print_exc()

            print(f"{self.alias}: Finished update process!")

        else:
            print("Can't get exclusive schema lock")
            

