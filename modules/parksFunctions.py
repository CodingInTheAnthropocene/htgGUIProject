import arcpy
from os import path
from modules.settingsWrapper import *

def northCowichanRecreationGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    print(f"{datasetClass.alias}: Starting North Cowichan Recreation Geoprocessing")

    # delete fields
    fieldsToDelete = [ "fme_type", "RESPONSIBI", "PUBLIC_MAP", "STATUS", "LOCATION", "PARK_ID", ]

    arcpy.DeleteField_management(rawPath, fieldsToDelete)

    # add fields
    fieldsToAdd = ["parkOwner", "Municiplty", "Source", "SOI", "HA"]

    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(rawPath, i, "FLOAT")
        else:
            arcpy.AddField_management(rawPath, i, "TEXT")

    # rename fields
    renameDict = {
        "PARK_NAME": "parkName",
        "PARK_CLASS": "parkClass",
        "PARK_TYPE": "parkType",
    }

    for i in renameDict:
        shapefileFieldRename(rawPath, i, renameDict[i], renameDict[i])

    cursor = arcpy.da.UpdateCursor(
        rawPath, ["parkType", "parkOwner", "Municiplty", "Source", "SOI", "parkClass"],
    )

    # field calculation
    for row in cursor:
        row[0], row[1], row[2], row[3], row[4] = (
            "municipal",
            "North Cowichan",
            "North Cowichan",
            "North Cowichan Parks/Recreation",
            "core",
        )
        cursor.updateRow(row)

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        rawPath, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # cleanup
    arcpy.DeleteField_management(rawPath, ["Shape_Leng", "Shape_Area"])

    return rawPath

def northCowichanNonDNCRecreationGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True
    
    print(
        f"{datasetClass.alias}: Starting north Cowichan non-DNC Recreation geoprocessing"
    )

    # delete fields
    fieldsToDelete = [ "fme_type", "RESPONSIBI", "PUBLIC_MAP", "STATUS", "LOCATION", "PARK_ID", ]

    arcpy.DeleteField_management(rawPath, fieldsToDelete)

    fieldsToAdd = ["parkOwner", "Municiplty", "Source", "SOI", "HA"]

    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(rawPath, i, "FLOAT")
        else:
            arcpy.AddField_management(rawPath, i, "TEXT")

    renameDict = {
        "PARK_NAME": "parkName",
        "PARK_CLASS": "parkClass",
        "PARK_TYPE": "parkType",
    }

    # rename fields
    for i in renameDict:
        shapefileFieldRename(rawPath, i, renameDict[i], renameDict[i])

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        rawPath, ["parkType", "parkOwner", "Municiplty", "Source", "SOI", "parkClass"],
    )

    for row in cursor:
        if row[5] not in (
            "Athletic/Sportsfield Park",
            "Recreation Facility",
            "Provincial Park",
        ):
            row[0], row[1], row[2], row[3], row[4] = (
                "regional",
                " ",
                "North Cowichan",
                "North Cowichan Parks/NonDNCRecreation",
                "core",
            )
            cursor.updateRow(row)
        else:
            cursor.deleteRow()

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        rawPath, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # cleanup
    arcpy.DeleteField_management(rawPath, ["Shape_Leng", "Shape_Area"])

    return rawPath


def northCowichanForestryRecreationGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True
    
    print(
        f"{datasetClass.alias}: Starting north Cowichan Forestry Recreation geoprocessing"
    )

    # delete fields
    fieldsToDelete = [ "fme_type", "RESPONSIBI", "PUBLIC_MAP", "STATUS", "LOCATION", "PARK_ID", ]

    arcpy.DeleteField_management(rawPath, fieldsToDelete)

    fieldsToAdd = ["parkOwner", "Municiplty", "Source", "SOI", "HA"]

    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(rawPath, i, "FLOAT")
        else:
            arcpy.AddField_management(rawPath, i, "TEXT")

    renameDict = {
        "PARK_NAME": "parkName",
        "PARK_CLASS": "parkClass",
        "PARK_TYPE": "parkType",
    }

    # rename fields
    for i in renameDict:
        shapefileFieldRename(rawPath, i, renameDict[i], renameDict[i])

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        rawPath, ["parkType", "parkOwner", "Municiplty", "Source", "SOI", "parkName"],
    )

    for row in cursor:
        if row[5] != "Osborne Bay Park":
            row[0], row[1], row[2], row[3], row[4] = (
                "municipal forest",
                "North Cowichan",
                "North Cowichan",
                "North Cowichan Parks/Forestry Recreation",
                "core",
            )
            cursor.updateRow(row)
        else:
            cursor.deleteRow()

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        rawPath, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # cleanup
    arcpy.DeleteField_management(rawPath, ["Shape_Leng", "Shape_Area"])

    return rawPath


def parksEcologicalProtectedGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True
    print(
        f"{datasetClass.alias}: Starting BC Parks, Ecological, Rserve Areas Geoprocessing"
    )

    # delete fields
    fieldsToDelete = [ "ADMIN_AREA", "PROT_CODE", "SRV_GEN_PL", "ORC_PRIMRY", "ORC_SCNDRY", "F_CODE", "SHAPE_1", "AREA_SQM", "FEAT_LEN", "OBJECTID", ]

    arcpy.DeleteField_management(rawPath, fieldsToDelete)

    fieldsToAdd = ["parkOwner", "Municiplty", "Source", "HA"]

    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(rawPath, i, "FLOAT")
        else:
            arcpy.AddField_management(rawPath, i, "TEXT")

    renameDict = {
        "PROT_NAME": "parkName",
        "PARK_CLASS": "parkClass",
        "PROT_DESG": "parkType",
    }

    # rename fields
    for i in renameDict:
        shapefileFieldRename(rawPath, i, renameDict[i], renameDict[i])

    # intersect wwith SOI
    rawPath = arcpy.Intersect_analysis(
        [rawPath, UniversalPathsWrapper.soiPath],
        "tempParksEcoPro_SOIintersect",
        join_attributes="NO_FID",
    )

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        rawPath, ["parkClass", "parkOwner", "Source", "parkType"]
    )

    for row in cursor:
        row[1], row[2] = "BC", "BC Parks data"
        if row[3] == " ":
            row[3] = row[4]

        cursor.updateRow(row)

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        rawPath, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # Cleanup
    arcpy.DeleteField_management(rawPath, ["Shape_Leng", "Shape_Area"])

    return rawPath


def nationalParksGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True
    print(f"{datasetClass.alias}: Starting National Parks Geoprocessing")

    # delete fields
    fieldsToDelete = [ "NTL_PRK_ID", "CLAB_ID", "FRENCH_NM", "LOCAL_NM", "AREA_SQM", "FEAT_LEN", "OBJECTID", ]

    arcpy.DeleteField_management(rawPath, fieldsToDelete)

    fieldsToAdd = ["parkType", "parkClass", "parkOwner", "Municiplty", "Source", "HA"]

    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(rawPath, i, "FLOAT")
        else:
            arcpy.AddField_management(rawPath, i, "TEXT")

    # rename fields
    renameDict = {"ENGLISH_NM": "parkName"}

    for i in renameDict.keys():
        shapefileFieldRename(rawPath, i, renameDict[i], renameDict[i])

    # intersect with SOI
    rawPath = arcpy.Intersect_analysis(
        [rawPath, UniversalPathsWrapper.soiPath],
        "tempNatParks_SOIintersect",
        join_attributes="NO_FID",
    )

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        rawPath, ["parkType", "parkClass", "parkOwner", "Municiplty", "Source",],
    )

    for row in cursor:
        row[0], row[1], row[2], row[3], row[4] = (
            "national",
            "national",
            "Canada",
            " ",
            "National Parks",
        )

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        rawPath, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # cleanup
    arcpy.DeleteField_management(rawPath, ["Shape_Leng", "Shape_Area"])



    return rawPath

def recreationPolygonsGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True

    print(f"{datasetClass.alias}: starting Recreation polygons Geoprocessing")

    # delete fields
    fieldsToDelete = [ "RMF_SKEY", "FFID", "SECTION_ID", "REC_MF_CD", "RETIRE_DT", "AMEND_ID", "MAP_LABEL", "REC_FT_CD", "RES_FT_IND", "ARCH_IND", "SITE_LOC", "PROJ_DATE", "REC_VW_IND", "RECDIST_CD", "DEF_CAMPS", "LIFE_ST_CD", "FILE_ST_CD", "GEO_DST_CD", "GEO_DST_NM", "FEAT_CLASS", "FEAT_AREA", "FEAT_PERIM", "AREA_SQM", "FEAT_LEN", "OBJECTID", ]

    arcpy.DeleteField_management(rawPath, fieldsToDelete)

    fieldsToAdd = ["parkClass", "parkOwner", "Municiplty", "Source", "HA"]

    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(rawPath, i, "FLOAT")
        else:
            arcpy.AddField_management(rawPath, i, "TEXT")

    # rename fields
    renameDict = {"PROJECT_NM": "parkName", "PROJECT_TP": "parkType"}

    for i in renameDict.keys():
        shapefileFieldRename(rawPath, i, renameDict[i], renameDict[i])

    # intersect with SOI
    rawPath = arcpy.Intersect_analysis(
        [rawPath, UniversalPathsWrapper.soiPath],
        "tempRecPoly_SOIintersect",
        join_attributes="NO_FID",
    )

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        rawPath, ["parkClass", "Municiplty", "Source", "parkType"]
    )

    for row in cursor:
        row[0], row[1], row[2] = row[3], " ", "Recreation Polygons"
        cursor.updateRow(row)

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        rawPath, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # cleanup
    arcpy.DeleteField_management(rawPath, ["Shape_Leng", "Shape_Area"])

    return rawPath


def nanaimoCityParksGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True

    print(f"{datasetClass.alias}: Starting nanaimo parks geoprocessing")

    # delete fields
    fieldsToDelete = ["PARKID", "PARKADDRES", "GLOBALID", "AREA"]

    arcpy.DeleteField_management(rawPath, fieldsToDelete)

    fieldsToAdd = ["parkType", "parkClass", "Municiplty", "Source", "SOI", "HA"]

    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(rawPath, i, "FLOAT")
        else:
            arcpy.AddField_management(rawPath, i, "TEXT")

    renameDict = {"CITYOWNED": "parkOwner", "PARKNAME": "parkName"}

    for i in renameDict:
        shapefileFieldRename(rawPath, i, renameDict[i], renameDict[i])

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        rawPath, ["parkClass", "parkType", "parkOwner", "Municiplty", "Source", "SOI"],
    )

    for row in cursor:
        row[0], row[1], row[3], row[4], row[5] = (
            "municipal",
            "municipal",
            "Nanaimo",
            "Nanaimo City Parks",
            "marine",
        )
        if row[2] == "Yes":
            row[2] = "Nanaimo"
        else:
            row[2] = " "

        cursor.updateRow(row)

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        rawPath, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # cleanup
    arcpy.DeleteField_management(rawPath, ["Shape_Leng", "Shape_Area"])

    return rawPath


def cvrdParksGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True

    print(f"{datasetClass.alias}: Starting cvrd parks Geoprocessing")

    # delete fields
    fieldsToDelete = ["Status", "Shape_Leng"]

    arcpy.DeleteField_management(rawPath, fieldsToDelete)

    fieldsToAdd = ["Municiplty", "Source", "SOI", "HA"]

    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(rawPath, i, "FLOAT")
        else:
            arcpy.AddField_management(rawPath, i, "TEXT")

    # rename fields
    renameDict = {
        "ParkName": "parkName",
        "ParkType": "parkClass",
        "Administra": "parkOwner",
    }

    for i in renameDict:
        shapefileFieldRename(rawPath, i, renameDict[i], renameDict[i])

    # add parkType
    arcpy.AddField_management(rawPath, "parkType", "TEXT")

    # field calculations
    cursor = arcpy.da.UpdateCursor(rawPath, ["parkType", "Source", "SOI", "parkOwner"])

    for row in cursor:
        if row[3] in ("Crown Provincial", "Municipality of North Cowichan"):
            cursor.deleteRow()
        else:
            row[0], row[1], row[2] = "regional", "CVRD Parks", " "
            cursor.updateRow(row)

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        rawPath, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # Cleaanup
    arcpy.DeleteField_management(rawPath, ["Shape_Leng", "Shape_Area"])

    return rawPath


def parksRecreationDatasetsGeoprocessing(rawFilePaths, datasetClass):
    def parksGeoprocessingChain():
        for filePath in rawFilePaths:
            fileName = path.split(filePath)[1]

            if "CLAB_NATPK_polygon.shp" == fileName:
                yield nationalParksGeoprocessing(filePath, datasetClass)
            elif "FTN_REC_PL_polygon.shp" == fileName:
                yield recreationPolygonsGeoprocessing(filePath, datasetClass)
            elif "TA_PEP_SVW_polygon.shp" == fileName:
                yield parksEcologicalProtectedGeoprocessing(filePath, datasetClass)
            elif "PARKS.shp" == fileName:
                yield nanaimoCityParksGeoprocessing(filePath, datasetClass)
            elif "ForestryRecreation.shp" == fileName:
                yield northCowichanForestryRecreationGeoprocessing(
                    filePath, datasetClass
                )
            elif "NonDNCRecreation.shp" == fileName:
                yield northCowichanNonDNCRecreationGeoprocessing(filePath, datasetClass)
            elif "Recreation.shp" == fileName:
                yield northCowichanRecreationGeoprocessing(filePath, datasetClass)
            elif "Park.shp" == fileName:
                yield cvrdParksGeoprocessing(filePath, datasetClass)

    processedFilePaths = [i for i in parksGeoprocessingChain()]

    recreationMerged = arcpy.Merge_management(processedFilePaths, datasetClass.fileName)

    for i in processedFilePaths:
        arcpy.Delete_management(i)

    return recreationMerged
