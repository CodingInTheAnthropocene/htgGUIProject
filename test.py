


from modules.customWidgets import datasetFrame
from modules.initiationDictionary import initiationDictionary
from modules import *
from modules.datasetObjects import *
import modules.settingsWrapper as Settings
import arcpy
from modules.settingsWrapper import *
from datetime import timedelta, date
from genericpath import getsize
from modules.universalFunctions import getFileCreatedDate, getCurrency
from modules.catalogueFunctions import *
from os.path import split, splitext
from json import load
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from re import sub
from traceback import print_exc


environmentalRemediationSiteRaw = r"C:\Users\laure\Desktop\test\data\RMDTN_STS_point.shp"
alcAlrRaw = r"C:\Users\laure\Desktop\test\data\TSLRPLS_polygon.shp"

digitalRoadRaw = r"C:\Users\laure\Desktop\test\rawdigitalRoads\DRA_DGTL_ROAD_ATLAS_MPAR_SP\DRA_MPAR_line.shp"

parcelsRaw = r"C:\Users\laure\Desktop\test\PMBC_PARCEL_FABRIC_POLY_SVW.gdb\WHSE_CADASTRE_PMBC_PARCEL_FABRIC_POLY_SVW"
tenuresRaw=r"C:\Users\laure\Desktop\test\TA_CROWN_TENURES_SVW\TA_CRT_SVW_polygon.shp"


pathsList=['C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\ForestryRecreation.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\NonDNCRecreation.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\Park.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\PARKS.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\Recreation.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\Water_Access.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\CLAB_NATIONAL_PARKS\\CLAB_NATPK_polygon.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\FTEN_RECREATION_POLY_SVW\\FTN_REC_PL_polygon.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\TA_PARK_ECORES_PA_SVW\\TA_PEP_SVW_polygon.shp']

test=Dataset("forestHarvestingAuthority")

test.archivedFile="test"
test.archiveStatus=True
test.name="test"
test.processedFile="test"
test.catalogueDownloadInfo="test"
test.writeLog()

# tic = time.perf_counter()
# alcAlrPolygonsGeoprocessing(alcAlrRaw, Dataset("alcAlrPolygons"))
# toc = time.perf_counter()
# print(f"geoprocessing: {toc - tic:0.4f} seconds")
        
#Dataset("digitalRoadAtlas").archiving()

# environmentalRemediationSitesGeoprocessing(environmentalRemediationSiteRaw, Dataset("environmentalRemediationSites"))

# Dataset("forestManagedLicense")

parcelsRaw = "C:\\Users\\laure\\Desktop\\test\\rawPMBC\\PMBC_PARCEL_FABRIC_POLY_SVW.gdb\\WHSE_CADASTRE_PMBC_PARCEL_FABRIC_POLY_SVW"

# tic = time.perf_counter()
# parcelMapBCGeoprocessing(parcelsRaw, Dataset("parcelMapBC"))
# toc = time.perf_counter()

# print(toc - tic)

# fieldList=[ "ATTRIBUTE_", "EN", "GEOMETRY_S", "H_", "Ha", "ICF", "ICF_AREA", "ICIS", "JUROL", "LAND_ACT_P", "LAND_DISTR", "LEGAL_FREE", "LOCALAREA", "LTSA_BLOCK", "LTSA_LOT", "LTSA_PARCE", "LTSA_PLAN", "OWNER_CLAS", "OtherComme", "PARCEL_DES", "PID", "PIN", "PIN_DISTLE", "PIN_SUBDLA", "PMBC", "RoW", "SOURCE_PRO", "TEMP_PolyI", "TENURES", "TimbeTable", "Title_Info", "Title_num", "Title_owne", "access", "apprais2BC", "apprais2HB", "apprais2Ha", "apprais2re", "appraisal2", "arch_sites", "avail_issu", "available", "comments", "confirm_qu", "ess_respon", "essential", "guide_outf", "interests", "label", "landval_20", "landval_sr", "location", "municipali", "needs_conf", "owner", "potential_", "prop_class", "result_val", "selected", "specific_l", "tourism_ca", "trapline", "use_on_pro", "valperHa_2", "zone_code", "zoning", "Shape_Leng", "Shape_Area", "new_owners", "ownership_", ]

# arcpy.env.workspace= r"C:\Users\laure\Desktop\test\test\Default.gdb"
# arcpy.env.overwriteOutput=True


# copySpecificFields( UniversalPathsWrapper.htgLandsPath, fieldList)

