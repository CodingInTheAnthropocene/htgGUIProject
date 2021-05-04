# Tantalus Crown Tenures Function Library
# Dataset ID: 4a63ae55e0a822631a47a8e865d4afa6

# download imports
from requests import post, Session
from urllib.request import urlopen, urlretrieve
from lxml.html import fromstring
from time import sleep

# geoprocessing imports
import arcpy

# archiving imports
from os import path, mkdir, walk, rename, remove
from datetime import datetime
from shutil import move, make_archive, rmtree, unpack_archive

# local imports
from modules.dataSettings import tenuresDataSettings as tds


def tenuresAchiving(currentTenuresPath, archiveFolder):

    currentTenuresPath = currentTenuresPath

    folderPath, shapefileNameWithExtension = path.split(currentTenuresPath)
    shapefileNameWithoutExtension = path.splitext(
        shapefileNameWithExtension)[0]

    # get date modified timestamp from tenures.shp
    tenuresModifiedTime = datetime.fromtimestamp(
        path.getmtime(currentTenuresPath)).strftime('%Y-%m-%d')

    # make a new directory in the name of the Shapefile with time added in archive folder
    newDirectoryPath = f"{archiveFolder}\\{shapefileNameWithoutExtension}{tenuresModifiedTime}"
    mkdir(newDirectoryPath)

    # iterate through current .shp directory, pull out files with the name of the shapefile, add the time to thoes file names, move the file to previously created directory
    # NOTE: Needs to work for xmls.
    count = 1
    for test, dir, files in walk(folderPath):
    
        numberofFiles = len(files)
        for fileNameWExtension in files:
            filename, extension = path.splitext(fileNameWExtension)
            if filename == shapefileNameWithoutExtension:
                rename(path.join(folderPath, fileNameWExtension),
                       path.join(folderPath, f"{filename}{tenuresModifiedTime}{extension}"))
                move(f"{folderPath}\\{filename}{tenuresModifiedTime}{extension}",
                     f"{newDirectoryPath}\\{filename}{tenuresModifiedTime}{extension}")
            count += 1

        if count > numberofFiles:
            break


    # make a .zip of the shapefile directory in detectory folder
    make_archive(
        newDirectoryPath, "zip", newDirectoryPath)

    # remove non zipped data
    rmtree(newDirectoryPath)
    remove(f"{currentTenuresPath}.xml")

    print("Done Archiving!")


def tenuresDownload(downloadFolder, email):
    """requests link to download raw shapefile file data with link sent to email of choice"""
    
    with Session() as s:
        # instantiate session with BC data catalogue, save important cookies in variable
        s.get("https://apps.gov.bc.ca/pub/dwds-ofi/jsp/dwds_pow_current_order.jsp?publicUrl=https%3A%2F%2Fapps.gov.bc.ca%2Fpub%2Fdwds-ofi%2Fpublic%2F&secureUrl=https%3A%2F%2Fapps.gov.bc.ca%2Fpub%2Fdwds-ofi%2Fsecure%2F&customAoiUrl=http%3A%2F%2Fmaps.gov.bc.ca%2Fess%2Fhm%2Faoi%2F&pastOrdersNbr=5&secureSite=false&orderSource=bcdc")
        jsession = s.cookies.get_dict()["JSESSIONID"]
        cookie2 = s.cookies.get_dict()["4a63ae55e0a822631a47a8e865d4afa6"]

        #cookies sent to data catalogue for shapefile link request
        cookies = {
            'JSESSIONID': jsession,
            '_ga': 'GA1.3.990723064.1619392484',
            '_gid': 'GA1.3.847311570.1619392484',
            '4a63ae55e0a822631a47a8e865d4afa6': cookie2,
            'WT_FPC': 'id=239981ddcf51d1babb01619389913272:lv=1619486491386:ss=1619485433432',
        }

        # headers sent to BC data catalogue for shapefile link request
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
            'Content-Type': 'application/json',
            'Origin': 'https://apps.gov.bc.ca',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://apps.gov.bc.ca/pub/dwds-ofi/jsp/dwds_pow_current_order.jsp?publicUrl=https%3A%2F%2Fapps.gov.bc.ca%2Fpub%2Fdwds-ofi%2Fpublic%2F&secureUrl=https%3A%2F%2Fapps.gov.bc.ca%2Fpub%2Fdwds-ofi%2Fsecure%2F&customAoiUrl=http%3A%2F%2Fmaps.gov.bc.ca%2Fess%2Fhm%2Faoi%2F&pastOrdersNbr=5&secureSite=false&orderSource=bcdc',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        # JSON payload sent to data catalogue for shapefile request 
        json = {
        "emailAddress": f"{email}",
        "aoiType": "1",
        "aoi": "{\"type\":\"FeatureCollection\",\"features\":[{\"type\":\"Feature\",\"geometry\":{\"bbox\":[-125.06139016888163,48.30224522044379,-122.40515460372072,49.3470925218454],\"type\":\"Polygon\",\"coordinates\":[[[-125.03939999215429,49.387443381941395],[-122.43518398330905,49.3480870937964],[-122.48762955305448,48.259285597314474],[-125.03356376204732,48.30199424617951],[-125.03939999215429,49.387443381941395]]]},\"properties\":{\"Id\":0}}],\"fileName\":\"SW_BC\"}",
        "orderingApplication": "BCDC",
        "crsType": "0",
        "clippingMethodType": "1",
        "formatType": "0",
        "useAOIBounds": "",
        "prepackagedItems": "",
        "aoiName": "",
        "featureItems": [
            {
                "featureItem": "WHSE_TANTALIS.TA_CROWN_TENURES_SVW",
                "filterValue": "",
                "layerName": "TANTALIS - Crown Tenures",
                "layerMetadataUrl": "https://caLike our forefatherstalogue.data.gov.bc.ca/dataset/tantalis-crown-tenures",
                "filterType": "No Filter",
                "pctOfMax": 3
            }
        ]
    }


        # Send request
        print("sending request")
        response = post('https://apps.gov.bc.ca/pub/dwds-ofi/public/order/createOrderFiltered/', headers=headers, cookies=cookies, json=json)

    
    #Check distribution.data.gov.bc.ca Every 15 seconds to see if order is available, download it To specified file path if it is
    orderNumber = response.json()["Value"]
    orderURL = f'https://apps.gov.bc.ca/pub/dwds-rasp/pickup/{orderNumber}'
    
    while True:
        sleep(15)
        print("checking...")
        connection = urlopen(orderURL)
        dom =  fromstring(connection.read())
        for link in dom.xpath('//a/@href'):
            if "distribution.data.gov.bc.ca/fme_temp.zip" in link:
                stopLoop = False
                break
            elif "distribution.data.gov.bc.ca" in link:
                downloadURL= link
                stopLoop = True
        if stopLoop == True:
            break
    
    downloadFilePath = f"{downloadFolder}\\tenuresShapefileRaw.zip"
    urlretrieve(downloadURL, f"{downloadFilePath}")

    #unzip
    unpack_archive(downloadFilePath, downloadFolder, "zip")
    
    #remove useless files
    remove(downloadFilePath)
    for i in ["Contents of Order.txt", "licence.txt", "README.txt", "TA_CROWN_TENURES_SVW.html"]:
        remove(f"{downloadFolder}\\{i}")

    #Path to raw tenures shapefile, *NOTE Will break if name changes
    tenuresRawPath = f"{downloadFolder}\\TA_CROWN_TENURES_SVW\\TA_CRT_SVW_polygon.shp"

    print("done downloading!")

    return tenuresRawPath

