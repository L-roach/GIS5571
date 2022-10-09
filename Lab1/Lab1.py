import arcpy
import pandas as pd
import io
import requests 

arcpy.env.workspace = r'C:\Users\roach258\Documents\ArcGIS\Labs'


layer_name = "Weather"
featureLayer = arcpy.MakeFeatureLayer_management("https://ndawn.ndsu.nodak.edu/table.csv?station=11&variable=ddmxt&variable=ddmxtt&variable=ddmnt&variable=ddmntt&variable=ddavt&variable=dddtr&variable=ddbst&variable=ddtst&variable=ddws&variable=ddmxws&variable=ddmxwst&variable=ddwd&variable=ddwdsd&variable=ddsr&variable=ddtpetp&variable=ddtpetjh&variable=ddr&variable=dddp&variable=ddwc&variable=ddmnwc&variable=ddmxt9&variable=ddmxtt9&variable=ddmnt9&variable=ddmntt9&variable=ddmxws10&variable=ddmxwst10&variable=ddwd10&variable=ddwdsd10&year=2022&ttype=daily&quick_pick=90_d&begin_date=2022-10-04&end_date=2022-10-04", 
                                                 layer_name)

import json
import pprint
import urllib
import ssl
import os

api_url = "https://ndawn.ndsu.nodak.edu/table.csv?station=11&variable=ddmxt&variable=ddmxtt&variable=ddmnt&variable=ddmntt&variable=ddavt&variable=dddtr&variable=ddbst&variable=ddtst&variable=ddws&variable=ddmxws&variable=ddmxwst&variable=ddwd&variable=ddwdsd&variable=ddsr&variable=ddtpetp&variable=ddtpetjh&variable=ddr&variable=dddp&variable=ddwc&variable=ddmnwc&variable=ddmxt9&variable=ddmxtt9&variable=ddmnt9&variable=ddmntt9&variable=ddmxws10&variable=ddmxwst10&variable=ddwd10&variable=ddwdsd10&year=2022&ttype=daily&quick_pick=90_d&begin_date=2022-10-04&end_date=2022-10-04"
>>> response = requests.get(api_url)
>>> response.json()

https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_metc/trans_transit_routes/shp_trans_transit_routes.zip

api_url = "https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_metc/trans_transit_routes/shp_trans_transit_routes.zip"
>>> response = requests.get(api_url)
>>> response.json()

api_url = "https://ndawn.ndsu.nodak.edu/table.csv?station=23&begin_date=2022-10-04&end_date=2022-10-04&quick_pick=90_d&ttype=daily&variable=ddmxt&variable=ddmxtt&variable=ddmnt&variable=ddmntt&variable=ddavt&variable=dddtr&variable=ddbst&variable=ddtst&variable=ddws&variable=ddmxws&variable=ddmxwst&variable=ddwd&variable=ddwdsd&variable=ddsr&variable=ddtpetp&variable=ddtpetjh&variable=ddr&variable=dddp&variable=ddwc&variable=ddmnwc&variable=ddmxt9&variable=ddmxtt9&variable=ddmnt9&variable=ddmntt9&variable=ddmxws10&variable=ddmxwst10&variable=ddwd10&variable=ddwdsd10"
>>> response = requests.get(api_url)
>>> response.json()

ndawn1 = pd.read_csv(r'C:\Users\roach258\Documents\ArcGIS\Labs\ndawn1.0.csv')

ndawn1.head()


transit = pd.read_file('https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_metc/trans_transit_routes/shp_trans_transit_routes.zip')
print (transit)

import geopandas

sudo apt-get install python-pip
sudo easy_install pyshp

import pip

import shapefile

transit = shapefile.Reader('https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_metc/trans_transit_routes/shp_trans_transit_routes.zip')

# check unique value in each field
for i in ndawn1_tot.columns:
    print(f'{i} : {len(ndawn1_tot[i].unique())}')

for i in ndawn1.columns:
    print(f'{i} : {len(ndawn1[i].unique())}'')

import shapefile

# from a zipped shapefile on website
sf = shapefile.Reader("http:resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_metc/trans_transit_routes/shp_trans_transit_routes.zip")

https://pypi.org/project/pyshp/

download_link = r'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_metc/trans_transit_routes/shp_trans_transit_routes.zip'
output = requests.post(download_link)
output.json



import zipfile
name = output.content

import io
zip_io = io.BytesIO(output.content)



zip_io.extractall(r'C:\Users\roach258\Documents\ArcGIS\Labs')



newname = zipfile.ZipFile(io.BytesIO(output.content))
#convert data to io bytes

zip_io = io.BytesIO(output.content)
newname.extractall(r'C:\Users\roach258\Documents\ArcGIS\Labs')

aprx = arcpy.mp.ArcGISProject("CURRENT")

aprx.defaultGeodatabase = r"C:\Users\roach258\Documents\ArcGIS\Labs"

aprx.save()

print(aprx.filePath)

m = aprx.listMaps("Map")[0]

#tutorial where code comes from
https://pro.arcgis.com/en/pro-app/latest/arcpy/mapping/tutorial-getting-started-with-arcpy-mp.htm

lyrFile = arcpy.mp.LayerFile(r"C:\Users\roach258\Documents\ArcGIS\Labs\TransitRoutes.shp")

aprx = arcpy.mp.ArcGISProject("Current")
map = aprx.listMaps()[0]

layer_path = <path>

lyr = arcpy.MakeFeatureLayer_management(r'C:\Users\roach258\Documents\ArcGIS\Labs\TransitRoutes.shp', "transit")

map.addDataFromPath(lyr)

shp_path = r'C:\Users\roach258\Documents\ArcGIS\Labs\TransitRoutes.shp'

aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]  # assumes data to be added to first map listed
map.addDataFromPath(r'C:\Users\roach258\Documents\ArcGIS\Labs\TransitRoutes.shp')

import geopandas as gpd



import pandas as pd

library1 = pd.read_csv(r'C:\Users\roach258\Documents\ArcGIS\Labs\ndawn3.0.csv')
library1.head()

import matplotlib as mpl

import matplotlib.pyplot as plt

library1.plot(kind="scatter", x="Lng", y="Lat", alpha=0.4)
plt.show()

##this just shows a scatter plot, not GIS 

import arcpy
aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]
map.addDataFromPath(r'C:\Users\roach258\Documents\ArcGIS\Labs\ndawn3.0.csv')

#above code added data to map

arcpy.management.XYTableToPoint(r'C:\Users\roach258\Documents\ArcGIS\Labs\ndawn3.0.csv', "libraries",
                                "longitude", "latitude",
                                arcpy.SpatialReference(4759, 115700))

arcpy.management.XYTableToPoint(r'C:\Users\roach258\Documents\ArcGIS\Labs\ndawn3.0.csv', "libraries",
                                "Lng", "Lat",
                                arcpy.SpatialReference(4759, 115700))

in_table = r'C:\Users\roach258\Documents\ArcGIS\Labs\ndawn3.0.csv'
out_feature_class = "libraries"
x_coords = "Lng"
y_coords = "Lat"

# Make the XY event layer...
arcpy.management.XYTableToPoint(in_table, out_feature_class,
                                x_coords, y_coords,
                                arcpy.SpatialReference(4759, 115700))


# The following string is the WKT for the 
# Geographic Coordinate system "WGS 1984" (factory code=4326)
wkt = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],\
              PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],\
              VERTCS['WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],\
              PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Meter',1.0]];\
              -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;\
              0.001;0.001;IsHighPrecision"

sr = arcpy.SpatialReference(text=wkt)

# Make the XY event layer...
arcpy.management.XYTableToPoint(in_table, out_feature_class,
                                x_coords, y_coords,
                                arcpy.SpatialReference(4326))

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 18N")
arcpy.env.geographicTransformations = "Arc_1950_To_WGS_1984_5; PSAD_1956_To_WGS_1984_6"

arcpy.management.XYTableToPoint(in_table, out_feature_class,
                                x_coords, y_coords)

in_table = r'C:\Users\roach258\Documents\ArcGIS\Labs\ndawn3.0.csv'
out_feature_class = "libraries"
x_coords = "Lng"
y_coords = "Lat"
XYevent_Layer = 
wkt = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],\
              PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],\
              VERTCS['WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],\
              PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Meter',1.0]];\
              -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;\
              0.001;0.001;IsHighPrecision"

arcpy.MakeXYEventLayer_management(in_table, x_coords, y_coords, XYevent_Layer, wkt)

