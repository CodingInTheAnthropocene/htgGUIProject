"""
settingsWrapper.py - Classes for handling configuration file reading and writing.
"""

from json import dump, load
import dependencies.bbox_SOIs as bbox_SOIs
from configuration.initiationDictionary import initiationDictionary
from modules.universalFunctions import *


# load settings file


class UniversalSettingsWrapper:
    """
    Reads from and writes to universalSettings in settings.json configuration file. Instantiated when a Dataset object is instantiated and  passes information to that object.
    """
    def __init__(self): 
        settingsFile = "configuration\\settings.json"

        with open(settingsFile) as settingsFile:
            configurationDictionary = load(settingsFile)

        # get information from settings.json    
        self.email = configurationDictionary["universalSettings"]["email"]
        self.downloadFolder = configurationDictionary["universalSettings"]["downloadFolder"]
        self.archiveFolder = configurationDictionary["universalSettings"]["archiveFolder"]
        self.logFolder = configurationDictionary["universalSettings"]["logFolder"]
        self.htgLandsPath = configurationDictionary["universalSettings"]["htgLandsPath"]
        self.soiPath = configurationDictionary["universalSettings"]["soiPath"]
        self.soiCorePath = configurationDictionary["universalSettings"]["soiCorePath"]
        self.soiMarinePath = configurationDictionary["universalSettings"]["soiMarinePath"]
        self.soiWhaPath = configurationDictionary["universalSettings"]["soiWhaPath"]
        self.aoiSwBcPath = configurationDictionary["universalSettings"]["aoiSwBcPath"]

    def settingsWriter(self, attributeDictionary):
        """Writes values in a dictionary back to universalSettings in settings.json"
        
        :param attributeDictionary: Values to populate in settings file. Keys must match those in universalSettings in settings.json.
        :type attributeDictionary: dictionary
        """

        # open settings.json for reading and load as Python dictionary
        with open("configuration\\settings.json", "r") as settingsFile:
            configurationDictionary = load(settingsFile)
        
        # open settings.json for writing and dump attributes from attributeDictionary
        with open("configuration\\settings.json", "w") as settingsFile:
            for attribute in attributeDictionary:
                configurationDictionary["universalSettings"][attribute] = attributeDictionary[attribute]
            
            dump(configurationDictionary, settingsFile)


