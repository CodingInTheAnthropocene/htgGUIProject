


from modules import *
import arcpy


environmentalRemediationSiteRaw = r"C:\Users\laure\Desktop\test\data\RMDTN_STS_point.shp"
alcAlrRaw = r"C:\Users\laure\Desktop\test\data\TSLRPLS_polygon.shp"

digitalRoadRaw = r"C:\Users\laure\Desktop\test\data\DRA_MPAR_line.shp"

parcelsRaw = r"C:\Users\laure\Desktop\test\PMBC_PARCEL_FABRIC_POLY_SVW.gdb\WHSE_CADASTRE_PMBC_PARCEL_FABRIC_POLY_SVW"
tenuresRaw=r"C:\Users\laure\Desktop\test\TA_CROWN_TENURES_SVW\TA_CRT_SVW_polygon.shp"

# parcelMapBCGeoprocessing(parcelsRaw)

# digitalRoadAtlasGeoprocessing(digitalRoadRaw)

#alcAlrPolygonsGeoprocessing(alcAlrRaw)

#environmentalRemediationSitesGeoprocessing(environmentalRemediationSiteRaw)

#crownTenuresGeoprocessing(tenuresRaw)


writeMetadata(r"C:\Users\laure\Desktop\test\crownTenuresProcessed.shp", crownTenuresSettings.jsonPayload, r"C:\Users\laure\Desktop\test\TA_CROWN_TENURES_SVW\TA_CRT_SVW_polygon.shp")