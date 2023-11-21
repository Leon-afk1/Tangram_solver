import json
from shapely import *

class ShapeGestion():
    def importFile(path):
        # JSON file
        f = open (path, "r")
        
        # Reading from file
        data = json.loads(f.read())
        poly = Polygon(data['polygon'])
        print(poly)
        return poly
    def saveFile(path,polygon):
        data = {'polygon':[]}
        
        data['polygon'] = polygon.exterior.coords[:]
        print(data)
        with open(path, 'w') as f:
            json.dump(data, f)