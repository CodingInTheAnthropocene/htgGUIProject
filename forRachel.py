from os import remove
from modules.functionLib import fieldsToDelete
import arcpy
from arcpy.management import AddField
from pandas.core.common import flatten, is_full_slice


def removeNotPenticton(pentictonDisseminationAreas, bcCSV):
    arcpy.env.workspace= r"C:\Users\laure\Desktop\test\test\Default.gdb"
    arcpy.env.overwriteOutput = True

    cursor = arcpy.da.UpdateCursor(pentictonDisseminationAreas, ["DSSMNTN_ID"])
    
    idList = [int(row[0]) for row in cursor]
    bcTable = arcpy.TableToTable_conversion(bcCSV,arcpy.env.workspace, "pentictononly")

    geoCodeField = ["GEO_CODE"]
    
    cursor = arcpy.da.UpdateCursor(bcTable, geoCodeField)

    for row in cursor:
        if row[0] not in idList:
            cursor.deleteRow()

    return bcTable

def makefeatureclassgood(feature, newFeatureName, pentictonDisseminationAreas):
    arcpy.env.workspace= r"C:\Users\laure\Desktop\test\test\Default.gdb"
    arcpy.env.overwriteOutput =  True

    name = "DisseminationAreaCode"
    attributeFieldName = "Attribute"
    codeFieldName = "Attribute_Code"
    stringCodeFieldName ="Attribute_Code_String"
    valueFieldName = "Value"

    
    feature = arcpy.CopyRows_management(feature, "PentictonOnlyCopy")

    arcpy.AlterField_management(feature, "GEO_CODE", name, name)
    arcpy.AlterField_management(feature, "DIM__Profile_of_Dissemination_Areas__2247_", attributeFieldName, attributeFieldName)
    arcpy.AlterField_management(feature, "Dim__Sex__3___Member_ID___1___Total___Sex", valueFieldName, valueFieldName)
    arcpy.AlterField_management(feature, 'Member_ID__Profile_of_Dissemination_Areas__2247_', codeFieldName, codeFieldName)
    arcpy.AddField_management(feature, stringCodeFieldName, "TEXT", field_length=30)
    
    deleteList =['GEO_LEVEL', 'GEO_NAME', 'GNR', 'GNR_LF', 'DATA_QUALITY_FLAG', 'ALT_GEO_CODE', 'Notes__Profile_of_Dissemination_Areas__2247_', 'Dim__Sex__3___Member_ID___2___Male', 'Dim__Sex__3___Member_ID___3___Female']

    arcpy.DeleteField_management(feature, deleteList)
    
    fieldsToAdd = []

    cursor = arcpy.da.UpdateCursor(feature, [attributeFieldName, codeFieldName, stringCodeFieldName])
    addField = True
    for row in cursor:
        row[2] = f"_{row[1]}"
        cursor.updateRow(row)
        if addField == True:
            fieldsToAdd.append((row[2], row[0]))
            if row[0] == "English only":
                addField = False

    for i in fieldsToAdd:
        arcpy.AddField_management(feature, i[0], "FLOAT")
  
    allFields = [i.name for i in arcpy.ListFields(feature)]

    cursor = arcpy.da.UpdateCursor(feature, allFields)
    
  
    for row in cursor:
        for item in allFields:
            try:
                value = float(row[allFields.index(valueFieldName)])
            except:
                value = row[allFields.index(valueFieldName)]
            if item == row[allFields.index(stringCodeFieldName)]:
                if isinstance(value, float): 
                    row[allFields.index(item)] = value
                else:
                    row[allFields.index(item)] = None
        
        cursor.updateRow(row)
    
    fieldsToAddStats = [[i[0], "SUM"] for i in fieldsToAdd]

    finalTable = arcpy.Statistics_analysis(feature, "tempTable", fieldsToAddStats, name)

    arcpy.DeleteField_management(finalTable, "FREQUENCY")

    for i in fieldsToAdd:
        arcpy.AlterField_management(finalTable, f"SUM_{i[0]}", i[0], i[1])

    pentictonDisseminationAreas = arcpy.CopyFeatures_management(pentictonDisseminationAreas, "pentictonDisseminationAreas")

    arcpy.AddField_management(pentictonDisseminationAreas, name, "LONG")

    cursor = arcpy.da.UpdateCursor(pentictonDisseminationAreas, ["DSSMNTN_ID", name])

    for row in cursor:
        row[1] = int(row[0])

        cursor.updateRow(row)

    del cursor

    arcpy.DeleteField_management(pentictonDisseminationAreas, "DSSMNTN_ID")

    pentictonDisseminationAreas = arcpy.MakeFeatureLayer_management(pentictonDisseminationAreas, "tempLayer")
    
    arcpy.AddJoin_management(pentictonDisseminationAreas, name, finalTable, name)

    finalFeature = arcpy.CopyFeatures_management(pentictonDisseminationAreas, newFeatureName)

    return finalFeature

pentictonList = removeNotPenticton(r"C:\Users\laure\Desktop\CEN_CENSUS_DISSEM_AREAS_SVW\CNCNSSDSS2_polygon.shp", r"C:\Users\laure\Downloads\98-401-X2016044_BRITISH_COLUMBIA_eng_CSV\98-401-X2016044_BRITISH_COLUMBIA_English_CSV_data.csv")

finalPentictonFeature = makefeatureclassgood(pentictonList, "flatpenticton", r"C:\Users\laure\Desktop\CEN_CENSUS_DISSEM_AREAS_SVW\CNCNSSDSS2_polygon.shp")

