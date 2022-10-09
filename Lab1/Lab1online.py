#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[ ]:


from arcgis.gis import GIS
gis = GIS("home")


# #### Now you are ready to start!

# In[ ]:


import requests

#this is the code from Google

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522%2C151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY"
#json? means return as a json
#%2C stays in the code line; between = and & are parameters to enter

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

#python package called folium
#pandas; import pandas as pd; import geopandas as gpd


# In[1]:


import requests

#location of Minneapolis= 44.97754974826651, -93.261548797858
#asking for Minneapolis, within 2000, public library

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=44.97754974826651%2C-93.261548797858&radius=2000&type=library&keyword=public&key=AIzaSyAM4yOPvTuAU4kAzUtwlBm7DpqfBMWQjYA"

payload={}
headers={}

response = requests.request("GET", url, header=headers, data=payload)

print(response.text)


# In[2]:


import requests

#location of Minneapolis= 44.97754974826651, -93.261548797858
#asking for Minneapolis, within 2000, public library

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=44.97754974826651%2C-93.261548797858&radius=2000&type=library&keyword=public&key=AIzaSyAM4yOPvTuAU4kAzUtwlBm7DpqfBMWQjYA"


payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


# In[3]:


import gmaps
gmaps.configure(api_key='AIzaSyAM4yOPvTuAU4kAzUtwlBm7DpqfBMWQjYA')

fig = gmaps.figure()
fig


# In[4]:


import arcpy


# In[5]:


libraries = response.text


# In[7]:


libraries.keys()


# In[9]:


libraries


# In[10]:


libraries['html_attributions']


# In[1]:


# xy to point in pro
# parse json dictionary structure

places_response['candidates'][0]['geometry']


# In[4]:


location = response['geometry']['location']

latitude = location['lat']
longitude = location['lng']


# In[5]:


import requests

#location of Minneapolis= 44.97754974826651, -93.261548797858
#asking for Minneapolis, within 2000, public library

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=44.97754974826651%2C-93.261548797858&radius=2000&type=library&keyword=public&key=AIzaSyAM4yOPvTuAU4kAzUtwlBm7DpqfBMWQjYA"


payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


# In[8]:


places_response ['candidates'][0]['geometry']


# In[9]:


response ['candidates'][0]['geometry']


# In[10]:


help


# In[ ]:


help()


# In[3]:


env.workspace = r'C:\Users\laure\OneDrive\Documents\ArcGIS I Labs'


# In[4]:


import requests
download_link = r'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_metc/trans_transit_count_headway_rt/shp_trans_transit_count_headway_rt.zip'
output = requests.post(download_link)
output.json

import zipfile
name = output.content

import io
zip_io = io.BytesIO(output.content)

zip_io.extractall(r'C:\Users\laure\OneDrive\Documents\ArcGIS I Labs')

transit = zipfile.ZipFile(io.BytesIO(output.content))
#convert data to io bytes

zip_io = io.BytesIO(output.content)
transit.extractall(r'C:\Users\laure\OneDrive\Documents\ArcGIS I Labs')


# In[5]:


import requests
download_link = r'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_metc/trans_transit_count_headway_rt/shp_trans_transit_count_headway_rt.zip'
output = requests.post(download_link)
output.json

import zipfile
name = output.content

import io
zip_io = io.BytesIO(output.content)

zip_io.extractall(r'C:\Users\laure\OneDrive\Documents\ArcGIS I Labs')

transit = zipfile.ZipFile(io.BytesIO(output.content))
#convert data to io bytes

zip_io = io.BytesIO(output.content)
transit.extractall(r'C:\Users\laure\OneDrive\Documents\ArcGIS I Labs')


# In[7]:


import requests
download_link = r'https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_metc/trans_transit_count_headway_rt/shp_trans_transit_count_headway_rt.zip'
output = requests.post(download_link)
output.json

import zipfile
transit = output.content


# In[11]:


import io
zip_io = io.BytesIO(output.content)


transit = zipfile.ZipFile(io.BytesIO(output.content))


# In[12]:


import arcgis
from arcgis.gis import GIS
# Create a GIS object, as an anonymous user for this example
gis = GIS()


# In[13]:


# Create a map widget
map1 = gis.map('USA') # Passing a place name to the constructor
                        # will initialize the extent of the map.
map1


# In[14]:


transit = gis.content.get('transit')


# In[15]:


transit_layer = transit.layers[0]
transit_layer


# In[16]:


from arcgis.gis import GIS
my_gis = GIS()
m = my_gis.map()

#let's put the shape file to AGOL
shp_item = my_gis.content.add(item_properties={ 
        'title' : 'Transit in MN',
        'type' : 'Shapefile',
        'tags' : 'transit'},
        data = r"https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_metc/trans_transit_count_headway_rt/shp_trans_transit_count_headway_rt.zip")


# In[ ]:




