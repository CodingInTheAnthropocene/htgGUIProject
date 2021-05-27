# download imports


from modules.dataSettings import *
from requests import post, Session
from urllib.request import urlopen, urlretrieve
from lxml.html import fromstring
from time import sleep
from pandas.core.common import flatten
import arcpy
from os import path, mkdir, walk, rename, remove
from datetime import datetime
from shutil import move, make_archive, rmtree, unpack_archive


####################################################################################################################
# Universal functions
####################################################################################################################
def getFileCreatedDate(filePath):
    return datetime.fromtimestamp(path.getctime(filePath)).date()

def fieldsToDelete(featureClass, keepFields):
    originalFields = [i.name for i in arcpy.ListFields(featureClass)]
    deleteFields = [i for i in originalFields if i not in keepFields]

    return deleteFields

def shapefileFieldRename(shapefile, currentFieldName, newFieldName):
    
    arcpy.AddField_management(shapefile, newFieldName)
    cursor=arcpy.da.UpdateCursor(shapefile, [currentFieldName, newFieldName])

    for row in cursor:
        row[1] = row[0]
        cursor.updateRow(row)

    del cursor

    arcpy.DeleteField_management(shapefile, currentFieldName)


def archiving(currentPath, archiveFolder):
    """ Takes the path of a shape file, and archives all files in that shapefile into the given archive folder. If path is gdb feature class, archives that whole GDB"""
    
    currentPathType = arcpy.Describe(currentPath).dataType

    if currentPathType == "ShapeFile":
        folderPath, shapefileNameWithExtension = path.split(currentPath)
        shapefileNameWithoutExtension = path.splitext(
            shapefileNameWithExtension)[0]

        # get date modified timestamp from tenures.shp
        tenuresModifiedTime = getFileCreatedDate(currentPath)

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

    elif currentPathType == "FeatureClass":
        currentGDB, fileName = path.split(currentPath)[0], path.split(currentPath)[1]
        make_archive(f"{archiveFolder}\\{fileName}{getFileCreatedDate(currentPath)}", "zip", currentGDB)
        arcpy.Delete_management(currentGDB)
    
    else:
        print("File not Recognizable type")

    print("Done Archiving!")


def shapeFileDownloadUnzip(url, downloadFolder, fileName):
    """Downloads a zipped shapefile from a specified url to a specified download folder. Unzips in download folder. Will walk through any number of directories to find shapefile. Returns z list of paths if multiple shapefiles exist, otherwise returns a path like string. He and allWill replace any identically named folders in the download location."""
    
    folderPath= f"{downloadFolder}\\raw{fileName}"
    if path.exists(folderPath):
        rmtree(folderPath)
    mkdir(folderPath)
    urlretrieve(url, f"{folderPath}.zip")
    filePaths = []
    unpack_archive(f"{folderPath}.zip", folderPath)
    remove(f"{folderPath}.zip")
    for dirname, _, files in walk(folderPath):
        for i in files:
            if i[-4:] == ".shp":
                filePaths.append(f"{dirname}\\{i}")
    
    if len(filePaths) > 1:
        return filePaths
    else:
        return filePaths[0]
        

def catalogueWarehouseDownload(downloadFolder, jsonPayload, fileName):
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
    
    rawPath = shapeFileDownloadUnzip(downloadURL, downloadFolder, fileName)

    print("done downloading!")

    return rawPath


####################################################################################################################
# Tantalis Crown Tenures
####################################################################################################################

def crownTenuresGeoprocessing(crownTenuresRawPath):
    """Takes raw crown tenures data set and runs it through standardized Geoprocessing"""

    fileName = crownTenuresSettings.fileName

    # ArcGIS environment settings
    arcpy.env.workspace = crownTenuresSettings.arcgisWorkspaceFolder
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
        if row[1] in ("BCAL INVENTORY", "NOTATION OF INTEREST") and row[2] not in ("UREP/RECREATION RESERVE", "FISH AND WILDLIFE MANAGEMENT", "ENVIRONMENT PROTECTION/CONSERVATION"):
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
        for i in crownTenuresSettings.valuesDictionary:
            first2 = f"{row[0]}, {row[1]}"
            if first2 == i:
                row[2] = crownTenuresSettings.valuesDictionary[first2]
                cursor.updateRow(row)
                break

    print("Fields added to display_cd")

    # intersect crown tenures with SOI, delete automatically created fields
    # FIX THIS: no_fid appropriate?? May eliminate need to delete added fields??
    tenuresSOIIntersect = arcpy.Intersect_analysis(
        [tenuresCopy, universalSettings.soiPath], "tenureSOIIntersect", join_attributes="NO_FID")

    print("tenure and SOI's intersected")

    # create new lands feature Class with removed fields. This is a workaround as disabling fields in arcpy is apparently very cumbersome.
    htgLandsCopy = arcpy.CopyFeatures_management(
        universalSettings.htgLandsPath, "htglandsCopy")

    # NOTE: should keep ['new_group', 'parcel_num', 'selected_by', 'new_ownership', 'ownership_type'] and default fields

    # full field names
    # fieldsToDeletehtgLandsCopy = [
    #    'ATTRIBUTE_SOURCE', 'EN', 'GEOMETRY_SOURCE', 'H_', 'Ha', 'ICF', 'ICF_AREA', 'ICIS', 'JUROL', 'LAND_ACT_PRIMARY_DESCRIPTION', 'LAND_DISTRICT', 'LEGAL_FREEFOQRM', 'LOCALAREA', 'LTSA_BLOCK', 'LTSA_LOT', 'LTSA_PARCEL', 'LTSA_PLAN', 'OWNER_CLASS', 'OtherComments', 'PARCEL_DESCRIPTION', 'PID', 'PIN', 'PIN_DISTLE', 'PIN_SUBDLA', 'PMBC', 'RoW', 'SOURCE_PROVISION_DATE', 'TEMP_PolyID', 'TENURES', 'TimbeTableLink', 'Title_Info', 'Title_num', 'Title_owner', 'access', 'apprais2BC_ID', 'apprais2HBU', 'apprais2Ha', 'apprais2reportID', 'appraisal2work', 'arch_sites', 'avail_issues', 'available', 'comments', 'confirm_question', 'ess_response', 'essential', 'guide_outfit', 'interests', 'label', 'landval_2017', 'landval_src', 'location', 'municipality', 'needs_confirm', 'owner', 'potential_FCyCmPD', 'prop_class', 'result_val_2017', 'selected', 'specific_location', 'tourism_capability', 'trapline', 'use_on_prop', 'valperHa_2017', 'zone_code', 'zoning',
    # ]

    fieldsToDeletehtgLandsCopy = ['ATTRIBUTE_', 'EN', 'GEOMETRY_S', 'H_', 'Ha', 'ICF', 'ICF_AREA', 'ICIS', 'JUROL', 'LAND_ACT_P', 'LAND_DISTR', 'LEGAL_FREE', 'LOCALAREA', 'LTSA_BLOCK', 'LTSA_LOT', 'LTSA_PARCE', 'LTSA_PLAN', 'OWNER_CLAS', 'OtherComme', 'PARCEL_DES', 'PID', 'PIN', 'PIN_DISTLE', 'PIN_SUBDLA', 'PMBC', 'RoW', 'SOURCE_PRO', 'TEMP_PolyI', 'TENURES', 'TimbeTable', 'Title_Info', 'Title_num', 'Title_owne', 'access',
                                  'apprais2BC', 'apprais2HB', 'apprais2Ha', 'apprais2re', 'appraisal2', 'arch_sites', 'avail_issu', 'available', 'comments', 'confirm_qu', 'ess_respon', 'essential', 'guide_outf', 'interests', 'label', 'landval_20', 'landval_sr', 'location', 'municipali', 'needs_conf', 'potential_', 'prop_class', 'result_val', 'selected', 'specific_l', 'tourism_ca', 'trapline', 'use_on_pro', 'valperHa_2', 'zone_code', 'zoning']

    arcpy.DeleteField_management(htgLandsCopy, fieldsToDeletehtgLandsCopy)

    print("Fields deleted from lands copy")

    # Intersect tenures/soi intersect with land parcels data
    crownTenuresProcessedPath = arcpy.Identity_analysis(
        tenuresSOIIntersect, htgLandsCopy, fileName, join_attributes="NO_FID")
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


