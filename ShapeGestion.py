import json
from shapely import *
from shapely.geometry import Point, Polygon

from Piece import Piece

class ShapeGestion():
    def saveShapeFile(self, path, pieces):
        data = {'poly': []}

        for piece in pieces:
            piece_data = {
                'polygon': piece.poly.exterior.coords[:],
            }
            data['poly'].append(piece_data)

        with open(path, 'w') as f:
            json.dump(data, f)

    def importShapeFile(self, path):
        with open(path, 'r') as f:
            data = json.load(f)

        polygons = []
        for piece_data in data.get('pieces', []):
            poly = Polygon(piece_data.get('polygon', []))
            position = piece_data.get('position', (0, 0))
            rotation = piece_data.get('rotation', 0.0)
            color = piece_data.get('color', (255, 255, 255))

            new_piece = Piece(poly.exterior.coords[:], color, position)
            new_piece.rotation_angle = rotation
            polygons.append(new_piece.poly)

        return MultiPolygon(polygons)    
        
    def importFile(path):
        with open(path, 'r') as f:
            data = json.load(f)

        pieces = []
        for piece_data in data.get('pieces', []):
            poly = Polygon(piece_data.get('polygon', []))
            position = piece_data.get('position', (0, 0))
            rotation = piece_data.get('rotation', 0.0)
            color = piece_data.get('color', (255, 255, 255))  # Ajout de la couleur avec une valeur par défaut

            new_piece = Piece(poly.exterior.coords[:], color, position)
            new_piece.rotation_angle = rotation
            pieces.append(new_piece)

        return pieces

    
    def saveFile(path,pieces):
        data = {'pieces': []}

        for piece in pieces:
            piece_data = {
                'polygon': piece.poly.exterior.coords[:],
                'position': (piece.coord.x, piece.coord.y),
                'rotation': piece.rotation_angle,
                'color': piece.color  # Ajout de la couleur
            }
            data['pieces'].append(piece_data)

        with open(path, 'w') as f:
            json.dump(data, f)