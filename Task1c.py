# Task 1c - Enabling user input

# Import modules
import arcpy

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"

# String variable that includes the path to the streams.shp feature class
streams = "streams.shp"

# Get user input for the buffer distance 
buffer_distance = arcpy.GetParameterAsText(0)  
# Format input with unit (meters)
buffer_distance_string = f"{buffer_distance} meters" 

# Get user input for the output path and filename for the buffer tool
output_1c = arcpy.GetParameterAsText(1) 

# Overwrite output
arcpy.env.overwriteOutput = True

# Buffer the streams feature class with user-specified parameters
arcpy.Buffer_analysis(streams, output_1c, buffer_distance_string, '', '', 'ALL')

# Display any messages, warnings, or errors
print(arcpy.GetMessages())
