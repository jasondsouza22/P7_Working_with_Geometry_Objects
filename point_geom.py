import arcpy
import os

x_mumbai = 72.83468645728531
y_mumbai = 18.92219716661799

# Point Object
pnt_obj = arcpy.Point(x_mumbai,y_mumbai)

# Spatial reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")

# Point Geometry
pnt_geom = arcpy.PointGeometry(pnt_obj, spatial_ref)

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P7_Working_with_Geometry_Objects\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
fc_name = "Gateway_of_India"
fc_path = os.path.join(gdb_path, fc_name)

arcpy.CopyFeatures_management(pnt_geom, fc_path)

print("Process Completed")

