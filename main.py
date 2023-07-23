"""
To build a DBMS (NoSQL), a I need:
 - Defined structure for .db files
 - Define how to create collections
 - Define how to add a document to that collection
 - Define how to read documents from a collections
 - Searching
"""


# Example Usage

"""


def test():
    
    # Create database
    db = Database("My_DB")
    
    # Create schema with dictionary
    schema = Schema({
        "name": "str",
        "age": "int"
    })

    # Create Collection with schema
    db.CreateCollection("people", schema)


"""



# Test script

# Local dependencies
import db



if __name__ == "__main__":
    database = db.Database("My_DB", "C:/Users/thoma/Desktop/CompSci/summer23/DBMS/database")
    
    
    print(database.Structure)

    # database.CreateCollection("people", {
    #     "name": "str",
    #     "age": "int"
    # })

    database.AddToCollection(
        "people",
        {
            "name": "Miles",
            "age": 16
        }
    )