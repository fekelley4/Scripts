# Task 5 

# Import modules
import arcpy

# Enables any existing ArcPy outputs to be overwritten
arcpy.env.overwriteOutput = True

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"

# Enable two inputs from the user: 
# a feature class and a field name
input_feature_class = arcpy.GetParameterAsText(0) 
input_field = arcpy.GetParameterAsText(1) 

# Create point object
point = arcpy.Point(590000, 230000)

# Create a SearchCursor from the feature class specified in step 1
#  retrieving the Shape@ field and the field the user specifies in step 1
with arcpy.da.SearchCursor(input_feature_class, ['SHAPE@', input_field]) as cursor:
    # Add a for loop to iterate through each feature in the feature class one at a time
    for row in cursor:
        #Create a variable called recShape assign it to the value of the current feature’s Shape object
        recShape = row[0] 

        # Determine whether the point created in the second step falls within the record’s shape
        # If it does, determine the attribute value of the field specified by the user
        if recShape.contains(point): 
            field_value = row[1] 
            # Send a message back to the ArcGIS Pro indicating what the field’s value is for the record
            arcpy.AddMessage(f"The point intersects with {field_value} County")
            break
    
    else:
        # If no intersection occurs
        arcpy.AddMessage("The point did not intersect with a feature.")
   