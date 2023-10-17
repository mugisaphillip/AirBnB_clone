#!/usr/bin/python3
import json


class FileStorage:
    "class to serialize and deserialize json"

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def get_classes(self):
        from models.base_model import BaseModel
        from models.user import User

        classes = {
                "BaseModel": BaseModel,
                "User": User
                }
        return classes

    def reload(self):

        obj = FileStorage.__objects
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    obj[key] = self.get_classes()[value["__class__"]](**value)
        except FileNotFoundError:
            pass