class DatasetSettingsWrapper:
    """Wrapper and writer for information from configuration files(settings.json, initiationDictionary.py). Instantiated when a Dataset object is instantiated, and passes configuration information to that object.
    """    
    def __init__(self, datasetAlias):
        """
        Constructor method

        :param datasetAlias: Alias used in settings.json and initiationDictionary describe different datasets. Alias must match one of these datasets.
        :type datasetAlias: str
        """
       
        self.universalSettingsWrapper= UniversalSettingsWrapper()  
        settingsFile = "configuration\\settings.json"

        with open(settingsFile) as settingsFile:
            configurationDictionary = load(settingsFile)
            

        # catalogue dictionaries
        catalogueDatasetsConfigurationDictionary = configurationDictionary["datasets"][
            "catalogueDatasets"
        ]
        catalogueDatasetsInitiationDictionary = initiationDictionary["datasets"][
            "catalogueDatasets"
        ]

        # hybrid dictionaries
        hybridDatasetsConfigurationDictionary = configurationDictionary["datasets"][
            "hybridDatasets"
        ]
        hybridDatasetsInitiationDictionary = initiationDictionary["datasets"][
            "hybridDatasets"
        ]

        # if dataset is a catalogue Dataset
        if datasetAlias in catalogueDatasetsConfigurationDictionary.keys():
            # configuration from settings.json
            self.configuration = catalogueDatasetsConfigurationDictionary[datasetAlias]
            # configuration from initiationDictionary.py
            self.initiation = catalogueDatasetsInitiationDictionary[datasetAlias]
            self.type="catalogue"
        
        # if dataset is a hybrid Dataset
        elif datasetAlias in hybridDatasetsConfigurationDictionary.keys():
            # configuration from settings.json
            self.configuration = hybridDatasetsConfigurationDictionary[datasetAlias]
            # configuration from initiationDictionary.py
            self.initiation = hybridDatasetsInitiationDictionary[datasetAlias]
            self.type= "hybrid"

        # attribute instantiation
        self.name = self.initiation["name"]
        self.alias = datasetAlias

        self.rawFormat = self.initiation["rawFormat"]
        self.geoprocessingFunction=self.initiation["geoprocessingFunction"]
        

        self.currentPath = self.configuration["currentPath"]
        self.updateFrequency = self.configuration["updateFrequency"]
        self.fileName = self.configuration["fileName"]
        self.aoi = self.configuration["aoi"]

        # choose between universal or custom download folders
        self.downloadFolder = (
            self.universalSettingsWrapper.downloadFolder
            if self.configuration["downloadFolder"] == "universal"
            else self.configuration["downloadFolder"]
        )

        self.archiveFolder = (
            self.universalSettingsWrapper.archiveFolder
            if self.configuration["archiveFolder"] == "universal"
            else self.configuration["archiveFolder"]
        )

        # choose between download folder or custom folder
        self.arcgisWorkspaceFolder = (
            self.downloadFolder
            if self.configuration["arcgisWorkspaceFolder"] == "download"
            else self.configuration["arcgisWorkspaceFolder"]
        )

        # choose which AOI to include as part of the json payload
        if self.aoi == "marine":
            aoiChoice = bbox_SOIs.marine
        elif self.aoi == "core":
            aoiChoice = bbox_SOIs.core
        elif self.aoi == "wha":
            aoiChoice = bbox_SOIs.wha
        elif self.aoi == "swbc":
            aoiChoice = bbox_SOIs.swbc

        # determine to request download in shapefile or geodatabase format
        if self.rawFormat == "shapefile":
            formatChoice = "0"
        elif self.rawFormat == "geodatabase":
            formatChoice = "3"
        
        # get list of all URLs in dataset. Only hybrid datasets will have url.
        self.urlList=itemGeneratorList(self.initiation, "url")

        # get list of all data catalog IDs for dataset
        self.dataCatalogueIdList = itemGeneratorList(self.initiation, "dataCatalogueId")

        #Create list of all JSON payload feature items for dataset
        self.jsonPayloadFeatureItems=itemGeneratorList(self.initiation, "jsonPayloadFeatureItems")

        self.jsonPayload = {
            "emailAddress": self.universalSettingsWrapper.email,
            "aoiType": "1",
            "aoi": aoiChoice,
            "orderingApplication": "BCDC",
            "crsType": "0",
            "clippingMethodType": "1",
            "formatType": formatChoice,
            "useAOIBounds": "",
            "prepackagedItems": "",
            "aoiName": "",
            "featureItems": self.jsonPayloadFeatureItems,
        }

    def settingsWriter(self, attributeDictionary):
        """Writes values in a dictionary back to both hybrid and catalogue dataset settings in settings.json"
        
        :param attributeDictionary: Values to populate in settings file. Keys must match those of datasets in settings.json.
        :type attributeDictionary: dictionary
        """       
        with open("configuration\\settings.json", "r") as settingsFile:
            configurationDictionary = load(settingsFile)
        
        with open("configuration\\settings.json", "w") as settingsFile:
            for attribute in attributeDictionary:
                if self.type == "catalogue":
                    configurationDictionary["datasets"]["catalogueDatasets"][self.alias][attribute] = attributeDictionary[attribute]
                elif self.type == "hybrid":
                    configurationDictionary["datasets"]["hybridDatasets"][self.alias][attribute] = attributeDictionary[attribute]
                
            dump(configurationDictionary, settingsFile)
        

    







        
    
    
        

