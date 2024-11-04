# Task 1b - Setting environment values in your script

# Import modules
import arcpy

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"

# String variable that includes the path to the streams.shp feature class
streams = "streams.shp"

# String variable that specifies the buffer distance as “1000 meters”
buffer_distance = "1000 meters"

# String variable that sets the path and filename of where the buffer tool should write its output
output_1b = "V:/ENV859_PS4/Scratch/StrmBuff1km.shp"

# Overwrite output
arcpy.env.overwriteOutput = True

# Buffer the selected roads feature class we just created
arcpy.Buffer_analysis(streams,output_1b,buffer_distance,'','','ALL')

# Display any messages, warnings, or errors
print(arcpy.GetMessages())