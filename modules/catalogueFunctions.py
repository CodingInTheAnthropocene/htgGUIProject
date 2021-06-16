"""
catalogueFunctions.py - Geoprocessing chains for BC data catalogue datasets.
"""

import arcpy

from modules.settingsWrapper import *
from modules.universalFunctions import *

def crownTenuresGeoprocessing(rawPath, dataset):
    """
    Tantalis Crown Tenures geoprocessing

    :param rawPath: Raw feature class path
    :type rawPath: str
    :param dataset: Input dataset
    :type dataset: Dataset
    :return: Processed file
    :rtype: result
    """    

    # dictionary for calculating fields
    fieldValueDictionary = {
        "AGRICULTURE, EXTENSIVE": "agriculture",
        "AGRICULTURE, INTENSIVE": "agriculture",
        "AQUACULTURE, PLANTS": "aquaculture",
        "AQUACULTURE, SHELL FISH": "aquaculture",
        "COMMERCIAL RECREATION, COMMUNITY OUTDOOR RECREATION": "commercial recreation",
        "COMMERCIAL RECREATION, ECO TOURIST LODGE/RESORT": "commercial recreation",
        "COMMERCIAL RECREATION, MISCELLANEOUS": "commercial recreation",
        "COMMERCIAL RECREATION, TRAIL RIDING": "commercial recreation",
        "COMMERCIAL, COMMERCIAL A": "commercial",
        "COMMERCIAL, COMMERCIAL B": "commercial",
        "COMMERCIAL, COMMERCIAL WHARF": "wharf",
        "COMMERCIAL, FILM PRODUCTION": "commercial",
        "COMMERCIAL, GENERAL": "commercial",
        "COMMERCIAL, GOLF COURSE": "commercial",
        "COMMERCIAL, MARINA": "marina",
        "COMMERCIAL, MISCELLANEOUS": "commercial",
        "COMMERCIAL, PRIVATE YACHT CLUB": "commercial",
        "COMMUNICATION, COMBINED USES": "communication",
        "COMMUNICATION, COMMUNICATION SITES": "communication",
        "COMMUNITY, COMMUNITY FACILITY": "community",
        "COMMUNITY, MISCELLANEOUS": "community",
        "COMMUNITY, TRAIL MAINTENANCE": "community",
        "ENVIRONMENT, CONSERVATION, & RECR, BUFFER ZONE": "environment protection",
        "ENVIRONMENT, CONSERVATION, & RECR, ECOLOGICAL RESERVE": "environment protection",
        "ENVIRONMENT, CONSERVATION, & RECR, ENVIRONMENT PROTECTION/CONSERVATION": "environment protection",
        "ENVIRONMENT, CONSERVATION, & RECR, FISH AND WILDLIFE MANAGEMENT": "wildlife management",
        "ENVIRONMENT, CONSERVATION, & RECR, FISHERY FACILITY": "fishery facility",
        "ENVIRONMENT, CONSERVATION, & RECR, FOREST MANAGEMENT RESEARCH": "forest/other research",
        "ENVIRONMENT, CONSERVATION, & RECR, PUBLIC ACCESS/PUBLIC TRAILS": "public access",
        "ENVIRONMENT, CONSERVATION, & RECR, SCIENCE MEASUREMENT/RESEARCH": "forest/other research",
        "ENVIRONMENT, CONSERVATION, & RECR, UREP/RECREATION RESERVE": "recreation reserve",
        "ENVIRONMENT, CONSERVATION, & RECR, WATERSHED RESERVE": "watershed reserve",
        "FIRST NATIONS, CULTURAL SIGNIFICANCE": "First Nations",
        "FIRST NATIONS, INTERIM MEASURES": "First Nations",
        "FIRST NATIONS, LAND CLAIM SETTLEMENT": "First Nations",
        "FIRST NATIONS, RESERVE EXPANSION": "First Nations",
        "FIRST NATIONS, TRADITIONAL USE": "First Nations",
        "FIRST NATIONS, TREATY AREA": "First Nations",
        "INDUSTRIAL, GENERAL": "industrial",
        "INDUSTRIAL, HEAVY INDUSTRIAL": "industrial",
        "INDUSTRIAL, LIGHT INDUSTRIAL": "industrial",
        "INDUSTRIAL, LOG HANDLING/STORAGE": "log handling",
        "INDUSTRIAL, MISCELLANEOUS": "industrial",
        "INSTITUTIONAL, FIRE HALL": "institutional",
        "INSTITUTIONAL, HOSPITAL/HEALTH FACILITY": "institutional",
        "INSTITUTIONAL, INDOOR RECREATION FACILITY": "institutional",
        "INSTITUTIONAL, LOCAL/REGIONAL PARK": "park",
        "INSTITUTIONAL, MILITARY SITE": "institutional",
        "INSTITUTIONAL, MISCELLANEOUS": "institutional",
        "INSTITUTIONAL, PUBLIC WORKS": "public works",
        "INSTITUTIONAL, SCHOOL/OUTDOOR EDUCATION FACILITY": "institutional",
        "INSTITUTIONAL, WASTE DISPOSAL SITE": "waste disposal",
        "MISCELLANEOUS LAND USES, LAND USE PLAN INTERIM AGREEMENT": "other uses",
        "MISCELLANEOUS LAND USES, OTHER": "other uses",
        "MISCELLANEOUS LAND USES, PLANNING/MARKETING/DEVELOP PROJECTS": "other uses",
        "OCEAN ENERGY, INVESTIGATIVE AND MONITORING PHASE": "alternate energy",
        "QUARRYING, CONSTRUCTION STONE": "quarrying",
        "QUARRYING, MISCELLANEOUS": "quarrying",
        "QUARRYING, SAND AND GRAVEL": "quarrying",
        "RESIDENTIAL, APPLICATION ONLY - PRIVATE MOORAGE": "moorage",
        "RESIDENTIAL, FLOATING CABIN": "residential",
        "RESIDENTIAL, MISCELLANEOUS": "residential",
        "RESIDENTIAL, PRIVATE MOORAGE": "moorage",
        "RESIDENTIAL, RECREATIONAL RESIDENTIAL": "residential",
        "RESIDENTIAL, REMOTE RESIDENTIAL": "residential",
        "RESIDENTIAL, RURAL RESIDENTIAL": "residential",
        "RESIDENTIAL, STRATA MOORAGE": "moorage",
        "RESIDENTIAL, THERMAL LOOPS": "alternate energy",
        "RESIDENTIAL, URBAN RESIDENTIAL": "residential",
        "TRANSPORTATION, BRIDGES": "bridges",
        "TRANSPORTATION, FERRY TERMINAL": "ferry terminal",
        "TRANSPORTATION, NAVIGATION AID": "navigation",
        "TRANSPORTATION, PUBLIC WHARF": "wharf",
        "TRANSPORTATION, RAILWAY": "rail",
        "TRANSPORTATION, ROADWAY": "road",
        "UTILITY, ELECTRIC POWER LINE": "electrical",
        "UTILITY, GAS AND OIL PIPELINE": "pipeline",
        "UTILITY, MISCELLANEOUS": "utility - other",
        "UTILITY, SEWER/EFFLUENT LINE": "sewer line",
        "UTILITY, TELECOMMUNICATION LINE": "communication",
        "UTILITY, WATER LINE": "water line",
        "WINDPOWER, INVESTIGATIVE AND MONITORING PHASE": "alternate energy",
    }

    # ArcGIS environment settings
    arcpy.env.workspace = dataset.arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    # create working copies,delete fields
    print(f"{dataset.alias}: Creaating working copies, Deleting fields")

    deleteFields = [ "INTRID_SID", "APP_TYPE_CD", "TEN_DOCMNT", "TEN_LGLDSC", "TEN_A_DRVN", "RESP_BUS_U", "DSP_TR_SID", "CD_CHR_STG", "SHAPE_1", "AREA_SQM", "FEAT_LEN", ]

    arcpy.DeleteField_management(rawPath, deleteFields)

    landsDeleteFields = [ "ATTRIBUTE_", "EN", "GEOMETRY_S", "H_", "Ha", "ICF", "ICF_AREA", "ICIS", "JUROL", "LAND_ACT_P", "LAND_DISTR", "LEGAL_FREE", "LOCALAREA", "LTSA_BLOCK", "LTSA_LOT", "LTSA_PARCE", "LTSA_PLAN", "OWNER_CLAS", "OtherComme", "PARCEL_DES", "PID", "PIN", "PIN_DISTLE", "PIN_SUBDLA", "PMBC", "RoW", "SOURCE_PRO", "TEMP_PolyI", "TENURES", "TimbeTable", "Title_Info", "Title_num", "Title_owne", "access", "apprais2BC", "apprais2HB", "apprais2Ha", "apprais2re", "appraisal2", "arch_sites", "avail_issu", "available", "comments", "confirm_qu", "ess_respon", "essential", "guide_outf", "interests", "label", "landval_20", "landval_sr", "location", "municipali", "needs_conf", "potential_", "prop_class", "result_val", "selected", "specific_l", "tourism_ca", "trapline", "use_on_pro", "valperHa_2", "zone_code", "zoning"]

    landsCopy=copySpecificFields(UniversalPathsWrapper.htgLandsPath, landsDeleteFields)
    
    # Calculate fields

    print(f"{dataset.alias}: Calculating fields")
    cursor = arcpy.da.UpdateCursor(
        rawPath, ["CL_FILE", "TEN_SUBTYP", "TEN_SUBPRP"],
    )
    for row in cursor:
        if row[0] == 1414573:
            cursor.deleteRow()
        if row[1] in ("BCAL INVENTORY", "NOTATION OF INTEREST") and row[2] not in (
            "UREP/RECREATION RESERVE",
            "FISH AND WILDLIFE MANAGEMENT",
            "ENVIRONMENT PROTECTION/CONSERVATION",
        ):
            cursor.deleteRow()
        if row[2] == "TREATY AREA":
            cursor.deleteRow()

    # add display_cd field
    arcpy.AddField_management(rawPath, "display_cd", "TEXT", field_length=30)

    # many updates to display_cd based on values in crownTenuresDictionary
    cursor = arcpy.da.UpdateCursor(
        rawPath, ["TEN_PURPOS", "TEN_SUBPRP", "display_cd"]
    )

    for row in cursor:
        # iterate over tenures dictionary
        for i in fieldValueDictionary:
            first2 = f"{row[0]}, {row[1]}"
            if first2 == i:
                row[2] = fieldValueDictionary[first2]
                cursor.updateRow(row)
                break


    print(f"{dataset.alias}: Starting tenures/SOI intersect")
    # intersect crown tenures with SOI
    tenuresSOIIntersect = arcpy.Intersect_analysis(
        [rawPath, UniversalPathsWrapper.soiPath],
        "temptenureSOIIntersect",
        join_attributes="NO_FID",
    )

    print(f"{dataset.alias}: Starting 'identity'" )

    # Identity tenures/soi with land parcels data. This performs a workaround with the union tool and then subsequently deleting records That aren't wanted.
    crownTenuresProcessedPath = arcpy.Union_analysis(
        [tenuresSOIIntersect, landsCopy],
        dataset.fileName,
        join_attributes="NO_FID",
    )
    cursor = arcpy.da.UpdateCursor(crownTenuresProcessedPath, ["TEN_STAGE"])

    for row in cursor:
        if row[0] == " ":
            cursor.deleteRow()
    del cursor

    # add and calculate HA field to tenures/soi/lands intersect
    print(f"{dataset.alias}: Calculating geometry" )    
    arcpy.AddField_management(crownTenuresProcessedPath, "HA", "FLOAT")

    arcpy.CalculateGeometryAttributes_management(
        crownTenuresProcessedPath, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # delete working copies
    arcpy.management.Delete(rawPath)
    arcpy.management.Delete(landsCopy)
    arcpy.management.Delete(tenuresSOIIntersect)

    return crownTenuresProcessedPath

def forestHarvestingAuthorityGeoprocessing(rawPath, dataset):
    """
    Forest Tenure Harvesting Authority Polygons geoprocessing.

    :param rawPath: Raw feature class path
    :type rawPath: str
    :param dataset: Input dataset
    :type dataset: Dataset
    :return: Processed file
    :rtype: result
    """   

    # env variables
    arcpy.env.workspace = dataset.arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    # delete fields
    print(f"{dataset.alias}: Creating working copies, deleting fields")
    
    deleteFields = [ "HVA_SKEY", "FFID", "CP_ID", "FEAT_CLASS", "HVA_ID", "HVA_MGMTID", "HVA_MGMTCD", "HRV_TP_CD", "HRV_TP_DSC", "HVA_ST_CD", "ISSUE_DATE", "CURR_EX_DT", "QTA_TP_CD", "CR_LND_CD", "SAL_TP_CD", "CASC_SP_CD", "CATAST_IND", "CR_GRT_IND", "CRUISE_IND", "DECID_IND", "RETIRE_DT", "FEAT_AREA", "FEAT_PERIM", "ADM_DST_CD", "GEO_DST_CD", "GEO_DST_NM", "TM_PRIME", "MRK_MD_CD", "MRK_MD_DSC", "MRK_IN_CD", "MRK_IN_DSC", "OTH_TM_IND", "CL_LOC_CD", "FILE_TP_CD", "FILE_ST_CD", "PFU_MGMTID", "SB_FND_IND", "BCTS_ORGCD", "BCTS_ORGNM", "MAP_LABEL", "AREA_SQM", "FEAT_LEN", "OBJECTID", ]

    arcpy.DeleteField_management(rawPath, deleteFields)

    # create lands copy the correct fields
    landsDeleteFields = [ "ATTRIBUTE_", "EN", "GEOMETRY_S", "H_", "Ha", "ICF", "ICF_AREA", "ICIS", "JUROL", "LAND_ACT_P", "LAND_DISTR", "LEGAL_FREE", "LOCALAREA", "LTSA_BLOCK", "LTSA_LOT", "LTSA_PARCE", "LTSA_PLAN", "OWNER_CLAS", "OtherComme", "PARCEL_DES", "PID", "PIN", "PIN_DISTLE", "PIN_SUBDLA", "PMBC", "RoW", "SOURCE_PRO", "TEMP_PolyI", "TENURES", "TimbeTable", "Title_Info", "Title_num", "Title_owne", "access", "apprais2BC", "apprais2HB", "apprais2Ha", "apprais2re", "appraisal2", "arch_sites", "avail_issu", "available", "comments", "confirm_qu", "ess_respon", "essential", "guide_outf", "interests", "label", "landval_20", "landval_sr", "location", "municipali", "needs_conf", "owner", "potential_", "prop_class", "result_val", "selected", "specific_l", "tourism_ca", "trapline", "use_on_pro", "valperHa_2", "zone_code", "zoning", "Shape_Leng", "Shape_Area", "new_owners", "ownership_", ]

    landsCopy=copySpecificFields(UniversalPathsWrapper.htgLandsPath, landsDeleteFields)

    # rename fields
    print(f"{dataset.alias}: Renaming, calculating fields")
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
        "FIL_TP_DSC": "LicnceType",
    }

    for i in forestHarvestingAuthorityRenameDict:
        shapefileFieldRename(
            rawPath, i, forestHarvestingAuthorityRenameDict[i]
        )

    # Calculate fields
  
    cursor = arcpy.da.UpdateCursor(
        rawPath, ["ExpiryDate", "EXTEND_DT"]
    )

    for row in cursor:
        if row[1] != " ":
            row[0] = row[1]
        cursor.updateRow(row)

    del cursor

    # intersect forest tenure with HTG lands
    print(f"{dataset.alias}: Starting intersect")

    forestHarvestingAuthorityProcessedPath = arcpy.Intersect_analysis(
        [rawPath, landsCopy],
        dataset.fileName,
        join_attributes="NO_FID",
    )

    # calculate geometry
    print(f"{dataset.alias}: Calculating geometry")
    arcpy.AddField_management(forestHarvestingAuthorityProcessedPath, "HA", "FLOAT")

    arcpy.CalculateGeometryAttributes_management(
        forestHarvestingAuthorityProcessedPath, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # Cleanup
    arcpy.DeleteField_management(forestHarvestingAuthorityProcessedPath, ["EXTEND_DT", "Shape_Leng", "Shape_Area"])
    arcpy.management.Delete(landsCopy)

    return forestHarvestingAuthorityProcessedPath

def forestManagedLicenceGeoprocessing(rawPath, dataset):
    """
    Forest Tenure Managed Licence geoprocessing.

    :param rawPath: Raw feature class path
    :type rawPath: str
    :param dataset: Input dataset
    :type dataset: Dataset
    :return: Processed file
    :rtype: result
    """  

    # environment settings
    arcpy.env.workspace = dataset.arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    # delete fields
    print(f"{dataset.alias}: Creating working copies, deleting fields")

    deleteFields = [ "MPBLCKD", "MLTPCD", "RTRMNTDT", "MNDMNTD", "MAP_LABEL", "FEAT_AREA", "FTRPRMTR", "FTRCLSSSK", "FLSTTSCD", "DMNDSTRCTC", "AREA_SQM", "FEAT_LEN", "OBJECTID", ]

    arcpy.DeleteField_management(rawPath, deleteFields)

    # create lands copy
    landsDeleteFields = [ "LOCALAREA", "ICF_AREA", "GEOMETRY_S", "ATTRIBUTE_", "PID", "PIN", "JUROL", "LTSA_LOT", "LTSA_BLOCK", "LTSA_PARCE", "LTSA_PLAN", "LEGAL_FREE", "LAND_DISTR", "LAND_ACT_P", "PARCEL_DES", "OWNER_CLAS", "SOURCE_PRO", "landval_20", "valperHa_2", "result_val", "Ha", "comments", "new_owners", "PMBC", "ICIS", "ICF", "landval_sr", "prop_class", "needs_conf", "confirm_qu", "selected", "selected_b", "label", "location", "specific_l", "H_", "use_on_pro", "potential_", "interests", "available", "avail_issu", "owner", "EN", "guide_outf", "trapline", "ess_respon", "tourism_ca", "access", "zoning", "zone_code", "TENURES", "PIN_DISTLE", "PIN_SUBDLA", "municipali", "arch_sites", "Title_num", "Title_owne", "Title_Info", "essential", "RoW", "OtherComme", "appraisal2", "apprais2HB", "apprais2re", "apprais2BC", "apprais2Ha", "TEMP_PolyI", "TimbeTable", "ownership_", "Shape_Leng", "Shape_Area", ]
    
    landsCopy=copySpecificFields(UniversalPathsWrapper.htgLandsPath, landsDeleteFields)
       
    # add, rename and calculate fields
    print(f"{dataset.alias}: Renaming Fields, calculating field values")

    arcpy.AddField_management(rawPath, "ClientGrp", "text")

    forestManagedLicenceRenameDict = {
        "CLNTNM": "Client",
        "FRSTFLD": "PermitID",
        "CLNTNMBR": "ClientNum",
        "DMNDSTRCTN": "District",
        "LFCCLSTTSC": "Status",
    }

    for i in forestManagedLicenceRenameDict:
        shapefileFieldRename(rawPath, i, forestManagedLicenceRenameDict[i])

    cursor = arcpy.da.UpdateCursor(rawPath, ["Client", "ClientGrp"])

    for row in cursor:
        if row[0] in (
            "HALALT FIRST NATION",
            "LYACKSON FIRST NATION",
            "PENELAKUT FIRST NATION",
        ):
            row[1] = "HTG"
        elif row[0] in ("MALAHAT TENURE HOLDING LTD.", "STZ'UMINUS FIRST NATION"):
            row[1] = "other FN"
        else:
            row[1] = "other"

        cursor.updateRow(row)

    del cursor

    # intersect with Lands
    print(f"{dataset.alias}: Starting intersect")     

    # intersect HTG lands and forest managed licenses
    forestManagedLicenceProcessedPath = arcpy.Intersect_analysis(
        [rawPath, landsCopy],
        dataset.fileName,
        join_attributes="NO_FID",
    )

    # calculate geometry
    print(f"{dataset.alias}: Calculating geometry")
    arcpy.AddField_management(forestManagedLicenceProcessedPath, "HA", "FLOAT")

    arcpy.CalculateGeometryAttributes_management(
        forestManagedLicenceProcessedPath, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # remove working files
    arcpy.management.Delete(landsCopy)

    return forestManagedLicenceProcessedPath

####################################################################################################################
# Harvested areas of BC (Consolidated Cut Blocks)
####################################################################################################################

def harvestedAreasGeoprocessing(rawPath, dataset):
    """
    Harvested Areas of BC geoprocessing.

    :param rawPath: Raw feature class path
    :type rawPath: str
    :param dataset: Input dataset
    :type dataset: Dataset
    :return: Processed file
    :rtype: result
    """  

    # environment settings
    arcpy.env.workspace = dataset.arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    # delete fields
    print(f"{dataset.alias}: Creating working copies, deleting fields")
    deleteFields = ["OPENINGID", "AREA_SQM", "FTLENGTHM", "SHAPE_1", "OBJECTID"]

    arcpy.DeleteField_management(rawPath, deleteFields)

    landsDeleteFields = [ "LOCALAREA", "ICF_AREA", "GEOMETRY_S", "ATTRIBUTE_", "PID", "PIN", "JUROL", "LTSA_LOT", "LTSA_BLOCK", "LTSA_PARCE", "LTSA_PLAN", "LEGAL_FREE", "LAND_DISTR", "LAND_ACT_P", "PARCEL_DES", "OWNER_CLAS", "SOURCE_PRO", "landval_20", "valperHa_2", "result_val", "Ha", "comments", "new_owners", "PMBC", "ICIS", "ICF", "landval_sr", "prop_class", "needs_conf", "confirm_qu", "selected", "label", "location", "specific_l", "H_", "use_on_pro", "potential_", "interests", "available", "avail_issu", "owner", "EN", "guide_outf", "trapline", "ess_respon", "tourism_ca", "access", "zoning", "zone_code", "TENURES", "PIN_DISTLE", "PIN_SUBDLA", "municipali", "arch_sites", "Title_num", "Title_owne", "Title_Info", "essential", "RoW", "OtherComme", "appraisal2", "apprais2HB", "apprais2re", "apprais2BC", "apprais2Ha", "TEMP_PolyI", "TimbeTable", "ownership_", "Shape_Leng", "Shape_Area", ]

    landsCopy=copySpecificFields(UniversalPathsWrapper.htgLandsPath, landsDeleteFields)

    # Field rename
    print(f"{dataset.alias}: Renaming Fields, calculating field values")

    harvestedAreasRenameDict = {
        "DSTRBSTDT": "startdate",
        "DSTRBEDDT": "enddate",
        "AREAHA": "HA",
    }

    for i in harvestedAreasRenameDict:
        shapefileFieldRename(rawPath, i, harvestedAreasRenameDict[i])

    # calculate fields
    cursor = arcpy.da.UpdateCursor(rawPath, ["startdate", "enddate"])
    
    for row in cursor:
        if row[0] != " ":
            row[0] = f"{row[0][0:4]}_{row[0][4:6]}"
            row[1] = f"{row[1][0:4]}_{row[1][4:6]}"

        cursor.updateRow(row)

    del cursor

    # Inteersect with lands
    print(f"{dataset.alias}: Starting intersect")     

    harvestedAreasProcessedPath = arcpy.Intersect_analysis(
        [rawPath, landsCopy],
        dataset.fileName,
        join_attributes="NO_FID",
    )

    # calculate geometry
    print(f"{dataset.alias}: Calculating geometry")
    arcpy.CalculateGeometryAttributes_management(
        harvestedAreasProcessedPath, [["HA", "AREA"]], area_unit="HECTARES"
    )

    # remove working files
    arcpy.management.Delete(landsCopy)
    return harvestedAreasProcessedPath


def parcelMapBCGeoprocessing(rawPath, dataset):
    """
    ParcelMap BC Parcel Fabric geoprocessing.

    :param rawPath: Raw feature class path
    :type rawPath: str
    :param dataset: Input dataset
    :type dataset: Dataset
    :return: Processed file
    :rtype: result
    """ 

    arcpy.env.overwriteOutput = True

    parcelsGdb=f"{dataset.downloadFolder}\\{dataset.fileName}.gdb"
    
    #create storage gdb
    arcpy.CreateFileGDB_management(dataset.downloadFolder, dataset.fileName)

    arcpy.env.workspace = parcelsGdb

    gdbSOI = arcpy.CopyFeatures_management(UniversalPathsWrapper.soiPath, parcelsGdb)

    #delete fields
    print(f"{dataset.alias}: Deleting fields")

    deleteFields = [ "PARCEL_FABRIC_POLY_ID", "PARCEL_STATUS", "PARCEL_CLASS", "PARCEL_START_DATE", "WHEN_UPDATED", "FEATURE_AREA_SQM", "FEATURE_LENGTH_M", "SE_ANNO_CAD_DATA", ]

    arcpy.DeleteField_management(rawPath, deleteFields)

    # intersect with SOIs
    print(f"{dataset.alias}: Starting intersect (This might take a while…)")

    parcelMapProcessedPath = arcpy.Intersect_analysis(
        [rawPath, gdbSOI], dataset.fileName, "NO_FID"
    )

    # cleanup
    arcpy.Delete_management(arcpy.Describe(rawPath).path)
    arcpy.Delete_management(gdbSOI)

    return parcelMapProcessedPath

def digitalRoadAtlasGeoprocessing(rawPath, dataset):
    """
    Digital Road Atlas geoprocessing.

    :param rawPath: Raw feature class path
    :type rawPath: str
    :param dataset: Input dataset
    :type dataset: Dataset
    :return: Processed file
    :rtype: result
    """ 

    # dictionary for calculating fields
    fieldValueDictionary = {
        ("freeway", "highway"): "highway",
        ("arterial", "collector", "ramp"): "main",
        ("local", "lane"): "local",
        "ferry": "ferry",
        "unclassified": "unnamed/logging",
        (
            "alleyway",
            "driveway",
            "private",
            "recreation",
            "resource",
            "restricted",
            "runway",
            "service",
            "strata",
            "yield",
        ): "other",
        ("pedestrian", "trail"): "path",
        "proposed": "proposed",
    }
  
    arcpy.env.workspace = dataset.arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    #delete fields from working copies
    print(f"{dataset.alias}: Deleting fields from working copies")

    deleteFields = [ "FTYPE", "HWYEXITNUM", "HWYRTENUM", "SEGLNGTH2D", "SEGLNGTH3D", "RDALIAS1ID", "RDALIAS3", "RDALIAS3ID", "RDALIAS4", "RDALIAS4ID", "RDNAMEID", "FNODE", "TNODE", "SPPLR", "SPPLR_DTL", "CPTRCHN", "FCODE", "OBJECTID", ]

    arcpy.DeleteField_management(rawPath, deleteFields)

    arcpy.AddField_management(rawPath, "road_type", "TEXT", field_length=30)

    cursor = arcpy.da.UpdateCursor(rawPath, ["ROAD_CLASS", "road_type"])

    # calculate field Values
    print(f"{dataset.alias}: Calculating field values")
    for row in cursor:
        for key in fieldValueDictionary:
            if row[0] in key:
                row[1] = fieldValueDictionary[key]
                cursor.updateRow(row)
                break

    del cursor

    print(f"{dataset.alias}: Starting Dissolve") 
    roadAtlasDisolve = arcpy.Dissolve_management(
        rawPath, "tempRoadDisolve.shp", ["RDNAME", "road_type"], [["RDALIAS1", "FIRST"], 
        ["RDALIAS2", "FIRST"], ["RDNAME", "FIRST"], ["RDSURFACE", "FIRST"], ["ROAD_CLASS", "FIRST"], ["NUMLANES","FIRST"], ["CPTRDATE","FIRST"], ["FEAT_LEN", "SUM"]], "SINGLE_PART"
    )    

    # intersect with SOI
    print(f"{dataset.alias}: Starting intersect") 
    roadAtlasIntersect = arcpy.Intersect_analysis(
        [roadAtlasDisolve, UniversalPathsWrapper.soiPath],
        dataset.fileName,
        "NO_FID",
    )

    #Cleanup   
    arcpy.Delete_management(roadAtlasDisolve)
    #arcpy.Delete_management(rawPath)

    return roadAtlasIntersect

def alcAlrPolygonsGeoprocessing(rawPath, dataset):
    """
    ALC ALR Polygons geoprocessing.

    :param rawPath: Raw feature class path
    :type rawPath: str
    :param dataset: Input dataset
    :type dataset: Dataset
    :return: Processed file
    :rtype: result
    """ 

    arcpy.env.workspace = dataset.arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True
    
    # delete fields from raw
    print(f"{dataset.alias}: Creating working copies, deleting fields")
    
    deleteFields = ["STATUS", "FTRCD", "OBJECTID", "AREA_SQM"]
    arcpy.DeleteField_management(rawPath, deleteFields)

    # create lands copy witth specific fieldsAll.
    landsDeleteFields = [ "LOCALAREA", "ICF_AREA", "GEOMETRY_SOURCE", "ATTRIBUTE_SOURCE", "PID", "PIN", "JUROL", "LTSA_LOT", "LTSA_BLOCK", "LTSA_PARCEL", "LTSA_PLAN", "LEGAL_FREEFORM", "LAND_DISTRICT", "LAND_ACT_PRIMARY_DESCRIPTION", "PARCEL_DESCRIPTION", "SOURCE_PROVISION_DATE", "landval_2017", "valperHa_2017", "result_val_2017", "Ha", "new_group", "comments", "new_ownership", "PMBC", "ICIS", "ICF", "landval_src", "prop_class", "needs_confirm", "confirm_question", "selected", "label", "location", "specific_location", "H_", "use_on_prop", "potential_FCyCmPD", "interests", "available", "avail_issues", "owner", "EN", "guide_outfit", "trapline", "ess_response", "tourism_capability", "access", "zoning", "zone_code", "TENURES", "parcel_num", "PIN_DISTLE", "PIN_SUBDLA", "municipality", "arch_sites", "Title_num", "Title_owner", "Title_Info", "essential", "RoW", "OtherComments", "appraisal2work", "apprais2HBU", "apprais2reportID", "apprais2BC_ID", "apprais2Ha", "TEMP_PolyID", "TimbeTableLink", "ownership_type", ]

    landsCopy =copySpecificFields(UniversalPathsWrapper.htgLandsPath, landsDeleteFields)

    #rename fields
    shapefileFieldRename(landsCopy, "OWNER_CLAS", "CROWN")

    # calculate values for "CROWN" field
    print(f"{dataset.alias}: Calculating field values")
    cursor = arcpy.da.UpdateCursor(landsCopy, ["CROWN"])

    for row in cursor:
        #NOTE: is this doing what we want?
        if "CROWN" in str(row[0]):
            row[0] = "yes"
        else:
            row[0] = "no"

        cursor.updateRow(row)

    del cursor

    # intersect with lands
    print(f"{dataset.alias}: Starting intersect")    
    alcAlrProcessed = arcpy.Intersect_analysis(
        [rawPath, landsCopy], dataset.fileName, join_attributes="NO_FID",
    )
    
    # cleanup
    arcpy.DeleteField_management(
        alcAlrProcessed, ["FEAT_LEN", "Shape_Leng", "Shape_Area"]
    )

    arcpy.Delete_management(rawPath)
    arcpy.Delete_management(landsCopy)

    return alcAlrProcessed

def environmentalRemediationSitesGeoprocessing(rawPath, dataset):
    """
    Environmental Remediation Sites geoprocessing.

    :param rawPath: Raw feature class path
    :type rawPath: str
    :param dataset: Input dataset
    :type dataset: Dataset
    :return: Processed file
    :rtype: result
    """ 


    arcpy.env.workspace = dataset.arcgisWorkspaceFolder
    arcpy.env.overwriteOutput = True

    #delete fields from raw
    print(f"{dataset.alias}: Creating working copies, deleting fields")

    deleteFields = [ "ENV_RMD_ID", "GEN_DESC", "VICFILENO", "REGFILENO", "COMMON_NM", "LATITUDE", "LONGITUDE", "OBJECTID", ]

    arcpy.DeleteField_management(rawPath, deleteFields)

    landsDeleteFields = [ "LOCALAREA", "ICF_AREA", "GEOMETRY_SOURCE", "ATTRIBUTE_SOURCE", "PID", "PIN", "JUROL", "LTSA_LOT", "LTSA_BLOCK", "LTSA_PARCEL", "LTSA_PLAN", "LEGAL_FREEFORM", "LAND_DISTRICT", "LAND_ACT_PRIMARY_DESCRIPTION", "PARCEL_DESCRIPTION", "SOURCE_PROVISION_DATE", "landval_2017", "valperHa_2017", "result_val_2017", "Ha", "new_group", "comments", "new_ownership", "PMBC", "ICIS", "ICF", "landval_src", "prop_class", "needs_confirm", "confirm_question", "selected", "label", "location", "specific_location", "H_", "use_on_prop", "potential_FCyCmPD", "interests", "available", "avail_issues", "owner", "EN", "guide_outfit", "trapline", "ess_response", "tourism_capability", "access", "zoning", "zone_code", "TENURES", "parcel_num", "PIN_DISTLE", "PIN_SUBDLA", "municipality", "arch_sites", "Title_num", "Title_owner", "Title_Info", "essential", "RoW", "OtherComments", "appraisal2work", "apprais2HBU", "apprais2reportID", "apprais2BC_ID", "apprais2Ha", "TEMP_PolyID", "TimbeTableLink", "ownership_type", ]

    landsCopy =copySpecificFields(UniversalPathsWrapper.htgLandsPath, landsDeleteFields)    
   
    # rename and calculate fields
    print(f"{dataset.alias}: Renaming Fields, Calculating field values")

    shapefileFieldRename(rawPath, "SITE_ID", "REMED_ID")
    shapefileFieldRename(landsCopy, "OWNER_CLAS", "CROWN" )

    cursor = arcpy.da.UpdateCursor(landsCopy, ["CROWN"])

    for row in cursor:
        #NOTE: is this doing what we want?
        if "CROWN" in str(row[0]):
            row[0] = "yes"
        else:
            row[0] = "no"

        cursor.updateRow(row)

    del cursor

    # intersect with Lands
    print(f"{dataset.alias}: Starting intersect") 
    remediationProcessed = arcpy.Intersect_analysis(
        [landsCopy, rawPath], dataset.fileName, join_attributes="NO_FID",
    )
    
    # cleanup
    arcpy.DeleteField_management(remediationProcessed, ["Shape_Lengt", "Shape_Area"])
    arcpy.Delete_management(landsCopy)
    arcpy.Delete_management(rawPath)

    return remediationProcessed
