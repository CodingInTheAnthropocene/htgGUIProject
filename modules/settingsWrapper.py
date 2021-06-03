import bbox_SOIs
from json import load
from catalogueFunctions import *

configurationDictionary = load("settings.json")

initDictionary = {
    "crownTenures": {
        "geoprocessingFunction": crownTenuresGeoprocessing,
        "rawFormat": "shapefile",
        "jsonPayloadFeatureItems": {
            "featureItem": "WHSE_TANTALIS.TA_CROWN_TENURES_SVW",
            "filterValue": "",
            "layerName": "TANTALIS - Crown Tenures",
            "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/tantalis-crown-tenures",
            "filterType": "No Filter",
            "pctOfMax": 3,
        },
    }
}



class UniversalSettingsWrapper:
    email = configurationDictionary["universalSettings"]["email"]
    downloadFolder = configurationDictionary["universalSettings"]["downloadFolder"]
    archiveFolder = configurationDictionary["universalSettings"]["archiveFolder"]
    logFolder = configurationDictionary["universalSettings"]["logFolder"]


class UniversalPathsWrapper:
    htgLandsPath = configurationDictionary["universalPaths"]["htgLands"]
    soiPath = configurationDictionary["universalPaths"]["soiPath"]
    soiCorePath = configurationDictionary["universalPaths"]["soiCorePath"]
    soiMarinePath = configurationDictionary["universalPaths"]["soiMarinePath"]
    soiWhaPath = configurationDictionary["universalPaths"]["soiWhaPath"]
    aoiPath = configurationDictionary["universalPaths"]["htgLands"]


class CatalogueDatasetsSettingsWrapper:
    def __init__(self, datasetAlias):
        datasetSettings = configurationDictionary["datasets"]["catalogueDatasets"][
            datasetAlias
        ]

        self.name = datasetSettings["name"]
        self.dataCatalogueId = datasetSettings["Data catalogueId"]
        self.alias = datasetSettings["alias"]
        self.currentPath = datasetSettings["currentPath"]
        self.updateFrequency = datasetSettings["updateFrequency"]
        self.fileName = datasetSettings["fileName"]
        self.downloadFolder = datasetSettings["archiveFolder"]
        self.archiveFolder = datasetSettings["archiveFolder"]
        self.arcgisWorkspaceFolder = datasetSettings["arcgisWorkspaceFolder"]
        self.soiArea = datasetSettings["soiArea"]
        self.rawFormat = initDictionary["shapefile"]
        self.jsonPayloadFeatureItems = initDictionary["jsonPayloadFeatureItems"]

        if self.soiArea == "marine":
            soiChoice = bbox_SOIs.marine
        elif self.soiArea == "core":
            soiChoice = bbox_SOIs.core
        elif self.soiArea == "wha":
            soiChoice = bbox_SOIs.wha

        if self.rawFormat == "shapefile":
            formatChoice = "0"
        elif self.rawFormat == "geodatabase":
            formatChoice = "3"

        self.jsonPayload = {
            "emailAddress": UniversalSettingsWrapper.email,
            "aoiType": "1",
            "aoi": soiChoice,
            "orderingApplication": "BCDC",
            "crsType": "0",
            "clippingMethodType": "1",
            "formatType": formatChoice,
            "useAOIBounds": "",
            "prepackagedItems": "",
            "aoiName": "",
            "featureItems": [self.jsonPayloadFeatureItems],
        }


class HybridDatasetsSettingsWraper:
    pass

