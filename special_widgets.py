import tkinter

class EntryCollection:
    def __init__(self) -> None:
        self.entries = []
        
    def register(self) -> dict:
        return {
            "entries": self.entries
        }
    
    def setEntry(self, *entry) -> None:
        self.entries.append(entry)

class Entry(tkinter.Entry):
    def __init__(self, master: tkinter.Tk | tkinter.Frame, width: int, hasSpecialCharacters: bool) -> None:
        super().__init__()

        self.master = master
        self.width = width
        self.hasSpecialCharacters = hasSpecialCharacters
        self.entry = tkinter.Entry(master=self.master, width=self.width)
        
    def pack(self, padx: int=None, pady: int=None) -> None:
        return self.entry.pack(padx=padx, pady=pady)
    
    def grid(self, row: int=None, column: int=None) -> None:
        return self.entry.grid(row=row, column=column)
    
    def get(self, symbol: str=None) -> list | str:
        return self.entry.get().split(symbol) if not isinstance(symbol, type(None)) else self.entry.get()
    
    def grid_forget(self) -> None:
        return self.entry.grid_forget()
    
    def pack_forget(self) -> None:
        return self.entry.pack_forget()
    
    def insert(self, index: str | int, string: str) -> None:
        return self.entry.insert(index, string)
    
    def delete(self, first: str | int, last: str | int | None = None) -> None:
        return self.entry.delete(first, last)
    
    def config(self, **kwargs) -> None:
        return self.entry.config(kwargs)