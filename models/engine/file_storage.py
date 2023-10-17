#!/usr/bin/python3
import json


class FileStorage:
    "class to serialize and deserialize json"

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            my_dict = {}
            for key, value in FileStorage.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, file)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User

        class_dict = {
                "BaseModel": BaseModel,
                }

        obj = FileStorage.__objects
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    obj[key] = class_dict[value["__class__"]](**value)
        except FileNotFoundError:
            pass
