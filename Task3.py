# Task 3

# Import modules
import arcpy

# Ensures the ArcPy product edition used is "ArcInfo"
arcpy.CheckProduct("ArcInfo")

# Enables any existing ArcPy outputs to be overwritten
arcpy.env.overwriteOutput = True

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"
# String variable that includes the path to feature classes starting with "BMR_" (using set workspace)
BMR_feature_classes = arcpy.ListFeatureClasses("BMR_*")

# String variable that includes the path to the TriCounties.shp feature class (using set workspace)
TriCounties = "TriCounties.shp"

# Loops through all 5 of these “BMR” feature classes
for BMR in BMR_feature_classes:
    # Extract BMR rank
    # Excludes .shp (last four characters) from folder name 
    bmr_rank = BMR.split("R")[1][:-4]
    # Creates a path for output
    folder_path = f"V:/ENV859_PS4/Scratch"
    # Specify output folder name
    output_3 = f"BMR{bmr_rank}"
    # Define variable for executing the CreateFolder 
    output_folders = arcpy.CreateFolder_management(folder_path, output_3)

    # break the features in the current BMR feature class by county features 
    # uses CO_NAME as the split field
    arcpy.analysis.Split(BMR, TriCounties, "CO_NAME", output_folders)