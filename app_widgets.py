from tkinter import *
import sub_functions as sf
import special_widgets as sw
import dynamic_widgets as dw
import themes as t
import preset_manager as pm
import os

def init_appWidgets(self, pm: pm, dw: dw, sf: sf, t: t, os: os, sw: sw) -> None:
    self.incrementerColl = sw.EntryCollection()
    self.randomizerColl  = sw.EntryCollection()
    self.replacerColl    = sw.EntryCollection()
    self.swapperColl     = sw.EntryCollection()
    self.copierColl      = sw.EntryCollection()
    self.mixerColl       = sw.EntryCollection()

    self.var = IntVar(self, 1)

    self.defaultThemeVar = BooleanVar(self, True)
    self.darkThemeVar = BooleanVar(self, False)
    self.pistachioThemeVar = BooleanVar(self, False)
        
    self.exclusive = BooleanVar(self, True)
    self.randomizedOperators = BooleanVar(self, False)
    self.reversedArray = BooleanVar(self, False)

    self.menuBar = Menu(self)
    
    self.optionMenu = Menu(self.menuBar, tearoff=0)
    self.optionMenu.add_command(label="Save/Load Preset File", command=lambda: pm.PresetWindow(self).run())

    self.corruptionSettingsMenu = Menu(self.menuBar, tearoff=0)
    self.corruptionSettingsMenu.add_checkbutton(label="Randomized Add/Sub Operators", variable=self.randomizedOperators)
    self.corruptionSettingsMenu.add_checkbutton(label="Invert File Bytes", variable=self.reversedArray)

    self.themesMenu = Menu(self.menuBar, tearoff=0)
    self.themesMenu.add_checkbutton(label="Default", command=lambda: t.Theme(self).setDefaultTheme(), variable=self.defaultThemeVar, activebackground=t.LightTheme.MENU_HIGHLIGHT.value)
    self.themesMenu.add_checkbutton(label="Dark", command=lambda: t.Theme(self).setDarkTheme(), variable=self.darkThemeVar, activebackground=t.DarkTheme.MENU_HIGHLIGHT.value)
    self.themesMenu.add_checkbutton(label="Pistachio", command=lambda: t.Theme(self).setPistachioTheme(), variable=self.pistachioThemeVar, activebackground=t.PistachioTheme.MENU_HIGHLIGHT.value)

    self.helpMenu = Menu(self.menuBar, tearoff=0)
    self.MenuItemsSubMenu = Menu(self.helpMenu, tearoff=0)
    self.helpMenu.add_cascade(label="Menu Items", menu=self.MenuItemsSubMenu)

    self.MenuItemsSubMenu.add_command(label="Randomized Add/Sub Operators", command=sf.randomizedAddSubOperators_HELP)
    self.MenuItemsSubMenu.add_command(label="Invert File Bytes", command=sf.invertFileBytes_HELP)

    self.menuBar.add_cascade(label="Options", menu=self.optionMenu)
    self.menuBar.add_cascade(label="Corruption Settings", menu=self.corruptionSettingsMenu)
    self.menuBar.add_cascade(label="Themes", menu=self.themesMenu)
    self.menuBar.add_cascade(label="Help", menu=self.helpMenu)
    self.config(menu=self.menuBar)

    self.topFrame = Frame(self)
    self.topFrame.pack()

    self.fileBtn = Button(self.topFrame, text="open…", command=lambda: sf.selectFile(self))
    self.fileBtn.grid(row=0, column=0, pady=5)

    self.fileEntry = Text(self.topFrame, width=50, height=1, state=DISABLED)
    self.fileEntry.grid(row=0, column=1, padx=5)

    self.fileHelpBtn = Button(self.topFrame, text="?", command=lambda: sf.info(buttonType="add file"))
    self.fileHelpBtn.grid(row=0, column=2, padx=5)
    
    self.saveBtn = Button(self.topFrame, text="save to…", command=lambda: sf.saveToPath(self))
    self.saveBtn.grid(row=1, column=0, pady=5)

    self.saveEntry = Text(self.topFrame, width=50, height=1, state=DISABLED)
    self.saveEntry.grid(row=1, column=1, padx=5)

    self.saveHelpBtn = Button(self.topFrame, text="?", command=lambda: sf.info(buttonType="save file"))
    self.saveHelpBtn.grid(row=1, column=2, padx=5)

    # **********
    self.incrementerLabel = Radiobutton(self, text="Incrementer", value=1, variable=self.var, command=lambda: dw.autoDisableAndEnable(self))
    self.incrementerLabel.pack(pady=5)

    self.incrementerFrame = Frame(self)
    self.incrementerFrame.pack(pady=5)

    self.incrementerStartAtLabel = Label(self.incrementerFrame, text="start at", cursor="hand2")
    self.incrementerStartAtLabel.grid(row=0, column=0, padx=5)
    self.incrementerStartAtLabel.bind("<Button-1>", lambda x=None: sf.info("start at"))

    self.incrementerStartEntry = Entry(self.incrementerFrame, width=9)
    self.incrementerStartEntry.grid(row=0, column=1)
    self.incrementerStartEntry.insert(END, "0")

    self.sep1 = Label(self.incrementerFrame)
    self.sep1.grid(row=0, column=2)

    self.incrementerByLabel = Label(self.incrementerFrame, text="increment by", cursor="hand2")
    self.incrementerByLabel.grid(row=0, column=3, padx=5)
    self.incrementerByLabel.bind("<Button-1>", lambda x=None: sf.info("inc by"))

    self.incrementerByEntry = Entry(self.incrementerFrame, width=7)
    self.incrementerByEntry.grid(row=0, column=4)
    self.incrementerByEntry.insert(END, "0")

    self.sep2 = Label(self.incrementerFrame)
    self.sep2.grid(row=0, column=5)

    self.incrementerGapLabel = Label(self.incrementerFrame, text="gap size", cursor="hand2")
    self.incrementerGapLabel.grid(row=0, column=6, padx=5)
    self.incrementerGapLabel.bind("<Button-1>", lambda x=None: sf.info("gap"))

    self.incrementerGapEntry = Entry(self.incrementerFrame, width=9)
    self.incrementerGapEntry.grid(row=0, column=7)
    self.incrementerGapEntry.insert(END, "0")

    self.sep3 = Label(self.incrementerFrame)
    self.sep3.grid(row=0, column=8)

    self.incrementerEndAtLabel = Label(self.incrementerFrame, text="end at", cursor="hand2")
    self.incrementerEndAtLabel.grid(row=0, column=9, padx=5)
    self.incrementerEndAtLabel.bind("<Button-1>", lambda x=None: sf.info("end at"))

    self.incrementerEndAtEntry = Entry(self.incrementerFrame, width=9)
    self.incrementerEndAtEntry.grid(row=0, column=10)
    self.incrementerEndAtEntry.insert(END, "0")

    self.incrementerEndFillBtn = Button(self.incrementerFrame, text="very last byte", command=lambda: (self.incrementerEndAtEntry.delete(0, END), self.incrementerEndAtEntry.insert(END, os.path.getsize(self.selectedFilePath))) if len(self.selectedFilePath) > 0 else sf.user32MessageBox("you haven't selected a file yet.", style=sf.MB_ICONEXCLAMATION))
    self.incrementerEndFillBtn.grid(row=0, column=11, padx=15)

    self.sep4 = Label(self.incrementerFrame)
    self.sep4.grid(row=1, column=0)

    self.incrementerColl.setEntry(
        self.incrementerStartEntry,
        self.incrementerByEntry,
        self.incrementerGapEntry,
        self.incrementerEndAtEntry
    )

    # **********
    self.randomizerLabel = Radiobutton(self, text="Randomizer", value=2, variable=self.var, command=lambda: dw.autoDisableAndEnable(self))
    self.randomizerLabel.pack(pady=5)

    self.randomizerFrame = Frame(self)
    self.randomizerFrame.pack(pady=5)

    self.randomizerStartLabel = Label(self.randomizerFrame, text="start at", cursor="hand2")
    self.randomizerStartLabel.grid(row=0, column=0, padx=5)
    self.randomizerStartLabel.bind("<Button-1>", lambda x=None: sf.info("start at"))

    self.randomizerStartEntry = Entry(self.randomizerFrame, width=9)
    self.randomizerStartEntry.grid(row=0, column=1)
    self.randomizerStartEntry.insert(END, "0")

    self.sep5 = Label(self.randomizerFrame)
    self.sep5.grid(row=0, column=2)

    self.randomizerByLabel = Label(self.randomizerFrame, text="min/max", cursor="hand2")
    self.randomizerByLabel.grid(row=0, column=3, padx=5)
    self.randomizerByLabel.bind("<Button-1>", lambda x=None: sf.info("min/max"))

    self.randomizerByEntry = sw.Entry(self.randomizerFrame, width=9, hasSpecialCharacters=True)
    self.randomizerByEntry.grid(row=0, column=4)
    self.randomizerByEntry.insert(END, "0/255")

    self.randomizer_ = Label(self.randomizerFrame)
    self.randomizer_.grid(row=0, column=5)

    self.randomizerGapLabel = Label(self.randomizerFrame, text="gap size", cursor="hand2")
    self.randomizerGapLabel.grid(row=0, column=6, padx=5)
    self.randomizerGapLabel.bind("<Button-1>", lambda x=None: sf.info("gap"))

    self.randomizerGapEntry = Entry(self.randomizerFrame, width=9)
    self.randomizerGapEntry.grid(row=0, column=7)
    self.randomizerGapEntry.insert(END, "0")

    self.sep6 = Label(self.randomizerFrame)
    self.sep6.grid(row=0, column=8)

    self.randomizerEndAtLabel = Label(self.randomizerFrame, text="end at", cursor="hand2")
    self.randomizerEndAtLabel.grid(row=0, column=9, padx=5)
    self.randomizerEndAtLabel.bind("<Button-1>", lambda x=None: sf.info("end at"))

    self.randomizerEndAtEntry = Entry(self.randomizerFrame, width=9)
    self.randomizerEndAtEntry.grid(row=0, column=10)
    self.randomizerEndAtEntry.insert(END, "0")

    self.randomizerEndFillBtn = Button(self.randomizerFrame, text="very last byte", command=lambda: (self.randomizerEndAtEntry.delete(0, END), self.randomizerEndAtEntry.insert(END, os.path.getsize(self.selectedFilePath))) if len(self.selectedFilePath) > 0 else sf.user32MessageBox("you haven't selected a file yet.", style=sf.MB_ICONEXCLAMATION))
    self.randomizerEndFillBtn.grid(row=0, column=11, padx=15)

    self.sep7 = Label(self.randomizerFrame)
    self.sep7.grid(row=1, column=0)

    self.randomizerColl.setEntry(
        self.randomizerStartEntry,
        self.randomizerByEntry,
        self.randomizerGapEntry,
        self.randomizerEndAtEntry
    )

    # **********

    self.replacerLabel = Radiobutton(self, text="Replacer", value=3, variable=self.var, command=lambda: dw.autoDisableAndEnable(self))
    self.replacerLabel.pack(pady=5)

    self.replacerFrame = Frame(self)
    self.replacerFrame.pack(pady=5)

    self.replacerStartLabel = Label(self.replacerFrame, text="start at", cursor="hand2")
    self.replacerStartLabel.grid(row=0, column=0, padx=5)
    self.replacerStartLabel.bind("<Button-1>", lambda x=None: sf.info("start at"))

    self.replacerStartEntry = Entry(self.replacerFrame, width=9)
    self.replacerStartEntry.grid(row=0, column=1)
    self.replacerStartEntry.insert(END, "0")

    self.sep8 = Label(self.replacerFrame)
    self.sep8.grid(row=0, column=2)

    self.replacerByLabel = Label(self.replacerFrame, text="original/new", cursor="hand2")
    self.replacerByLabel.grid(row=0, column=3, padx=5)
    self.replacerByLabel.bind("<Button-1>", lambda x=None: sf.info("original/new"))

    self.replacerByEntry = sw.Entry(self.replacerFrame, width=8, hasSpecialCharacters=True)
    self.replacerByEntry.insert(END, "0/255")

    self.sep9 = Label(self.replacerFrame)
    self.sep9.grid(row=0, column=5)

    self.replacerGapLabel = Label(self.replacerFrame, text="gap size", cursor="hand2")
    self.replacerGapLabel.grid(row=0, column=6, padx=5)
    self.replacerGapLabel.bind("<Button-1>", lambda x=None: sf.info("gap"))

    self.replacerGapEntry = Entry(self.replacerFrame, width=9)
    self.replacerGapEntry.grid(row=0, column=7)
    self.replacerGapEntry.insert(END, "0")

    self.sep10 = Label(self.replacerFrame)
    self.sep10.grid(row=0, column=8)

    self.replacerEndAtLabel = Label(self.replacerFrame, text="end at", cursor="hand2")
    self.replacerEndAtLabel.grid(row=0, column=9, padx=5)
    self.replacerEndAtLabel.bind("<Button-1>", lambda x=None: sf.info("end at"))

    self.replacerEndAtEntry = Entry(self.replacerFrame, width=9)
    self.replacerEndAtEntry.grid(row=0, column=10)
    self.replacerEndAtEntry.insert(END, "0")

    self.replacerEndFillBtn = Button(self.replacerFrame, text="very last byte", command=lambda: (self.replacerEndAtEntry.delete(0, END), self.replacerEndAtEntry.insert(END, os.path.getsize(self.selectedFilePath))) if len(self.selectedFilePath) > 0 else sf.user32MessageBox("you haven't selected a file yet.", style=sf.MB_ICONEXCLAMATION))
    self.replacerEndFillBtn.grid(row=0, column=11, padx=15)

    self.replacerExclusiveCb = Checkbutton(self, text="Exclusive bytes", variable=self.exclusive, command=lambda: dw.exclusiveToggle(self))
    self.replacerExclusiveCb.pack()

    # hidden (page1) *****
    self.replacerNonExclusiveEntry = Entry(self.replacerFrame, width=5)
    self.replacerNonExclusiveEntry.insert(END, "0")

    self.replacerColl.setEntry(
        self.replacerStartEntry,
        self.replacerByEntry,
        self.replacerGapEntry,
        self.replacerEndAtEntry,
        self.replacerNonExclusiveEntry
    )

    # **********

    # page 2 items

    self.swapperLabel = Radiobutton(self, text="Swapper", value=4, variable=self.var, command=lambda: dw.autoDisableAndEnable(self))

    self.swapperFrame = Frame(self)

    self.swapperStartLabel = Label(self.swapperFrame, text="start at", cursor="hand2")
    self.swapperStartLabel.bind("<Button-1>", lambda x=None: sf.info("start at"))

    self.swapperStartEntry = Entry(self.swapperFrame, width=9)
    self.swapperStartEntry.insert(END, 0)

    self.sep11 = Label(self.swapperFrame)

    self.swapperByLabel = Label(self.swapperFrame, text="swap with next", cursor="hand2")
    self.swapperByLabel.bind("<Button-1>", lambda x=None: sf.info("swap with"))

    self.swapperByEntry = Entry(self.swapperFrame, width=8)
    self.swapperByEntry.insert(END, 0)

    self.swapperGapLabel = Label(self.swapperFrame, text="gap size", cursor="hand2")
    self.swapperGapLabel.bind("<Button-1>", lambda x=None: sf.info("gap"))

    self.swapperGapEntry = Entry(self.swapperFrame, width=8)
    self.swapperGapEntry.insert(END, 0)

    self.swapperEndAtLabel = Label(self.swapperFrame, text="end at", cursor="hand2")
    self.swapperEndAtLabel.bind("<Button-1>", lambda x=None: sf.info("end at"))

    self.swapperEndAtEntry = Entry(self.swapperFrame, width=9)
    self.swapperEndAtEntry.insert(END, 0)

    self.swapperEndFillBtn = Button(self.swapperFrame, text="very last byte", command=lambda: (self.swapperEndAtEntry.delete(0, END), self.swapperEndAtEntry.insert(END, os.path.getsize(self.selectedFilePath))) if len(self.selectedFilePath) > 0 else sf.user32MessageBox("you haven't selected a file yet.", style=sf.MB_ICONEXCLAMATION))

    self.swapperColl.setEntry(
        self.swapperStartEntry,
        self.swapperByEntry,
        self.swapperGapEntry,
        self.swapperEndAtEntry
    )

    # **********

    self.copierLabel = Radiobutton(self, text="Copier", value=5, variable=self.var, command=lambda: dw.autoDisableAndEnable(self))

    self.copierFrame = Frame(self)

    self.copierStartLabel = Label(self.copierFrame, text="start at", cursor="hand2")
    self.copierStartLabel.bind("<Button-1>", lambda x=None: sf.info("start at"))

    self.copierStartEntry = Entry(self.copierFrame, width=9)
    self.copierStartEntry.insert(END, 0)

    self.sep12 = Label(self.copierFrame)

    self.copierByLabel = Label(self.copierFrame, text="copy byte at", cursor="hand2")
    self.copierByLabel.bind("<Button-1>", lambda x=None: sf.info("copy byte at"))

    self.copierByEntry = Entry(self.copierFrame, width=8)
    self.copierByEntry.insert(END, 0)

    self.copierGapLabel = Label(self.copierFrame, text="gap size", cursor="hand2")
    self.copierGapLabel.bind("<Button-1>", lambda x=None: sf.info("gap"))

    self.copierGapEntry = Entry(self.copierFrame, width=8)
    self.copierGapEntry.insert(END, 0)

    self.copierEndAtLabel = Label(self.copierFrame, text="end at", cursor="hand2")
    self.copierEndAtLabel.bind("<Button-1>", lambda x=None: sf.info("end at"))

    self.copierEndAtEntry = Entry(self.copierFrame, width=9)
    self.copierEndAtEntry.insert(END, 0)

    self.copierEndFillBtn = Button(self.copierFrame, text="very last byte", command=lambda: (self.copierEndAtEntry.delete(0, END), self.copierEndAtEntry.insert(END, os.path.getsize(self.selectedFilePath))) if len(self.selectedFilePath) > 0 else sf.user32MessageBox("you haven't selected a file yet.", style=sf.MB_ICONEXCLAMATION))

    self.copierColl.setEntry(
        self.copierStartEntry,
        self.copierByEntry,
        self.copierGapEntry,
        self.copierEndAtEntry
    )

    # **********

    self.mixerLabel = Radiobutton(self, text="Mixer", value=6, variable=self.var, command=lambda: dw.autoDisableAndEnable(self))

    self.mixerFrame = Frame(self)

    self.mixerStartLabel = Label(self.mixerFrame, text="start at", cursor="hand2")
    self.mixerStartLabel.bind("<Button-1>", lambda x=None: sf.info("start at"))

    self.mixerStartEntry = Entry(self.mixerFrame, width=9)
    self.mixerStartEntry.insert(END, 0)

    self.sep13 = Label(self.swapperFrame)

    self.fileToMixBtn = Button(self.mixerFrame, text="select file", command=lambda: sf.selectFileToMixWith(self))

    self.mixerByEntry = Entry(self.mixerFrame, width=8)
    self.mixerByEntry.insert(END, 0)

    self.mixerGapLabel = Label(self.mixerFrame, text="gap size", cursor="hand2")
    self.mixerGapLabel.bind("<Button-1>", lambda x=None: sf.info("gap"))

    self.mixerGapEntry = Entry(self.mixerFrame, width=8)
    self.mixerGapEntry.insert(END, 0)

    self.mixerEndAtLabel = Label(self.mixerFrame, text="end at", cursor="hand2")
    self.mixerEndAtLabel.bind("<Button-1>", lambda x=None: sf.info("end at"))

    self.mixerEndAtEntry = Entry(self.mixerFrame, width=9)
    self.mixerEndAtEntry.insert(END, 0)

    self.mixerEndFillBtn = Button(self.mixerFrame, text="very last byte", command=lambda: (self.mixerEndAtEntry.delete(0, END), self.mixerEndAtEntry.insert(END, os.path.getsize(self.selectedFilePath))) if len(self.selectedFilePath) > 0 else sf.user32MessageBox("you haven't selected a file yet.", style=sf.MB_ICONEXCLAMATION))

    self.fileToMixLabel = Label(self, text="no file is selected")

    self.mixerColl.setEntry(
        self.mixerStartEntry,
        self.mixerByEntry,
        self.mixerGapEntry,
        self.mixerEndAtEntry
    )

    # **********

    self.bottomFrame = Frame(self)
    self.bottomFrame.pack(pady=10, side="bottom")

    self.prevPageBtn = Button(self.bottomFrame, text="<<<", font=("Helvetica", 15, "bold"), state=NORMAL, command=lambda: dw.prevAndNextSwitch(self, 0))
    self.prevPageBtn.grid(row=0, column=0, padx=5)

    self.corruptBtn = Button(self.bottomFrame, text="Corrupt", font=("Helvetica", 20, "bold"), state=DISABLED, command=self.runCorruption)
    self.corruptBtn.grid(row=0, column=1)

    self.nextPageBtn = Button(self.bottomFrame, text=">>>", font=("Helvetica", 15, "bold"), state=NORMAL, command=lambda: dw.prevAndNextSwitch(self, 1))
    self.nextPageBtn.grid(row=0, column=2, padx=5)

    # **********