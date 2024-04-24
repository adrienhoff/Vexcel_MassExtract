#Created by Adrien Hoff, Senior GIS Analyst, Jeffcom911
#For questions or feedback, email adrien.hoff@jeffcom911.org

import arcpy
import urllib.request
import os

# Specify the path to your tessellation layer, Vexcel Token, and imagery needs
tessellation_layer = 'your tessellation layer'
Imagery_layer = 'your imagery layer' #can be bluesky-ultra-g, bluesky-ultra, bluesky-high, urban-r
YOUR_TOKEN = 'YOUR TOKEN'

# Function to construct the API URL for each polygon
def construct_api_url(x_min, y_min, x_max, y_max):
    api_url = "https://api.vexcelgroup.com/images/ExtractOrthoImages/{}".format(Imagery_layer)
    api_url += "?EPSG=4326&zoom=21"
    api_url += "&wkt=POLYGON(({0}%20{1},{2}%20{1},{2}%20{3},{0}%20{3},{0}%20{1}))".format(x_min, y_min, x_max, y_max)
    api_url += "&format=tiff&crop=exact&token={}".format(YOUR_TOKEN)
    return api_url

# Create a directory to save the downloaded images
output_folder = r"G:\GIS ORG\GIS Local\PROJECTS\imagery\PARK_2024"
os.makedirs(output_folder, exist_ok=True)

# Open a cursor to iterate through the features in the layer
with arcpy.da.SearchCursor(tessellation_layer, ["OID@", "SHAPE@"]) as cursor:
    for row in cursor:
        # Get the extent of the polygon
        extent = row[1].extent
        x_min, y_min, x_max, y_max = extent.XMin, extent.YMin, extent.XMax, extent.YMax
        
        # Construct the API URL for the current polygon
        api_url = construct_api_url(x_min, y_min, x_max, y_max)
        print(api_url)
        
        # Download the image
        image_path = os.path.join(output_folder, f"polygon_{row[0]}.tiff")
        urllib.request.urlretrieve(api_url, image_path)
        print(f"Downloaded image for polygon {row[0]}")