## turning lat and long of library locations into shapefile
arcpy.management.XYTableToPoint("ndawn3.0.csv", r"C:\Users\roach258\Documents\ArcGIS\Labs\ndawn3_XYTableToPoint1.shp", "Lng", "Lat", None, 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision')

#spatial join of transit routes and lat and long of library locations

arcpy.analysis.SpatialJoin("ndawn3_XYTableToPoint3", "TransitRoutes", r"C:\Users\roach258\Documents\ArcGIS\Labs\ndawn3_XYTableToPoint3_Spati.shp", "JOIN_ONE_TO_MANY", "KEEP_ALL", 'Lat "Lat" true true false 19 Double 0 0,First,#,ndawn3_XYTableToPoint3,Lat,-1,-1;Lng "Lng" true true false 19 Double 0 0,First,#,ndawn3_XYTableToPoint3,Lng,-1,-1;route "route" true true false 5 Text 0 0,First,#,TransitRoutes,route,0,5;route_oper "route_oper" true true false 254 Text 0 0,First,#,TransitRoutes,route_oper,0,254;RouteClass "RouteClass" true true false 254 Text 0 0,First,#,TransitRoutes,RouteClass,0,254;routedscrp "routedscrp" true true false 50 Text 0 0,First,#,TransitRoutes,routedscrp,0,50;routesort "routesort" true true false 10 Long 0 10,First,#,TransitRoutes,routesort,-1,-1;RoutePayLe "RoutePayLe" true true false 5 Long 0 5,First,#,TransitRoutes,RoutePayLe,-1,-1;EffectiveD "EffectiveD" true true false 8 Date 0 0,First,#,TransitRoutes,EffectiveD,-1,-1;PayLeaveDi "PayLeaveDi" true true false 5 Long 0 5,First,#,TransitRoutes,PayLeaveDi,-1,-1;wk_ftrip "wk_ftrip" true true false 16 Text 0 0,First,#,TransitRoutes,wk_ftrip,0,16;wk_ltrip "wk_ltrip" true true false 16 Text 0 0,First,#,TransitRoutes,wk_ltrip,0,16;wk_span "wk_span" true true false 16 Text 0 0,First,#,TransitRoutes,wk_span,0,16;wk_trip_fr "wk_trip_fr" true true false 10 Long 0 10,First,#,TransitRoutes,wk_trip_fr,-1,-1;sat_ftrip "sat_ftrip" true true false 16 Text 0 0,First,#,TransitRoutes,sat_ftrip,0,16;sat_ltrip "sat_ltrip" true true false 16 Text 0 0,First,#,TransitRoutes,sat_ltrip,0,16;sat_span "sat_span" true true false 16 Text 0 0,First,#,TransitRoutes,sat_span,0,16;sat_trip_f "sat_trip_f" true true false 10 Long 0 10,First,#,TransitRoutes,sat_trip_f,-1,-1;sun_ftrip "sun_ftrip" true true false 16 Text 0 0,First,#,TransitRoutes,sun_ftrip,0,16;sun_ltrip "sun_ltrip" true true false 16 Text 0 0,First,#,TransitRoutes,sun_ltrip,0,16;sun_span "sun_span" true true false 16 Text 0 0,First,#,TransitRoutes,sun_span,0,16;sun_trip_f "sun_trip_f" true true false 10 Long 0 10,First,#,TransitRoutes,sun_trip_f,-1,-1;fri_ftrip "fri_ftrip" true true false 16 Text 0 0,First,#,TransitRoutes,fri_ftrip,0,16;fri_ltrip "fri_ltrip" true true false 16 Text 0 0,First,#,TransitRoutes,fri_ltrip,0,16;fri_span "fri_span" true true false 16 Text 0 0,First,#,TransitRoutes,fri_span,0,16;fri_trip_f "fri_trip_f" true true false 10 Long 0 10,First,#,TransitRoutes,fri_trip_f,-1,-1;hol_ftrip "hol_ftrip" true true false 16 Text 0 0,First,#,TransitRoutes,hol_ftrip,0,16;hol_ltrip "hol_ltrip" true true false 16 Text 0 0,First,#,TransitRoutes,hol_ltrip,0,16;hol_span "hol_span" true true false 16 Text 0 0,First,#,TransitRoutes,hol_span,0,16;hol_trip_f "hol_trip_f" true true false 10 Long 0 10,First,#,TransitRoutes,hol_trip_f,-1,-1;Shape_Leng "Shape_Leng" true true false 19 Double 0 0,First,#,TransitRoutes,Shape_Leng,-1,-1', "INTERSECT", None, '')


