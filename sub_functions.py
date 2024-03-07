from tkinter import *
import ctypes
import special_widgets as sw
import special_errors as se
from tkinter.filedialog import *

MB_OK = 0x00000000
MB_ICONEXCLAMATION = 0x00000030
MB_ICONASTERISK = 0x00000040
MB_ICONSTOP = 0x00000010

def user32MessageBox(message: str, title: str="warning", style: int=MB_OK | MB_ICONEXCLAMATION):
    ctypes.windll.user32.MessageBoxW(None, message, title, style)

def info(buttonType: str) -> None:
    if buttonType == "add file":
        return user32MessageBox(
            message="specify the path for your target file.\nnote: the program will only copy the content of it, so you don't have to worry about it",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "save file":
        return user32MessageBox(
            message="specify the path for your corrupted file.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "start at":
        return user32MessageBox(
            message="specify where you want to start the corruption in file bytes.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "inc by":
        return user32MessageBox(
            message="the number by which the bytes will get incremented or decremented.\nnote: add a '-' mark before writing the number to indicate subtraction.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "gap":
        return user32MessageBox(
            message="specify the distance from each corrupted byte.\nthe lower the number, the more bytes will be corrupted.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "end at":
        return user32MessageBox(
            message="specify where you want to end bytes corruption.\nclick the \"very last byte\" button to get the total size of the file.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "min/max":
        return user32MessageBox(
            message="specify range for randomly generated numbers to be used to increment bytes.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "original/new":
        return user32MessageBox(
            message="specify a particular value to replace with a new one.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "replace all with":
        return user32MessageBox(
            message="specify a value to replace every byte with.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "swap with":
        return user32MessageBox(
            message="specify the index of the byte you would like to swap with.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "copy byte at":
        return user32MessageBox(
            message="specify the index of the byte you would like to copy and spam with.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    
def randomizedAddSubOperators_HELP() -> None:
    return user32MessageBox(
        message="when this option is enabled, the corruptor will randomly increment and decrement byte values (this functionality works with Incrementer and Randomizer only)",
        title="help",
        style=MB_OK | MB_ICONASTERISK
    )

def invertFileBytes_HELP() -> None:
    return user32MessageBox(
        message="when this option is enabled, the corruptor will write the bytes of a file in reverse (not recommended if you're corrupting a binary file, as it does not adhere to the \"gap size\" parameter)",
        title="help",
        style=MB_OK | MB_ICONASTERISK
    )

def reverseBytes(byteArray: list, start: str, end: str) -> list:
    reversedArray = []
    reversedArray.clear()
    reversedArray = byteArray[int(start):int(end)]
    reversedArray.reverse()
    return reversedArray

def selectFileToMixWith(self):
    try: self.fileToMixWith = askopenfile().name
    except AttributeError: return
    self.fileToMixLabel["text"] = self.fileToMixWith

def checkEntriesValuesType(var: int, **collection: sw.EntryCollection) -> bool:
    ent: sw.Entry
    if var == 1: # incrementer
        for ent in (collection["incr"]["entries"][0]):
            try:
                if len(ent.get()) == 0: raise se.EmptyEntry()
            except se.EmptyEntry:
                user32MessageBox(message="make sure to fill all empty fields")
                return False
            try:
                int(ent.get())
            except ValueError:
                user32MessageBox(message="invalid symbols were inserted")
                return False
        return True
    
    elif var == 2: # randomizer
        for ent in (collection["rand"]["entries"][0]):
            try:
                if len(ent.get()) == 0: raise se.EmptyEntry()
            except se.EmptyEntry:
                user32MessageBox(message="make sure to fill all empty fields")
                return False
            try:
                if ent.hasSpecialCharacters:
                    try:
                        if len(ent.get().split("/")) > 2: raise se.SoManySlashesInEntry()
                        if len(ent.get().split("/")) == 1: raise se.SoFewSlashesInEntry()
                    except se.SoManySlashesInEntry:
                        user32MessageBox(message="entry must not have more than a single slash")
                        return False
                    except se.SoFewSlashesInEntry:
                        user32MessageBox(message="entry must have at least one slash")
                        return False
            except AttributeError:
                try:
                    int(ent.get())
                except ValueError:
                    user32MessageBox(message="invalid symbols were inserted")
                    return False
        return True
    
    elif var == 3: # replacer
        for ent in (collection["repl"]["entries"][0]):
            try:
                if len(ent.get()) == 0: raise se.EmptyEntry()
            except se.EmptyEntry:
                user32MessageBox(message="make sure to fill all empty fields")
                return False
            try:
                if ent.hasSpecialCharacters:
                    try:
                        if len(ent.get().split("/")) > 2: raise se.SoManySlashesInEntry()
                        if len(ent.get().split("/")) == 1: raise se.SoFewSlashesInEntry()
                    except se.SoManySlashesInEntry:
                        user32MessageBox(message="entry must not have more than a single slash")
                        return False
                    except se.SoFewSlashesInEntry:
                        user32MessageBox(message="entry must have at least one slash")
                        return False
            except AttributeError:
                try:
                    int(ent.get())
                except ValueError:
                    user32MessageBox(message="invalid symbols were inserted")
                    return False
        return True
    
    elif var == 4: # swapper
        for ent in (collection["swap"]["entries"][0]):
            try:
                if len(ent.get()) == 0: raise se.EmptyEntry()
            except se.EmptyEntry:
                user32MessageBox(message="make sure to fill all empty fields")
                return False
            try:
                int(ent.get())
            except ValueError:
                user32MessageBox(message="invalid symbols were inserted")
                return False
        return True
    
    elif var == 5: # copier
        for ent in (collection["copy"]["entries"][0]):
            try:
                if len(ent.get()) == 0: raise se.EmptyEntry()
            except se.EmptyEntry:
                user32MessageBox(message="make sure to fill all empty fields")
                return False
            try:
                int(ent.get())
            except ValueError:
                user32MessageBox(message="invalid symbols were inserted")
                return False
        return True
    
    elif var == 6: # mixer
        for ent in (collection["mixe"]["entries"][0]):
            try:
                if len(ent.get()) == 0: raise se.EmptyEntry()
            except se.EmptyEntry:
                user32MessageBox(message="make sure to fill all empty fields")
                return False
            try:
                int(ent.get())
            except ValueError:
                user32MessageBox(message="invalid symbols were inserted")
                return False
        return True

def selectFile(self) -> None:
    try: self.selectedFilePath = askopenfile().name
    except AttributeError: return
    self.fileEntry.config(state=NORMAL)
    self.fileEntry.delete("1.0", END)
    self.fileEntry.insert(END, "../"+self.selectedFilePath.split("/")[-2]+"/"+self.selectedFilePath.split("/")[-1])
    self.fileEntry.config(state=DISABLED)
    self.saveBtn.config(state=NORMAL)

def saveToPath(self) -> None:
    if not self.selectedFilePath: return
    self.saveBtn.config(state=NORMAL)
    try: self.savePath = asksaveasfile(initialfile=self.selectedFilePath).name
    except AttributeError: return
    self.saveEntry.config(state=NORMAL)
    self.saveEntry.delete("1.0", END)
    self.saveEntry.insert(END, "../"+self.savePath.split("/")[-2]+"/"+self.savePath.split("/")[-1])
    self.saveEntry.config(state=DISABLED)
    self.incrementerEndFillBtn.config(state=NORMAL)
    self.corruptBtn.config(state=NORMAL)