def crownTenuresProcess():
    """Entire crown tenure chain: archive old, download new, process new. This function is called from the GUI"""
    try:
        archiving(crownTenuresSettings.currentPath, crownTenuresSettings.archiveFolder)
    except:
        print("cannot archive this file, check path")

    crownTenuresGeoprocessing(catalogueWarehouseDownload(crownTenuresSettings.downloadFolder, crownTenuresSettings.jsonPayload, crownTenuresSettings.fileName))
    
####################################################################################################################
# Forest Tenure Harvesting Authority Polygons (Forest Tenure Cut Permits)
####################################################################################################################


def forestHarvestingAuthorityGeoprocessing(rawForestHarvestingAuthorityPath, downloadFolder, fileName, htgLandsPath, arcgisWorkspaceFolder):

    print("Starting forest tenure geoprocessing")

    # env variables
    arcpy.env.workspace = arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    # get Name of Raw shape file
    rawName = path.splitext(
        arcpy.Describe(rawForestHarvestingAuthorityPath).name)[0]

    # Create a temporary GDB and create a copy of forest tenure in it. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(downloadFolder, "temp.gdb")
    tempGdbPath = f"{downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(
        rawForestHarvestingAuthorityPath, tempGdbPath)

    print("Raw Shapefile copied to temp Geodatabase")

    forestHarvestingAuthorityCopy = f"{tempGdbPath}\\{rawName}"

    print("Fields deleted from forest tenure")

    # Update EXPIRY_DT
    cursor = arcpy.da.UpdateCursor(
        forestHarvestingAuthorityCopy, ["EXPIRY_DT", "EXTEND_DT"]
    )

    for row in cursor:
        if row[1] != " ":
            row[0] = row[1]

        cursor.updateRow(row)

    del cursor

    # delete fields from forest tenure
    fieldsToDelete = ['HVA_SKEY', 'FFID', 'CP_ID', 'FEAT_CLASS', 'HVA_ID', 'HVA_MGMTID', 'HVA_MGMTCD', 'HRV_TP_CD', 'HRV_TP_DSC', 'HVA_ST_CD', 'ISSUE_DATE', 'EXTEND_DT', 'CURR_EX_DT', 'QTA_TP_CD', 'CR_LND_CD', 'SAL_TP_CD', 'CASC_SP_CD', 'CATAST_IND', 'CR_GRT_IND', 'CRUISE_IND', 'DECID_IND', 'RETIRE_DT',
                      'FEAT_AREA', 'FEAT_PERIM', 'ADM_DST_CD', 'GEO_DST_CD', 'GEO_DST_NM', 'TM_PRIME', 'MRK_MD_CD', 'MRK_MD_DSC', 'MRK_IN_CD', 'MRK_IN_DSC', 'OTH_TM_IND', 'CL_LOC_CD', 'FILE_TP_CD', 'FILE_ST_CD', 'PFU_MGMTID', 'SB_FND_IND', 'BCTS_ORGCD', 'BCTS_ORGNM', 'MAP_LABEL', 'AREA_SQM', 'FEAT_LEN', 'OBJECTID']

    arcpy.DeleteField_management(forestHarvestingAuthorityCopy, fieldsToDelete)

    # dictionary to rename fields
    forestHarvestingAuthorityRenameDict = {
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
    for i in forestHarvestingAuthorityRenameDict:
        arcpy.AlterField_management(
            forestHarvestingAuthorityCopy, i, forestHarvestingAuthorityRenameDict[i])

    # create copy of lands And delete fields that aren't wanted in final product
    htgLandsCopy = arcpy.CopyFeatures_management(
        htgLandsPath, "htglandsCopy")

    fieldsToDeletehtgLands = ['ATTRIBUTE_', 'EN', 'GEOMETRY_S', 'H_', 'Ha', 'ICF', 'ICF_AREA', 'ICIS', 'JUROL', 'LAND_ACT_P', 'LAND_DISTR', 'LEGAL_FREE', 'LOCALAREA', 'LTSA_BLOCK', 'LTSA_LOT', 'LTSA_PARCE', 'LTSA_PLAN', 'OWNER_CLAS', 'OtherComme', 'PARCEL_DES', 'PID', 'PIN', 'PIN_DISTLE', 'PIN_SUBDLA', 'PMBC', 'RoW', 'SOURCE_PRO', 'TEMP_PolyI', 'TENURES', 'TimbeTable', 'Title_Info', 'Title_num', 'Title_owne', 'access',
                              'apprais2BC', 'apprais2HB', 'apprais2Ha', 'apprais2re', 'appraisal2', 'arch_sites', 'avail_issu', 'available', 'comments', 'confirm_qu', 'ess_respon', 'essential', 'guide_outf', 'interests', 'label', 'landval_20', 'landval_sr', 'location', 'municipali', 'needs_conf', 'owner', 'potential_', 'prop_class', 'result_val', 'selected', 'specific_l', 'tourism_ca', 'trapline', 'use_on_pro', 'valperHa_2', 'zone_code', 'zoning', "Shape_Leng", "Shape_Area", "new_owners", "ownership_"]

    arcpy.DeleteField_management(htgLandsCopy, fieldsToDeletehtgLands)

    # intersect forest tenure with HTG lands
    forestHarvestingAuthorityProcessedPath = arcpy.Intersect_analysis([forestHarvestingAuthorityCopy, htgLandsCopy],
                                                                      fileName, join_attributes="NO_FID")

    print("Forest tenure and lands intersected")

    # calculate geometry
    arcpy.AddField_management(
        forestHarvestingAuthorityProcessedPath, "HA", "FLOAT")

    arcpy.CalculateGeometryAttributes_management(
        forestHarvestingAuthorityProcessedPath, [["HA", "AREA"]], area_unit="HECTARES")

    print("HA calculated")

    # remove working files
    arcpy.management.Delete(htgLandsCopy)
    arcpy.management.Delete(tempGdbPath)

    return forestHarvestingAuthorityProcessedPath


def forestHarvestingAuthorityProcess(downloadFolder, currentForestHarvestingAuthorityPath, archiveFolder, fileName, htgLandsPath, arcgisWorkspaceFolder, jsonPayload):
    archiving(currentForestHarvestingAuthorityPath, archiveFolder)
    forestHarvestingAuthorityGeoprocessing(catalogueWarehouseDownload(
        downloadFolder, jsonPayload, fileName), downloadFolder, fileName, htgLandsPath, arcgisWorkspaceFolder)

# test
#forestHarvestingAuthorityProcess(forestHarvestingAuthoritySettings.downloadFolder, forestHarvestingAuthoritySettings.currentPath, forestHarvestingAuthoritySettings.archiveFolder, forestHarvestingAuthoritySettings.fileName, universalSettings.htgLandsPath, forestHarvestingAuthoritySettings.arcgisWorkspaceFolder, forestHarvestingAuthoritySettings.jsonPayload)

####################################################################################################################
# forest tenure managed licence
####################################################################################################################


def forestManagedLicenceGeoprocessing(rawForestManagedLicence, downloadFolder, fileName, htgLandsPath, arcgisWorkspaceFolder):
    # environment settings
    arcpy.env.workspace = arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    # get name of Raw shape file
    rawName = path.splitext(
        arcpy.Describe(rawForestManagedLicence).name)[0]

    # create temporary GDB and copy raw shape file to it
    arcpy.CreateFileGDB_management(downloadFolder, "temp.gdb")
    tempGdbPath = f"{downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(
        rawForestManagedLicence, tempGdbPath)

    print("Raw Shapefile copied to temp Geodatabase")

    forestManagedLicenceCopy = f"{tempGdbPath}\\{rawName}"

    # delete fields
    fieldsToDelete = ['MPBLCKD', 'MLTPCD', 'ML_COMMENT', 'RTRMNTDT', 'MNDMNTD', 'MAP_LABEL',
                      'FEAT_AREA', 'FTRPRMTR', 'FTRCLSSSK', 'FLSTTSCD', 'DMNDSTRCTC', 'AREA_SQM', 'FEAT_LEN', 'OBJECTID']

    arcpy.DeleteField_management(forestManagedLicenceCopy, fieldsToDelete)

    print("Fields Deleted")

    # rename fields
    forestManagedLicenceRenameDict = {
        "CLNTNM": "Client", "FRSTFLD": "PermitID", "CLNTNMBR": "ClientNum", "DMNDSTRCTN": "District", "LFCCLSTTSC": "Status"
    }

    for i in forestManagedLicenceRenameDict:
        arcpy.AlterField_management(
            forestManagedLicenceCopy, i, forestManagedLicenceRenameDict[i])

    arcpy.AddField_management(forestManagedLicenceCopy, "ClientGrp", "TEXT")

    # Update EXPIRY_DT
    cursor = arcpy.da.UpdateCursor(
        forestManagedLicenceCopy, ["Client", "ClientGrp"]
    )

    for row in cursor:
        if row[0] in ("HALALT FIRST NATION", "LYACKSON FIRST NATION", "PENELAKUT FIRST NATION"):
            row[1] = "HTG"
        elif row[0] in ("MALAHAT TENURE HOLDING LTD.", "STZ'UMINUS FIRST NATION"):
            row[1] = "other FN"
        else:
            row[1] = "other"

        cursor.updateRow(row)

    del cursor

    print("EXPIRY_DT updated")

    # create HTG lands copy and delete fields from it
    fieldsToDeletehtgLands = ['LOCALAREA', 'ICF_AREA', 'GEOMETRY_S', 'ATTRIBUTE_', 'PID', 'PIN', 'JUROL', 'LTSA_LOT', 'LTSA_BLOCK', 'LTSA_PARCE', 'LTSA_PLAN', 'LEGAL_FREE', 'LAND_DISTR', 'LAND_ACT_P', 'PARCEL_DES', 'OWNER_CLAS', 'SOURCE_PRO', 'landval_20', 'valperHa_2', 'result_val', 'Ha', 'comments', 'new_owners', 'PMBC', 'ICIS', 'ICF', 'landval_sr', 'prop_class', 'needs_conf', 'confirm_qu', 'selected', 'selected_b', 'label', 'location', 'specific_l', 'H_',
                              'use_on_pro', 'potential_', 'interests', 'available', 'avail_issu', 'owner', 'EN', 'guide_outf', 'trapline', 'ess_respon', 'tourism_ca', 'access', 'zoning', 'zone_code', 'TENURES', 'PIN_DISTLE', 'PIN_SUBDLA', 'municipali', 'arch_sites', 'Title_num', 'Title_owne', 'Title_Info', 'essential', 'RoW', 'OtherComme', 'appraisal2', 'apprais2HB', 'apprais2re', 'apprais2BC', 'apprais2Ha', 'TEMP_PolyI', 'TimbeTable', 'ownership_', 'Shape_Leng', 'Shape_Area']

    htgLandsCopy = arcpy.CopyFeatures_management(
        htgLandsPath, "htglandsCopy")
    arcpy.DeleteField_management(htgLandsCopy, fieldsToDeletehtgLands)

    print("Fields from HTG copy deleted")

    # intersect HTG lands and forest managed licenses
    forestManagedLicenceProcessedPath = arcpy.Intersect_analysis([forestManagedLicenceCopy, htgLandsCopy],
                                                                 fileName, join_attributes="NO_FID")

    # calculate geometry
    arcpy.AddField_management(
        forestManagedLicenceProcessedPath, "HA", "FLOAT")

    arcpy.CalculateGeometryAttributes_management(
        forestManagedLicenceProcessedPath, [["HA", "AREA"]], area_unit="HECTARES")

    # remove working files
    arcpy.management.Delete(htgLandsCopy)
    arcpy.management.Delete(tempGdbPath)


