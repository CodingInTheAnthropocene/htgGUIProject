
class crownTenuresSettings:
    # Tantatlis Crown Tenures
    name = "Tantalis Crown Tenures"
    dataCatalogueId = "3544ad91-0cf2-4926-a08a-bfe42d9a031d"
    fileName = "crownTenuresProcessed.shp"
    currentPath = r"C:\Users\laure\Desktop\test\crownTenuresProcessed.shp"
    downloadFolder = universalSettings.downloadFolder
    archiveFolder = universalSettings.archiveFolder
    arcgisWorkspaceFolder = downloadFolder
    alias = "crownTenures"
    updateDays = 1

    jsonPayload = {
        "emailAddress": universalSettings.email,
        "aoiType": "1",
        "aoi": bbox_SOIs.marine,
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
                "pctOfMax": 3,
            }
        ],
    }

    # cd_display values derived from this dictionary
    valuesDictionary = {
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


class forestHarvestingAuthoritySettings:
    # Forest Tenure Harvesting Authority Polygons (cut permits)
    name = "Forest Tenure Harvesting Authority Polygons"
    dataCatalogueId = "cff7b8f7-6897-444f-8c53-4bb93c7e9f8b"
    fileName = "forestTenureProcessed.shp"
    currentPath = r"C:\Users\laure\Desktop\test\forestTenureProcessed.shp"
    downloadFolder = universalSettings.downloadFolder
    archiveFolder = universalSettings.archiveFolder
    arcgisWorkspaceFolder = downloadFolder
    alias = "forestHarvestingAuthority"
    updateDays = 1

    jsonPayload = {
        "emailAddress": universalSettings.email,
        "aoiType": "1",
        "aoi": bbox_SOIs.core,
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
                "pctOfMax": 3,
            }
        ],
    }


class forestManagedLicenceSettings:
    # forest tenure managed licence
    name = "Forest Tenure Managed Licence"
    dataCatalogueId = "c3e96239-cdc9-4328-ac19-58fba1623ef8"
    fileName = "forestManagedLicenceProcessed.shp"
    currentPath = r"C:\Users\laure\Desktop\test\forestManagedLicenceProcessed.shp"
    downloadFolder = universalSettings.downloadFolder
    archiveFolder = universalSettings.archiveFolder
    arcgisWorkspaceFolder = downloadFolder
    alias = "forestManagedLicence"
    updateDays = 1

    jsonPayload = {
        "emailAddress": universalSettings.email,
        "aoiType": "1",
        "aoi": bbox_SOIs.core,
        "orderingApplication": "BCDC",
        "crsType": "0",
        "clippingMethodType": "1",
        "formatType": "0",
        "useAOIBounds": "",
        "prepackagedItems": "",
        "aoiName": "",
        "featureItems": [
            {
                "featureItem": "WHSE_FOREST_TENURE.FTEN_MANAGED_LICENCE_POLY_SVW",
                "filterValue": "",
                "layerName": "Forest Tenure Managed Licence",
                "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/forest-tenure-managed-licence",
                "filterType": "No Filter",
                "pctOfMax": 3,
            }
        ],
    }


class harvestedAreasSettings:

    name = "Harvested Areas of BC"
    dataCatalogueId = "b1b647a6-f271-42e0-9cd0-89ec24bce9f7"
    fileName = "harvestedAreas.shp"
    currentPath = r"C:\Users\laure\Desktop\test\harvestedAreas.shp"
    downloadFolder = universalSettings.downloadFolder
    archiveFolder = universalSettings.archiveFolder
    arcgisWorkspaceFolder = downloadFolder
    alias = "harvestedAreas"
    updateDays = 1

    jsonPayload = {
        "emailAddress": universalSettings.email,
        "aoiType": "1",
        "aoi": bbox_SOIs.core,
        "orderingApplication": "BCDC",
        "crsType": "0",
        "clippingMethodType": "1",
        "formatType": "0",
        "useAOIBounds": "",
        "prepackagedItems": "",
        "aoiName": "",
        "featureItems": [
            {
                "featureItem": "WHSE_FOREST_VEGETATION.VEG_CONSOLIDATED_CUT_BLOCKS_SP",
                "filterValue": "",
                "layerName": "Harvested Areas of BC (Consolidated Cutblocks)",
                "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/harvested-areas-of-bc-consolidated-cutblocks-",
                "filterType": "No Filter",
                "pctOfMax": 3,
            }
        ],
    }


