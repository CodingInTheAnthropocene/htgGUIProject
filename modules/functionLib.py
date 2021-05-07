# download imports
from dataSettings import forestTenureSettings, universalSettings
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


####################################################################################################################
# Universal functions
####################################################################################################################
def getFileCreatedDate(filePath):
    return datetime.fromtimestamp(path.getctime(filePath)).strftime('%Y-%m-%d')


def shapefileArchiving(shapefilePath, archiveFolder):
    """ Takes the path of a shape file, and archives all files in that shapefile into the given archive folder"""

    folderPath, shapefileNameWithExtension = path.split(shapefilePath)
    shapefileNameWithoutExtension = path.splitext(
        shapefileNameWithExtension)[0]

    # get date modified timestamp from tenures.shp
    tenuresModifiedTime = getFileCreatedDate(shapefilePath)

    # make a new directory in the name of the Shapefile with time added in archive folder
    newDirectoryPath = f"{archiveFolder}\\{shapefileNameWithoutExtension}{tenuresModifiedTime}"
    mkdir(newDirectoryPath)

    # iterate through current .shp directory, pull out files with the name of the shapefile, add the time to thoes file names, move the file to previously created directory
    count = 1
    for _, _, files in walk(folderPath):

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
    #remove(f"{shapefilePath}.xml")

    print("Done Archiving!")


def catalogueWarehouseDownload(downloadFolder, jsonPayload, rawDownloadFolderName, rawShapefileName):
    """requests link to download raw download from data catalogue warehouse, and downloads and unzips file from that link"""

    with Session() as s:
        # instantiate session with BC data catalogue, save important cookies in variable
        s.get("https://apps.gov.bc.ca/pub/dwds-ofi/jsp/dwds_pow_current_order.jsp?publicUrl=https%3A%2F%2Fapps.gov.bc.ca%2Fpub%2Fdwds-ofi%2Fpublic%2F&secureUrl=https%3A%2F%2Fapps.gov.bc.ca%2Fpub%2Fdwds-ofi%2Fsecure%2F&customAoiUrl=http%3A%2F%2Fmaps.gov.bc.ca%2Fess%2Fhm%2Faoi%2F&pastOrdersNbr=5&secureSite=false&orderSource=bcdc")
        jsession = s.cookies.get_dict()["JSESSIONID"]
        cookie2 = s.cookies.get_dict()["4a63ae55e0a822631a47a8e865d4afa6"]

        # cookies sent to data catalogue for shapefile link request
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
        json = jsonPayload

        # Send request
        print("sending request")
        response = post('https://apps.gov.bc.ca/pub/dwds-ofi/public/order/createOrderFiltered/',
                        headers=headers, cookies=cookies, json=json)

    # Check distribution.data.gov.bc.ca Every 15 seconds to see if order is available, download it To specified file path if it is
    orderNumber = response.json()["Value"]
    orderURL = f'https://apps.gov.bc.ca/pub/dwds-rasp/pickup/{orderNumber}'

    stopLoop = False

    while stopLoop == False:
        sleep(15)
        print("checking...")
        connection = urlopen(orderURL)
        dom = fromstring(connection.read())
        for link in dom.xpath('//a/@href'):
            if "distribution.data.gov.bc.ca/fme_temp.zip" in link:
                stopLoop = False
                break
            elif "distribution.data.gov.bc.ca" in link:
                downloadURL = link
                stopLoop = True
                break

    downloadFilePath = f"{downloadFolder}\\tempDataCatalogueDownload.zip"
    urlretrieve(downloadURL, f"{downloadFilePath}")

    # unzip
    unpack_archive(downloadFilePath, downloadFolder, "zip")

    # remove useless files
    remove(downloadFilePath)
    for i in ["Contents of Order.txt", "licence.txt", "README.txt", f"{rawDownloadFolderName}.html"]:
        remove(f"{downloadFolder}\\{i}")

    # Path to raw tenures shapefile, *NOTE Will break if name changes
    rawPath = f"{downloadFolder}\\{rawDownloadFolderName}\\{rawShapefileName}"

    print("done downloading!")

    return rawPath


####################################################################################################################
# Tantalis Crown Tenures
####################################################################################################################

