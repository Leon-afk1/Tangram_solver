import json
from shapely import *
from shapely.geometry import Point, Polygon

class ShapeGestion():
    def saveShapeFile(self, path, pieces):
        exterior_coords = []
        for piece in pieces:
            exterior_coords.extend(piece.poly.exterior.coords)

        shape_data = {'exterior_coords': exterior_coords}

        with open(path, 'w') as f:
            json.dump(shape_data, f)

    def importShapeFile(self, path):
        with open(path, 'r') as f:
            shape_data = json.load(f)

        exterior_coords = shape_data.get('exterior_coords', [])
        exterior_polygon = Polygon(exterior_coords)

        return exterior_polygon
    
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