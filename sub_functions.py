# hardcoded stuff

from tkinter import *
import ctypes
import special_widgets as sw
import special_errors as se

MB_OK = 0x00000000
MB_ICONEXCLAMATION = 0x00000030
MB_ICONASTERISK = 0x00000040

def user32MessageBox(message: str, title: str="warning", style: int=MB_OK | MB_ICONEXCLAMATION):
    ctypes.windll.user32.MessageBoxW(None, message, title, style)

def info(buttonType: str):
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
            message="specify the index of the byte you would like to swap with\nnote: Add a \"-\" if you would like to swap with a byte that is to the left of the original byte.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )

def checkEntriesValuesType(self, var: int, **collection: sw.EntryCollection) -> bool:
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

def _setBottomBtnsLayout(self):
    self.bottomFrame.pack(pady=10, side="bottom")
    self.prevPageBtn.grid(row=0, column=0, padx=5)
    self.runBtn.grid(row=0, column=1)
    self.nextPageBtn.grid(row=0, column=2, padx=5)

def _setFileLayout(self):
    self.topFrame.pack()
    self.fileBtn.grid(row=0, column=0, pady=5)
    self.fileEntry.grid(row=0, column=1, padx=5)
    self.fileHelpBtn.grid(row=0, column=2, padx=5)
    self.saveBtn.grid(row=1, column=0, pady=5)
    self.saveEntry.grid(row=1, column=1, padx=5)
    self.saveHelpBtn.grid(row=1, column=2, padx=5)

def _setPageItems(self, pageNum):
    if pageNum == 1:
        _setFileLayout(self)
        self.swapperLabel.pack(pady=5)
        self.swapperFrame.pack(pady=5)
        self.swapperStartLabel.grid(row=0, column=0, padx=5)
        self.swapperStartEntry.grid(row=0, column=1)
        self.sep11.grid(row=0, column=2)
        self.swapperByLabel.grid(row=0, column=3, padx=5)
        self.swapperByEntry.grid(row=0, column=4, padx=3)
        self.swapperGapLabel.grid(row=0, column=5, padx=3)
        self.swapperGapEntry.grid(row=0, column=6, padx=3)
        self.swapperEndAtLabel.grid(row=0, column=7, padx=5)
        self.swapperEndAtEntry.grid(row=0, column=8)
        self.swapperEndFillBtn.grid(row=0, column=9, padx=15)
    _setBottomBtnsLayout(self)

    if pageNum == 0:
        _setFileLayout(self)
        self.incrementerLabel.pack(pady=5)
        self.incrementerFrame.pack(pady=5)
        self.incrementerStartAtLabel.grid(row=0, column=0, padx=5)
        self.incrementerStartEntry.grid(row=0, column=1)
        self.sep1.grid(row=0, column=2)
        self.incrementerByLabel.grid(row=0, column=3, padx=5)
        self.incrementerByEntry.grid(row=0, column=4)
        self.sep2.grid(row=0, column=5)
        self.incrementerGapLabel.grid(row=0, column=6, padx=5)
        self.incrementerGapEntry.grid(row=0, column=7)
        self.sep3.grid(row=0, column=8)
        self.incrementerEndAtLabel.grid(row=0, column=9, padx=5)
        self.incrementerEndAtEntry.grid(row=0, column=10)
        self.incrementerEndFillBtn.grid(row=0, column=11, padx=15)
        self.sep4.grid(row=1, column=0)

        self.randomizerLabel.pack(pady=5)
        self.randomizerFrame.pack(pady=5)
        self.randomizerStartLabel.grid(row=0, column=0, padx=5)
        self.randomizerStartEntry.grid(row=0, column=1)
        self.sep5.grid(row=0, column=2)
        self.randomizerByLabel.grid(row=0, column=3, padx=5)
        self.randomizerByEntry.grid(row=0, column=4)
        self.randomizerGapLabel.grid(row=0, column=6, padx=5)
        self.randomizerGapEntry.grid(row=0, column=7)
        self.sep6.grid(row=0, column=8)
        self.randomizerEndAtLabel.grid(row=0, column=9, padx=5)
        self.randomizerEndAtEntry.grid(row=0, column=10)
        self.randomizerEndFillBtn.grid(row=0, column=11, padx=15)
        self.sep7.grid(row=1, column=0)

        self.replacerLabel.pack(pady=5)
        self.replacerFrame.pack(pady=5)
        self.replacerStartLabel.grid(row=0, column=0, padx=5)
        self.replacerStartEntry.grid(row=0, column=1)
        self.sep8.grid(row=0, column=2)
        self.replacerByLabel.grid(row=0, column=3, padx=5)
        self.sep9.grid(row=0, column=5)
        self.replacerGapLabel.grid(row=0, column=6, padx=5)
        self.replacerGapEntry.grid(row=0, column=7)
        self.sep10.grid(row=0, column=8)
        self.replacerEndAtLabel.grid(row=0, column=9, padx=5)
        self.replacerEndAtEntry.grid(row=0, column=10)
        self.replacerEndFillBtn.grid(row=0, column=11, padx=15)
        self.replacerExclusiveCb.pack()
        _setBottomBtnsLayout(self)

