import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P7_Working_with_Geometry_Objects\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
output_fc_name = "Mumbai_to_Alibag_to_Lonavala_Polygon"
output_fc_path = os.path.join(gdb_path, output_fc_name)

x_mumbai = 72.83468645728531
y_mumbai = 18.92219716661799

x_alibag = 72.87200120958518
y_alibag = 18.641134839264023

x_lonavala = 73.40654304595003
y_lonavala = 18.75730127064558

pnt_mumbai_obj = arcpy.Point(x_mumbai, y_mumbai)
pnt_alibag_obj = arcpy.Point(x_alibag, y_alibag)
pnt_lonavala_obj = arcpy.Point(x_lonavala, y_lonavala)

# Spatial Reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")

# Array Object
polygon_array = arcpy.Array()

polygon_array.add(pnt_mumbai_obj)
polygon_array.add(pnt_alibag_obj)
polygon_array.add(pnt_lonavala_obj)

polygon_geom =arcpy.Polygon(polygon_array, spatial_ref)

arcpy.CopyFeatures_management(polygon_geom, output_fc_path)
print("Process Completed")
