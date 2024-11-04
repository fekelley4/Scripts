# Task 1d - Adding auto-generated output names

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

# String variable that sets the path and filename of where the buffer tool should write its output
output_1d = f"V:/ENV859_PS4/Scratch/buff_{buffer_distance}m.shp"
 

# Overwrite output
arcpy.env.overwriteOutput = True

# Buffer the streams feature class with user-specified parameters
arcpy.Buffer_analysis(streams, output_1d, buffer_distance_string, '', '', 'ALL')

# Display any messages, warnings, or errors
print(arcpy.GetMessages())
