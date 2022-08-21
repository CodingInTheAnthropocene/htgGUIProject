"""
1 of 2 configuration filles for application. The other being settings.json. This dictionary contains information which won't need to be changed in GUI settings. It can be changed, but likely other things will have to be changed as well to accommodate that. For example, if  you were to change the format from shapefile to Geodatabase, it's not a guarantee that the corresponding geoprocessing chain is set up for that.
"""

initiationDictionary = {
    "datasets": {
        "catalogueDatasets": {
            "crownTenures": {
                "name": "Tantalis Crown Tenures",
                "dataCatalogueId": "3544ad91-0cf2-4926-a08a-bfe42d9a031d",
                "geoprocessingFunction": "crownTenuresGeoprocessing",
                "rawFormat": "shapefile",
                "jsonPayloadFeatureItems": {
                    "featureItem": "WHSE_TANTALIS.TA_CROWN_TENURES_SVW",
                    "filterValue": "",
                    "layerName": "TANTALIS - Crown Tenures",
                    "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/tantalis-crown-tenures",
                    "filterType": "No Filter",
                    "pctOfMax": 3,
                },
            },
            "forestHarvestingAuthority": {
                "name": "Forest Tenure Harvesting Authority Polygons",
                "dataCatalogueId": "cff7b8f7-6897-444f-8c53-4bb93c7e9f8b",
                "geoprocessingFunction": "forestHarvestingAuthorityGeoprocessing",
                "rawFormat": "shapefile",
                "jsonPayloadFeatureItems": {
                    "featureItem": "WHSE_FOREST_TENURE.FTEN_HARVEST_AUTH_POLY_SVW",
                    "filterValue": "",
                    "layerName": "Forest Tenure Harvesting Authority Polygons",
                    "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/forest-tenure-harvesting-authority-polygons",
                    "filterType": "No Filter",
                    "pctOfMax": 3,
                },
            },
            "forestManagedLicence": {
                "name": "Forest Tenure Managed Licence",
                "dataCatalogueId": "c3e96239-cdc9-4328-ac19-58fba1623ef8",
                "geoprocessingFunction": "forestManagedLicenceGeoprocessing",
                "rawFormat": "shapefile",
                "jsonPayloadFeatureItems": {
                    "featureItem": "WHSE_FOREST_TENURE.FTEN_MANAGED_LICENCE_POLY_SVW",
                    "filterValue": "",
                    "layerName": "Forest Tenure Managed Licence",
                    "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/forest-tenure-managed-licence",
                    "filterType": "No Filter",
                    "pctOfMax": 3,
                },
            },
            "harvestedAreas": {
                "name": "Harvested Areas of BC",
                "dataCatalogueId": "b1b647a6-f271-42e0-9cd0-89ec24bce9f7",
                "geoprocessingFunction": "harvestedAreasGeoprocessing",
                "rawFormat": "shapefile",
                "jsonPayloadFeatureItems": {
                    "featureItem": "WHSE_FOREST_VEGETATION.VEG_CONSOLIDATED_CUT_BLOCKS_SP",
                    "filterValue": "",
                    "layerName": "Harvested Areas of BC (Consolidated Cutblocks)",
                    "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/harvested-areas-of-bc-consolidated-cutblocks-",
                    "filterType": "No Filter",
                    "pctOfMax": 3,
                },
            },
            "parcelMapBC": {
                "name": "ParcelMap BC Parcel Fabric",
                "dataCatalogueId": "4cf233c2-f020-4f7a-9b87-1923252fbc24",
                "geoprocessingFunction": "parcelMapBCGeoprocessing",
                "rawFormat": "geodatabase",
                "jsonPayloadFeatureItems": {
                    "featureItem": "WHSE_CADASTRE.PMBC_PARCEL_FABRIC_POLY_SVW",
                    "filterValue": "",
                    "layerName": "ParcelMap BC Parcel Fabric",
                    "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/parcelmap-bc-parcel-fabric",
                    "filterType": "No Filter",
                    "pctOfMax": 7,
                },
            },
            "digitalRoadAtlas": {
                "name": "Digital Road Atlas",
                "dataCatalogueId": "bb060417-b6e6-4548-b837-f9060d94743e",
                "geoprocessingFunction": "digitalRoadAtlasGeoprocessing",
                "rawFormat": "shapefile",
                "jsonPayloadFeatureItems": {
                    "featureItem": "WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP",
                    "filterValue": "",
                    "layerName": "Digital Road Atlas (DRA) - Master Partially-Attributed Roads",
                    "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/digital-road-atlas-dra-master-partially-attributed-roads",
                    "filterType": "No Filter",
                    "pctOfMax": 9,
                },
            },
            "alcAlrPolygons": {
                "name": "ALC ALR Polygons",
                "dataCatalogueId": "92e17599-ac8a-47c8-877c-107768cb373c",
                "geoprocessingFunction": "alcAlrPolygonsGeoprocessing",
                "rawFormat": "shapefile",
                "jsonPayloadFeatureItems": {
                    "featureItem": "WHSE_LEGAL_ADMIN_BOUNDARIES.OATS_ALR_POLYS",
                    "filterValue": "",
                    "layerName": "ALC ALR Polygons",
                    "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/alc-alr-polygons",
                    "filterType": "No Filter",
                    "pctOfMax": 3,
                },
            },
            "environmentalRemediationSites": {
                "name": "Environmental Remediation Sites",
                "dataCatalogueId": "63804e64-a4f3-4bc7-b1e3-5f736bbc3967",
                "geoprocessingFunction": "environmentalRemediationSitesGeoprocessing",
                "rawFormat": "shapefile",
                "jsonPayloadFeatureItems": {
                    "featureItem": "WHSE_WASTE.SITE_ENV_RMDTN_SITES_SVW",
                    "filterValue": "",
                    "layerName": "Environmental Remediation Sites",
                    "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/environmental-remediation-sites",
                    "filterType": "No Filter",
                    "pctOfMax": 3,
                },
            },
        },
        "hybridDatasets": {
            "parksRecreationDatasets": {
                "name": "Parks and Recreation Datasets",
                "rawFormat": "shapefile",
                "geoprocessingFunction": "parksRecreationDatasetsGeoprocessing",
                "catalogueDatasets": {
                    "recreationPolygons": {
                        "dataCatalogueId": "263338a7-93ee-49c1-83e8-13f0bde70833",
                        "jsonPayloadFeatureItems": {
                            "featureItem": "WHSE_FOREST_TENURE.FTEN_RECREATION_POLY_SVW",
                            "filterValue": "",
                            "layerName": "Recreation Polygons",
                            "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/recreation-polygons",
                            "filterType": "No Filter",
                            "pctOfMax": 3,
                        },
                    },
                    "nationalParks": {
                        "dataCatalogueId": "88e61a14-19a0-46ab-bdae-f68401d3d0fb",
                        "jsonPayloadFeatureItems": {
                            "featureItem": "WHSE_ADMIN_BOUNDARIES.CLAB_NATIONAL_PARKS",
                            "filterValue": "",
                            "layerName": "National Parks of Canada within British Columbia",
                            "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/national-parks-of-canada-within-british-columbia",
                            "filterType": "No Filter",
                            "pctOfMax": 3,
                        },
                    },
                    "parksEcologicalProtected": {
                        "dataCatalogueId": "1130248f-f1a3-4956-8b2e-38d29d3e4af7",
                        "jsonPayloadFeatureItems": {
                            "featureItem": "WHSE_TANTALIS.TA_PARK_ECORES_PA_SVW",
                            "filterValue": "",
                            "layerName": "BC Parks, Ecological Reserves, and Protected Areas",
                            "layerMetadataUrl": "https://catalogue.data.gov.bc.ca/dataset/bc-parks-ecological-reserves-and-protected-areas",
                            "filterType": "No Filter",
                            "pctOfMax": 3,
                        },
                    },
                },
                "otherDatasets": {
                    "nanaimoParks": {
                        "url": "https://www.nanaimo.ca/open-data-catalogue/Download/Index?container=nanaimo&entitySetName=ParksGeoSpatial&downloadID=79",
                        "geoprocessingFunction": "nanaimoParksGeoprocessing",
                    },
                    "cvrdParks": {
                        "url": "https://maps.cvrd.ca/downloads/Shapefiles/Parks.zip",
                    },
                    "northCowichanParks": {
                        "url": "https://s3-us-west-2.amazonaws.com/openfiles.northcowichan.ca/GIS/Parks/Recreation_SHP.zip",
                    },
                },
            },
        },
    }
}
