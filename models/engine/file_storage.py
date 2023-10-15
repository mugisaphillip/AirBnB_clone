#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.____name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        serialized = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls, obj_id = key.split('.')
                    if cls == 'User':
                        obj_dict = value
                        obj = User(**obj_dict)
                    else:
                        obj_dict = value
                        obj = globals()[cls](**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
