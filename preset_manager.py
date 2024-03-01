from tkinter import *
import themes as t
import json, os
import dynamic_widgets as dw
from sub_functions import user32MessageBox, MB_OK, MB_ICONSTOP

class PresetWindow(Toplevel):
    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.title("Presets Manager")
        self.resizable(0, 0)
        self.wm_attributes("-toolwindow", True)
        self.wm_attributes("-topmost", True)

        self.saveFolder = os.path.abspath(".")+"\\presets\\"

        self.savePathLabel = Label(self, text=self.saveFolder)
        self.savePathLabel.pack(pady=5)

        self.presetsListBox = Listbox(self, width=32, height=10, justify=CENTER, activestyle=DOTBOX)
        self.presetsListBox.pack(pady=10)

        self.buttonsFrame = Frame(self)
        self.buttonsFrame.pack(pady=5)

        self.loadPresetBtn = Button(self.buttonsFrame, text="load preset", width=15, command=self.load)
        self.loadPresetBtn.grid(row=0, column=0, padx=5)
        
        self.delPresetBtn = Button(self.buttonsFrame, text="delete preset", width=15, command=self.delete)
        self.delPresetBtn.grid(row=0, column=1, padx=5)

        self.createPresetBtn = Button(self.buttonsFrame, text="create preset", width=15, command=self.create)
        self.createPresetBtn.grid(row=1, column=0, padx=5)

        self.cancelPresetBtn = Button(self.buttonsFrame, text="cancel", width=15, command=self.destroy)
        self.cancelPresetBtn.grid(row=1, column=1, padx=5)

        self.t = t.Theme(self.master)

        self.t.setPresetManagerTheme(self)
        self._scanFolder()

    def _scanFolder(self):
        if not os.path.exists(self.saveFolder):
            os.mkdir(self.saveFolder)
            self.presetsListBox.insert(END, "empty")
            self.presetsListBox.config(state=DISABLED)
            return
        
        self.presetsListBox.delete(0, END)
        dirList = os.listdir(self.saveFolder)
        jsons = [x for x in dirList if x.lower().endswith(".json")]
        
        if len(jsons) == 0:
            self.presetsListBox.insert(END, "empty")
            self.presetsListBox.config(state=DISABLED)
            return

        for file in jsons:
            if file.lower().endswith(".json"):
                self.presetsListBox.insert(END, file)

    def _createFile(self, name: str, parent: Toplevel):
        if self.master.fileEntry["state"] == DISABLED: return user32MessageBox(
            title="",
            message="input and/or output files must be specified",
            style=MB_OK | MB_ICONSTOP
        )
        if self.master.saveEntry["state"] == DISABLED: return user32MessageBox(
            title="",
            message="input and/or output files must be specified",
            style=MB_OK | MB_ICONSTOP
        )
        newData = {
            "vars": {
                "var": self.master.var.get(),
                "defaultThemeVar": self.master.defaultThemeVar.get(),
                "darkThemeVar": self.master.darkThemeVar.get(),
            },

            "menuBar": {
                "randomizedOperators": self.master.randomizedOperators.get(),
            },

            "topFrame": {
                "fileEntry": self.master.fileEntry.get("1.0", END).replace("\n", ""),
                "saveEntry": self.master.saveEntry.get("1.0", END).replace("\n", ""),
                "selectedFilePath": self.master.selectedFilePath,
                "savePath": self.master.savePath,
            },
            
            "incrementerFrame": {
                "incrementerStartEntry": self.master.incrementerStartEntry.get(),
                "incrementerByEntry": self.master.incrementerByEntry.get(),
                "incrementerGapEntry": self.master.incrementerGapEntry.get(),
                "incrementerEndAtEntry": self.master.incrementerEndAtEntry.get(),
            },

            "randomizerFrame": {
                "randomizerStartEntry": self.master.randomizerStartEntry.get(),
                "randomizerByEntry": self.master.randomizerByEntry.get(),
                "randomizerGapEntry": self.master.randomizerGapEntry.get(),
                "randomizerEndAtEntry": self.master.randomizerEndAtEntry.get(),
            },

            "replacerFrame": {
                "replacerStartEntry": self.master.replacerStartEntry.get(),
                "replacerByEntry": self.master.replacerByEntry.get(),
                "replacerGapEntry": self.master.replacerGapEntry.get(),
                "replacerEndAtEntry": self.master.replacerEndAtEntry.get(),
                "replacerNonExclusiveEntry": self.master.replacerNonExclusiveEntry.get(),
                "exclusive": self.master.exclusive.get(),
            },

            "swapperFrame": {
                "swapperStartEntry": self.master.swapperStartEntry.get(),
                "swapperByEntry": self.master.swapperByEntry.get(),
                "swapperGapEntry": self.master.swapperGapEntry.get(),
                "swapperEndAtEntry": self.master.swapperEndAtEntry.get(),
            }
        }

        open(self.saveFolder+name+".json", "w")
        with open(self.saveFolder+name+".json", "w") as file:
            json.dump(newData, file, indent=4)

        parent.destroy()

    def create(self):
        w = Toplevel(self)
        w.title("create preset")
        w.wm_attributes("-toolwindow", True)
        w.wm_attributes("-topmost", True)

        w.l = Label(w, text="new preset name")
        w.l.pack(pady=5)

        w.e = Entry(w)
        w.e.pack(pady=5)

        w.f = Frame(w)
        w.f.pack(pady=5)

        w.ok = Button(w.f, text="OK", width=10, command=lambda: self._createFile(w.e.get(), w))
        w.ok.grid(row=0, column=0, padx=5)

        w.cancel = Button(w.f, text="Cancel", width=10, command=w.destroy)
        w.cancel.grid(row=0, column=1, padx=5)

        self.t.setPresetManagerThemeCreate(w)

    def delete(self):
        fileToDel: str = self.saveFolder+self.presetsListBox.get(ACTIVE)
        if self.presetsListBox.get(ACTIVE) == "empty" and not os.path.isfile(fileToDel):
            return
        os.remove(fileToDel)
        self._scanFolder()

    def load(self):
        savedFile = self.saveFolder+"\\"+self.presetsListBox.get(ACTIVE)
        if not os.path.isfile(savedFile) or (self.presetsListBox.get(ACTIVE) == "empty" and self.presetsListBox["state"] == DISABLED): return
        with open(savedFile, "r") as dataFile:
            data = json.load(dataFile)
        
        self.master.var.set(data["vars"]["var"])
        self.master.defaultThemeVar.set(data["vars"]["defaultThemeVar"])
        self.master.darkThemeVar.set(data["vars"]["darkThemeVar"])
        
        self.master.randomizedOperators.set(data["menuBar"]["randomizedOperators"])

        self.master.fileEntry.config(state=NORMAL); self.master.fileEntry.delete("1.0", END)
        self.master.saveEntry.config(state=NORMAL); self.master.saveEntry.delete("1.0", END)

        self.master.fileEntry.insert("1.0", data["topFrame"]["fileEntry"])
        self.master.saveEntry.insert("1.0", data["topFrame"]["saveEntry"])
        self.master.selectedFilePath = data["topFrame"]["selectedFilePath"]
        self.master.savePath = data["topFrame"]["savePath"]

        self.master.incrementerStartEntry.config(state=NORMAL); self.master.incrementerStartEntry.delete(0, END)
        self.master.incrementerByEntry.config(state=NORMAL); self.master.incrementerByEntry.delete(0, END)
        self.master.incrementerGapEntry.config(state=NORMAL); self.master.incrementerGapEntry.delete(0, END)
        self.master.incrementerEndAtEntry.config(state=NORMAL); self.master.incrementerEndAtEntry.delete(0, END)

        self.master.incrementerStartEntry.insert(0, data["incrementerFrame"]["incrementerStartEntry"]); self.master.incrementerStartEntry.config(state=DISABLED)
        self.master.incrementerByEntry.insert(0, data["incrementerFrame"]["incrementerByEntry"]); self.master.incrementerByEntry.config(state=DISABLED)
        self.master.incrementerGapEntry.insert(0, data["incrementerFrame"]["incrementerGapEntry"]); self.master.incrementerGapEntry.config(state=DISABLED)
        self.master.incrementerEndAtEntry.insert(0, data["incrementerFrame"]["incrementerEndAtEntry"]); self.master.incrementerEndAtEntry.config(state=DISABLED)

        self.master.randomizerStartEntry.config(state=NORMAL); self.master.randomizerStartEntry.delete(0, END)
        self.master.randomizerByEntry.config(state=NORMAL); self.master.randomizerByEntry.delete(0, END)
        self.master.randomizerGapEntry.config(state=NORMAL); self.master.randomizerGapEntry.delete(0, END)
        self.master.randomizerEndAtEntry.config(state=NORMAL); self.master.randomizerEndAtEntry.delete(0, END)

        self.master.randomizerStartEntry.insert(0, data["randomizerFrame"]["randomizerStartEntry"]); self.master.randomizerStartEntry.config(state=DISABLED)
        self.master.randomizerByEntry.insert(0, data["randomizerFrame"]["randomizerByEntry"]); self.master.randomizerByEntry.config(state=DISABLED)
        self.master.randomizerGapEntry.insert(0, data["randomizerFrame"]["randomizerGapEntry"]); self.master.randomizerGapEntry.config(state=DISABLED)
        self.master.randomizerEndAtEntry.insert(0, data["randomizerFrame"]["randomizerEndAtEntry"]); self.master.randomizerEndAtEntry.config(state=DISABLED)

        self.master.replacerStartEntry.config(state=NORMAL); self.master.replacerStartEntry.delete(0, END)
        self.master.replacerByEntry.config(state=NORMAL); self.master.replacerByEntry.delete(0, END)
        self.master.replacerGapEntry.config(state=NORMAL); self.master.replacerGapEntry.delete(0, END)
        self.master.replacerEndAtEntry.config(state=NORMAL); self.master.replacerEndAtEntry.delete(0, END)
        self.master.replacerNonExclusiveEntry.config(state=NORMAL); self.master.replacerNonExclusiveEntry.delete(0, END)

        self.master.replacerStartEntry.insert(0, data["replacerFrame"]["replacerStartEntry"]); self.master.replacerStartEntry.config(state=DISABLED)
        self.master.replacerByEntry.insert(0, data["replacerFrame"]["replacerByEntry"]); self.master.replacerByEntry.config(state=DISABLED)
        self.master.replacerGapEntry.insert(0, data["replacerFrame"]["replacerGapEntry"]); self.master.replacerGapEntry.config(state=DISABLED)
        self.master.replacerEndAtEntry.insert(0, data["replacerFrame"]["replacerEndAtEntry"]); self.master.replacerEndAtEntry.config(state=DISABLED)
        self.master.replacerNonExclusiveEntry.insert(0, data["replacerFrame"]["replacerNonExclusiveEntry"]); self.master.replacerNonExclusiveEntry.config(state=DISABLED)
        self.master.exclusive.set(data["replacerFrame"]["exclusive"])

        self.master.swapperStartEntry.config(state=NORMAL); self.master.swapperStartEntry.delete(0, END)
        self.master.swapperByEntry.config(state=NORMAL); self.master.swapperByEntry.delete(0, END)
        self.master.swapperGapEntry.config(state=NORMAL); self.master.swapperGapEntry.delete(0, END)
        self.master.swapperEndAtEntry.config(state=NORMAL); self.master.swapperEndAtEntry.delete(0, END)

        self.master.swapperStartEntry.insert(0, data["swapperFrame"]["swapperStartEntry"]); self.master.swapperStartEntry.config(state=DISABLED)
        self.master.swapperByEntry.insert(0, data["swapperFrame"]["swapperByEntry"]); self.master.swapperByEntry.config(state=DISABLED)
        self.master.swapperGapEntry.insert(0, data["swapperFrame"]["swapperGapEntry"]); self.master.swapperGapEntry.config(state=DISABLED)
        self.master.swapperEndAtEntry.insert(0, data["swapperFrame"]["swapperEndAtEntry"]); self.master.swapperEndAtEntry.config(state=DISABLED)

        if self.master.defaultThemeVar.get():
            self.t.setDefaultTheme()

        if self.master.darkThemeVar.get():
            self.t.setDarkTheme()

        dw.autoDisableAndEnable(self.master)
        dw.exclusiveToggle(self.master)
        dw.prevAndNextSwitch(self.master, 0)
        self.master.corruptBtn.config(state=NORMAL)

        self.destroy()

    def run(self):
        self.mainloop()