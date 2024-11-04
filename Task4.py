# Task 4

# Import necessary modules
import arcpy
import os
import sys

arcpy.env.overwriteOutput = True

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"

# User input variable
inFC = arcpy.GetParameterAsText(0)

# Describe a feature class using arcpy.da.Describe
desc = arcpy.da.Describe(inFC)

# Catalog path message
arcpy.AddMessage ("Catalog path: "+desc["catalogPath"])

# Extent messages
extent = desc['extent']
arcpy.AddMessage(f"XMin: {round (extent.XMin,1)}")
arcpy.AddMessage(f"XMax: {round (extent.XMax,1)}")
arcpy.AddMessage(f"YMin: {round (extent.YMin,1)}")
arcpy.AddMessage(f"YMax: {round (extent.YMax,1)}")

# Check data set type  
# If it is a FeatureClass, report the data set’s shapeType as a warning message.
if desc['datasetType'] == "FeatureClass":
    arcpy.AddWarning(desc['shapeType'])

# If it’s a RasterDataset, report the data set’s format, as well as the number of rows, and the number of columns in the data set as warning messages
elif desc['datasetType'] == "RasterDataset":
    arcpy.AddWarning(f"Raster Format: {desc['format']}")
    arcpy.AddWarning(f"# of Rows: {desc['height']}")
    arcpy.AddWarning(f"# of Columns: {desc['width']}")

#If it is any other type of data set, print out what data set type it is as an error message.
else:
    arcpy.AddError(f"Data type not supported: {desc['datasetType']}")