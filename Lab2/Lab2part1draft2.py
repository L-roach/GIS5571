#create mosaic dataset
arcpy.management.CreateMosaicDataset(r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab2work\Lab2work.gdb", "Normals", 'GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', None, '', "NONE", None)

#create raster dataset
with arcpy.EnvManager(outputCoordinateSystem='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]'):
    arcpy.management.CreateRasterDataset(r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab2work\BilsFromPRISM.gdb", "PRISM_ppt_30yr_normal_4kmM3_12_bil.bil", None, "8_BIT_UNSIGNED", 'PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]', 1, '', "PYRAMIDS -1 NEAREST DEFAULT 75 NO_SKIP NO_SIPS", "128 128", "LZ77", None)

#add rasters to mosaic dataset
arcpy.management.AddRastersToMosaicDataset("Normals", "Raster Dataset", r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab2work\BilsFromPRISM.gdb", "UPDATE_CELL_SIZES", "UPDATE_BOUNDARY", "NO_OVERVIEWS", None, 0, 1500, None, '', "SUBFOLDERS", "ALLOW_DUPLICATES", "NO_PYRAMIDS", "NO_STATISTICS", "NO_THUMBNAILS", '', "NO_FORCE_SPATIAL_REFERENCE", "NO_STATISTICS", None, "NO_PIXEL_CACHE", r"C:\Users\roach258\AppData\Local\ESRI\rasterproxies\Normals")

#build multidimensional info
arcpy.md.BuildMultidimensionalInfo("Normals", "Name", "HighPS # #", "bil_10 # #;bil_12 # #;bil_9 # #;bil_8 # #;bil_11 # #", "NO_DELETE_MULTIDIMENSIONAL_INFO")

#make multidimensional raster layer
arcpy.md.MakeMultidimensionalRasterLayer("Normals", "Normals_MultidimLayer3", "'LowPS, HighPS, CenterX, CenterY, ZOrder'", "ALL", None, None, '', '', '', None, '', "3.00435000042398E-04 -68.5111304979999 137.023114225 2.76397000064321E-04", "DIMENSIONS", None)

#create space time cube FAILED
arcpy.stpm.CreateSpaceTimeCubeMDRasterLayer("Normals_MultidimLayer3", r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab2work\draft3.nc", "ZEROS")