def forestManagedLicenceProcess(downloadFolder, currentForestManagedLicencePath, archiveFolder, fileName, htgLandsPath, arcgisWorkspaceFolder, jsonPayload, rawDownloadFolderName, rawShapefileName):
    archiving(currentForestManagedLicencePath, archiveFolder)
    forestManagedLicenceGeoprocessing(catalogueWarehouseDownload(
        downloadFolder, jsonPayload, rawDownloadFolderName, rawShapefileName), downloadFolder, fileName, htgLandsPath, arcgisWorkspaceFolder)


####################################################################################################################
# Harvested areas of BC (Consolidated Cut Blocks)
####################################################################################################################


def harvestedAreasGeoprocessing(rawHarvestedAreas, downloadFolder, fileName, htgLandsPath, arcgisWorkspaceFolder):

    # environment settings
    arcpy.env.workspace = arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    # get name of Raw shape file
    rawName = path.splitext(
        arcpy.Describe(rawHarvestedAreas).name)[0]

    # create temporary GDB and copy raw shape file to it
    arcpy.CreateFileGDB_management(downloadFolder, "temp.gdb")
    tempGdbPath = f"{downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(
        rawHarvestedAreas, tempGdbPath)

    print("Raw Shapefile copied to temp Geodatabase")

    harvestedAreasCopy = f"{tempGdbPath}\\{rawName}"

    # delete fields
    fieldsToDelete = ['OPENINGID', 'AREA_SQM',
                      'FTLENGTHM', 'SHAPE_1', 'OBJECTID']

    arcpy.DeleteField_management(harvestedAreasCopy, fieldsToDelete)

    #Field rename
    harvestedAreasRenameDict = {
        "CUTBLOCKID": "CUTBLOCKID",
        "HARVESTYR": "HARVESTYR",
        "DSTRBSTDT": "startdate",
        "DSTRBEDDT": "enddate",
        "DATASOURCE": "DATASOURCE",
        "AREAHA": "HA"
    }

    for i in harvestedAreasRenameDict:
        arcpy.AlterField_management(
            harvestedAreasCopy, i, harvestedAreasRenameDict[i])


    print("Fields Deleted")

    cursor = arcpy.da.UpdateCursor(
        harvestedAreasCopy, ["startdate", "enddate"]
    )

    # change date format in stardate, enddate
    for row in cursor:
        if row[0] != " ":
            row[0] = f"{row[0][0:4]}_{row[0][4:6]}"
            row[1] = f"{row[1][0:4]}_{row[1][4:6]}"
    
        cursor.updateRow(row)
    
    del cursor


    # create HTG lands copy and delete fields from it
    fieldsToDeletehtgLands = ['LOCALAREA', 'ICF_AREA', 'GEOMETRY_S', 'ATTRIBUTE_', 'PID', 'PIN', 'JUROL', 'LTSA_LOT', 'LTSA_BLOCK', 'LTSA_PARCE', 'LTSA_PLAN', 'LEGAL_FREE', 'LAND_DISTR', 'LAND_ACT_P', 'PARCEL_DES', 'OWNER_CLAS', 'SOURCE_PRO', 'landval_20', 'valperHa_2', 'result_val', 'Ha', 'comments', 'new_owners', 'PMBC', 'ICIS', 'ICF', 'landval_sr', 'prop_class', 'needs_conf', 'confirm_qu', 'selected', 'label', 'location', 'specific_l', 'H_',
                              'use_on_pro', 'potential_', 'interests', 'available', 'avail_issu', 'owner', 'EN', 'guide_outf', 'trapline', 'ess_respon', 'tourism_ca', 'access', 'zoning', 'zone_code', 'TENURES', 'PIN_DISTLE', 'PIN_SUBDLA', 'municipali', 'arch_sites', 'Title_num', 'Title_owne', 'Title_Info', 'essential', 'RoW', 'OtherComme', 'appraisal2', 'apprais2HB', 'apprais2re', 'apprais2BC', 'apprais2Ha', 'TEMP_PolyI', 'TimbeTable', 'ownership_', 'Shape_Leng', 'Shape_Area']

    htgLandsCopy = arcpy.CopyFeatures_management(
        htgLandsPath, "htglandsCopy")
    arcpy.DeleteField_management(htgLandsCopy, fieldsToDeletehtgLands)

    print("Fields from HTG copy deleted")

    # intersect HTG landS and harvested areas        
    harvestedAreasProcessedPath = arcpy.Intersect_analysis([harvestedAreasCopy, htgLandsCopy],
                                                                 fileName, join_attributes="NO_FID")


    arcpy.CalculateGeometryAttributes_management(
        harvestedAreasProcessedPath, [["HA", "AREA"]], area_unit="HECTARES")

    # remove working files
    arcpy.management.Delete(htgLandsCopy)
    arcpy.management.Delete(tempGdbPath)