def prevAndNextSwitch(self, pageNum):
    if pageNum == 0:
        self.prevPageBtn.config(state=DISABLED)
        self.nextPageBtn.config(state=NORMAL)
        self.swapperLabel.pack_forget()
        self.swapperFrame.pack_forget()
        self.swapperStartLabel.grid_forget()
        self.swapperStartEntry.grid_forget()
        self.sep11.grid_forget()
        self.swapperByLabel.grid_forget()
        self.swapperByEntry.grid_forget()
        self.swapperGapLabel.grid_forget()
        self.swapperGapEntry.grid_forget()
        self.swapperEndAtLabel.grid_forget()
        self.swapperEndAtEntry.grid_forget()
        self.swapperEndFillBtn.grid_forget()

    if pageNum == 1:
        self.nextPageBtn.config(state=DISABLED)
        self.prevPageBtn.config(state=NORMAL)
        self.topFrame.pack_forget()
        self.fileBtn.grid_forget()
        self.fileEntry.grid_forget()
        self.fileHelpBtn.grid_forget()
        self.saveBtn.grid_forget()
        self.saveEntry.grid_forget()
        self.saveHelpBtn.grid_forget()

        self.incrementerLabel.pack_forget()
        self.incrementerFrame.pack_forget()
        self.incrementerStartAtLabel.grid_forget()
        self.incrementerStartEntry.grid_forget()
        self.sep1.grid_forget()
        self.incrementerByLabel.grid_forget()
        self.incrementerByEntry.grid_forget()
        self.sep2.grid_forget()
        self.incrementerGapLabel.grid_forget()
        self.incrementerGapEntry.grid_forget()
        self.sep3.grid_forget()
        self.incrementerEndAtLabel.grid_forget()
        self.incrementerEndAtEntry.grid_forget()
        self.incrementerEndFillBtn.grid_forget()
        self.sep4.grid_forget()

        self.randomizerLabel.pack_forget()
        self.randomizerFrame.pack_forget()
        self.randomizerStartLabel.grid()
        self.randomizerStartEntry.grid()
        self.sep5.grid()
        self.randomizerByLabel.grid()
        self.randomizerByEntry.grid()
        self.randomizerGapLabel.grid()
        self.randomizerGapEntry.grid()
        self.sep6.grid()
        self.randomizerEndAtLabel.grid()
        self.randomizerEndAtEntry.grid()
        self.randomizerEndFillBtn.grid()
        self.sep7.grid()

        self.replacerLabel.pack_forget()
        self.replacerFrame.pack_forget()
        self.replacerStartLabel.grid_forget()
        self.replacerStartEntry.grid_forget()
        self.sep8.grid_forget()
        self.replacerByLabel.grid_forget()
        self.sep9.grid_forget()
        self.replacerGapLabel.grid_forget()
        self.replacerGapEntry.grid_forget()
        self.sep10.grid_forget()
        self.replacerEndAtLabel.grid_forget()
        self.replacerEndAtEntry.grid_forget()
        self.replacerEndFillBtn.grid_forget()
        self.replacerExclusiveCb.pack_forget()

        self.bottomFrame.pack_forget()
        self.prevPageBtn.grid_forget()
        self.runBtn.grid_forget()
        self.nextPageBtn.grid_forget()
    
    _setPageItems(self, pageNum)

def exclusiveToggle(self):
    exclusive = self.exclusive.get()
    if not exclusive:
        self.replacerByLabel["text"] = "replace all with"
        self.replacerByLabel.unbind("<Button-1>")
        self.replacerByEntry.grid_forget()
        self.replacerNonExclusiveEntry.grid(row=0, column=4)
        self.replacerByLabel.bind("<Button-1>", lambda x=None: info("replace all with"))
    else:
        self.replacerByLabel["text"] = "original/new"
        self.replacerByLabel.unbind("<Button-1>")
        self.replacerByLabel.bind("<Button-1>", lambda x=None: info("original/new"))
        self.replacerByEntry.grid(row=0, column=4)
        self.replacerNonExclusiveEntry.grid_forget()

