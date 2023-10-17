#!/usr/bin/python3
from .engine.file_storage import FileStorage
from .base_model import BaseModel

# create an instance of FileStorage
storage = FileStorage()

# Call the reload() method
storage.reload()
