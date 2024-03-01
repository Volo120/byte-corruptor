from tkinter import *
from enum import Enum

class DarkTheme(Enum):
    BG: str = "#1E1E1E"
    FG: str = "#FFFFFF"
    LABEL_BG: str = BG
    LABEL_FG: str = FG
    ENTRY_BG: str = "#333333"
    ENTRY_FG: str = FG
    BTN_BG: str = BG
    BTN_FG: str = LABEL_FG
    BTN_ABG: str = BG
    BTN_AFG: str = FG
    MENU_HIGHLIGHT: str = "#68007A"

class LightTheme(Enum):
    BG: str = "SystemButtonFace"
    FG: str = "#000000"
    LABEL_BG: str = BG
    LABEL_FG: str = FG
    ENTRY_BG: str = "#FFFFFF"
    ENTRY_FG: str = FG
    BTN_BG: str = BG
    BTN_FG: str = LABEL_FG
    BTN_ABG: str = BG
    BTN_AFG: str = FG
    MENU_HIGHLIGHT: str = "SystemHighlight"

class Theme:
    def __init__(self, master):
        self.master = master
        self.isDefault: BooleanVar = self.master.defaultThemeVar
        self.isDark:    BooleanVar = self.master.darkThemeVar

    def setDarkTheme(self):
        self.master.config(bg=DarkTheme.BG.value)

        self.master.optionMenu.config(activebackground=DarkTheme.MENU_HIGHLIGHT.value)
        self.master.themesMenu.config(activebackground=DarkTheme.MENU_HIGHLIGHT.value)

        self.master.topFrame.config(bg=DarkTheme.BG.value)
        self.master.fileBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.fileEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.fileHelpBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        
        self.master.saveBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.saveEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.saveHelpBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)

        self.master.incrementerLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value, activebackground=DarkTheme.BG.value, activeforeground=DarkTheme.FG.value, selectcolor=DarkTheme.BG.value)
        self.master.incrementerFrame.config(bg=DarkTheme.BG.value)
        self.master.incrementerStartAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerStartEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.sep1.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerByLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerByEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.sep2.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerGapLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerGapEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.sep3.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerEndAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerEndAtEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.incrementerEndFillBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.sep4.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)

        self.master.randomizerLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value, activebackground=DarkTheme.BG.value, activeforeground=DarkTheme.FG.value, selectcolor=DarkTheme.BG.value)
        self.master.randomizerFrame.config(bg=DarkTheme.BG.value)
        self.master.randomizerStartLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerStartEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.sep5.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerByLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerByEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.randomizer_.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerGapLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerGapEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.sep6.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerEndAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerEndAtEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.randomizerEndFillBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.sep7.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)

        self.master.replacerLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value, activebackground=DarkTheme.BG.value, activeforeground=DarkTheme.FG.value, selectcolor=DarkTheme.BG.value)
        self.master.replacerFrame.config(bg=DarkTheme.BG.value)
        self.master.replacerStartLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerStartEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.sep8.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerByLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerByEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.sep9.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerGapLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerGapEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.sep10.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerEndAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerEndAtEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.replacerEndFillBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.replacerExclusiveCb.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value, activebackground=DarkTheme.BG.value, activeforeground=DarkTheme.FG.value, selectcolor=DarkTheme.BG.value)
        self.master.replacerNonExclusiveEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)

        self.master.swapperLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value, activebackground=DarkTheme.BG.value, activeforeground=DarkTheme.FG.value, selectcolor=DarkTheme.BG.value)
        self.master.swapperFrame.config(bg=DarkTheme.BG.value)
        self.master.swapperStartLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.swapperStartEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.sep11.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.swapperByLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.swapperByEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.swapperGapLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.swapperGapEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.swapperEndAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.swapperEndAtEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
        self.master.swapperEndFillBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)

        self.master.bottomFrame.config(bg=DarkTheme.BG.value)
        self.master.prevPageBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.corruptBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.nextPageBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)

        self.isDark.set(True)
        self.isDefault.set(False)

    def setDefaultTheme(self):
        self.master.config(bg=LightTheme.BG.value)

        self.master.optionMenu.config(activebackground=LightTheme.MENU_HIGHLIGHT.value)
        self.master.themesMenu.config(activebackground=LightTheme.MENU_HIGHLIGHT.value)

        self.master.topFrame.config(bg=LightTheme.BG.value)
        self.master.fileBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.fileEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.fileHelpBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        
        self.master.saveBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.saveEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.saveHelpBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)

        self.master.incrementerLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value, activebackground=LightTheme.BG.value, activeforeground=LightTheme.FG.value, selectcolor=LightTheme.ENTRY_BG.value)
        self.master.incrementerFrame.config(bg=LightTheme.BG.value)
        self.master.incrementerStartAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerStartEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.sep1.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerByLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerByEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.sep2.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerGapLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerGapEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.sep3.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerEndAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerEndAtEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.incrementerEndFillBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.sep4.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)

        self.master.randomizerLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value, activebackground=LightTheme.BG.value, activeforeground=LightTheme.FG.value, selectcolor=LightTheme.ENTRY_BG.value)
        self.master.randomizerFrame.config(bg=LightTheme.BG.value)
        self.master.randomizerStartLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerStartEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.sep5.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerByLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerByEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.randomizer_.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerGapLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerGapEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.sep6.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerEndAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerEndAtEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.randomizerEndFillBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.sep7.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)

        self.master.replacerLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value, activebackground=LightTheme.BG.value, activeforeground=LightTheme.FG.value, selectcolor=LightTheme.ENTRY_BG.value)
        self.master.replacerFrame.config(bg=LightTheme.BG.value)
        self.master.replacerStartLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerStartEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.sep8.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerByLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerByEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.sep9.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerGapLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerGapEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.sep10.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerEndAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerEndAtEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.replacerEndFillBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.replacerExclusiveCb.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value, activebackground=LightTheme.BG.value, activeforeground=LightTheme.FG.value, selectcolor=LightTheme.ENTRY_BG.value)
        self.master.replacerNonExclusiveEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)

        self.master.swapperLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value, activebackground=LightTheme.BG.value, activeforeground=LightTheme.FG.value, selectcolor=LightTheme.ENTRY_BG.value)
        self.master.swapperFrame.config(bg=LightTheme.BG.value)
        self.master.swapperStartLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.swapperStartEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.sep11.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.swapperByLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.swapperByEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.swapperGapLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.swapperGapEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.swapperEndAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.swapperEndAtEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
        self.master.swapperEndFillBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)

        self.master.bottomFrame.config(bg=LightTheme.BG.value)
        self.master.prevPageBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.corruptBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.nextPageBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)

        self.isDark.set(False)
        self.isDefault.set(True)

    def setPresetManagerTheme(self, presetManager: Toplevel):
        if self.isDefault.get():
            presetManager.config(bg=LightTheme.BG.value)
            presetManager.savePathLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
            presetManager.presetsListBox.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
            presetManager.buttonsFrame.config(bg=LightTheme.BG.value)
            presetManager.loadPresetBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
            presetManager.delPresetBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
            presetManager.createPresetBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
            presetManager.cancelPresetBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)

        if self.isDark.get():
            presetManager.config(bg=DarkTheme.BG.value)
            presetManager.savePathLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
            presetManager.presetsListBox.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
            presetManager.buttonsFrame.config(bg=DarkTheme.BG.value)
            presetManager.loadPresetBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
            presetManager.delPresetBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
            presetManager.createPresetBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
            presetManager.cancelPresetBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)

    def setPresetManagerThemeCreate(self, w: Toplevel):
        if self.isDefault.get():
            w.config(bg=LightTheme.BG.value)
            w.l.config(bg=LightTheme.BG.value, fg=LightTheme.LABEL_FG.value)
            w.e.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value)
            w.f.config(bg=LightTheme.BG.value)
            w.ok.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
            w.cancel.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)

        if self.isDark.get():
            w.config(bg=DarkTheme.BG.value)
            w.l.config(bg=DarkTheme.BG.value, fg=DarkTheme.LABEL_FG.value)
            w.e.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value)
            w.f.config(bg=DarkTheme.BG.value)
            w.ok.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
            w.cancel.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
            