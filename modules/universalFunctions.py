from requests import get
from urllib.request import urlretrieve
import arcpy
from os import path, mkdir, walk, remove
from datetime import datetime
from shutil import rmtree, unpack_archive



def arcpyGetPath(x):
    return arcpy.Describe(x).catalogPath


def getCurrency(idList):
    """Returns most recent date  in datetime format of dataset update given a list of BC data catalogue IDs"""
    dateStrings = [
        get(
            f"https://catalogue.data.gov.bc.ca/api/3/action/package_show?id={id}"
        ).json()["result"]["record_last_modified"]
        for id in idList
    ]

    return max(
        [datetime.strptime(dateString, "%Y-%m-%d").date() for dateString in dateStrings]
    )


def getFileCreatedDate(filePath):
    return datetime.fromtimestamp(path.getctime(filePath)).date()


def excludeFields(featureClass, excludeFields):

    

    returnFields = [i.name for i in arcpy.ListFields(featureClass) if i.name[0:10] not in excludeFields and i.name not in excludeFields] 

    return returnFields


def copySpecificFields(featureClass, fieldDeleteList):
    
    fieldKeep= excludeFields(featureClass, fieldDeleteList)

    fm = arcpy.FieldMappings()
    

    for field in fieldKeep:
        if field  in ('Shape', "OBJECTID"):
            continue
        fieldMap=arcpy.FieldMap()
        fieldMap.addInputField(featureClass, field)        
        fm.addFieldMap(fieldMap)


    copy = arcpy.FeatureClassToFeatureClass_conversion(
        featureClass,
        arcpy.env.workspace,
        "tempLands",
        field_mapping=fm,
    )

    return copy

def shapefileFieldRename(shapefile, currentFieldName, newFieldName, newFieldAlias=None):
    if newFieldAlias==None:
        newFieldAlias=newFieldName

    for field in arcpy.ListFields(shapefile):
        if field.name == currentFieldName:
            fieldType = field.type

    arcpy.AddField_management(shapefile, newFieldName, fieldType, field_alias=newFieldAlias)
    cursor = arcpy.da.UpdateCursor(shapefile, [currentFieldName, newFieldName])

    for row in cursor:
        row[1] = row[0]
        cursor.updateRow(row)

    del cursor

    arcpy.DeleteField_management(shapefile, currentFieldName)


def shapeFileDownloadUnzip(url, downloadFolder, fileName):
    """Downloads a zipped shapefile from a specified url to a specified download folder. Unzips in download folder. Will walk through any number of directories to find shapefile. Returns z list of paths if multiple shapefiles exist, otherwise returns a path like string. Will replace any identically named folders in the download location."""

    folderPath = f"{downloadFolder}\\raw{fileName}"
    if path.exists(folderPath) == False:
        mkdir(folderPath)

    urlretrieve(url, f"{folderPath}.zip")
    filePaths = []
    unpack_archive(f"{folderPath}.zip", folderPath)
    remove(f"{folderPath}.zip")
    for dirname, _, files in walk(folderPath):
        for i in files:
            if i[-4:] == ".shp":
                filePaths.append(f"{dirname}\\{i}")

    return filePaths


def item_generator(json_input, lookup_key):
    """recursively iterates through JSON to find all values with a specific key. https://stackoverflow.com/questions/21028979/recursive-iteration-through-nested-json-for-specific-key-in-python"""

    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)


def itemGeneratorList(targetDictionary, targetKey):
    """ returns list of items in generator object returned by item_generator"""
    return [i for i in item_generator(targetDictionary, targetKey)]

