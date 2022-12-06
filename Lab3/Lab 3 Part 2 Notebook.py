import pandas as pd
import requests
from datetime import date
from io import StringIO

#building the URL for the data from NDAWN

START = "begin_date=2022-11-05"

END = "end_date=2022-12-05"

base_URL= "https://ndawn.ndsu.nodak.edu/table.csv?station=78&station=111&station=98&station=174&station=142&station=138&station=161&station=9&station=10&station=118&station=56&station=11&station=12&station=58&station=13&station=84&station=55&station=7&station=87&station=14&station=15&station=96&station=16&station=137&station=124&station=143&station=17&station=85&station=140&station=134&station=18&station=136&station=65&station=104&station=99&station=19&station=129&station=20&station=101&station=81&station=21&station=97&station=22&station=75&station=2&station=172&station=139&station=23&station=62&station=86&station=24&station=89&station=126&station=93&station=90&station=25&station=83&station=107&station=156&station=77&station=26&station=70&station=127&station=27&station=132&station=28&station=29&station=30&station=31&station=102&station=32&station=119&station=4&station=80&station=33&station=59&station=105&station=82&station=34&station=72&station=135&station=35&station=76&station=120&station=141&station=109&station=36&station=79&station=71&station=37&station=38&station=39&station=130&station=73&station=40&station=41&station=54&station=69&station=113&station=128&station=42&station=43&station=103&station=116&station=88&station=114&station=3&station=163&station=64&station=115&station=67&station=44&station=133&station=106&station=100&station=121&station=45&station=46&station=61&station=66&station=74&station=60&station=125&station=8&station=47&station=122&station=108&station=5&station=152&station=48&station=68&station=49&station=50&station=91&station=117&station=63&station=150&station=51&station=6&station=52&station=92&station=112&station=131&station=123&station=95&station=53&station=57&station=149&station=148&station=110&variable=ddmxt&variable=ddmnt&variable=ddavt&variable=ddavt&year=2022&ttype=daily&quick_pick=30_d&"

dailytemps = base_URL + START + "&" + END

print(dailytemps)

print('dailytemps url created')

# request this url created

mydata= requests.get(dailytemps)

#bring data and write into CSV

file_name = 'ndawn_data_Lab3.csv'
csv = open(file_name, 'w')
csv.write(mydata.text)
csv.close()

print('generating csv')

#csv to read into DF

ndawn_df = pd.read_csv(file_name, header=3, skiprows=[4])
ndawn_df.rename(columns={'Unnamed: 0':'Station Name', 'deg':'Lat', 'deg.1':'Lon', 'ft':'Elevation', 'Unnamed: 4':'Year', 'Unnamed: 5':'Month', 'Unnamed: 6':'Day', 'Degrees F':'Max', 'Degrees F.1': 'Min', 'Degrees F.2':'Avg'}, inplace=True)
ndawn_df.head()

#simplify data to only needed columns

columns= ['Station Name', 'Lat', 'Lon', 'Max', 'Min', 'Avg']
cleaned_NDAWN = ndawn_df[columns].copy()


#aggregate data

agg_functions = {'Lat':'first', 'Lon':'first', 'Max':'mean', 'Min':'mean', 'Avg':'mean'}
agg_df = cleaned_NDAWN.groupby(cleaned_NDAWN['Station Name']).aggregate(agg_functions)

agg_df.head()

#export the aggregated DF to CSV
agg_df.to_csv(r'C:\Users\roach258\Documents\ArcGIS\Labs\Lab 3\aggregated_ndawn_temps_Lab3.csv')

#convert the data to a feature class

import arcpy
csv_path = r"C:\Users\roach258\Documents\ArcGIS\Labs\Lab 3\aggregated_ndawn_temps_Lab3.csv"
temp_features = arcpy.management.XYTableToPoint(csv_path, 'station_temperatures', 'Lon', 'Lat')

#setting environment
from arcpy import env
env.workspace = r'C:\Users\roach258\Documents\ArcGIS\Labs\Lab 3'

#Interpolation via IDW
import arcpy
outIDW = arcpy.sa.Idw("station_temperatures", "Avg", 0.0132, 2, "Variable 12", None)
outIDW.save(r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab 3\Lab 3.gdb\Idw_station_NDAWN")

#Interpolation via Kriging
outKriging = arcpy.sa.Kriging("station_temperatures", "Avg", "Spherical 0.014479 # # #", 0.014479, "VARIABLE 12", None)
outKriging.save(r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab 3\Lab 3.gdb\Kriging2_stat1")

#Interpolation via Global Polynomial Interpolation

# Set environment settings
arcpy.env.workspace = r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab 3\Lab 3.gdb"

# Set local variables
inPointFeatures = "station_temperatures"
zField = "Avg"
outLayer = "GPI"
outRaster = r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab 3\Lab 3.gdb\outGPI"
cellSize = 0.0144
power = 1

# Execute GlobalPolynomialInterpolation
arcpy.GlobalPolynomialInterpolation_ga(inPointFeatures, zField, outLayer, 
                                       outRaster, cellSize, power)

#interpolation for min temp
#via Kriging
#Interpolation via Kriging
outKrigingMin = arcpy.sa.Kriging("station_temperatures", "Min", "Spherical 0.014479 # # #", 0.014479, "VARIABLE 12", None)
outKrigingMin.save(r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab 3\Lab 3.gdb\Kriging2_stat1")

#interpolation for max temp
#via Kriging
#Interpolation via Kriging
outKrigingMax = arcpy.sa.Kriging("station_temperatures", "Max", "Spherical 0.014479 # # #", 0.014479, "VARIABLE 12", None)
outKrigingMax.save(r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab 3\Lab 3.gdb\Kriging2_stat1")

#Interpolation via Kriging with Circular
outKrigingCircular = arcpy.sa.Kriging("station_temperatures", "Avg", "Circular 0.014479 # # #", 0.014479, "VARIABLE 12", None)
outKrigingCircular.save(r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab 3\Lab 3.gdb\Kriging3_stat1")

#Interpolation via Kriging with smaller cells
outKriging2 = arcpy.sa.Kriging("station_temperatures", "Avg", "Spherical 0.00014479 # # #", 0.014479, "VARIABLE 12", None)
outKriging2.save(r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab 3\Lab 3.gdb\Kriging2_stat1")

#Interpolation via IDW 
#Min temperatures
import arcpy
outIDWmin = arcpy.sa.Idw("station_temperatures", "Min", 0.0132, 2, "Variable 12", None)
outIDWmin.save(r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab 3\Lab 3.gdb\Idw_station_minNDAWN")

#Interpolation via IDW
#max temp
import arcpy
outIDWmax = arcpy.sa.Idw("station_temperatures", "Max", 0.0132, 2, "Variable 12", None)
outIDWmax.save(r"C:\Users\roach258\Documents\ArcGIS\Projects\Lab 3\Lab 3.gdb\Idw_station_maxNDAWN")