class parksEcologicalProtectedSettings:
    name = "BC Parks, Ecological Reserves, and Protected Areas"
    dataCatalogueId = "1130248f-f1a3-4956-8b2e-38d29d3e4af7"
    fileName = "parksEcologicalProtected.shp"
    currentPath = r"C:\Users\laure\Desktop\test\parksEcologicalProtected.shp"
    downloadFolder = universalSettings.downloadFolder
    archiveFolder = universalSettings.archiveFolder
    alias = "parksEcologicalProtected"

    jsonPayload = {
        "emailAddress": universalSettings.email,
        "aoiType": "1",
        "aoi": bbox_SOIs.wha,
        "orderingApplication": "BCDC",
        "crsType": "0",
        "clippingMethodType": "1",
        "formatType": "0",
        "useAOIBounds": "",
        "prepackagedItems": "",
        "aoiName": "",
        "featureItems": [
            {
                "featureItem": "WHSE_TANTALIS.TA_PARK_ECORES_PA_SVW",
                "filterValue": "",
                "layerName": "BC Parks, Ecological Reserves, and Protected Areas",
                "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/bc-parks-ecological-reserves-and-protected-areas",
                "filterType": "No Filter",
                "pctOfMax": 3,
            }
        ],
    }


class nationalParksSettings:
    name = "National Parks of Canada"
    dataCatalogueId = "88e61a14-19a0-46ab-bdae-f68401d3d0fb"
    fileName = "nationalParks.shp"
    currentPath = r"C:\Users\laure\Desktop\test\nationalParks.shp"
    downloadFolder = universalSettings.downloadFolder
    archiveFolder = universalSettings.archiveFolder
    alias = "nationalParks"

    jsonPayload = {
        "emailAddress": universalSettings.email,
        "aoiType": "1",
        "aoi": bbox_SOIs.wha,
        "orderingApplication": "BCDC",
        "crsType": "0",
        "clippingMethodType": "1",
        "formatType": "0",
        "useAOIBounds": "",
        "prepackagedItems": "",
        "aoiName": "",
        "featureItems": [
            {
                "featureItem": "WHSE_ADMIN_BOUNDARIES.CLAB_NATIONAL_PARKS",
                "filterValue": "",
                "layerName": "National Parks of Canada within British Columbia",
                "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/national-parks-of-canada-within-british-columbia",
                "filterType": "No Filter",
                "pctOfMax": 3,
            }
        ],
    }


class recreationPolygonsSettings:
    name = "Recreation Polygons"
    dataCatalogueId = "263338a7-93ee-49c1-83e8-13f0bde70833"
    fileName = "recreationPolygons.shp"
    currentPath = r"C:\Users\laure\Desktop\test\recreationPolygons.shp"
    downloadFolder = universalSettings.downloadFolder
    archiveFolder = universalSettings.archiveFolder
    name = "recreationPolygons"

    jsonPayload = {
        "emailAddress": universalSettings.email,
        "aoiType": "1",
        "aoi": bbox_SOIs.wha,
        "crsType": "0",
        "clippingMethodType": "1",
        "formatType": "0",
        "useAOIBounds": "",
        "prepackagedItems": "",
        "aoiName": "",
        "featureItems": [
            {
                "featureItem": "WHSE_FOREST_TENURE.FTEN_RECREATION_POLY_SVW",
                "filterValue": "",
                "layerName": "Recreation Polygons",
                "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/recreation-polygons",
                "filterType": "No Filter",
                "pctOfMax": 3,
            }
        ],
    }


class parcelMapBCSettings:
    name = "ParcelMap BC Parcel Fabric"
    dataCatalogueId = "4cf233c2-f020-4f7a-9b87-1923252fbc24"
    fileName = "PMBC.shp"
    currentPath = ""
    downloadFolder = universalSettings.downloadFolder
    archiveFolder = universalSettings.archiveFolder
    arcgisWorkspaceFolder = downloadFolder
    alias = "parcelMapBC"
    updateDays = 1

    jsonPayload = {
        "emailAddress": universalSettings.email,
        "aoiType": "1",
        "aoi": bbox_SOIs.marine,
        "orderingApplication": "BCDC",
        "crsType": "0",
        "clippingMethodType": "1",
        "formatType": "3",
        "useAOIBounds": "",
        "prepackagedItems": "",
        "aoiName": "",
        "featureItems": [
            {
                "featureItem": "WHSE_CADASTRE.PMBC_PARCEL_FABRIC_POLY_SVW",
                "filterValue": "",
                "layerName": "ParcelMap BC Parcel Fabric",
                "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/parcelmap-bc-parcel-fabric",
                "filterType": "No Filter",
                "pctOfMax": 7,
            }
        ],
    }


