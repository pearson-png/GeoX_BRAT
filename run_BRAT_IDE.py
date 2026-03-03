# -------------------------------------------------------------------------------
# Name:        Run BRAT Code
# Purpose:     Performs all steps of ArcGIS Pro BRAT toolbox by running this file
#
# Author:      Jordan Gilbert
#
# Created:     03/03/2026
# Latest Update: 03/03/2026
# -------------------------------------------------------------------------------
# https://coderivers.org/blog/run-a-python-script-in-python/

import subprocess
from BRAT_Toolboxes.

def run_script(path):
    '''
    Create a function to run a python script and print the text output if succeeded.
    First file path segment should be 'BRAT_Toolboxes/'.
    '''
    result = subprocess.run(['python', path], capture_output=True, text=True)

    if result.returncode == 0:
        print("Script executed successfully. Output:")
        print(result.stdout)
    else:
        print("Script execution failed. Error:")
        print(result.stderr)

# Run BRAT.py to create tool classes
run_script('BRAT_Toolboxes/pyBRAT-3.1.01-ArcGISPro/BRAT.pyt')

# Run RCAT.pyt to create tool classes
run_script('BRAT_Toolboxes/0_RCAT/RCAT-2.0.3/RCAT.pyt')

# Assign inputs for NHD Network Builder
NDHNetworkBuilder_dict = {
    "inFlowline":r"C:\Users\lukap\OneDrive\Documents\mgis\geog5545_geospatialX\BRAT\BRAT_Workshop\BRAT_Workshop_March2025\BRAT_Inputs\NHD\NHD_Flow_Clip.shp",
    "inWaterbody":r"C:\Users\lukap\OneDrive\Documents\mgis\geog5545_geospatialX\BRAT\BRAT_Workshop\BRAT_Workshop_March2025\BRAT_Inputs\NHD\NHD_WB_Clip.shp",
    "inArea":r"C:\Users\lukap\OneDrive\Documents\mgis\geog5545_geospatialX\BRAT\BRAT_Workshop\BRAT_Workshop_March2025\BRAT_Inputs\NHD\NHD_Area_Clip.shp",
    "ap_fix":None,
    "subsize":0.001,
    "boolArtPath":True,
    "boolCanals":None,
    "boolAqueducts":None,
    "boolStormwater":None,
    "boolConnectors":None,
    "boolStreams":True,
    "boolIntermittent":None,
    "boolPerennial":None,
    "boolEphemeral":True,
    "outNetwork":r"C:\Users\lukap\OneDrive\Documents\mgis\geog5545_geospatialX\BRAT\BRAT_Workshop\FlowBuilder.shp",
    "proj":'PROJCS["NAD_1983_California_Teale_Albers",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",-4000000.0],PARAMETER["Central_Meridian",-120.0],PARAMETER["Standard_Parallel_1",34.0],PARAMETER["Standard_Parallel_2",40.5],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
    "scratchWS":r"C:\Users\lukap\OneDrive\Documents\mgis\geog5545_geospatialX\BRAT\BRAT_Workshop\BRAT_Workshop_March2025\Scratch"

# Run NHD Network Builder
run_script('BRAT_Toolboxes/0_RCAT/RCAT-2.0.3/NHDNetworkBuilder.py')