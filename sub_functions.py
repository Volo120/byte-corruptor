from tkinter import *
import ctypes

MB_OK = 0x00000000
MB_ICONEXCLAMATION = 0x00000030
MB_ICONASTERISK = 0x00000040

def windowsMessageBox(message: str, title: str="warning", style: int=MB_OK | MB_ICONEXCLAMATION):
    ctypes.windll.user32.MessageBoxW(None, message, title, style)

def info(buttonType: str):
    if buttonType == "add file":
        return windowsMessageBox(
            message="specify the path for your target file.\nnote: the program will only copy the content of it, so you don't have to worry about it",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "save file":
        return windowsMessageBox(
            message="specify the path for your corrupted file.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "start at":
        return windowsMessageBox(
            message="specify where you want to start the corruption in file bytes.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "inc by":
        return windowsMessageBox(
            message="the number by which the bytes will get incremented or decremented.\nnote: add a '-' mark before writing the number to indicate subtraction.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "gap":
        return windowsMessageBox(
            message="specify the distance from each corrupted byte.\nthe lower the number, the more bytes will be corrupted.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "end at":
        return windowsMessageBox(
            message="specify where you want to end bytes corruption.\nclick the \"very last byte\" button to get the total size of the file.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "min/max":
        return windowsMessageBox(
            message="specify range for randomly generated numbers to be used to increment bytes.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "original/new":
        return windowsMessageBox(
            message="specify a particular value to replace with a new one.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )
    elif buttonType == "replace all with":
        return windowsMessageBox(
            message="specify a value to replace every byte with.",
            title="help",
            style=MB_OK | MB_ICONASTERISK
        )

def checkType(self, *tkWidgets: Entry):
    if self.var.get() == 1:
        for item in tkWidgets[0]:
            try:
                int(item.get())
            except:
                windowsMessageBox("invalid value type.")
                return False
        return True
    elif self.var.get() == 2:
        for item in tkWidgets[1]:
            try:
                if not "/" in item.get():
                    int(item.get())
                if not len(item.get().split("/")) > 0:
                    windowsMessageBox("invalid min/max value.")
                    return False
            except:
                windowsMessageBox("invalid value type.")
                return False
        return True
    
    elif self.var.get() == 3:
        for item in tkWidgets[2]:
            try:
                if not "/" in item.get():
                    int(item.get())
                if not len(item.get().split("/")) > 0:
                    windowsMessageBox("invalid original/new value.")
                    return False
            except:
                windowsMessageBox("invalid value type.")
                return False
        return True

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