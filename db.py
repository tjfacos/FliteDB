
import os
from os import mkdir
from os.path import exists

import pickle

from errors import *

class Collection:
    def __init__(self, name: str, parent_path: str, **kwargs) -> None:
        
        self.path = parent_path + f"/{name}.dat"
        
        if "schema" in kwargs.keys():
            self.schema = kwargs["schema"]


        self.name = name
        
        if not exists(self.path):
            with open(self.path, "wb") as f:
                pickle.dump(self.schema, f)
        
    def Add(self, payload: dict):
        # First, check the payload conforms to the schema

        for k, v in payload.items():
            
            if k not in self.schema.keys():
                raise SchemaException(f"[{k}] is not a key in this collection's schema")
            
            if self.schema[k] not in str(type(v)):
                raise SchemaException(f"[{k}: {v}] is the wrong data type; should be [{self.schema[k]}] type.")

        # Next, if it conforms to the schema (and it does if it's gotten this far), add to file

        with open(self.path, "ab") as f:
                pickle.dump(payload, f)

        return True
        


class Database:
    def __init__(self, name: str, root : str) -> None:
        self.collections: list[Collection] = []
        self.name = name
        self.path = f"{root}/{name}.database"
        self.__GetDir()

    @property
    def CollectionNames(self):
        return [c.name for c in self.collections]
    
    @property
    def Structure(self):
        return [(c.name, c.schema) for c in self.collections]


    def __GetDir(self):
        """Create the database directory, if it doesn't exist"""
        if not exists(self.path):
            mkdir(self.path)
            return
        
        # Load existing collections
        for file in os.listdir(self.path):
            
            if not file.endswith(".dat"):
                continue

            
            loaded_data = pickle.load(
                open(self.path + "/" + file, "rb")
            )

            self.collections.append(Collection(
                file.strip(".dat"),
                self.path,
                schema=loaded_data
            ))
            

    def CreateCollection(self, name: str, schema: dict):
        """Create a new collection, and add a .dat file for it in the database's directory"""

        if type(schema) != dict:
            raise TypeError("Schema must be a Python dictionary")
        
        for c in self.collections:
            if c.name == name:
                raise CollectionAlreadyExists(f"\nA collection with the name [{name}] already exists!")
        
        self.collections.append(Collection(
            name, 
            self.path,
            schema=schema
        ))

    def AddToCollection(self, name:str, payload: dict):
        if type(payload) != dict:
            raise TypeError("Schema must be a Python dictionary")
        
        # if name not in [c.name for c in self.collections]:
        for c in self.collections:
            if name == c.name:
                return c.Add(payload)

        raise CollectionDoesNotExist(f"There is not collection with the name [{name}] in this database")
        