import arcpy
import pandas as pd
import requests
import io

arcpy.env.workspace = r'C:\Users\roach258\Documents\ArcGIS\Labs'

#bring in downloaded csv

ndawn1 = pd.read_csv(r'C:\Users\roach258\Documents\ArcGIS\Labs\ndawn1.0.csv')

#see the first five rows
ndawn1.head()