def harvestedAreasProcess(downloadFolder, currentForestManagedLicencePath, archiveFolder, fileName, htgLandsPath, arcgisWorkspaceFolder, jsonPayload, rawDownloadFolderName, rawShapefileName):
    archiving(currentForestManagedLicencePath, archiveFolder)
    harvestedAreasGeoprocessing(catalogueWarehouseDownload(
        downloadFolder, jsonPayload, rawDownloadFolderName, rawShapefileName), downloadFolder, fileName, htgLandsPath, arcgisWorkspaceFolder)


####################################################################################################################
# recreation datasets
####################################################################################################################

def recreationDownload():
    print("Starting Parks download")
    settingsList = nanaimoParksSettings, northCowichanParksSettings, cvrdParksSettings

    filePaths = list(flatten([shapeFileDownloadUnzip(i.downloadURL, i.downloadFolder, i.fileName) for i in settingsList]))

    dataList = [(parksEcologicalProtectedSettings.downloadFolder, parksEcologicalProtectedSettings.jsonPayload, parksEcologicalProtectedSettings.fileName), (northCowichanParksSettings.downloadFolder, nationalParksSettings.jsonPayload, nationalParksSettings.fileName), (recreationPolygonsSettings.downloadFolder, recreationPolygonsSettings.jsonPayload, recreationPolygonsSettings.fileName)]

    for i in dataList:
        filePaths.append(catalogueWarehouseDownload(*i))
    
    print("Finished Parks Donnload")
    return filePaths

