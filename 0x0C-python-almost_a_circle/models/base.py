#!/usr/bin/python3
"""
base class
"""
import json
import csv

class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ class construc"""
        if id is not None :
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string rep """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return []
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ write json str rep to file """
        filename = cls.__name__ + ".json"
        listo = []

        if list_objs is not None:
            for i in list_objs:
                listo.append(cls.to_dictionary(i))
            with open(filename, 'w') as f:
                f.write(cls.to_json_string(listo))

    @staticmethod
    def from_json_string(json_string):
        """ return json rep list """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ instance with all attr """
        if cls.__name__ is "Rectangle":
            creclass = cls(1, 1)
        elif cls.__name__ is "Square":
            creclass = cls(1)
        else:
            creclass.update(**dictionary)
        return creclass

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        listo2 = []
        try:
            with open(filename, 'r') as f:
                listo2 = cls.from_json_string(f.read())
            for i, x in enumerate(listo2):
                listo2[i] = cls.create(**listo2[i])
        except:
            pass
        return listo2
    @classmethod
    def load_from_file_csv(cls):
        """ deserialize """
        filename = cls.__name__ + ".csv"
        newli = []
        try:
            with open(filename, 'r', newline='') as csf:
                reader = csv.DictReader(f)
                for row in reader:
                    for i, x in row.items():
                        row[i] = int(x)
                    newli = csv.DictReader(csf, fieldnames=fieldnames)
                    newli = [dict([k, int(v)] for k, v in d.items()) for d in list_dictionaries]
                    return [cls.create(**d) for d in list_dictionaries]
        except:
                return []
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serialize """
        filename = cls.__name__ + ".csv"
        if cls.__name__ is "Rectangle":
            att = ["width", "height", "x", "y", "id"]
        elif cls.__name__ is "Square":
            att = ["size", "x", "y", "id"]
        with open(filename, 'w', newline="") as csf:
            writer = csv.DictWriter(csf, fieldnames=att)
            if list_objs is not None:
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
            else:
                writer.writerow([[]])