class digitalRoadAtlasSettings:
    name = "Digital Road Atlas"
    dataCatalogueId = "bb060417-b6e6-4548-b837-f9060d94743e"
    fileName = "roads.shp"
    currentPath = ""
    downloadFolder = universalSettings.downloadFolder
    archiveFolder = universalSettings.archiveFolder
    arcgisWorkspaceFolder = downloadFolder
    alias = "digitalRoadAtlas"
    updateDays = 1

    jsonPayload = {
        "emailAddress": universalSettings.email,
        "aoiType": "1",
        "aoi": bbox_SOIs.roadsMask,
        "orderingApplication": "BCDC",
        "crsType": "0",
        "clippingMethodType": "1",
        "formatType": "0",
        "useAOIBounds": "",
        "prepackagedItems": "",
        "aoiName": "",
        "featureItems": [
            {
                "featureItem": "WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP",
                "filterValue": "",
                "layerName": "Digital Road Atlas (DRA) - Master Partially-Attributed Roads",
                "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/digital-road-atlas-dra-master-partially-attributed-roads",
                "filterType": "No Filter",
                "pctOfMax": 9,
            }
        ],
    }

    valuesDictionary = {
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


class alcAlrPolygonsSettings:
    name = "ALC ALR Polygons"
    dataCatalogueId = "92e17599-ac8a-47c8-877c-107768cb373c"
    fileName = "ALR.shp"
    currentPath = ""
    downloadFolder = universalSettings.downloadFolder
    archiveFolder = universalSettings.archiveFolder
    arcgisWorkspaceFolder = downloadFolder
    alias = "alcAlrPolygons"
    updateDays = 1

    jsonPayload = {
        "emailAddress": universalSettings.email,
        "aoiType": "1",
        "aoi": bbox_SOIs.wha,
        "orderingApplication": "BCDC",
        "crsType": "0",
        "clippingMethodType": "1",
        "formatType": "0",
        "useAOIBounds": "",
        "prepackagedItems": "",
        "aoiName": "",
        "featureItems": [
            {
                "featureItem": "WHSE_LEGAL_ADMIN_BOUNDARIES.OATS_ALR_POLYS",
                "filterValue": "",
                "layerName": "ALC ALR Polygons",
                "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/alc-alr-polygons",
                "filterType": "No Filter",
                "pctOfMax": 3,
            }
        ],
    }


class environmentalRemediationSitesSettings:
    name = "Environmental Remediation Sites"
    dataCatalogueId = "63804e64-a4f3-4bc7-b1e3-5f736bbc3967"
    fileName = "remediation_sites.shp"
    currentPath = ""
    downloadFolder = universalSettings.downloadFolder
    archiveFolder = universalSettings.archiveFolder
    arcgisWorkspaceFolder = downloadFolder
    alias = "environmentalRemediationSites"
    updateDays = 1

    jsonPayload = {
        "emailAddress": "laurencejperry@outlook.com",
        "aoiType": "1",
        "aoi": bbox_SOIs.SW_BC,
        "orderingApplication": "BCDC",
        "crsType": "0",
        "clippingMethodType": "1",
        "formatType": "3",
        "useAOIBounds": "",
        "prepackagedItems": "",
        "aoiName": "",
        "featureItems": [
            {
                "featureItem": "WHSE_WASTE.SITE_ENV_RMDTN_SITES_SVW",
                "filterValue": "",
                "layerName": "Environmental Remediation Sites",
                "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/environmental-remediation-sites",
                "filterType": "No Filter",
                "pctOfMax": 3,
            }
        ],
    }


# Other datasets
class nanaimoParksSettings:
    name = "Nanaimo City Parks"
    fileName = "nanaimoParks.shp"
    downloadFolder = universalSettings.downloadFolder
    downloadURL = "https://www.nanaimo.ca/open-data-catalogue/Download/Index?container=nanaimo&entitySetName=ParksGeoSpatial&downloadID=79"
    alias = "nanaimoParks"


class cvrdParksSettings:
    name = "CVRD Parks"
    fileName = "cvrdParks.shp"
    downloadFolder = universalSettings.downloadFolder
    downloadURL = "https://maps.cvrd.ca/downloads/Shapefiles/Parks.zip"
    alias = "cvrdParks"


class northCowichanParksSettings:
    name = "North Cowichan Recreation"
    dataCatalogueId = "c9f0be75-81d1-4a8b-b463-09afe46e03b2"
    fileName = "northCowichanParksShapefiles"
    downloadFolder = universalSettings.downloadFolder
    downloadURL = "https://s3-us-west-2.amazonaws.com/openfiles.northcowichan.ca/GIS/Parks/Recreation_SHP.zip"
    alias = "northCowichanParks"


# hybrid datasets
class parksRecreationDatasetsSettings:
    name = "Parks/Recreation Datasets"
    dataCatalogueId = "N/A"
    fileName = "parksProcessed.shp"
    currentPath = r"C:\Users\laure\Desktop\test\parksProcessed.shp"
    archiveFolder = universalSettings.archiveFolder
    downloadFolder = universalSettings.downloadFolder
    arcgisWorkspaceFolder = downloadFolder
    alias = "parksRecreationDatasets"
    updateDays = 1
