routes= r"C:\Users\roach258\Downloads\shp_trans_memorial_routes\Memorial_Routes_in_Minnesota.shp"

# Import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:\Users\roach258\Downloads\shp_trans_memorial_routes\memorial_routes.gdb"



# Buffer areas of impact around major roads

arcpy.Buffer_analysis(roads, roadsBuffer, distanceField, sideType, endType, 
                      dissolveType, dissolveField)


roads = "majorrds"
roadsBuffer = "C:/output/Output.gdb/buffer_output"
distanceField = "Distance"
sideType = "FULL"
endType = "ROUND"
dissolveType = "LIST"
dissolveField = "Distance"

#create a gdb
import arcpy

out_folder_path = r"C:\Users\roach258\Downloads\shp_trans_memorial_routes"
out_name = "routes_gdb.gdb"

arcpy.CreateFileGDB_management(out_folder_path, out_name)

#assign environment

arcpy.env.workspace = r"C:\Users\roach258\Downloads\shp_trans_memorial_routes"

#how to see if file was created
arcpy.ListFiles()

arcpy.Buffer_analysis(routes, r"C:\Users\roach258\Downloads\shp_trans_memorial_routes\routes_gdb.gdb\routes_buffer", "3 Miles", "FULL", "ROUND", "LIST", "Distance")

arcpy.Buffer_analysis(routes, r"C:\Users\roach258\Downloads\shp_trans_memorial_routes\routes_gdb.gdb\routes_buffer", "3 USSurveyMiles", "FULL", "ROUND", "LIST", "Distance")

arcpy.Buffer_analysis(routes, r"C:\Users\roach258\Downloads\shp_trans_memorial_routes\routes_gdb.gdb\routes_buffer", "3", "FULL", "ROUND", "LIST", "Distance")

help

help()

arcpy.Buffer_analysis(routes, r"C:\Users\roach258\Downloads\shp_trans_memorial_routes\routes_gdb.gdb\routes_buffer", 3, "FULL", "ROUND", "LIST", "Distance")

arcpy.Buffer_analysis(in_features=routes, out_feature_class=r"C:\Users\roach258\Downloads\shp_trans_memorial_routes\routes_gdb.gdb\routes_buffer", buffer_distance_or_field= "3", line_side= "FULL", line_end_type= "ROUND", dissolve_option= "LIST", dissolve_field= "Distance", method=None)

arcpy.analysis.Buffer("Memorial_Routes_in_Minnesota", r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab0\Lab0.gdb\Memorial_Routes_Buffer", "3 Miles", "FULL", "ROUND", "NONE", None, "PLANAR")


