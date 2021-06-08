import arcpy
from os import path
from modules.settingsWrapper import *


def northCowichanRecreationGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    print(f"{datasetClass.alias}: Starting North Cowichan Recreation Geoprocessing")

    # get name of Raw shape fileNo
    rawName = path.splitext(arcpy.Describe(rawPath).name)[0]

    # Create a temporary GDB and create a copy feature class in it. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(datasetClass.downloadFolder, "temp.gdb")
    tempGdbPath = f"{datasetClass.downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(rawPath, tempGdbPath)

    northCowichanRecreationCopy = f"{tempGdbPath}\\{rawName}"

    # delete fields
    fieldsToDelete = [
        "fme_type",
        "RESPONSIBI",
        "PUBLIC_MAP",
        "STATUS",
        "LOCATION",
        "PARK_ID",
    ]

    arcpy.DeleteField_management(northCowichanRecreationCopy, fieldsToDelete)

    # add fields
    fieldsToAdd = ["parkOwner", "Municiplty", "Source", "SOI", "HA"]

    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(northCowichanRecreationCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(northCowichanRecreationCopy, i, "TEXT")

    # rename fields
    renameDict = {
        "PARK_NAME": "parkName",
        "PARK_CLASS": "parkClass",
        "PARK_TYPE": "parkType",
    }

    for i in renameDict:
        arcpy.AlterField_management(
            northCowichanRecreationCopy, i, renameDict[i], renameDict[i]
        )

    cursor = arcpy.da.UpdateCursor(
        northCowichanRecreationCopy,
        ["parkType", "parkOwner", "Municiplty", "Source", "SOI", "parkClass"],
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
        northCowichanRecreationCopy, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # convert back to shape file
    northCowichanRecreationCopy = arcpy.CopyFeatures_management(
        northCowichanRecreationCopy, "tempNCRecreation.shp"
    )

    # Delete extraneous fields and temp GDB
    arcpy.DeleteField_management(
        northCowichanRecreationCopy, ["Shape_Leng", "Shape_Area"]
    )
    arcpy.management.Delete(tempGdbPath)

    
    return northCowichanRecreationCopy


def northCowichanNonDNCRecreationGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True
    print(f"{datasetClass.alias}: Starting north Cowichan non-DNC Recreation geoprocessing")

    # get Name of Raw shape file
    rawName = path.splitext(arcpy.Describe(rawPath).name)[0]

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(datasetClass.downloadFolder, "temp.gdb")
    tempGdbPath = f"{datasetClass.downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(rawPath, tempGdbPath)

    northCowichanNonDNCRecreationCopy = f"{tempGdbPath}\\{rawName}"

    # delete fields
    fieldsToDelete = [
        "fme_type",
        "RESPONSIBI",
        "PUBLIC_MAP",
        "STATUS",
        "LOCATION",
        "PARK_ID",
    ]

    arcpy.DeleteField_management(northCowichanNonDNCRecreationCopy, fieldsToDelete)

    fieldsToAdd = ["parkOwner", "Municiplty", "Source", "SOI", "HA"]

    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(northCowichanNonDNCRecreationCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(northCowichanNonDNCRecreationCopy, i, "TEXT")

    renameDict = {
        "PARK_NAME": "parkName",
        "PARK_CLASS": "parkClass",
        "PARK_TYPE": "parkType",
    }

    # rename fields
    for i in renameDict:
        arcpy.AlterField_management(
            northCowichanNonDNCRecreationCopy, i, renameDict[i], renameDict[i]
        )

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        northCowichanNonDNCRecreationCopy,
        ["parkType", "parkOwner", "Municiplty", "Source", "SOI", "parkClass"],
    )

    for row in cursor:
        if row[5] not in (
            "Athletic/Sportsfield Park",
            "Recreation Facility",
            "Provincial Park",
        ):
            row[0], row[1], row[2], row[3], row[4] = (
                "regional",
                None,
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
        northCowichanNonDNCRecreationCopy, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # transfer Back to shapefile
    northCowichanNonDNCRecreationCopy = arcpy.CopyFeatures_management(
        northCowichanNonDNCRecreationCopy, "tempNCNonDNCParks.shp"
    )

    # delete extraneous fields and temp GDB
    arcpy.DeleteField_management(
        northCowichanNonDNCRecreationCopy, ["Shape_Leng", "Shape_Area"]
    )
    arcpy.management.Delete(tempGdbPath)

    

    return northCowichanNonDNCRecreationCopy


def northCowichanForestryRecreationGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True
    print(f"{datasetClass.alias}: Starting north Cowichan Forestry Recreation geoprocessing")

    # get Name of Raw shape file
    rawName = path.splitext(arcpy.Describe(rawPath).name)[0]

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(datasetClass.downloadFolder, "temp.gdb")
    tempGdbPath = f"{datasetClass.downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(rawPath, tempGdbPath)

    northCowichanForestryRecreationCopy = f"{tempGdbPath}\\{rawName}"

    # delete fields
    fieldsToDelete = [
        "fme_type",
        "RESPONSIBI",
        "PUBLIC_MAP",
        "STATUS",
        "LOCATION",
        "PARK_ID",
    ]

    arcpy.DeleteField_management(northCowichanForestryRecreationCopy, fieldsToDelete)

    fieldsToAdd = ["parkOwner", "Municiplty", "Source", "SOI", "HA"]

    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(northCowichanForestryRecreationCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(northCowichanForestryRecreationCopy, i, "TEXT")

    renameDict = {
        "PARK_NAME": "parkName",
        "PARK_CLASS": "parkClass",
        "PARK_TYPE": "parkType",
    }

    # rename fields
    for i in renameDict:
        arcpy.AlterField_management(
            northCowichanForestryRecreationCopy, i, renameDict[i], renameDict[i]
        )

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        northCowichanForestryRecreationCopy,
        ["parkType", "parkOwner", "Municiplty", "Source", "SOI", "parkName"],
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
        northCowichanForestryRecreationCopy, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # transfer Back to shapefile
    northCowichanForestryRecreationCopy = arcpy.CopyFeatures_management(
        northCowichanForestryRecreationCopy, "tempNCForestryRec.shp"
    )

    # delete extraneous fields and temp GDB
    arcpy.DeleteField_management(
        northCowichanForestryRecreationCopy, ["Shape_Leng", "Shape_Area"]
    )
    arcpy.management.Delete(tempGdbPath)

    

    return northCowichanForestryRecreationCopy


def parksEcologicalProtectedGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True
    print(f"{datasetClass.alias}: starting BC Parks, Ecological, Rserve Areas Geoprocessing")

    # get Name of Raw shape file
    rawName = path.splitext(arcpy.Describe(rawPath).name)[0]

    # clip to htg AOI
    clippedFeatures = arcpy.Clip_analysis(
        rawPath, UniversalPathsWrapper.aoiPath, rawName
    )

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(datasetClass.downloadFolder, "temp.gdb")
    tempGdbPath = f"{datasetClass.downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(clippedFeatures, tempGdbPath)

    parksEcologicalProtectedCopy = f"{tempGdbPath}\\{rawName}"

    # delete fields
    fieldsToDelete = [
        "ADMIN_AREA",
        "PROT_CODE",
        "SRV_GEN_PL",
        "ORC_PRIMRY",
        "ORC_SCNDRY",
        "F_CODE",
        "SHAPE_1",
        "AREA_SQM",
        "FEAT_LEN",
        "OBJECTID",
    ]

    arcpy.DeleteField_management(parksEcologicalProtectedCopy, fieldsToDelete)

    fieldsToAdd = ["parkOwner", "Municiplty", "Source", "HA"]

    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(parksEcologicalProtectedCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(parksEcologicalProtectedCopy, i, "TEXT")

    renameDict = {
        "PROT_NAME": "parkName",
        "PARK_CLASS": "parkClass",
        "PROT_DESG": "parkType",
    }

    # rename fields
    for i in renameDict:
        arcpy.AlterField_management(
            parksEcologicalProtectedCopy, i, renameDict[i], renameDict[i]
        )

    # intersect wwith SOI
    parksEcologicalProtectedCopy = arcpy.Intersect_analysis(
        [parksEcologicalProtectedCopy, UniversalPathsWrapper.soiPath],
        "tempParksEcoPro_SOIintersect",
        join_attributes="NO_FID",
    )

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        parksEcologicalProtectedCopy, ["parkClass", "parkOwner", "Source", "parkType"]
    )

    for row in cursor:
        row[1], row[2] = "BC", "BC Parks data"
        if row[3] == " ":
            row[3] = row[4]

        cursor.updateRow(row)

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        parksEcologicalProtectedCopy, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # delete extraneous fields and temp GDB
    arcpy.DeleteField_management(
        parksEcologicalProtectedCopy, ["Shape_Leng", "Shape_Area"]
    )
    arcpy.management.Delete(clippedFeatures)
    arcpy.management.Delete(tempGdbPath)

    

    return parksEcologicalProtectedCopy


def nationalParksGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True
    print(f"{datasetClass.alias}: starting National Parks Geoprocessing")

    # get Name of Raw shape file
    rawName = path.splitext(arcpy.Describe(rawPath).name)[0]

    # clip to htg AOI
    clippedFeatures = arcpy.Clip_analysis(
        rawPath, UniversalPathsWrapper.aoiPath, rawName
    )

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(datasetClass.downloadFolder, "temp.gdb")
    tempGdbPath = f"{datasetClass.downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(clippedFeatures, tempGdbPath)

    nationalParksCopy = f"{tempGdbPath}\\{rawName}"

    # delete fields
    fieldsToDelete = [
        "NTL_PRK_ID",
        "CLAB_ID",
        "FRENCH_NM",
        "LOCAL_NM",
        "AREA_SQM",
        "FEAT_LEN",
        "OBJECTID",
    ]

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
    nationalParksCopy = arcpy.Intersect_analysis(
        [nationalParksCopy, UniversalPathsWrapper.soiPath],
        "tempNatParks_SOIintersect",
        join_attributes="NO_FID",
    )

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        nationalParksCopy,
        ["parkType", "parkClass", "parkOwner", "Municiplty", "Source",],
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
        nationalParksCopy, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # delete extraneous fields and temp GDB
    arcpy.DeleteField_management(nationalParksCopy, ["Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(clippedFeatures)
    arcpy.management.Delete(tempGdbPath)

    print("Finished National parks geoprocessing")

    return nationalParksCopy


def recreationPolygonsGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True

    print(f"{datasetClass.alias}: starting Recreation polygons Geoprocessing")

    # get Name of Raw shape file
    rawName = path.splitext(arcpy.Describe(rawPath).name)[0]

    # clip to htg AOI
    clippedFeatures = arcpy.Clip_analysis(
        rawPath, UniversalPathsWrapper.aoiPath, rawName
    )

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(datasetClass.downloadFolder, "temp.gdb")
    tempGdbPath = f"{datasetClass.downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(clippedFeatures, tempGdbPath)

    recreationPolygonsCopy = f"{tempGdbPath}\\{rawName}"

    # delete fields
    fieldsToDelete = [
        "RMF_SKEY",
        "FFID",
        "SECTION_ID",
        "REC_MF_CD",
        "RETIRE_DT",
        "AMEND_ID",
        "MAP_LABEL",
        "REC_FT_CD",
        "RES_FT_IND",
        "ARCH_IND",
        "SITE_LOC",
        "PROJ_DATE",
        "REC_VW_IND",
        "RECDIST_CD",
        "DEF_CAMPS",
        "LIFE_ST_CD",
        "FILE_ST_CD",
        "GEO_DST_CD",
        "GEO_DST_NM",
        "FEAT_CLASS",
        "FEAT_AREA",
        "FEAT_PERIM",
        "AREA_SQM",
        "FEAT_LEN",
        "OBJECTID",
    ]

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
        arcpy.AlterField_management(
            recreationPolygonsCopy, i, renameDict[i], renameDict[i]
        )

    # intersect with SOI
    recreationPolygonsCopy = arcpy.Intersect_analysis(
        [recreationPolygonsCopy, UniversalPathsWrapper.soiPath],
        "tempRecPoly_SOIintersect",
        join_attributes="NO_FID",
    )

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        recreationPolygonsCopy, ["parkClass", "Municiplty", "Source", "parkType"]
    )

    for row in cursor:
        row[0], row[1], row[2] = row[3], " ", "Recreation Polygons"
        cursor.updateRow(row)

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        recreationPolygonsCopy, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # delete extraneous fields and temp GDB
    arcpy.DeleteField_management(recreationPolygonsCopy, ["Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(clippedFeatures)
    arcpy.management.Delete(tempGdbPath)

    

    return recreationPolygonsCopy


def nanaimoCityParksGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True

    print("starting nanaimo parks Geoprocessing")

    # get Name of Raw shape file
    rawName = path.splitext(arcpy.Describe(rawPath).name)[0]

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(datasetClass.downloadFolder, "temp.gdb")
    tempGdbPath = f"{datasetClass.downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(rawPath, tempGdbPath)

    nanaimoCityParksCopy = f"{tempGdbPath}\\{rawName}"

    # delete fields
    fieldsToDelete = ["PARKID", "PARKADDRES", "GLOBALID", "AREA"]

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

    renameDict = {"CITYOWNED": "parkOwner", "thisisasillybug": "parkName"}

    for i in renameDict:
        arcpy.AlterField_management(
            nanaimoCityParksCopy, i, renameDict[i], renameDict[i], field_length=50
        )

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        nanaimoCityParksCopy,
        ["parkClass", "parkType", "parkOwner", "Municiplty", "Source", "SOI"],
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
        nanaimoCityParksCopy, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # transfer Back to shapefile
    nanaimoCityParksCopy = arcpy.CopyFeatures_management(
        nanaimoCityParksCopy, "tempNanaimoParks.shp"
    )

    # delete extraneous fields and temp GDB
    arcpy.DeleteField_management(nanaimoCityParksCopy, ["Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(tempGdbPath)

    

    return nanaimoCityParksCopy


def cvrdParksGeoprocessing(rawPath, datasetClass):

    arcpy.env.workspace = datasetClass.downloadFolder
    arcpy.env.overwriteOutput = True

    print(f"{datasetClass.alias}starting cvrd parks Geoprocessing")

    # get Name of Raw shape file
    rawName = path.splitext(arcpy.Describe(rawPath).name)[0]

    # Create a temporary GDB and create new copy feature class there. This is a workaround so that renaming fields is easy.
    arcpy.CreateFileGDB_management(datasetClass.downloadFolder, "temp.gdb")
    tempGdbPath = f"{datasetClass.downloadFolder}\\temp.gdb"

    arcpy.FeatureClassToGeodatabase_conversion(rawPath, tempGdbPath)

    cvrdParksCopy = f"{tempGdbPath}\\{rawName}"

    # delete fields
    fieldsToDelete = ["Status", "Shape_Leng"]

    arcpy.DeleteField_management(cvrdParksCopy, fieldsToDelete)

    fieldsToAdd = ["Municiplty", "Source", "SOI", "HA"]

    # add fields
    for i in fieldsToAdd:
        if i == "HA":
            arcpy.AddField_management(cvrdParksCopy, i, "FLOAT")
        else:
            arcpy.AddField_management(cvrdParksCopy, i, "TEXT")

    # rename fields
    renameDict = {
        "ParkName": "parkName",
        "ParkType": "parkClass",
        "Administra": "parkOwner",
    }

    for i in renameDict:
        arcpy.AlterField_management(cvrdParksCopy, i, renameDict[i], renameDict[i])

    # add parkType
    arcpy.AddField_management(cvrdParksCopy, "parkType", "TEXT")

    # field calculations
    cursor = arcpy.da.UpdateCursor(
        cvrdParksCopy, ["parkType", "Source", "SOI", "parkOwner"]
    )

    for row in cursor:
        if row[3] in ("Crown Provincial", "Municipality of North Cowichan"):
            cursor.deleteRow()
        else:
            row[0], row[1], row[2] = "regional", "CVRD Parks", " "
            cursor.updateRow(row)

    del cursor

    # calculate geometry
    arcpy.CalculateGeometryAttributes_management(
        cvrdParksCopy, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # transfer Back to shapefile
    cvrdParksCopy = arcpy.CopyFeatures_management(cvrdParksCopy, "tempCVRDParks.shp")

    # delete extraneous fields and temp GDB
    arcpy.DeleteField_management(cvrdParksCopy, ["Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(tempGdbPath)

    

    return cvrdParksCopy


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
                yield northCowichanNonDNCRecreationGeoprocessing(
                    filePath, datasetClass
                )
            elif "Recreation.shp" == fileName:
                yield northCowichanRecreationGeoprocessing(filePath, datasetClass)
            elif "Park.shp" == fileName:
                yield cvrdParksGeoprocessing(filePath, datasetClass)

    processedFilePaths = [i for i in parksGeoprocessingChain()]

    recreationMerged = arcpy.Merge_management(
        processedFilePaths, datasetClass.fileName
    )

    for i in processedFilePaths:
        arcpy.Delete_management(i)

    return recreationMerged
