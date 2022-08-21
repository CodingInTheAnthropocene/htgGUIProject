"""
universalFunctions.py- Functions utilized at various points throughout the application not associated with a particular dataset.
"""
import arcpy
from requests import get
from urllib.request import urlretrieve
from os import path, mkdir, walk, remove
from datetime import datetime
from shutil import rmtree, unpack_archive


def arcpyGetPath(filePath):
    """
    Returns path of spatial data. Most useful for result objects and Geodatabase Feature classes.

    :param filePath: ArcGIS object with a path
    :type filePath: Any ArcGIS compatible file type
    :return: Complete file path
    :rtype: str
    """    
  
    return arcpy.Describe(filePath).catalogPath

def getCurrency(idList):
    """
    Finds the Update date of the most recently updated BC data catalogue dataset from a list of IDs.

    :param idList: list of data catalogue IDs
    :type idList: list
    :return: Update date of most recently updated dataset
    :rtype: datetime.date
    """ 
    # generate list of update dates from BC data catalogue API  
    dateStrings = [
        get(
            f"https://catalogue.data.gov.bc.ca/api/3/action/package_show?id={id}"
        ).json()["result"]["record_last_modified"]
        for id in idList
    ]

    # return newest date from that list
    return max(
        [datetime.strptime(dateString, "%Y-%m-%d").date() for dateString in dateStrings]
    )


def getFileCreatedDate(filePath):
    """
    :param filePath: Path of file
    :type filePath: str
    :return: file created date
    :rtype: datetime.date
    """    
    return datetime.fromtimestamp(path.getctime(filePath)).date()


def excludeFields(featureClass, excludeFields):
    """
    Shows the remainder of fields in a feature class from a given list of fields to exclude. 

    :param featureClass: Target feature class
    :type featureClass: Feature Class
    :param excludeFields: Fields to exclude
    :type excludeFields: list
    :return: list of remaining fields
    :rtype: list
    """    

    returnFields = [
        i.name
        for i in arcpy.ListFields(featureClass)
        if i.name[0:10] not in excludeFields and i.name not in excludeFields
    ]

    return returnFields


def copySpecificFields(featureClass, fieldDeleteList):
    """
    Creates a copy of a feature class WITHOUT fields from a given list.

    :param featureClass: Target feature class
    :type featureClass: Feature class
    :param fieldDeleteList: Fields to not include in copy
    :type fieldDeleteList: list
    :return: Copied feature class
    :rtype: result
    """    
    # determine fields to keep
    fieldKeep = excludeFields(featureClass, fieldDeleteList)

    # create field mapping
    fm = arcpy.FieldMappings()

    for field in fieldKeep:
        if field in ("Shape", "OBJECTID"):
            continue
        fieldMap = arcpy.FieldMap()
        fieldMap.addInputField(featureClass, field)
        fm.addFieldMap(fieldMap)

    # create copy with field mappings
    copy = arcpy.FeatureClassToFeatureClass_conversion(
        featureClass, arcpy.env.workspace, "tempLands", field_mapping=fm,
    )

    return copy

def shapefileFieldRename(shapefile, currentFieldName, newFieldName, newFieldAlias=None):
    """
    Creates a copy of the field with a different name in a feature class, deletes old field. Very similar to arcpy's alter field Tool but works on shapefiles.

    :param shapefile: Target feature class
    :type shapefile: Feature class
    :param currentFieldName: Target Field Name
    :type currentFieldName: str
    :param newFieldName: New field name
    :type newFieldName: str
    :param newFieldAlias: New field alias, defaults to new field name
    :type newFieldAlias: str, optional
    """    
    # set new field alias to be same as name if none given
    if newFieldAlias == None:
        newFieldAlias = newFieldName

    # Determine field type of original field
    for field in arcpy.ListFields(shapefile):
        if field.name == currentFieldName:
            fieldType = field.type

    # add new field
    arcpy.AddField_management(
        shapefile, newFieldName, fieldType, field_alias=newFieldAlias
    )
    
    # copy information to new field
    cursor = arcpy.da.UpdateCursor(shapefile, [currentFieldName, newFieldName])

    for row in cursor:
        row[1] = row[0]
        cursor.updateRow(row)

    del cursor

    # delete old field
    arcpy.DeleteField_management(shapefile, currentFieldName)

def shapeFileDownloadUnzip(url, downloadFolder, fileName):
    """Downloads shapefile zip, unzips it, searches through archive for shapefiles and their paths to a list.

    :param url: URL for shapefile download
    :type url: str
    :param downloadFolder: folder for download
    :type downloadFolder: str
    :param fileName: Intended filename For processed datA
    :type fileName: str
    :return: List of all shapefile paths in downloaded directory
    :rtype: list
    """    

    #create download folder, preface it with "raw", remove existing folder if it exists
    folderPath = f"{downloadFolder}\\raw{fileName}"
    if path.exists(folderPath):
        rmtree(folderPath)
    
    mkdir(folderPath)

    # download
    urlretrieve(url, f"{folderPath}.zip")
    filePaths = []

    # unzip folder and find all shapefiles
    unpack_archive(f"{folderPath}.zip", folderPath)
    remove(f"{folderPath}.zip")
    for dirname, _, files in walk(folderPath):
        for i in files:
            if i[-4:] == ".shp":
                filePaths.append(f"{dirname}\\{i}")

    return filePaths

def item_generator(targetDictionary, targetKey):
    """
    Recursively search through a dictionary for values from a specific key.

    :param targetDictionary: Target Python dictionary
    :type targetDictionary: dict
    :param targetKey: Target key
    :type targetKey: str
    :yield: All values for target key
    :rtype: generator
    """    

    if isinstance(targetDictionary, dict):
        for k, v in targetDictionary.items():
            if k == targetKey:
                yield v
            else:
                yield from item_generator(v, targetKey)
    elif isinstance(targetDictionary, list):
        for item in targetDictionary:
            yield from item_generator(item, targetKey)


def itemGeneratorList(targetDictionary, targetKey):
    """
    Recursively search through a dictionary for values from a specific key. Returns a list rather than a generator.

    :param targetDictionary: Target Python dictionary
    :type targetDictionary: dict
    :param targetKey: Target key
    :type targetKey: str
    :yield: All values for target key
    :rtype: list
    """    
    return [i for i in item_generator(targetDictionary, targetKey)]

