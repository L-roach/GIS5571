#Esri toolbox from the MN DNR website
https://resources.gisdata.mn.gov/pub/gdrs/apps/pub/us_mn_state_dnr/dnr_arcgis_toolbox.zip
    
#geodatabase for lidar data of Ramsey county
https://resources.gisdata.mn.gov/pub/data/elevation/lidar/county/ramsey/geodatabase/
    #from this link: https://resources.gisdata.mn.gov/pub/data/elevation/lidar/county/ramsey/
    ##NOT GOOD

##USE THIS:
https://resources.gisdata.mn.gov/pub/data/elevation/lidar/examples/lidar_sample/las/
    
#convert lidar to dem resource
https://www.caee.utexas.edu/prof/maidment/CE365KSpr15/Terrain/Terrain.pdf
    ArcGIS help: https://desktop.arcgis.com/en/arcmap/10.3/manage-data/las-dataset/lidar-solutions-creating-raster-dems-and-dsms-from-large-lidar-point-collections.htm

#python command for create las dataset

arcpy.management.CreateLasDataset(r"C:\Users\roach258\Downloads\4342-13-07(2).las", r"C:\Users\roach258\Documents\ArcGIS\Projects\MyProject\c4342-13-07(2)_LasDataset.lasd", "NO_RECURSION", None, 'PROJCS["NAD_1983_UTM_Zone_15N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-93.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]],VERTCS["NAVD_1988",VDATUM["North_American_Vertical_Datum_1988"],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]]', "COMPUTE_STATS", "ABSOLUTE_PATHS", "NO_FILES", "DEFAULT", None, "INTERSECTED_FILES")



#python command for create raster from dataset
arcpy.conversion.LasDatasetToRaster("c4342-13-07(2)_LasDataset.lasd", r"c:\users\roach258\documents\arcgis\projects\myproject\myproject.gdb\c43421_lasda", "ELEVATION", "BINNING AVERAGE LINEAR", "FLOAT", "CELLSIZE", 10, 1)

##This is the history of what I did in arcgis pro

#extract las
arcpy.ddd.ExtractLas("4342-13-07.las", r"C:\Users\roach258\Downloads", "DEFAULT", None, "PROCESS_EXTENT", '', "MAINTAIN_VLR", "REARRANGE_POINTS", "COMPUTE_STATS", r"C:\Users\roach258\Documents\ArcGIS\Projects\MyProject\output.lasd", "SAME_AS_INPUT")

#create las dataset
arcpy.management.CreateLasDataset(r"C:\Users\roach258\Downloads\4342-13-07(2).las", r"C:\Users\roach258\Documents\ArcGIS\Projects\MyProject\c4342-13-07(2)_LasDataset.lasd", "NO_RECURSION", None, 'PROJCS["NAD_1983_UTM_Zone_15N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-93.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]],VERTCS["NAVD_1988",VDATUM["North_American_Vertical_Datum_1988"],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]]', "COMPUTE_STATS", "ABSOLUTE_PATHS", "NO_FILES", "DEFAULT", None, "INTERSECTED_FILES")

#las dataset to raster
arcpy.conversion.LasDatasetToRaster("c4342-13-07(2)_LasDataset.lasd", r"c:\users\roach258\documents\arcgis\projects\myproject\myproject.gdb\c43421_lasda", "ELEVATION", "BINNING AVERAGE LINEAR", "FLOAT", "CELLSIZE", 10, 1)

#raster to tin
arcpy.ddd.RasterTin("c43421_lasda", r"C:\Users\roach258\Documents\ArcGIS\Projects\MyProject\c43421_lasda_RasterTin", 9.11, 1500000, 1)

#raster to tin again
arcpy.ddd.RasterTin("c43421_lasda", r"C:\Users\roach258\Documents\ArcGIS\Projects\MyProject\c43421_lasda_RasterTin", 2, 1000000, 1)

#and again
arcpy.ddd.RasterTin("c43421_lasda", r"C:\Users\roach258\Documents\ArcGIS\Projects\MyProject\c43421_lasda_RasterTin4.0", 100, 15000000, 1)

#and again
arcpy.ddd.RasterTin("c43421_lasda", r"C:\Users\roach258\Documents\ArcGIS\Projects\MyProject\c43421_lasda_RasterTin5.0", 1, 15000000, 1)


#PRISM data
https://prism.oregonstate.edu/normals/
    
    
    #create space time cube esri help
    https://pro.arcgis.com/en/pro-app/latest/tool-reference/space-time-pattern-mining/createcubefrommdrasterlayer.htm
