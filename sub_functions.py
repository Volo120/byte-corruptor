from tkinter import *
import ctypes
import special_widgets as sw
import special_errors as se
from tkinter.filedialog import *

MB_OK = 0x00000000
MB_YESNO = 0x00000004

MB_ICONEXCLAMATION = 0x00000030
MB_ICONASTERISK = 0x00000040
MB_ICONSTOP = 0x00000010
MB_ICONQUESTION = 0x00000020

IDYES = 6
IDNO = 7

def user32MessageBox(message: str, title: str="warning", style: int=MB_OK | MB_ICONEXCLAMATION):
    return ctypes.windll.user32.MessageBoxW(None, message, title, style)

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
    elif buttonType == "bit shift amount":
        return user32MessageBox(
            message=f"specify the number of bits that will be used to (left/right) shift each byte.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    
def randomizedAddSubOperators_HELP() -> None:
    return user32MessageBox(
        message="when this option is enabled, the corruptor will randomly increment and decrement byte values (this functionality works with Incrementer only)",
        title="help",
        style=MB_OK | MB_ICONASTERISK
    )

def invertFileBytes_HELP() -> None:
    return user32MessageBox(
        message="when this option is enabled, the corruptor will write the bytes of a file in reverse (not recommended if you're corrupting a binary file, as it does not adhere to the \"gap size\" parameter)",
        title="help",
        style=MB_OK | MB_ICONASTERISK
    )

def hexModeToggle(self):
    incrementerColl = self.incrementerColl.register()
    randomizerColl = self.randomizerColl.register()
    replacerColl = self.replacerColl.register()
    swapperColl = self.swapperColl.register()
    copierColl = self.copierColl.register()
    mixerColl = self.mixerColl.register()
    bitShifterColl = self.bitShifterColl.register()

    ent: Entry
    if self.hexMode.get():
        try:
            for ent in incrementerColl["entries"][0]:
                ent.config(state=NORMAL)
                dec = int(ent.get())
                ent.delete(0, END)
                ent.insert(0, hex(dec)[2:].upper())
                if self.var.get() != 1:
                    ent.config(state=DISABLED)
            
            for ent in randomizerColl["entries"][0]:
                ent.config(state=NORMAL)
                if isinstance(ent, sw.Entry):
                    min_, max_ = ent.get("/")
                    ent.delete(0, END)
                    ent.insert(0, "{0}/{1}".format(hex(int(min_))[2:].upper(), hex(int(max_))[2:].upper()))
                else:
                    dec = int(ent.get())
                    ent.delete(0, END)
                    ent.insert(0, hex(dec)[2:].upper())
                if self.var.get() != 2:
                    ent.config(state=DISABLED)

            for ent in replacerColl["entries"][0]:
                ent.config(state=NORMAL)
                if isinstance(ent, sw.Entry):
                    org, new = ent.get("/")
                    ent.delete(0, END)
                    ent.insert(0, "{0}/{1}".format(hex(int(org))[2:].upper(), hex(int(new))[2:].upper()))
                else:
                    dec = int(ent.get())
                    ent.delete(0, END)
                    ent.insert(0, hex(dec)[2:].upper())
                if self.var.get() != 3:
                    ent.config(state=DISABLED)

            for ent in swapperColl["entries"][0]:
                ent.config(state=NORMAL)
                dec = int(ent.get())
                ent.delete(0, END)
                ent.insert(0, hex(dec)[2:].upper())
                if self.var.get() != 4:
                    ent.config(state=DISABLED)

            for ent in copierColl["entries"][0]:
                ent.config(state=NORMAL)
                dec = int(ent.get())
                ent.delete(0, END)
                ent.insert(0, hex(dec)[2:].upper())
                if self.var.get() != 5:
                    ent.config(state=DISABLED)

            for ent in mixerColl["entries"][0]:
                ent.config(state=NORMAL)
                dec = int(ent.get())
                ent.delete(0, END)
                ent.insert(0, hex(dec)[2:].upper())
                if self.var.get() != 6:
                    ent.config(state=DISABLED)

            for ent in bitShifterColl["entries"][0]:
                ent.config(state=NORMAL)
                dec = int(ent.get())
                ent.delete(0, END)
                ent.insert(0, hex(dec)[2:].upper())
                if self.var.get() != 7:
                    ent.config(state=DISABLED)
        except ValueError as exc:
            self.hexMode.set(False)
            return user32MessageBox(
                message="cannot convert {0} to hexadecimal".format(str(exc).split(" ")[-1]),
                title="error",
                style=MB_ICONSTOP | MB_OK
            )
    else:
        try:
            for ent in incrementerColl["entries"][0]:
                ent.config(state=NORMAL)
                int_ = int(ent.get(), 16)
                ent.delete(0, END)
                ent.insert(0, int_)
                if self.var.get() != 1:
                    ent.config(state=DISABLED)
            
            for ent in randomizerColl["entries"][0]:
                ent.config(state=NORMAL)
                if isinstance(ent, sw.Entry):
                    min_, max_ = ent.get("/")
                    ent.delete(0, END)
                    ent.insert(0, f"{int(min_, 16)}/{int(max_, 16)}")
                else:
                    int_ = int(ent.get(), 16)
                    ent.delete(0, END)
                    ent.insert(0, int_)
                if self.var.get() != 2:
                    ent.config(state=DISABLED)

            for ent in replacerColl["entries"][0]:
                ent.config(state=NORMAL)
                if isinstance(ent, sw.Entry):
                    org, new = ent.get("/")
                    ent.delete(0, END)
                    ent.insert(0, f"{int(org, 16)}/{int(new, 16)}")
                else:
                    int_ = int(ent.get(), 16)
                    ent.delete(0, END)
                    ent.insert(0, int_)
                if self.var.get() != 3:
                    ent.config(state=DISABLED)

            for ent in swapperColl["entries"][0]:
                ent.config(state=NORMAL)
                int_ = int(ent.get(), 16)
                ent.delete(0, END)
                ent.insert(0, int_)
                if self.var.get() != 4:
                    ent.config(state=DISABLED)

            for ent in copierColl["entries"][0]:
                ent.config(state=NORMAL)
                int_ = int(ent.get(), 16)
                ent.delete(0, END)
                ent.insert(0, int_)
                if self.var.get() != 5:
                    ent.config(state=DISABLED)

            for ent in mixerColl["entries"][0]:
                ent.config(state=NORMAL)
                int_ = int(ent.get(), 16)
                ent.delete(0, END)
                ent.insert(0, int_)
                if self.var.get() != 6:
                    ent.config(state=DISABLED)

            for ent in bitShifterColl["entries"][0]:
                ent.config(state=NORMAL)
                int_ = int(ent.get(), 16)
                ent.delete(0, END)
                ent.insert(0, int_)
                if self.var.get() != 7:
                    ent.config(state=DISABLED)
        except ValueError as exc:
            self.hexMode.set(True)
            return user32MessageBox(
                message="cannot convert {0} to decimal".format(str(exc).split(" ")[-1]),
                title="error",
                style=MB_ICONSTOP | MB_OK
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

HEX_NUMS = "0123456789abcdef"
def checkEntriesValuesType(self, var: int, **collection: sw.EntryCollection) -> bool:
    ent: sw.Entry
    if var == 1: # incrementer
        for ent in (collection["incr"]["entries"][0]):
            try:
                if len(ent.get()) == 0: raise se.EmptyEntry()
            except se.EmptyEntry:
                user32MessageBox(message="make sure to fill all empty fields")
                return False
            try:
                if self.hexMode.get():
                    for i in ent.get().lower():
                        if i not in HEX_NUMS: raise ValueError()
                else:
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
                        min_, max_ = ent.get("/")
                        if self.hexMode.get():
                            for i in min_.lower():
                                if i not in HEX_NUMS: raise ValueError()
                            for i in max_.lower():
                                if i not in HEX_NUMS: raise ValueError()
                        else:
                            int(min_); int(max_)
                        if len(ent.get().split("/")) > 2: raise se.SoManySlashesInEntry()
                        if len(ent.get().split("/")) == 1: raise se.SoFewSlashesInEntry()
                    except se.SoManySlashesInEntry:
                        user32MessageBox(message="entry must not have more than a single slash")
                        return False
                    except se.SoFewSlashesInEntry:
                        user32MessageBox(message="entry must have at least one slash")
                        return False
            except ValueError:
                user32MessageBox(message="invalid symbols were inserted")
                return False
            except AttributeError: # hasSpecialCharacters == False
                try:
                    if self.hexMode.get():
                        for i in ent.get().lower():
                            if i not in HEX_NUMS: raise ValueError()
                    else:
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
                        org, new = ent.get("/")
                        if self.hexMode.get():
                            for i in org.lower():
                                if i not in HEX_NUMS: raise ValueError()
                            for i in new.lower():
                                if i not in HEX_NUMS: raise ValueError()
                        else:
                            int(org); int(new)
                            if len(ent.get().split("/")) > 2: raise se.SoManySlashesInEntry()
                            if len(ent.get().split("/")) == 1: raise se.SoFewSlashesInEntry()
                    except ValueError:
                        user32MessageBox(message="invalid symbols were inserted")
                        return False
                    except se.SoManySlashesInEntry:
                        user32MessageBox(message="entry must not have more than a single slash")
                        return False
                    except se.SoFewSlashesInEntry:
                        user32MessageBox(message="entry must have at least one slash")
                        return False
            except AttributeError:
                try:
                    if self.hexMode.get():
                        for i in ent.get().lower():
                            if i not in HEX_NUMS: raise ValueError()
                    else:
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
                if self.hexMode.get():
                    for i in ent.get().lower():
                        if i not in HEX_NUMS: raise ValueError()
                else:
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
                if self.hexMode.get():
                    for i in ent.get().lower():
                        if i not in HEX_NUMS: raise ValueError()
                else:
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
                if self.hexMode.get():
                    for i in ent.get().lower():
                        if i not in HEX_NUMS: raise ValueError()
                else:
                    int(ent.get())
            except ValueError:
                user32MessageBox(message="invalid symbols were inserted")
                return False
        return True
    
    elif var == 7: # bit shifter
        for ent in (collection["bits"]["entries"][0]):
            try:
                if len(ent.get()) == 0: raise se.EmptyEntry()
            except se.EmptyEntry:
                user32MessageBox(message="make sure to fill all empty fields")
                return False
            try:
                if self.hexMode.get():
                    for i in ent.get().lower():
                        if i not in HEX_NUMS: raise ValueError()
                else:
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
