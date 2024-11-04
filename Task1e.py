# Task 1d - Adding auto-generated output names


# Import modules
import arcpy

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"

# Overwrite output
arcpy.env.overwriteOutput = True

# String variable that includes the path to the streams.shp feature class
streams = "streams.shp"

# Get user input for the buffer distance 
buffer_distance = [100, 200, 300, 400, 500] 

# for loop iterating through distances
for distance in buffer_distance:
    # Format input with unit (meters)
    buffer_distance_string = f"{distance} meters" 

    # String variable that sets the path and filename of where the buffer tool should write its output
    output_1e = f"V:/ENV859_PS4/Scratch/buff_{distance}m.shp"

    # Buffer the streams feature class with user-specified parameters
    arcpy.Buffer_analysis(streams, output_1e, buffer_distance_string, '', '', 'ALL')

# Display any messages, warnings, or errors
print(arcpy.GetMessages())