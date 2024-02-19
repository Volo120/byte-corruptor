class SoManySlashesInEntry(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class SoFewSlashesInEntry(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class EmptyEntry(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
