# Task 2 

# Import modules
import arcpy

# Enables any existing ArcPy outputs to be overwritten
arcpy.env.overwriteOutput = True

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"
# String variable that includes the path to the Roads.shp feature class (using set workspace)
roads = "Roads.shp"

# Creates a string variable with the value “0;201;203” 
# (i.e. a “multi-value string”) of the road type class values to be processed.
road_type = "0;201;203"

# Creates a list variable by splitting the values between the semi-colons in the string created above 
# the three values each become an item in the list
road_type_list = road_type.split(";")

# Loops through each item (i.e. each road type value) in roads type list
for type in road_type_list:
    # String variable that sets the path and filename of output, includes road type in filename
    output_2 = f"V:/ENV859_PS4/Scratch/roads_{type}.shp"

    # Selects features in the roads.shp feature class with the ROAD_TYPE attribute matching the value in the list
    # Chat GPT helped format where_clause to run properly: 
    where_clause = f"ROAD_TYPE = {type}"

    # Execute Select
    arcpy.Select_analysis(roads, output_2, where_clause)
