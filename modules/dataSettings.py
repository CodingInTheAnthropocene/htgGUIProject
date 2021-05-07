
from os.path import getsize, getctime
from datetime import datetime


class universalSettings:
    htgLandsPath = r"C:\Users\laure\Desktop\test\data\dummy_lands.gdb\lands1_sub_2"
    soiPath = r"C:\Users\laure\Desktop\test\data\HTG_SOIs_all.shp"
    email = ""


class crownTenuresSettings:
    # Tantatlis Crown Tenures
    fileName = "crownTenuresProcessed.shp"
    currentPath = r"C:\Users\laure\Desktop\test\data\CrownTenuresProcessed.shp"
    downloadFolder = r"C:\Users\laure\Desktop\test"
    archiveFolder = r"C:\Users\laure\Desktop\test\testArchive"
    arcgisWorkspaceFolder = downloadFolder
    createdDate = datetime.fromtimestamp(
        getctime(currentPath)).strftime('%B %d-%Y')
    size = getsize(currentPath)

    # Names given by data catalogue
    rawDownloadFolderName = "TA_CROWN_TENURES_SVW"
    rawShapefileName = "TA_CRT_SVW_polygon.shp"

    # json payload sent to data catalogue
    jsonPayload = {
        "emailAddress": f"{universalSettings.email}",
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
                "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/tantalis-crown-tenures",
                "filterType": "No Filter",
                "pctOfMax": 3
            }
        ]
    }

    # cd_display values derived from this dictionary
    tenuresDictionary = {
        'AGRICULTURE, EXTENSIVE': 'agriculture',
        'AGRICULTURE, INTENSIVE': 'agriculture',
        'AQUACULTURE, PLANTS': 'aquaculture',
        'AQUACULTURE, SHELL FISH': 'aquaculture',
        'COMMERCIAL RECREATION, COMMUNITY OUTDOOR RECREATION': 'commercial recreation',
        'COMMERCIAL RECREATION, ECO TOURIST LODGE/RESORT': 'commercial recreation',
        'COMMERCIAL RECREATION, MISCELLANEOUS': 'commercial recreation',
        'COMMERCIAL RECREATION, TRAIL RIDING': 'commercial recreation',
        'COMMERCIAL, COMMERCIAL A': 'commercial',
        'COMMERCIAL, COMMERCIAL B': 'commercial',
        'COMMERCIAL, COMMERCIAL WHARF': 'wharf',
        'COMMERCIAL, FILM PRODUCTION': 'commercial',
        'COMMERCIAL, GENERAL': 'commercial',
        'COMMERCIAL, GOLF COURSE': 'commercial',
        'COMMERCIAL, MARINA': 'marina',
        'COMMERCIAL, MISCELLANEOUS': 'commercial',
        'COMMERCIAL, PRIVATE YACHT CLUB': 'commercial',
        'COMMUNICATION, COMBINED USES': 'communication',
        'COMMUNICATION, COMMUNICATION SITES': 'communication',
        'COMMUNITY, COMMUNITY FACILITY': 'community',
        'COMMUNITY, MISCELLANEOUS': 'community',
        'COMMUNITY, TRAIL MAINTENANCE': 'community',
        'ENVIRONMENT, CONSERVATION, & RECR, BUFFER ZONE': 'environment protection',
        'ENVIRONMENT, CONSERVATION, & RECR, ECOLOGICAL RESERVE': 'environment protection',
        'ENVIRONMENT, CONSERVATION, & RECR, ENVIRONMENT PROTECTION/CONSERVATION': 'environment protection',
        'ENVIRONMENT, CONSERVATION, & RECR, FISH AND WILDLIFE MANAGEMENT': 'wildlife management',
        'ENVIRONMENT, CONSERVATION, & RECR, FISHERY FACILITY': 'fishery facility',
        'ENVIRONMENT, CONSERVATION, & RECR, FOREST MANAGEMENT RESEARCH': 'forest/other research',
        'ENVIRONMENT, CONSERVATION, & RECR, PUBLIC ACCESS/PUBLIC TRAILS': 'public access',
        'ENVIRONMENT, CONSERVATION, & RECR, SCIENCE MEASUREMENT/RESEARCH': 'forest/other research',
        'ENVIRONMENT, CONSERVATION, & RECR, UREP/RECREATION RESERVE': 'recreation reserve',
        'ENVIRONMENT, CONSERVATION, & RECR, WATERSHED RESERVE': 'watershed reserve',
        'FIRST NATIONS, CULTURAL SIGNIFICANCE': 'First Nations',
        'FIRST NATIONS, INTERIM MEASURES': 'First Nations',
        'FIRST NATIONS, LAND CLAIM SETTLEMENT': 'First Nations',
        'FIRST NATIONS, RESERVE EXPANSION': 'First Nations',
        'FIRST NATIONS, TRADITIONAL USE': 'First Nations',
        'FIRST NATIONS, TREATY AREA': 'First Nations',
        'INDUSTRIAL, GENERAL': 'industrial',
        'INDUSTRIAL, HEAVY INDUSTRIAL': 'industrial',
        'INDUSTRIAL, LIGHT INDUSTRIAL': 'industrial',
        'INDUSTRIAL, LOG HANDLING/STORAGE': 'log handling',
        'INDUSTRIAL, MISCELLANEOUS': 'industrial',
        'INSTITUTIONAL, FIRE HALL': 'institutional',
        'INSTITUTIONAL, HOSPITAL/HEALTH FACILITY': 'institutional',
        'INSTITUTIONAL, INDOOR RECREATION FACILITY': 'institutional',
        'INSTITUTIONAL, LOCAL/REGIONAL PARK': 'park',
        'INSTITUTIONAL, MILITARY SITE': 'institutional',
        'INSTITUTIONAL, MISCELLANEOUS': 'institutional',
        'INSTITUTIONAL, PUBLIC WORKS': 'public works',
        'INSTITUTIONAL, SCHOOL/OUTDOOR EDUCATION FACILITY': 'institutional',
        'INSTITUTIONAL, WASTE DISPOSAL SITE': 'waste disposal',
        'MISCELLANEOUS LAND USES, LAND USE PLAN INTERIM AGREEMENT': 'other uses',
        'MISCELLANEOUS LAND USES, OTHER': 'other uses',
        'MISCELLANEOUS LAND USES, PLANNING/MARKETING/DEVELOP PROJECTS': 'other uses',
        'OCEAN ENERGY, INVESTIGATIVE AND MONITORING PHASE': 'ocean energy',
        'QUARRYING, CONSTRUCTION STONE': 'quarrying',
        'QUARRYING, MISCELLANEOUS': 'quarrying',
        'QUARRYING, SAND AND GRAVEL': 'quarrying',
        'RESIDENTIAL, APPLICATION ONLY - PRIVATE MOORAGE': 'moorage',
        'RESIDENTIAL, FLOATING CABIN': 'residential',
        'RESIDENTIAL, MISCELLANEOUS': 'residential',
        'RESIDENTIAL, PRIVATE MOORAGE': 'moorage',
        'RESIDENTIAL, RECREATIONAL RESIDENTIAL': 'residential',
        'RESIDENTIAL, REMOTE RESIDENTIAL': 'residential',
        'RESIDENTIAL, RURAL RESIDENTIAL': 'residential',
        'RESIDENTIAL, STRATA MOORAGE': 'moorage',
        'RESIDENTIAL, THERMAL LOOPS': 'alternate energy',
        'RESIDENTIAL, URBAN RESIDENTIAL': 'residential',
        'TRANSPORTATION, BRIDGES': 'bridges',
        'TRANSPORTATION, FERRY TERMINAL': 'ferry terminal',
        'TRANSPORTATION, NAVIGATION AID': 'navigation',
        'TRANSPORTATION, PUBLIC WHARF': 'wharf',
        'TRANSPORTATION, RAILWAY': 'rail',
        'TRANSPORTATION, ROADWAY': 'road',
        'UTILITY, ELECTRIC POWER LINE': 'electrical',
        'UTILITY, GAS AND OIL PIPELINE': 'pipeline',
        'UTILITY, MISCELLANEOUS': 'utility - other',
        'UTILITY, SEWER/EFFLUENT LINE': 'sewer line',
        'UTILITY, TELECOMMUNICATION LINE': 'communication',
        'UTILITY, WATER LINE': 'water line',
        'WINDPOWER, INVESTIGATIVE AND MONITORING PHASE': 'alternate energy'
    }


class forestTenureSettings:
    # Forest Tenure Harvesting Authority Polygons
    fileName = "forestTenureProcessed.shp"
    currentPath = r"C:\Users\laure\Desktop\test\forestTenureProcessed.shp"
    downloadFolder = r"C:\Users\laure\Desktop\test"
    archiveFolder = r"C:\Users\laure\Desktop\test\testArchive"
    arcgisWorkspaceFolder = downloadFolder
    createdDate = datetime.fromtimestamp(
        getctime(currentPath)).strftime('%B %d-%Y')
    size = getsize(currentPath)

    # Names given by data catalogue
    rawDownloadFolderName = "FTEN_HARVEST_AUTH_POLY_SVW"
    rawShapefileName = "FTN_HA_SVW_polygon.shp"

    jsonPayload={
	"emailAddress": f"{universalSettings.email}",
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
			"featureItem": "WHSE_FOREST_TENURE.FTEN_HARVEST_AUTH_POLY_SVW",
			"filterValue": "",
			"layerName": "Forest Tenure Harvesting Authority Polygons",
			"layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/forest-tenure-harvesting-authority-polygons",
			"filterType": "No Filter",
			"pctOfMax": 3
		}
	]
}