def northCowichanRecreationGeoprocessing(rawPath):
    downloadFolder = northCowichanParksSettings.downloadFolder
    arcgisWorkspaceFolder = downloadFolder
    
    arcpy.env.workspace = arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    print("Starting North Cowichan Recreation Geoprocessing")

    # get name of Raw shape fileNo
    rawName = path.splitext(
        arcpy.Describe(rawPath).name)[0]

    # Create a temporary GDB and create a copy feature class in it. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(downloadFolder, "temp.gdb")
    tempGdbPath = f"{downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(
        rawPath, tempGdbPath)

    northCowichanRecreationCopy = f"{tempGdbPath}\\{rawName}"

    #delete fields    
    fieldsToDelete = ["fme_type", "RESPONSIBI","PUBLIC_MAP", "STATUS", "LOCATION", "PARK_ID"]

    arcpy.DeleteField_management(northCowichanRecreationCopy, fieldsToDelete)

    # add fields
    fieldsToAdd = ["parkOwner", "Municiplty", "Source", "SOI", "HA"]
    
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(northCowichanRecreationCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(northCowichanRecreationCopy, i, "TEXT")   

    # rename fields
    renameDict = {"PARK_NAME": "parkName", "PARK_CLASS":"parkClass", "PARK_TYPE": "parkType"
    }

    for i in renameDict:
        arcpy.AlterField_management(northCowichanRecreationCopy, i, renameDict[i], renameDict[i])
    
    cursor = arcpy.da.UpdateCursor(northCowichanRecreationCopy, ["parkType", "parkOwner", "Municiplty", "Source", "SOI", "parkClass"])

    # field calculation

    for row in cursor:
        row[0],row[1], row[2], row[3], row[4]= "municipal", "North Cowichan", "North Cowichan", "North Cowichan Parks/Recreation", "core"
        cursor.updateRow(row)
    
    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        northCowichanRecreationCopy, [["HA", "AREA"]], area_unit="HECTARES")
    
    # convert back to shape file
    northCowichanRecreationCopy = arcpy.CopyFeatures_management(northCowichanRecreationCopy, "tempNCRecreation.shp")

    #Delete extraneous fields and temp GDB
    arcpy.DeleteField_management(northCowichanRecreationCopy, ["Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(tempGdbPath)
    
    print("Finished North Cowichan Recreation Geoprocessing")
    return northCowichanRecreationCopy


def northCowichanNonDNCRecreationGeoprocessing(rawPath):
    
    downloadFolder = northCowichanParksSettings.downloadFolder
    arcpy.env.workspace = downloadFolder
    arcpy.env.overwriteOutput = True
    print("Starting north Cowichan non-DNC Recreation geoprocessing")

    # get Name of Raw shape file
    rawName = path.splitext(
        arcpy.Describe(rawPath).name)[0]

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(downloadFolder, "temp.gdb")
    tempGdbPath = f"{downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(
        rawPath, tempGdbPath)

    northCowichanNonDNCRecreationCopy = f"{tempGdbPath}\\{rawName}"
    
    #delete fields
    fieldsToDelete = ["fme_type", "RESPONSIBI","PUBLIC_MAP", "STATUS", "LOCATION", "PARK_ID"]

    arcpy.DeleteField_management(northCowichanNonDNCRecreationCopy, fieldsToDelete)

    fieldsToAdd = ["parkOwner", "Municiplty", "Source", "SOI", "HA"]
    
    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(northCowichanNonDNCRecreationCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(northCowichanNonDNCRecreationCopy, i, "TEXT")   

    renameDict = {"PARK_NAME": "parkName", "PARK_CLASS":"parkClass", "PARK_TYPE": "parkType"
    }

    # rename fields
    for i in renameDict:
        arcpy.AlterField_management(northCowichanNonDNCRecreationCopy, i, renameDict[i], renameDict[i])
    
    # field calculations
    cursor = arcpy.da.UpdateCursor(northCowichanNonDNCRecreationCopy, ["parkType", "parkOwner", "Municiplty", "Source", "SOI", "parkClass"])

    for row in cursor:
        if row[5] not in ("Athletic/Sportsfield Park", "Recreation Facility", "Provincial Park"): 
            row[0],row[1], row[2], row[3], row[4]= "regional", None, "North Cowichan", "North Cowichan Parks/NonDNCRecreation", "core"
            cursor.updateRow(row)
        else:
            cursor.deleteRow()

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        northCowichanNonDNCRecreationCopy, [["HA", "AREA"]], area_unit="HECTARES")
    
    # transfer Back to shapefile
    northCowichanNonDNCRecreationCopy = arcpy.CopyFeatures_management(northCowichanNonDNCRecreationCopy, "tempNCNonDNCParks.shp")

    #delete extraneous fields and temp GDB
    arcpy.DeleteField_management(northCowichanNonDNCRecreationCopy, ["Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(tempGdbPath)

    print("Finished North Cowichan non-DNC recreation geoprocessing")
    
    return northCowichanNonDNCRecreationCopy


def northCowichanForestryRecreationGeoprocessing(rawPath):
    
    downloadFolder = northCowichanParksSettings.downloadFolder
    arcpy.env.workspace = downloadFolder
    arcpy.env.overwriteOutput = True
    print("Starting north Cowichan Forestry Recreation geoprocessing")

    # get Name of Raw shape file
    rawName = path.splitext(
        arcpy.Describe(rawPath).name)[0]

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(downloadFolder, "temp.gdb")
    tempGdbPath = f"{downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(
        rawPath, tempGdbPath)

    northCowichanForestryRecreationCopy = f"{tempGdbPath}\\{rawName}"
    
    #delete fields
    fieldsToDelete = ["fme_type", "RESPONSIBI","PUBLIC_MAP", "STATUS", "LOCATION", "PARK_ID"]

    arcpy.DeleteField_management(northCowichanForestryRecreationCopy, fieldsToDelete)

    fieldsToAdd = ["parkOwner", "Municiplty", "Source", "SOI", "HA"]
    
    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(northCowichanForestryRecreationCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(northCowichanForestryRecreationCopy, i, "TEXT")   

    renameDict = {"PARK_NAME": "parkName", "PARK_CLASS":"parkClass", "PARK_TYPE": "parkType"
    }

    # rename fields
    for i in renameDict:
        arcpy.AlterField_management(northCowichanForestryRecreationCopy, i, renameDict[i], renameDict[i])
    
    # field calculations
    cursor = arcpy.da.UpdateCursor(northCowichanForestryRecreationCopy, ["parkType", "parkOwner", "Municiplty", "Source", "SOI", "parkName"])

    for row in cursor:
        if row[5] != "Osborne Bay Park": 
            row[0],row[1], row[2], row[3], row[4]= "municipal forest", "North Cowichan", "North Cowichan", "North Cowichan Parks/Forestry Recreation", "core"
            cursor.updateRow(row)
        else:
            cursor.deleteRow()

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        northCowichanForestryRecreationCopy, [["HA", "AREA"]], area_unit="HECTARES")
    
    # transfer Back to shapefile
    northCowichanForestryRecreationCopy = arcpy.CopyFeatures_management(northCowichanForestryRecreationCopy, "tempNCForestryRec.shp")

    #delete extraneous fields and temp GDB
    arcpy.DeleteField_management(northCowichanForestryRecreationCopy, ["Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(tempGdbPath)

    print("Finished North Cowichan Forestry recreation geoprocessing")
    
    return northCowichanForestryRecreationCopy


def parksEcologicalProtectedGeoprocessing(rawPath):
    
    downloadFolder = parksEcologicalProtectedSettings.downloadFolder
    arcpy.env.workspace = downloadFolder
    arcpy.env.overwriteOutput = True
    print("starting BC Parks, Ecological, Rserve Areas Geoprocessing")


    # get Name of Raw shape file
    rawName = path.splitext(
        arcpy.Describe(rawPath).name)[0]

    # clip to htg AOI
    clippedFeatures =arcpy.Clip_analysis(rawPath, universalSettings.aoiPath, rawName)

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(downloadFolder, "temp.gdb")
    tempGdbPath = f"{downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(
        clippedFeatures, tempGdbPath)

    parksEcologicalProtectedCopy = f"{tempGdbPath}\\{rawName}"
    
    
    #delete fields
    fieldsToDelete =  ['ADMIN_AREA', 'PROT_CODE', 'SRV_GEN_PL', 'ORC_PRIMRY', 'ORC_SCNDRY', 'F_CODE', 'SHAPE_1', 'AREA_SQM', 'FEAT_LEN', 'OBJECTID']

    arcpy.DeleteField_management(parksEcologicalProtectedCopy, fieldsToDelete)

    fieldsToAdd = ["parkOwner", "Municiplty", "Source", "HA"]
    
    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(parksEcologicalProtectedCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(parksEcologicalProtectedCopy, i, "TEXT")   

    renameDict = {"PROT_NAME": "parkName", "PARK_CLASS":"parkClass", "PROT_DESG": "parkType"
    }

    # rename fields
    for i in renameDict:
        arcpy.AlterField_management(parksEcologicalProtectedCopy, i, renameDict[i], renameDict[i])
    
    # intersect wwith SOI
    parksEcologicalProtectedCopy =arcpy.Intersect_analysis([parksEcologicalProtectedCopy, universalSettings.soiPath], "tempParksEcoPro_SOIintersect", join_attributes="NO_FID")
    
    # field calculations
    cursor = arcpy.da.UpdateCursor(parksEcologicalProtectedCopy, ["parkClass", "parkOwner", "Source", "parkType"])

    for row in cursor:
        row[1], row[2] = "BC", "BC Parks data"
        if row[3] == " ":
            row[3] = row[4]
        
        cursor.updateRow(row)

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        parksEcologicalProtectedCopy, [["HA", "AREA"]], area_unit="HECTARES")
    

    #delete extraneous fields and temp GDB
    arcpy.DeleteField_management(parksEcologicalProtectedCopy, ["Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(clippedFeatures)
    arcpy.management.Delete(tempGdbPath)

    print("Finished BC Parks, Ecological, Reserve areas geoprocessing")
    
    return parksEcologicalProtectedCopy


def nationalParksGeoprocessing(rawPath):
    
    downloadFolder = nationalParksSettings.downloadFolder
    arcpy.env.workspace = downloadFolder
    arcpy.env.overwriteOutput = True
    print("starting National Parks Geoprocessing")


    # get Name of Raw shape file
    rawName = path.splitext(
        arcpy.Describe(rawPath).name)[0]

    # clip to htg AOI
    clippedFeatures =arcpy.Clip_analysis(rawPath, universalSettings.aoiPath, rawName)

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(downloadFolder, "temp.gdb")
    tempGdbPath = f"{downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(
        clippedFeatures, tempGdbPath)

    nationalParksCopy = f"{tempGdbPath}\\{rawName}"
    
    
    #delete fields
    fieldsToDelete =  ['NTL_PRK_ID', 'CLAB_ID', 'FRENCH_NM', 'LOCAL_NM', 'AREA_SQM', 'FEAT_LEN', 'OBJECTID']

    arcpy.DeleteField_management(nationalParksCopy, fieldsToDelete)

    fieldsToAdd = ["parkType", "parkClass", "parkOwner", "Municiplty", "Source", "HA"]
    
    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(nationalParksCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(nationalParksCopy, i, "TEXT")   
    
    # rename fields
    renameDict = {"ENGLISH_NM": "parkName"}
   
    for i in renameDict.keys():
        arcpy.AlterField_management(nationalParksCopy, i, renameDict[i], renameDict[i])
    
    # intersect with SOI
    nationalParksCopy =arcpy.Intersect_analysis([nationalParksCopy, universalSettings.soiPath], "tempNatParks_SOIintersect", join_attributes="NO_FID")
    
    # field calculations
    cursor = arcpy.da.UpdateCursor(nationalParksCopy, ["parkType", "parkClass", "parkOwner", "Municiplty", "Source",])

    for row in cursor:
        row[0], row[1], row[2], row[3],row[4] = "national", "national", "Canada", " ", "National Parks"

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        nationalParksCopy, [["HA", "AREA"]], area_unit="HECTARES")
    

    #delete extraneous fields and temp GDB
    arcpy.DeleteField_management(nationalParksCopy, ["Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(clippedFeatures)
    arcpy.management.Delete(tempGdbPath)

    print("Finished National parks geoprocessing")
    
    return nationalParksCopy


def recreationPolygonsGeoprocessing(rawPath):
    downloadFolder = recreationPolygonsSettings.downloadFolder
    arcpy.env.workspace = downloadFolder
    arcpy.env.overwriteOutput = True

    print("starting Recreation polygons Geoprocessing")


    # get Name of Raw shape file
    rawName = path.splitext(
        arcpy.Describe(rawPath).name)[0]

    # clip to htg AOI
    clippedFeatures =arcpy.Clip_analysis(rawPath, universalSettings.aoiPath, rawName)

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(downloadFolder, "temp.gdb")
    tempGdbPath = f"{downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(
        clippedFeatures, tempGdbPath)

    recreationPolygonsCopy = f"{tempGdbPath}\\{rawName}"
    
    
    #delete fields
    fieldsToDelete =  ['RMF_SKEY', 'FFID', 'SECTION_ID', 'REC_MF_CD', 'RETIRE_DT', 'AMEND_ID', 'MAP_LABEL', 'REC_FT_CD', 'RES_FT_IND', 'ARCH_IND', 'SITE_LOC', 'PROJ_DATE', 'REC_VW_IND', 'RECDIST_CD', 'DEF_CAMPS', 'LIFE_ST_CD', 'FILE_ST_CD', 'GEO_DST_CD', 'GEO_DST_NM', 'FEAT_CLASS', 'FEAT_AREA', 'FEAT_PERIM', 'AREA_SQM', 'FEAT_LEN', 'OBJECTID']

    arcpy.DeleteField_management(recreationPolygonsCopy, fieldsToDelete)

    fieldsToAdd = ["parkClass", "parkOwner", "Municiplty", "Source", "HA"]
    
    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(recreationPolygonsCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(recreationPolygonsCopy, i, "TEXT")   
    
    # rename fields
    renameDict = {"PROJECT_NM": "parkName", "PROJECT_TP": "parkType"}
   
    for i in renameDict.keys():
        arcpy.AlterField_management(recreationPolygonsCopy, i, renameDict[i], renameDict[i])
    
    # intersect with SOI
    recreationPolygonsCopy =arcpy.Intersect_analysis([recreationPolygonsCopy, universalSettings.soiPath], "tempRecPoly_SOIintersect", join_attributes="NO_FID")
    
    # field calculations
    cursor = arcpy.da.UpdateCursor(recreationPolygonsCopy, ["parkClass", "Municiplty", "Source", "parkType"])

    for row in cursor:
        row[0], row[1], row[2] = row[3], " ", "Recreation Polygons"
        cursor.updateRow(row)
    
    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        recreationPolygonsCopy, [["HA", "AREA"]], area_unit="HECTARES")
    

    #delete extraneous fields and temp GDB
    arcpy.DeleteField_management(recreationPolygonsCopy, ["Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(clippedFeatures)
    arcpy.management.Delete(tempGdbPath)

    print("Finished Recreation polygons geoprocessing")
    
    return recreationPolygonsCopy


def nanaimoCityParksGeoprocessing(rawPath):
    
    downloadFolder = nanaimoParksSettings.downloadFolder
    arcpy.env.workspace = downloadFolder
    arcpy.env.overwriteOutput = True

    print("starting nanaimo parks Geoprocessing")


    # get Name of Raw shape file
    rawName = path.splitext(
        arcpy.Describe(rawPath).name)[0]

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(downloadFolder, "temp.gdb")
    tempGdbPath = f"{downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(
        rawPath, tempGdbPath)

    nanaimoCityParksCopy = f"{tempGdbPath}\\{rawName}"
    
    
    #delete fields
    fieldsToDelete =  ['PARKID', 'PARKADDRES', 'GLOBALID', 'AREA']

    arcpy.DeleteField_management(nanaimoCityParksCopy, fieldsToDelete)

    fieldsToAdd = ["parkType", "parkClass", "Municiplty", "Source", "SOI", "HA"]
    
    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(nanaimoCityParksCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(nanaimoCityParksCopy, i, "TEXT")        

    
    # rename fields
    
    arcpy.AlterField_management(nanaimoCityParksCopy, "PARKNAME", "thisisasillybug")

    renameDict = {"CITYOWNED":"parkOwner", "thisisasillybug": "parkName"}

    for i in renameDict:
        arcpy.AlterField_management(nanaimoCityParksCopy, i, renameDict[i], renameDict[i], field_length= 50)  
        
    # field calculations
    cursor = arcpy.da.UpdateCursor(nanaimoCityParksCopy, ["parkClass", "parkType", "parkOwner", "Municiplty", "Source", "SOI"])

    for row in cursor:
        row[0], row[1], row[3], row[4], row[5] =  "municipal", "municipal", "Nanaimo", "Nanaimo City Parks", "marine"
        if row[2] == "Yes":
            row[2] = "Nanaimo"
        else:
            row[2] = " "
            
        cursor.updateRow(row)
    
    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        nanaimoCityParksCopy, [["HA", "AREA"]], area_unit="HECTARES")
    
    # transfer Back to shapefile
    nanaimoCityParksCopy = arcpy.CopyFeatures_management(nanaimoCityParksCopy, "tempNanaimoParks.shp")

    #delete extraneous fields and temp GDB
    arcpy.DeleteField_management(nanaimoCityParksCopy, ["Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(tempGdbPath)

    print("Finished Nanaimo Parks geoprocessing")
    
    return nanaimoCityParksCopy


def cvrdParksGeoprocessing(rawPath):
    
    downloadFolder = cvrdParksSettings.downloadFolder
    arcpy.env.workspace = downloadFolder
    arcpy.env.overwriteOutput = True

    print("starting cvrd parks Geoprocessing")

    # get Name of Raw shape file
    rawName = path.splitext(
        arcpy.Describe(rawPath).name)[0]

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(downloadFolder, "temp.gdb")
    tempGdbPath = f"{downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(
        rawPath, tempGdbPath)

    cvrdParksCopy = f"{tempGdbPath}\\{rawName}"
    
    #delete fields
    fieldsToDelete =  ['Status', 'Shape_Leng']

    arcpy.DeleteField_management(cvrdParksCopy, fieldsToDelete)

    fieldsToAdd = ["Municiplty", "Source", "SOI", "HA"]
    
    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(cvrdParksCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(cvrdParksCopy, i, "TEXT")        

    
    # rename fields
    renameDict = {"ParkName":"parkName", "ParkType": "parkClass", "Administra":"parkOwner"}


    for i in renameDict:
        arcpy.AlterField_management(cvrdParksCopy, i, renameDict[i], renameDict[i])  

    #add parkType
    arcpy.AddField_management(cvrdParksCopy, "parkType", "TEXT")
        
    # field calculations
    cursor = arcpy.da.UpdateCursor(cvrdParksCopy, ["parkType", "Source", "SOI", "parkOwner"])

    for row in cursor:
        if row[3] in ('Crown Provincial', 'Municipality of North Cowichan'):
            cursor.deleteRow()
        else:
            row[0], row[1], row[2] =  "regional", "CVRD Parks", " "
            cursor.updateRow(row)
    
    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        cvrdParksCopy, [["HA", "AREA"]], area_unit="HECTARES")
    
    # transfer Back to shapefile
    cvrdParksCopy = arcpy.CopyFeatures_management(cvrdParksCopy, "tempCVRDParks.shp")

    #delete extraneous fields and temp GDB
    arcpy.DeleteField_management(cvrdParksCopy, ["Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(tempGdbPath)

    print("Finished cvrd parks geoprocessing")
    
    return cvrdParksCopy


def parksRecreationDatasetsProcess():
    arcpy.env.workspace = parksRecreationDatasetsSettings.arcgisWorkspaceFolder
    try:
        archiving(parksRecreationDatasetsSettings.currentPath, parksRecreationDatasetsSettings.archiveFolder)
    except:
        print("Can't Archive. Check File Path")
    #NOTE, north cowicahn parks are fragile if names change

    rawFilePaths = recreationDownload()
    processedFilePaths = []

    for filePath in rawFilePaths:
        if northCowichanParksSettings.fileName in filePath and "ForestryRecreation" in filePath:
            processedFilePaths.append(northCowichanForestryRecreationGeoprocessing(filePath))
        elif northCowichanParksSettings.fileName in filePath and "nonDNCRecreation" in filePath:
            processedFilePaths.append(northCowichanNonDNCRecreationGeoprocessing(filePath))
        elif northCowichanParksSettings.fileName in filePath and path.split(filePath)[1] == "Recreation":
            processedFilePaths.append(northCowichanRecreationGeoprocessing(filePath))
        elif cvrdParksSettings.fileName in filePath:
            processedFilePaths.append(cvrdParksGeoprocessing(filePath))
        elif nanaimoParksSettings.fileName in filePath:
            processedFilePaths.append(nanaimoCityParksGeoprocessing(filePath))
        elif recreationPolygonsSettings.fileName in filePath:
            processedFilePaths.append(recreationPolygonsGeoprocessing(filePath))
        elif nationalParksSettings.fileName in filePath:
            processedFilePaths.append(nationalParksGeoprocessing(filePath))
        elif parksEcologicalProtectedSettings.fileName in filePath:
            processedFilePaths.append(parksEcologicalProtectedGeoprocessing(filePath))
        
    recreationMerged = arcpy.Merge_management(processedFilePaths, parksRecreationDatasetsSettings.fileName)

    return recreationMerged


####################################################################################################################
# Parcel fabric file Geodatabase
####################################################################################################################

def parcelMapBCGeoprocessing(rawPath):
    
    print("Starting Parcel Map Geoprocessing")

    newGDB = arcpy.CreateFileGDB_management(parcelMapBCSettings.downloadFolder, "parcelMapContainer")

    arcpy.env.workspace = newGDB
    arcpy.env.overwriteOutput = True
    
    #NOTE may be best to work with original data, copying takes a long time
    parcelMapCopy= arcpy.CopyFeatures_management(rawPath, "tempParcelMapCopy")

    fieldsToDelete = ['PARCEL_FABRIC_POLY_ID', 'PARCEL_STATUS', 'PARCEL_CLASS', 'PARCEL_START_DATE', 'WHEN_UPDATED', 'FEATURE_AREA_SQM', 'FEATURE_LENGTH_M', 'SE_ANNO_CAD_DATA']

    arcpy.DeleteField_management(parcelMapCopy, fieldsToDelete)

    print("Finished Copying Parcelmap")


    parcelMapProcessedPath = arcpy.Intersect_analysis([parcelMapCopy, universalSettings.soiPath], parcelMapBCSettings.fileName)

    arcpy.management.Delete(parcelMapCopy)

    print("Finished Parcel Map Geoprocessing")

    return parcelMapProcessedPath


def parcelMapBCProcess():
    try:
        archiving(parcelMapBCSettings.currentPath, parcelMapBCSettings.archiveFolder)
    except:
        print("Can't Archive. Check File Path")
   
    parcelMapBCGeoprocessing(catalogueWarehouseDownload(parcelMapBCSettings.downloadFolder, parcelMapBCSettings.jsonPayload, parcelMapBCSettings.fileName))


####################################################################################################################
# Road Atlas
####################################################################################################################

def digitalRoadAtlasGeoprocessing(rawPath):
    print("starting road atlas geoprocessing")

    arcpy.env.workspace = digitalRoadAtlasSettings.arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    #NOTE, maybe best to work with original data for this one... Copying takes a long time
    print("Copying features")
    roadAtlasCopy= arcpy.CopyFeatures_management(rawPath, "tempRoad.shp")

    fieldsToDelete = ['FTYPE', 'HWYEXITNUM', 'HWYRTENUM', 'SEGLNGTH2D', 'SEGLNGTH3D', 'RDALIAS1ID', 'RDALIAS3', 'RDALIAS3ID', 'RDALIAS4', 'RDALIAS4ID', 'RDNAMEID', 'FNODE', 'TNODE', 'SPPLR', 'SPPLR_DTL', 'CPTRCHN', 'FCODE', 'OBJECTID']

    arcpy.DeleteField_management(roadAtlasCopy, fieldsToDelete)

    arcpy.AddField_management(roadAtlasCopy, "road_type", "TEXT", field_length=30)

    cursor = arcpy.da.UpdateCursor(roadAtlasCopy,  ["ROAD_CLASS", "road_type"])

    print("starting field calculations")
    for row in cursor:
        for key in digitalRoadAtlasSettings.valuesDictionary:
            if row[0] in key:
                row[1] = digitalRoadAtlasSettings.valuesDictionary[key]
                cursor.updateRow(row)
                break
    
    del cursor
    
    #NOTE, can we just create multi_part features here instead of disolving then exploding? Do we still want those other fields Because if we dissolve without them aren't they gone??I'm not sure this is really doing what's wanted. Do we want this spatially joined to administrative areas Or municipalities or something then dissolved?? https://catalogue.data.gov.bc.ca/dataset/regional-districts-legally-defined-administrative-areas-of-bc. 

    roadAtlasDisolve = arcpy.Dissolve_management(roadAtlasCopy, "tempRoadDisolve.shp", ["RDNAME", "road_type"], multi_part=False)
    print("Starting Intersect")
    roadAtlasIntersect = arcpy.Intersect_analysis([roadAtlasDisolve, universalSettings.soiPath], digitalRoadAtlasSettings.fileName, "NO_FID")

    arcpy.Delete_management(roadAtlasDisolve)
    arcpy.Delete_management(roadAtlasCopy)
    
    print("Finished Road atlas geoprocessing")

    return roadAtlasIntersect

def digitalRoadAtlasProcess():
    try:
        archiving(digitalRoadAtlasSettings.currentPath, digitalRoadAtlasSettings.archiveFolder)
    except:
        print("Can't Archive, Check file path")
    
    digitalRoadAtlasGeoprocessing((catalogueWarehouseDownload(digitalRoadAtlasSettings.downloadFolder, digitalRoadAtlasSettings.jsonPayload, digitalRoadAtlasSettings.fileName)))


####################################################################################################################
# Alc Alr Polygons
####################################################################################################################

def alcAlrPolygonsGeoprocessing(rawPath):

    arcpy.env.workspace = alcAlrPolygonsSettings.arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True
    
    alcAlrCopy = arcpy.CopyFeatures_management(rawPath, "tempALCALR.shp")

    fieldsToDelete = ['STATUS', 'FTRCD', 'OBJECTID', 'AREA_SQM']

    arcpy.DeleteField_management(alcAlrCopy, fieldsToDelete)

    landsCopy = arcpy.CopyFeatures_management(universalSettings.htgLandsPath, f"{path.split(universalSettings.htgLandsPath)[0]}\\tempLandsCopy")

    landsDeleteFields = ['LOCALAREA', 'ICF_AREA', 'GEOMETRY_SOURCE', 'ATTRIBUTE_SOURCE', 'PID', 'PIN', 'JUROL', 'LTSA_LOT', 'LTSA_BLOCK', 'LTSA_PARCEL', 'LTSA_PLAN', 'LEGAL_FREEFORM', 'LAND_DISTRICT', 'LAND_ACT_PRIMARY_DESCRIPTION', 'PARCEL_DESCRIPTION', 'SOURCE_PROVISION_DATE', 'landval_2017', 'valperHa_2017', 'result_val_2017', 'Ha', 'new_group', 'comments', 'new_ownership', 'PMBC', 'ICIS', 'ICF', 'landval_src', 'prop_class', 'needs_confirm', 'confirm_question', 'selected', 'label', 'location', 'specific_location', 'H_', 'use_on_prop', 'potential_FCyCmPD', 'interests', 'available', 'avail_issues', 'owner', 'EN', 'guide_outfit', 'trapline', 'ess_response', 'tourism_capability', 'access', 'zoning', 'zone_code', 'TENURES', 'parcel_num', 'PIN_DISTLE', 'PIN_SUBDLA', 'municipality', 'arch_sites', 'Title_num', 'Title_owner', 'Title_Info', 'essential', 'RoW', 'OtherComments', 'appraisal2work', 'apprais2HBU', 'apprais2reportID', 'apprais2BC_ID', 'apprais2Ha', 'TEMP_PolyID', 'TimbeTableLink', 'ownership_type']

    arcpy.DeleteField_management(landsCopy, landsDeleteFields)

    arcpy.AlterField_management(landsCopy, "OWNER_CLASS", "CROWN")

    cursor = arcpy.da.UpdateCursor(landsCopy, ["CROWN"])

    for row in cursor:
        if "CROWN" in row[0]:
            row[0] = "yes"
        else:
            row[0] = "no"
        
        cursor.updateRow(row)
    
    del cursor
    
    alcAlrProcessed = arcpy.Intersect_analysis([alcAlrCopy, landsCopy], alcAlrPolygonsSettings.fileName , join_attributes="NO_FID")

    arcpy.DeleteField_management(alcAlrProcessed, ["FEAT_LEN", "Shape_Leng", "Shape_Area"])

    arcpy.Delete_management(alcAlrCopy)
    arcpy.Delete_management(landsCopy)


    return alcAlrProcessed


def alcAlrPolygonsProcess():
    try : 
        archiving(alcAlrPolygonsSettings.currentPath, alcAlrPolygonsSettings.archiveFolder)
    except :
        print("Can't Archive, Check file path")
    
    alcAlrPolygonsGeoprocessing(catalogueWarehouseDownload(alcAlrPolygonsSettings.downloadFolder, alcAlrPolygonsSettings.jsonPayload, alcAlrPolygonsSettings.fileName))

####################################################################################################################
# environmental remediation
####################################################################################################################

def environmentalRemediationSitesGeoprocessing(rawPath):
    
    arcpy.env.workspace = environmentalRemediationSitesSettings.arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    sitesCopy = arcpy.CopyFeatures_management(rawPath, "tempEnvRem.shp")

    fieldsToDelete=['ENV_RMD_ID', 'GEN_DESC', 'VICFILENO', 'REGFILENO', 'COMMON_NM', 'LATITUDE', 'LONGITUDE', 'OBJECTID']

    arcpy.DeleteField_management(sitesCopy, fieldsToDelete)

    shapefileFieldRename(sitesCopy, "SITE_ID", "REMED_ID")
    
    landsCopy = arcpy.CopyFeatures_management(universalSettings.htgLandsPath, f"{path.split(universalSettings.htgLandsPath)[0]}\\tempLandsCopy")

    landsDeleteFields = ['LOCALAREA', 'ICF_AREA', 'GEOMETRY_SOURCE', 'ATTRIBUTE_SOURCE', 'PID', 'PIN', 'JUROL', 'LTSA_LOT', 'LTSA_BLOCK', 'LTSA_PARCEL', 'LTSA_PLAN', 'LEGAL_FREEFORM', 'LAND_DISTRICT', 'LAND_ACT_PRIMARY_DESCRIPTION', 'PARCEL_DESCRIPTION', 'SOURCE_PROVISION_DATE', 'landval_2017', 'valperHa_2017', 'result_val_2017', 'Ha', 'new_group', 'comments', 'new_ownership', 'PMBC', 'ICIS', 'ICF', 'landval_src', 'prop_class', 'needs_confirm', 'confirm_question', 'selected', 'label', 'location', 'specific_location', 'H_', 'use_on_prop', 'potential_FCyCmPD', 'interests', 'available', 'avail_issues', 'owner', 'EN', 'guide_outfit', 'trapline', 'ess_response', 'tourism_capability', 'access', 'zoning', 'zone_code', 'TENURES', 'parcel_num', 'PIN_DISTLE', 'PIN_SUBDLA', 'municipality', 'arch_sites', 'Title_num', 'Title_owner', 'Title_Info', 'essential', 'RoW', 'OtherComments', 'appraisal2work', 'apprais2HBU', 'apprais2reportID', 'apprais2BC_ID', 'apprais2Ha', 'TEMP_PolyID', 'TimbeTableLink', 'ownership_type']

    arcpy.DeleteField_management(landsCopy, landsDeleteFields)

    remediationProcessed = arcpy.Intersect_analysis([landsCopy, sitesCopy], environmentalRemediationSitesSettings.fileName, join_attributes="NO_FID")

    arcpy.DeleteField_management(remediationProcessed, ["Shape_Lengt","Shape_Area"])

    arcpy.Delete_management(landsCopy)
    arcpy.Delete_management(sitesCopy)

    return remediationProcessed

def environmentalRemediationSitesProcess():
    try:
        archiving(environmentalRemediationSitesSettings.currentPath, environmentalRemediationSitesSettings.archiveFolder)
    
    except:
        print("Can't Archive, Check file path")
    
    environmentalRemediationSitesGeoprocessing(catalogueWarehouseDownload(environmentalRemediationSitesSettings.downloadFolder, environmentalRemediationSitesSettings.jsonPayload, environmentalRemediationSitesSettings.fileName))


    