def autoDisableAndEnable(self):
    if self.var.get() == 1:
        self.incrementerStartAtLabel.config(state=NORMAL)
        self.incrementerStartEntry.config(state=NORMAL)
        self.incrementerEndAtLabel.config(state=NORMAL)
        self.incrementerEndAtEntry.config(state=NORMAL)
        self.incrementerByLabel.config(state=NORMAL)
        self.incrementerByEntry.config(state=NORMAL)
        self.incrementerGapLabel.config(state=NORMAL)
        self.incrementerGapEntry.config(state=NORMAL)
        self.incrementerEndFillBtn.config(state=NORMAL)

        self.randomizerStartLabel.config(state=DISABLED)
        self.randomizerStartEntry.config(state=DISABLED)
        self.randomizerEndAtLabel.config(state=DISABLED)
        self.randomizerEndAtEntry.config(state=DISABLED)
        self.randomizerByLabel.config(state=DISABLED)
        self.randomizerByEntry.config(state=DISABLED)
        self.randomizerGapLabel.config(state=DISABLED)
        self.randomizerGapEntry.config(state=DISABLED)
        self.randomizerEndFillBtn.config(state=DISABLED)
        
        self.replacerStartLabel.config(state=DISABLED)
        self.replacerStartEntry.config(state=DISABLED)
        self.replacerEndAtLabel.config(state=DISABLED)
        self.replacerEndAtEntry.config(state=DISABLED)
        self.replacerByLabel.config(state=DISABLED)
        self.replacerByEntry.config(state=DISABLED)
        self.replacerGapLabel.config(state=DISABLED)
        self.replacerGapEntry.config(state=DISABLED)
        self.replacerEndFillBtn.config(state=DISABLED)
        self.replacerNonExclusiveEntry.config(state=DISABLED)
        self.replacerExclusiveCb.config(state=DISABLED)

        self.swapperStartLabel.config(state=DISABLED)
        self.swapperStartEntry.config(state=DISABLED)
        self.swapperEndAtLabel.config(state=DISABLED)
        self.swapperEndAtEntry.config(state=DISABLED)
        self.swapperByLabel.config(state=DISABLED)
        self.swapperByEntry.config(state=DISABLED)
        self.swapperGapLabel.config(state=DISABLED)
        self.swapperGapEntry.config(state=DISABLED)
        self.swapperEndFillBtn.config(state=DISABLED)

    elif self.var.get() == 2:
        self.randomizerStartLabel.config(state=NORMAL)
        self.randomizerStartEntry.config(state=NORMAL)
        self.randomizerEndAtLabel.config(state=NORMAL)
        self.randomizerEndAtEntry.config(state=NORMAL)
        self.randomizerByLabel.config(state=NORMAL)
        self.randomizerByEntry.config(state=NORMAL)
        self.randomizerGapLabel.config(state=NORMAL)
        self.randomizerGapEntry.config(state=NORMAL)
        self.randomizerEndFillBtn.config(state=NORMAL)
        
        self.incrementerStartAtLabel.config(state=DISABLED)
        self.incrementerStartEntry.config(state=DISABLED)
        self.incrementerEndAtLabel.config(state=DISABLED)
        self.incrementerEndAtEntry.config(state=DISABLED)
        self.incrementerByLabel.config(state=DISABLED)
        self.incrementerByEntry.config(state=DISABLED)
        self.incrementerGapLabel.config(state=DISABLED)
        self.incrementerGapEntry.config(state=DISABLED)
        self.incrementerEndFillBtn.config(state=DISABLED)

        self.replacerStartLabel.config(state=DISABLED)
        self.replacerStartEntry.config(state=DISABLED)
        self.replacerEndAtLabel.config(state=DISABLED)
        self.replacerEndAtEntry.config(state=DISABLED)
        self.replacerByLabel.config(state=DISABLED)
        self.replacerByEntry.config(state=DISABLED)
        self.replacerGapLabel.config(state=DISABLED)
        self.replacerGapEntry.config(state=DISABLED)
        self.replacerEndFillBtn.config(state=DISABLED)
        self.replacerNonExclusiveEntry.config(state=DISABLED)
        self.replacerExclusiveCb.config(state=DISABLED)

        self.swapperStartLabel.config(state=DISABLED)
        self.swapperStartEntry.config(state=DISABLED)
        self.swapperEndAtLabel.config(state=DISABLED)
        self.swapperEndAtEntry.config(state=DISABLED)
        self.swapperByLabel.config(state=DISABLED)
        self.swapperByEntry.config(state=DISABLED)
        self.swapperGapLabel.config(state=DISABLED)
        self.swapperGapEntry.config(state=DISABLED)
        self.swapperEndFillBtn.config(state=DISABLED)

    elif self.var.get() == 3:
        self.replacerStartLabel.config(state=NORMAL)
        self.replacerStartEntry.config(state=NORMAL)
        self.replacerEndAtLabel.config(state=NORMAL)
        self.replacerEndAtEntry.config(state=NORMAL)
        self.replacerByLabel.config(state=NORMAL)
        self.replacerByEntry.config(state=NORMAL)
        self.replacerGapLabel.config(state=NORMAL)
        self.replacerGapEntry.config(state=NORMAL)
        self.replacerEndFillBtn.config(state=NORMAL)
        self.replacerNonExclusiveEntry.config(state=NORMAL)
        self.replacerExclusiveCb.config(state=NORMAL)

        self.incrementerStartAtLabel.config(state=DISABLED)
        self.incrementerStartEntry.config(state=DISABLED)
        self.incrementerEndAtLabel.config(state=DISABLED)
        self.incrementerEndAtEntry.config(state=DISABLED)
        self.incrementerByLabel.config(state=DISABLED)
        self.incrementerByEntry.config(state=DISABLED)
        self.incrementerGapLabel.config(state=DISABLED)
        self.incrementerGapEntry.config(state=DISABLED)
        self.incrementerEndFillBtn.config(state=DISABLED)

        self.randomizerStartLabel.config(state=DISABLED)
        self.randomizerStartEntry.config(state=DISABLED)
        self.randomizerEndAtLabel.config(state=DISABLED)
        self.randomizerEndAtEntry.config(state=DISABLED)
        self.randomizerByLabel.config(state=DISABLED)
        self.randomizerByEntry.config(state=DISABLED)
        self.randomizerGapLabel.config(state=DISABLED)
        self.randomizerGapEntry.config(state=DISABLED)
        self.randomizerEndFillBtn.config(state=DISABLED)

        self.swapperStartLabel.config(state=DISABLED)
        self.swapperStartEntry.config(state=DISABLED)
        self.swapperEndAtLabel.config(state=DISABLED)
        self.swapperEndAtEntry.config(state=DISABLED)
        self.swapperByLabel.config(state=DISABLED)
        self.swapperByEntry.config(state=DISABLED)
        self.swapperGapLabel.config(state=DISABLED)
        self.swapperGapEntry.config(state=DISABLED)
        self.swapperEndFillBtn.config(state=DISABLED)

    elif self.var.get() == 4:
        self.swapperStartLabel.config(state=NORMAL)
        self.swapperStartEntry.config(state=NORMAL)
        self.swapperEndAtLabel.config(state=NORMAL)
        self.swapperEndAtEntry.config(state=NORMAL)
        self.swapperByLabel.config(state=NORMAL)
        self.swapperByEntry.config(state=NORMAL)
        self.swapperGapLabel.config(state=NORMAL)
        self.swapperGapEntry.config(state=NORMAL)
        self.swapperEndFillBtn.config(state=NORMAL)

        self.replacerStartLabel.config(state=DISABLED)
        self.replacerStartEntry.config(state=DISABLED)
        self.replacerEndAtLabel.config(state=DISABLED)
        self.replacerEndAtEntry.config(state=DISABLED)
        self.replacerByLabel.config(state=DISABLED)
        self.replacerByEntry.config(state=DISABLED)
        self.replacerGapLabel.config(state=DISABLED)
        self.replacerGapEntry.config(state=DISABLED)
        self.replacerEndFillBtn.config(state=DISABLED)
        self.replacerNonExclusiveEntry.config(state=DISABLED)
        self.replacerExclusiveCb.config(state=DISABLED)

        self.incrementerStartAtLabel.config(state=DISABLED)
        self.incrementerStartEntry.config(state=DISABLED)
        self.incrementerEndAtLabel.config(state=DISABLED)
        self.incrementerEndAtEntry.config(state=DISABLED)
        self.incrementerByLabel.config(state=DISABLED)
        self.incrementerByEntry.config(state=DISABLED)
        self.incrementerGapLabel.config(state=DISABLED)
        self.incrementerGapEntry.config(state=DISABLED)
        self.incrementerEndFillBtn.config(state=DISABLED)

        self.randomizerStartLabel.config(state=DISABLED)
        self.randomizerStartEntry.config(state=DISABLED)
        self.randomizerEndAtLabel.config(state=DISABLED)
        self.randomizerEndAtEntry.config(state=DISABLED)
        self.randomizerByLabel.config(state=DISABLED)
        self.randomizerByEntry.config(state=DISABLED)
        self.randomizerGapLabel.config(state=DISABLED)
        self.randomizerGapEntry.config(state=DISABLED)
        self.randomizerEndFillBtn.config(state=DISABLED)