def crownTenuresGeoprocessing(crownTenuresRawPath, fileName, htgLandsPath, soiPath, arcgisWorkspaceFolder, crownTenuresDictionary):
    """Takes raw crown tenures data set and runs it through standardized Geoprocessing"""

    # ArcGIS environment settings
    arcpy.env.workspace = arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    # copy Shapefile To leave original intact
    tenuresCopy = arcpy.CopyFeatures_management(
        crownTenuresRawPath, "tenuresCopy.shp")
    print("Raw Shapefile copied")

    # delete fields from crown tenures
    # NOTE: This May error with GDB instead of Shapefile
    fieldsToDelete = ["INTRID_SID", "APP_TYPE_CD", "TEN_DOCMNT", "TEN_LGLDSC", "TEN_A_DRVN",
                      "RESP_BUS_U", "DSP_TR_SID", "CD_CHR_STG", "SHAPE_1", "AREA_SQM", "FEAT_LEN"]

    arcpy.DeleteField_management(tenuresCopy, fieldsToDelete)
    print("Fields deleted")

    # delete records which meet specified criteria
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

    # many updates to display_cd based on values in crownTenuresDictionary

    cursor = arcpy.da.UpdateCursor(
        tenuresCopy, ["TEN_PURPOS", "TEN_SUBPRP", "display_cd"])

    for row in cursor:
        # iterate over tenures dictionary
        for i in crownTenuresDictionary:
            first2 = f"{row[0]}, {row[1]}"
            if first2 == i:
                row[2] = crownTenuresDictionary[first2]
                cursor.updateRow(row)
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

    # NOTE: should keep ['new_group', 'parcel_num', 'selected_by', 'new_ownership', 'ownership_type'] and default fields

    # full field names
    # fieldsToDeletehtgLandsCopy = [
    #    'ATTRIBUTE_SOURCE', 'EN', 'GEOMETRY_SOURCE', 'H_', 'Ha', 'ICF', 'ICF_AREA', 'ICIS', 'JUROL', 'LAND_ACT_PRIMARY_DESCRIPTION', 'LAND_DISTRICT', 'LEGAL_FREEFOQRM', 'LOCALAREA', 'LTSA_BLOCK', 'LTSA_LOT', 'LTSA_PARCEL', 'LTSA_PLAN', 'OWNER_CLASS', 'OtherComments', 'PARCEL_DESCRIPTION', 'PID', 'PIN', 'PIN_DISTLE', 'PIN_SUBDLA', 'PMBC', 'RoW', 'SOURCE_PROVISION_DATE', 'TEMP_PolyID', 'TENURES', 'TimbeTableLink', 'Title_Info', 'Title_num', 'Title_owner', 'access', 'apprais2BC_ID', 'apprais2HBU', 'apprais2Ha', 'apprais2reportID', 'appraisal2work', 'arch_sites', 'avail_issues', 'available', 'comments', 'confirm_question', 'ess_response', 'essential', 'guide_outfit', 'interests', 'label', 'landval_2017', 'landval_src', 'location', 'municipality', 'needs_confirm', 'owner', 'potential_FCyCmPD', 'prop_class', 'result_val_2017', 'selected', 'specific_location', 'tourism_capability', 'trapline', 'use_on_prop', 'valperHa_2017', 'zone_code', 'zoning',
    # ]

    fieldsToDeletehtgLandsCopy = ['ATTRIBUTE_', 'EN', 'GEOMETRY_S', 'H_', 'Ha', 'ICF', 'ICF_AREA', 'ICIS', 'JUROL', 'LAND_ACT_P', 'LAND_DISTR', 'LEGAL_FREE', 'LOCALAREA', 'LTSA_BLOCK', 'LTSA_LOT', 'LTSA_PARCE', 'LTSA_PLAN', 'OWNER_CLAS', 'OtherComme', 'PARCEL_DES', 'PID', 'PIN', 'PIN_DISTLE', 'PIN_SUBDLA', 'PMBC', 'RoW', 'SOURCE_PRO', 'TEMP_PolyI', 'TENURES', 'TimbeTable', 'Title_Info', 'Title_num', 'Title_owne', 'access',
                                  'apprais2BC', 'apprais2HB', 'apprais2Ha', 'apprais2re', 'appraisal2', 'arch_sites', 'avail_issu', 'available', 'comments', 'confirm_qu', 'ess_respon', 'essential', 'guide_outf', 'interests', 'label', 'landval_20', 'landval_sr', 'location', 'municipali', 'needs_conf', 'owner', 'potential_', 'prop_class', 'result_val', 'selected', 'specific_l', 'tourism_ca', 'trapline', 'use_on_pro', 'valperHa_2', 'zone_code', 'zoning']

    arcpy.DeleteField_management(htgLandsCopy, fieldsToDeletehtgLandsCopy)

    print("Fields deleted from lands copy")

    # Intersect tenures/soi intersect with land parcels data
    crownTenuresProcessedPath = arcpy.Intersect_analysis(
        [tenuresSOIIntersect, htgLandsCopy], fileName, join_attributes="NO_FID")
    print("tenure SOI lands intersect completed")

    # add and calculate HA field to tenures/soi/lands intersect
    arcpy.AddField_management(crownTenuresProcessedPath, "HA", "FLOAT")

    # NOTE: Path is hardcoded in here... doesn't seem to work with a relative path
    arcpy.CalculateGeometryAttributes_management(
        crownTenuresProcessedPath, [["HA", "AREA"]], area_unit="HECTARES")
    print("geometry calculated")

    print("Done Crown Tenures Geoprocessing!")

    # delete working copies
    arcpy.management.Delete(tenuresCopy)
    arcpy.management.Delete(htgLandsCopy)
    arcpy.management.Delete(tenuresSOIIntersect)

    return crownTenuresProcessedPath

