class CollectionAlreadyExists(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class CollectionDoesNotExist(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class SchemaException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)