def tenuresGeoprocessing(tenuresRawPath, htgLandsPath, soiPath, arcgisWorkspaceFolder, tenuresDictionary = tds.tenuresDictionary):
    """Takes raw crown tenures data set and runs it through standardized Geoprocessing"""

    # ArcGIS environment settings
    arcpy.env.workspace = arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True


    # copy Shapefile for testing
    tenuresCopy = arcpy.CopyFeatures_management(tenuresRawPath, "tenuresCopy.shp")
    print("Raw Shapefile copied")

    # delete fields from crown tenures
    # NOTE: This May error with GDB instead of Shapefile
    fieldsToDelete = ["INTRID_SID", "APP_TYPE_CD", "TEN_DOCMNT", "TEN_LGLDSC", "TEN_A_DRVN",
                      "RESP_BUS_U", "DSP_TR_SID", "CD_CHR_STG", "SHAPE_1", "AREA_SQM", "FEAT_LEN"]

    arcpy.DeleteField_management(tenuresCopy, fieldsToDelete)
    print("Fields deleted")

    #delete records which meet specified criteria
    cursor = arcpy.da.UpdateCursor(
        tenuresCopy, ["CL_FILE", "TEN_SUBTYP", "TEN_SUBPRP"],)
    for row in cursor:
        if row[0] == 1414573:
            cursor.deleteRow()
        if row[1] == "BCAL INVENTORY" or row[1] == "NOTATION OF INTEREST":
            cursor.deleteRow()
        if row[2] == "TREATY AREA":
            cursor.deleteRow()
    
    print("Rows deleted")

    # add display_cd field
    arcpy.AddField_management(
        tenuresCopy, "display_cd", "TEXT", field_length=30)


    # many updates to display_cd based on values in tenuresDictionary

    cursor = arcpy.da.UpdateCursor(
        tenuresCopy, ["TEN_PURPOS", "TEN_SUBPRP", "display_cd"])

    for rowShapefile in cursor:
        # iterate over tenures dictionary
        for i in tenuresDictionary:
            first2 = f"{rowShapefile[0]}, {rowShapefile[1]}" 
            if first2 == i:
                rowShapefile[2] = tenuresDictionary[first2]
                cursor.updateRow(rowShapefile)
                break


    print("Fields added to display_cd")

    # intersect crown tenures with SOI, delete automatically created fields
    # FIX THIS: no_fid appropriate?? May eliminate need to delete added fields??
    tenuresSOIIntersect = arcpy.Intersect_analysis(
        [tenuresCopy, soiPath], "tenureSOIIntersect", join_attributes="NO_FID")

    print("tenure and SOI's intersected")

    # create new lands feature Class with removed fields. This is a workaround as disabling fields in arcpy is apparently very cumbersome.
    htgLandsCopy = arcpy.CopyFeatures_management(
        htgLandsPath, "htglandsCopy")

    #NOTE: should keep ['new_group', 'parcel_num', 'selected_by', 'new_ownership', 'ownership_type'] and default fields

    #full field names
    #fieldsToDeleteLandsCopy = [
    #    'ATTRIBUTE_SOURCE', 'EN', 'GEOMETRY_SOURCE', 'H_', 'Ha', 'ICF', 'ICF_AREA', 'ICIS', 'JUROL', 'LAND_ACT_PRIMARY_DESCRIPTION', 'LAND_DISTRICT', 'LEGAL_FREEFOQRM', 'LOCALAREA', 'LTSA_BLOCK', 'LTSA_LOT', 'LTSA_PARCEL', 'LTSA_PLAN', 'OWNER_CLASS', 'OtherComments', 'PARCEL_DESCRIPTION', 'PID', 'PIN', 'PIN_DISTLE', 'PIN_SUBDLA', 'PMBC', 'RoW', 'SOURCE_PROVISION_DATE', 'TEMP_PolyID', 'TENURES', 'TimbeTableLink', 'Title_Info', 'Title_num', 'Title_owner', 'access', 'apprais2BC_ID', 'apprais2HBU', 'apprais2Ha', 'apprais2reportID', 'appraisal2work', 'arch_sites', 'avail_issues', 'available', 'comments', 'confirm_question', 'ess_response', 'essential', 'guide_outfit', 'interests', 'label', 'landval_2017', 'landval_src', 'location', 'municipality', 'needs_confirm', 'owner', 'potential_FCyCmPD', 'prop_class', 'result_val_2017', 'selected', 'specific_location', 'tourism_capability', 'trapline', 'use_on_prop', 'valperHa_2017', 'zone_code', 'zoning',
    #]

    fieldsToDeleteLandsCopy = ['ATTRIBUTE_', 'EN', 'GEOMETRY_S', 'H_', 'Ha', 'ICF', 'ICF_AREA', 'ICIS', 'JUROL', 'LAND_ACT_P', 'LAND_DISTR', 'LEGAL_FREE', 'LOCALAREA', 'LTSA_BLOCK', 'LTSA_LOT', 'LTSA_PARCE', 'LTSA_PLAN', 'OWNER_CLAS', 'OtherComme', 'PARCEL_DES', 'PID', 'PIN', 'PIN_DISTLE', 'PIN_SUBDLA', 'PMBC', 'RoW', 'SOURCE_PRO', 'TEMP_PolyI', 'TENURES', 'TimbeTable', 'Title_Info', 'Title_num', 'Title_owne', 'access', 'apprais2BC', 'apprais2HB', 'apprais2Ha', 'apprais2re', 'appraisal2', 'arch_sites', 'avail_issu', 'available', 'comments', 'confirm_qu', 'ess_respon', 'essential', 'guide_outf', 'interests', 'label', 'landval_20', 'landval_sr', 'location', 'municipali', 'needs_conf', 'owner', 'potential_', 'prop_class', 'result_val', 'selected', 'specific_l', 'tourism_ca', 'trapline', 'use_on_pro', 'valperHa_2', 'zone_code', 'zoning']

    arcpy.DeleteField_management(htgLandsCopy, fieldsToDeleteLandsCopy)

    print("Fields deleted from lands copy")

    # Intersect tenures/soi intersect with land parcels data
    tenuresShapefileProcessed = arcpy.Intersect_analysis(
        [tenuresSOIIntersect, htgLandsCopy], "tenuresShapefileProcessed", join_attributes="NO_FID")
    print("tenure SOI lands intersect completed")

    # add and calculate HA field to tenures/soi/lands intersect
    arcpy.AddField_management(tenuresShapefileProcessed, "HA", "FLOAT")

    # NOTE: Path is hardcoded in here... doesn't seem to work with a relative path
    arcpy.CalculateGeometryAttributes_management(
        tenuresShapefileProcessed, [["HA", "AREA"]], area_unit="HECTARES")
    print("geometry calculated")

    print("Done Crown Tenures Geoprocessing!")

    # delete working copies
    arcpy.management.Delete(tenuresCopy)
    arcpy.management.Delete(htgLandsCopy)
    arcpy.management.Delete(tenuresSOIIntersect)

    return tenuresShapefileProcessed



def tenuresProcess(downloadFolder, email, currentTenuresPath, archiveFolder, htgLandsPath, soiPath, arcgisWorkspaceFolder):
    tenuresAchiving(currentTenuresPath, archiveFolder)
    tenuresGeoprocessing(tenuresDownload(downloadFolder, email), htgLandsPath, soiPath, arcgisWorkspaceFolder)

def getFileCreatedDate(filePath):
    return datetime.fromtimestamp(path.getctime(filePath)).strftime('%Y-%m-%d')
