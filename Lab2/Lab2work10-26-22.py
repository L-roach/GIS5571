import arcpy

arcpy.management.CreateFileGDB(r"C:\Users\roach258\Documents", "PRISMdata", "CURRENT")

arcpy.management.CreateMosaicDataset(r"C:\Users\roach258\Documents\ArcGIS\Projects\MyProject\MyProject.gdb", "PRISMmosaic", 'GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', None, '', "NONE", None)

#above code created a mosaic dataset
#below code adds all of the rasters to the mosaic dataset

arcpy.management.AddRastersToMosaicDataset("PRISMmosaic", "Raster Dataset", r"C:\Users\roach258\Downloads\PRISM_ppt_30yr_normal_4kmM3_all_bil\PRISM_ppt_30yr_normal_4kmM3_01_bil.bil;C:\Users\roach258\Downloads\PRISM_ppt_30yr_normal_4kmM3_all_bil\PRISM_ppt_30yr_normal_4kmM3_02_bil.bil;C:\Users\roach258\Downloads\PRISM_ppt_30yr_normal_4kmM3_all_bil\PRISM_ppt_30yr_normal_4kmM3_03_bil.bil;C:\Users\roach258\Downloads\PRISM_ppt_30yr_normal_4kmM3_all_bil\PRISM_ppt_30yr_normal_4kmM3_04_bil.bil;C:\Users\roach258\Downloads\PRISM_ppt_30yr_normal_4kmM3_all_bil\PRISM_ppt_30yr_normal_4kmM3_05_bil.bil;C:\Users\roach258\Downloads\PRISM_ppt_30yr_normal_4kmM3_all_bil\PRISM_ppt_30yr_normal_4kmM3_06_bil.bil;C:\Users\roach258\Downloads\PRISM_ppt_30yr_normal_4kmM3_all_bil\PRISM_ppt_30yr_normal_4kmM3_07_bil.bil;C:\Users\roach258\Downloads\PRISM_ppt_30yr_normal_4kmM3_all_bil\PRISM_ppt_30yr_normal_4kmM3_08_bil.bil;C:\Users\roach258\Downloads\PRISM_ppt_30yr_normal_4kmM3_all_bil\PRISM_ppt_30yr_normal_4kmM3_09_bil.bil;C:\Users\roach258\Downloads\PRISM_ppt_30yr_normal_4kmM3_all_bil\PRISM_ppt_30yr_normal_4kmM3_10_bil.bil;C:\Users\roach258\Downloads\PRISM_ppt_30yr_normal_4kmM3_all_bil\PRISM_ppt_30yr_normal_4kmM3_11_bil.bil;C:\Users\roach258\Downloads\PRISM_ppt_30yr_normal_4kmM3_all_bil\PRISM_ppt_30yr_normal_4kmM3_12_bil.bil", "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", None, 0, 1500, None, '', "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", '', "NO_FORCE_SPATIAL_REFERENCE", "NO_STATISTICS", None, "NO_PIXEL_CACHE", r"C:\Users\roach258\AppData\Local\ESRI\rasterproxies\PRISMmosaic")

#this is an attempt to add time as a date to the PRSIM 01 raster
arcpy.management.CalculateField("PRISM_ppt_30yr_normal_4kmM3_01_bil.bil", "time", "12/31/2001", "PYTHON3", '', "DATE", "NO_ENFORCE_DOMAINS")

# helpful site: https://www.esri.com/arcgis-blog/products/arcgis-pro/analytics/explore-your-raster-data-with-space-time-pattern-mining/

#this creates the variable field with text ppt
arcpy.management.CalculateField(r"PRISMmosaic\Footprint", "Variable", '"ppt"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")

#this creates the time field
arcpy.management.CalculateField(r"PRISMmosaic\Footprint", "Timestamp", "DateAdd(Date(2020,0,1), $feature.OBJECTID-1, 'year')", "ARCADE", '', "DATE", "NO_ENFORCE_DOMAINS")

#this builds multidimensionable info
arcpy.md.BuildMultidimensionalInfo("PRISMmosaic", "Variable", "Timestamp # #", None, "NO_DELETE_MULTIDIMENSIONAL_INFO")

#change layer time to no time in the layer properties of the mosaic

#convert the time-enabled mosaic into a single time-enabled layer that is compatible with other ArcGIS tools

#make multidimensional raster layer
arcpy.md.MakeMultidimensionalRasterLayer("PRISMmosaic", "PRISMmosaic_MultidimLayer", "ppt", "ALL", None, None, '', '', '', None, '', '-125.020833333333 24.0624999997935 -66.4791666661985 49.9375000000005 GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', "DIMENSIONS", None)

arcpy.md.MakeMultidimensionalRasterLayer("PRISMmosaic", "PRISMmosaic_MultidimLayer3.crf", "ppt", "ALL", None, None, '', '', '', None, '', '-125.020833333333 24.0624999997935 -66.4791666661985 49.9375000000005 GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', "DIMENSIONS", None)

arcpy.env.workspace = r'C:\Users\roach258\Documents\ArcGIS\Projects\PRISM Lab'

arcpy.md.MakeMultidimensionalRasterLayer("PRISMmosaic", "PRISMmosaic_MultidimLayer4.crf", "ppt", "ALL", None, None, '', '', '', None, '', '-125.020833333333 24.0624999997935 -66.4791666661985 49.9375000000005 GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', "DIMENSIONS", None)

#create space time cube tool
arcpy.stpm.CreateSpaceTimeCubeMDRasterLayer("PRISMmosaic_MultidimLayer4.crf", r"C:\Users\roach258\Documents\ArcGIS\Projects\PRISM Lab\PRISMcube.nc", "ZEROS")

arcpy.stpm.VisualizeSpaceTimeCube2D(r"C:\Users\roach258\Documents\ArcGIS\Projects\PRISM Lab\PRISMcube.nc", "PPT_NONE_ZEROS", "TRENDS", r"C:\Users\roach258\Documents\ArcGIS\Projects\MyProject\myproject.gdb\PRISMcube_VisualizeSpaceTimeCube2D", "NO_POPUP")
