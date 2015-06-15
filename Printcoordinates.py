import arcpy
from arcpy import env
env.workspace ="C:\Users\shaohu.zhang@sdstate.edu\Desktop\DataPython\SR_Brookings\SR_Brookings"
fc = "SR_Brookings.shp"
cursor = arcpy.da.SearchCursor(fc, (["FID","SHAPE@XY"]))
for row in cursor:
    print ("{0}".format(row[0]) )                          
    x, y = row[1]
    print("{0}, {1}".format(x, y))
del cursor
          
          
