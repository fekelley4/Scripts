# Task 1a - Creating the initial buffer script


# Import modules
import arcpy

# String variable that includes the path to the streams.shp feature class
streams = 'V:/ENV859_PS4/Data/streams.shp'

# String variable that specifies the buffer distance as “1000 meters”
buffer_distance = "1000 meters"

# String variable that sets the path and filename of where the buffer tool should write its output
output_1a = "V:/ENV859_PS4/Scratch/StrmBuff1km.shp"

# Buffer the selected roads feature class we just created
arcpy.Buffer_analysis(streams,output_1a,buffer_distance,'','','ALL')

# Display any messages, warnings, or errors
print(arcpy.GetMessages())