def crownTenuresProcess(downloadFolder, crownTenuresPath, archiveFolder, fileName, htgLandsPath, soiPath, arcgisWorkspaceFolder, crownTenuresDictionary, jsonPayload, rawDownloadFolderName, rawShapeFileName):
    """Entire crown tenure chain: archive old, download new, process new. This function is called from the GUI"""
    shapefileArchiving(crownTenuresPath, archiveFolder)
    crownTenuresGeoprocessing(catalogueWarehouseDownload(downloadFolder, jsonPayload, rawDownloadFolderName, rawShapeFileName), fileName, htgLandsPath, soiPath, arcgisWorkspaceFolder, crownTenuresDictionary)

####################################################################################################################
# Forest Tenure Harvesting Authority Polygons
####################################################################################################################
def forestTenureGeoprocessing(forestTenureRawPath, downloadFolder, fileName, htgLandsPath, arcgisWorkspaceFolder):

    print("Starting forest tenure geoprocessing")

    #env variables
    arcpy.env.workspace = arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True
    
    forestTenureNameTemp = path.splitext(
        arcpy.Describe(forestTenureRawPath).name)[0]

    # Create a temporary GDB and create a copy of forest tenure in it. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(downloadFolder, "temp.gdb")
    tempGdbPath = f"{downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(
        forestTenureRawPath, tempGdbPath)

    print("Raw Shapefile copied to temp Geodatabase")

    
    forestTenureCopy = f"{tempGdbPath}\\{forestTenureNameTemp}"



    print("Fields deleted from forest tenure")

    # Update EXPIRY of all you and live in_DT *NOTE, doesn't make sense to me but arcpy is reading null as " ". Should be extra cautious to make sure that this is working.
    cursor=arcpy.da.UpdateCursor(
        forestTenureCopy, ["EXPIRY_DT", "EXTEND_DT"]
    )

    for row in cursor:
        if row[1] != " ":
            row[0] = row[1]

    del cursor

    # delete fields from forest tenure
    fieldsToDelete = ['HVA_SKEY', 'FFID', 'CP_ID', 'FEAT_CLASS', 'HVA_ID', 'HVA_MGMTID', 'HVA_MGMTCD', 'HRV_TP_CD', 'HRV_TP_DSC', 'HVA_ST_CD', 'ISSUE_DATE', 'EXTEND_DT', 'CURR_EX_DT', 'QTA_TP_CD', 'CR_LND_CD', 'SAL_TP_CD', 'CASC_SP_CD', 'CATAST_IND', 'CR_GRT_IND', 'CRUISE_IND', 'DECID_IND', 'RETIRE_DT',
                      'FEAT_AREA', 'FEAT_PERIM', 'ADM_DST_CD', 'GEO_DST_CD', 'GEO_DST_NM', 'TM_PRIME', 'MRK_MD_CD', 'MRK_MD_DSC', 'MRK_IN_CD', 'MRK_IN_DSC', 'OTH_TM_IND', 'CL_LOC_CD', 'FILE_TP_CD', 'FILE_ST_CD', 'PFU_MGMTID', 'SB_FND_IND', 'BCTS_ORGCD', 'BCTS_ORGNM', 'MAP_LABEL', 'AREA_SQM', 'FEAT_LEN', 'OBJECTID']

    arcpy.DeleteField_management(forestTenureCopy, fieldsToDelete)


    # dictionary to rename fields
    forestTenureRenameDict = {
        "ADM_DST_NM": "AdmnDstrct",
        "QTA_TP_DSC": "Type",
        "SAL_TP_DSC": "SlvgType",
        "CLIENT_NM": "ClientName",
        "CR_LND_DSC": "CLDistrict",
        "CLIENT_NUM": "ClientNum",
        "EXPIRY_DT": "ExpiryDate",
        "LOCATION": "location",
        "LIFE_ST_CD": "status",
        "FIL_TP_DSC": "LicnceType"
    }

    # rename fields
    for i in forestTenureRenameDict:
        arcpy.AlterField_management(
            forestTenureCopy, i, forestTenureRenameDict[i])

    # create copy of lands And delete fields that aren't wanted in final product
    htgLandsCopy = arcpy.CopyFeatures_management(
        htgLandsPath, "htglandsCopy")

    fieldsToDeletehtgLandsCopy = ['ATTRIBUTE_', 'EN', 'GEOMETRY_S', 'H_', 'Ha', 'ICF', 'ICF_AREA', 'ICIS', 'JUROL', 'LAND_ACT_P', 'LAND_DISTR', 'LEGAL_FREE', 'LOCALAREA', 'LTSA_BLOCK', 'LTSA_LOT', 'LTSA_PARCE', 'LTSA_PLAN', 'OWNER_CLAS', 'OtherComme', 'PARCEL_DES', 'PID', 'PIN', 'PIN_DISTLE', 'PIN_SUBDLA', 'PMBC', 'RoW', 'SOURCE_PRO', 'TEMP_PolyI', 'TENURES', 'TimbeTable', 'Title_Info', 'Title_num', 'Title_owne', 'access',
                                  'apprais2BC', 'apprais2HB', 'apprais2Ha', 'apprais2re', 'appraisal2', 'arch_sites', 'avail_issu', 'available', 'comments', 'confirm_qu', 'ess_respon', 'essential', 'guide_outf', 'interests', 'label', 'landval_20', 'landval_sr', 'location', 'municipali', 'needs_conf', 'owner', 'potential_', 'prop_class', 'result_val', 'selected', 'specific_l', 'tourism_ca', 'trapline', 'use_on_pro', 'valperHa_2', 'zone_code', 'zoning', "Shape_Leng", "Shape_Area", "new_owners", "ownership_" ]


    
    arcpy.DeleteField_management(htgLandsCopy, fieldsToDeletehtgLandsCopy)

    # intersect forest tenure with HTG lands
    forestTenureProcessedPath = arcpy.Intersect_analysis([forestTenureCopy, htgLandsCopy], 
                        fileName, join_attributes="NO_FID")

    print("Forest tenure and lands intersected")
    
    # calculate geometry
    arcpy.AddField_management(forestTenureProcessedPath, "HA", "FLOAT")

    arcpy.CalculateGeometryAttributes_management(
        forestTenureProcessedPath, [["HA", "AREA"]], area_unit="HECTARES")
    
    print("HA calculated")

    # remove working files
    arcpy.management.Delete(htgLandsCopy)
    arcpy.management.Delete(tempGdbPath)
    
    return forestTenureProcessedPath

def forestTenureProcess(downloadFolder, currentForestTenurePath, archiveFolder, filename, htgLandsPath, arcgisWorkspaceFolder, jsonPayload, rawDownloadFoldernName, rawShapefileName):
    shapefileArchiving(currentForestTenurePath, archiveFolder)
    forestTenureGeoprocessing(catalogueWarehouseDownload(downloadFolder, jsonPayload, rawDownloadFoldernName, rawShapefileName), downloadFolder, filename, htgLandsPath, arcgisWorkspaceFolder)

# test
forestTenureProcess(forestTenureSettings.downloadFolder, forestTenureSettings.currentPath, forestTenureSettings.archiveFolder, forestTenureSettings.fileName, universalSettings.htgLandsPath, forestTenureSettings.arcgisWorkspaceFolder, forestTenureSettings.jsonPayload, forestTenureSettings.rawDownloadFolderName, forestTenureSettings.rawShapefileName)


