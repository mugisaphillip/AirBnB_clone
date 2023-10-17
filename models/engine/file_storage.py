#!/usr/bin/python3
import json

class FileStorage:
    "class to serialize and deserialize json"


    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj.id in type(self).__objects:
            return

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        serialized = {key: obj.to_dict() for key, obj in
                      FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User

        class_dict = {
                "BaseModel": BaseModel,
                "User": User
                }

        obj = FileStorage.__objects
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    obj[key] = class_dict[value["__class__"]](**value)
        except FileNotFoundError:
            pass
