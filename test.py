


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

digitalRoadRaw = r"C:\Users\laure\Desktop\test\data\DRA_MPAR_line.shp"

parcelsRaw = r"C:\Users\laure\Desktop\test\PMBC_PARCEL_FABRIC_POLY_SVW.gdb\WHSE_CADASTRE_PMBC_PARCEL_FABRIC_POLY_SVW"
tenuresRaw=r"C:\Users\laure\Desktop\test\TA_CROWN_TENURES_SVW\TA_CRT_SVW_polygon.shp"


pathsList=['C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\ForestryRecreation.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\NonDNCRecreation.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\Park.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\PARKS.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\Recreation.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\Water_Access.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\CLAB_NATIONAL_PARKS\\CLAB_NATPK_polygon.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\FTEN_RECREATION_POLY_SVW\\FTN_REC_PL_polygon.shp', 'C:\\Users\\laure\\Desktop\\test\\rawparksRecreationDatasets\\TA_PARK_ECORES_PA_SVW\\TA_PEP_SVW_polygon.shp']

# test=Dataset("forestHarvestingAuthority")
# test.rawFilePaths=r"C:\Users\laure\Desktop\test\data\RMDTN_STS_point.shp"
# test.geoprocessing()

