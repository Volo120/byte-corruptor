from tkinter import *
from enum import Enum

class DarkTheme(Enum):
    BG: str = "#1E1E1E"
    FG: str = "#FFFFFF"
    LABEL_BG: str = BG
    LABEL_FG: str = FG
    ENTRY_BG: str = "#333333"
    ENTRY_FG: str = FG
    ENTRY_DB: str = BG
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
    ENTRY_DB: str = BG
    BTN_BG: str = BG
    BTN_FG: str = LABEL_FG
    BTN_ABG: str = BG
    BTN_AFG: str = FG
    MENU_HIGHLIGHT: str = "SystemHighlight"

class PistachioTheme(Enum):
    BG: str = "#93C572"
    FG: str = "#FFFFFF"
    LABEL_BG: str = BG
    LABEL_FG: str = FG
    ENTRY_BG: str = "#7DAF3F"
    ENTRY_FG: str = FG
    ENTRY_DB: str = BG
    BTN_BG: str = "#7DAF3F"
    BTN_FG: str = LABEL_FG
    BTN_ABG: str = BG
    BTN_AFG: str = FG
    MENU_HIGHLIGHT: str = "#B2D994"

class Theme:
    def __init__(self, master):
        self.master = master
        self.isDefault: BooleanVar = self.master.defaultThemeVar
        self.isDark:    BooleanVar = self.master.darkThemeVar
        self.isPistachio: BooleanVar = self.master.pistachioThemeVar

    def setDarkTheme(self):
        self.master.config(bg=DarkTheme.BG.value)

        self.master.optionMenu.config(activebackground=DarkTheme.MENU_HIGHLIGHT.value)
        self.master.corruptionSettingsMenu.config(activebackground=DarkTheme.MENU_HIGHLIGHT.value)
        self.master.helpMenu.config(activebackground=DarkTheme.MENU_HIGHLIGHT.value)
        self.master.MenuItemsSubMenu.config(activebackground=DarkTheme.MENU_HIGHLIGHT.value)

        self.master.bitShiftDirectionMenu.menu.config(activebackground=DarkTheme.MENU_HIGHLIGHT.value)
        self.master.bitShiftAmountMenu.menu.config(activebackground=DarkTheme.MENU_HIGHLIGHT.value)

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
        self.master.incrementerStartEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.sep1.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerByLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerByEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.sep2.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerGapLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerGapEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.sep3.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerEndAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.incrementerEndAtEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.incrementerEndFillBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.sep4.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)

        self.master.randomizerLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value, activebackground=DarkTheme.BG.value, activeforeground=DarkTheme.FG.value, selectcolor=DarkTheme.BG.value)
        self.master.randomizerFrame.config(bg=DarkTheme.BG.value)
        self.master.randomizerStartLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerStartEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.sep5.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerByLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerByEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.randomizer_.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerGapLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerGapEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.sep6.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerEndAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.randomizerEndAtEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.randomizerEndFillBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.sep7.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)

        self.master.replacerLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value, activebackground=DarkTheme.BG.value, activeforeground=DarkTheme.FG.value, selectcolor=DarkTheme.BG.value)
        self.master.replacerFrame.config(bg=DarkTheme.BG.value)
        self.master.replacerStartLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerStartEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.sep8.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerByLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerByEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.sep9.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerGapLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerGapEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.sep10.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerEndAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.replacerEndAtEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.replacerEndFillBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.replacerExclusiveCb.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value, activebackground=DarkTheme.BG.value, activeforeground=DarkTheme.FG.value, selectcolor=DarkTheme.BG.value)
        self.master.replacerNonExclusiveEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)

        self.master.swapperLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value, activebackground=DarkTheme.BG.value, activeforeground=DarkTheme.FG.value, selectcolor=DarkTheme.BG.value)
        self.master.swapperFrame.config(bg=DarkTheme.BG.value)
        self.master.swapperStartLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.swapperStartEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.sep11.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.swapperByLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.swapperByEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.swapperGapLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.swapperGapEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.swapperEndAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.swapperEndAtEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.swapperEndFillBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)

        self.master.copierLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value, activebackground=DarkTheme.BG.value, activeforeground=DarkTheme.FG.value, selectcolor=DarkTheme.BG.value)
        self.master.copierFrame.config(bg=DarkTheme.BG.value)
        self.master.copierStartLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.copierStartEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.sep12.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.copierByLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.copierByEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.copierGapLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.copierGapEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.copierEndAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.copierEndAtEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.copierEndFillBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)

        self.master.mixerLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value, activebackground=DarkTheme.BG.value, activeforeground=DarkTheme.FG.value, selectcolor=DarkTheme.BG.value)
        self.master.mixerFrame.config(bg=DarkTheme.BG.value)
        self.master.mixerStartLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.mixerStartEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.sep13.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.fileToMixBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.mixerByEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.mixerGapLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.mixerGapEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.mixerEndAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.mixerEndAtEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.mixerEndFillBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.fileToMixLabel.config(bg=DarkTheme.BG.value, fg=DarkTheme.FG.value)

        self.master.bitShiftLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value, activebackground=DarkTheme.BG.value, activeforeground=DarkTheme.FG.value, selectcolor=DarkTheme.BG.value)
        self.master.bitShiftFrame.config(bg=DarkTheme.BG.value)
        self.master.bitShiftStartAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.bitShiftStartAtEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.bitShiftDirectionMenu.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.bitShiftAmountMenu.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.bitShiftGapLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.bitShiftGapEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.bitShiftEndAtLabel.config(bg=DarkTheme.LABEL_BG.value, fg=DarkTheme.LABEL_FG.value)
        self.master.bitShiftEndtAtEntry.config(bg=DarkTheme.ENTRY_BG.value, fg=DarkTheme.ENTRY_FG.value, disabledbackground=DarkTheme.ENTRY_DB.value)
        self.master.bitShiftEndFillBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)

        self.master.bottomFrame.config(bg=DarkTheme.BG.value)
        self.master.prevPageBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.corruptBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)
        self.master.nextPageBtn.config(bg=DarkTheme.BTN_BG.value, fg=DarkTheme.BTN_FG.value, activebackground=DarkTheme.BTN_ABG.value, activeforeground=DarkTheme.BTN_AFG.value)

        self.isDark.set(True)
        self.isDefault.set(False)
        self.isPistachio.set(False)

    def setDefaultTheme(self):
        self.master.config(bg=LightTheme.BG.value)

        self.master.optionMenu.config(activebackground=LightTheme.MENU_HIGHLIGHT.value)
        self.master.corruptionSettingsMenu.config(activebackground=LightTheme.MENU_HIGHLIGHT.value)
        self.master.helpMenu.config(activebackground=LightTheme.MENU_HIGHLIGHT.value)
        self.master.MenuItemsSubMenu.config(activebackground=LightTheme.MENU_HIGHLIGHT.value)

        self.master.bitShiftDirectionMenu.menu.config(activebackground=LightTheme.MENU_HIGHLIGHT.value)
        self.master.bitShiftAmountMenu.menu.config(activebackground=LightTheme.MENU_HIGHLIGHT.value)

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
        self.master.incrementerStartEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.sep1.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerByLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerByEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.sep2.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerGapLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerGapEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.sep3.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerEndAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.incrementerEndAtEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.incrementerEndFillBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.sep4.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)

        self.master.randomizerLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value, activebackground=LightTheme.BG.value, activeforeground=LightTheme.FG.value, selectcolor=LightTheme.ENTRY_BG.value)
        self.master.randomizerFrame.config(bg=LightTheme.BG.value)
        self.master.randomizerStartLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerStartEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.sep5.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerByLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerByEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.randomizer_.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerGapLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerGapEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.sep6.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerEndAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.randomizerEndAtEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.randomizerEndFillBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.sep7.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)

        self.master.replacerLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value, activebackground=LightTheme.BG.value, activeforeground=LightTheme.FG.value, selectcolor=LightTheme.ENTRY_BG.value)
        self.master.replacerFrame.config(bg=LightTheme.BG.value)
        self.master.replacerStartLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerStartEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.sep8.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerByLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerByEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.sep9.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerGapLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerGapEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.sep10.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerEndAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.replacerEndAtEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.replacerEndFillBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.replacerExclusiveCb.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value, activebackground=LightTheme.BG.value, activeforeground=LightTheme.FG.value, selectcolor=LightTheme.ENTRY_BG.value)
        self.master.replacerNonExclusiveEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)

        self.master.swapperLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value, activebackground=LightTheme.BG.value, activeforeground=LightTheme.FG.value, selectcolor=LightTheme.ENTRY_BG.value)
        self.master.swapperFrame.config(bg=LightTheme.BG.value)
        self.master.swapperStartLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.swapperStartEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.sep11.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.swapperByLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.swapperByEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.swapperGapLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.swapperGapEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.swapperEndAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.swapperEndAtEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.swapperEndFillBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)

        self.master.copierLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value, activebackground=LightTheme.BG.value, activeforeground=LightTheme.FG.value, selectcolor=LightTheme.ENTRY_BG.value)
        self.master.copierFrame.config(bg=LightTheme.BG.value)
        self.master.copierStartLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.copierStartEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.sep12.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.copierByLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.copierByEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.copierGapLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.copierGapEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.copierEndAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.copierEndAtEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.copierEndFillBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)

        self.master.mixerLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value, activebackground=LightTheme.BG.value, activeforeground=LightTheme.FG.value, selectcolor=LightTheme.ENTRY_BG.value)
        self.master.mixerFrame.config(bg=LightTheme.BG.value)
        self.master.mixerStartLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.mixerStartEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.sep13.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.fileToMixBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.mixerByEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.mixerGapLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.mixerGapEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.mixerEndAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.mixerEndAtEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.mixerEndFillBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.fileToMixLabel.config(bg=LightTheme.BG.value, fg=LightTheme.FG.value)

        self.master.bitShiftLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value, activebackground=LightTheme.BG.value, activeforeground=LightTheme.FG.value, selectcolor=LightTheme.ENTRY_BG.value)
        self.master.bitShiftFrame.config(bg=LightTheme.BG.value)
        self.master.bitShiftStartAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.bitShiftStartAtEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.bitShiftDirectionMenu.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.bitShiftAmountMenu.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.bitShiftGapLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.bitShiftGapEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.bitShiftEndAtLabel.config(bg=LightTheme.LABEL_BG.value, fg=LightTheme.LABEL_FG.value)
        self.master.bitShiftEndtAtEntry.config(bg=LightTheme.ENTRY_BG.value, fg=LightTheme.ENTRY_FG.value, disabledbackground=LightTheme.ENTRY_DB.value)
        self.master.bitShiftEndFillBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)

        self.master.bottomFrame.config(bg=LightTheme.BG.value)
        self.master.prevPageBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.corruptBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)
        self.master.nextPageBtn.config(bg=LightTheme.BTN_BG.value, fg=LightTheme.BTN_FG.value, activebackground=LightTheme.BTN_ABG.value, activeforeground=LightTheme.BTN_AFG.value)

        self.isDark.set(False)
        self.isDefault.set(True)
        self.isPistachio.set(False)

    def setPistachioTheme(self):
        self.master.config(bg=PistachioTheme.BG.value)

        self.master.optionMenu.config(activebackground=PistachioTheme.MENU_HIGHLIGHT.value)
        self.master.corruptionSettingsMenu.config(activebackground=PistachioTheme.MENU_HIGHLIGHT.value)
        self.master.helpMenu.config(activebackground=PistachioTheme.MENU_HIGHLIGHT.value)
        self.master.MenuItemsSubMenu.config(activebackground=PistachioTheme.MENU_HIGHLIGHT.value)

        self.master.bitShiftDirectionMenu.menu.config(activebackground=PistachioTheme.MENU_HIGHLIGHT.value)
        self.master.bitShiftAmountMenu.menu.config(activebackground=PistachioTheme.MENU_HIGHLIGHT.value)

        self.master.topFrame.config(bg=PistachioTheme.BG.value)
        self.master.fileBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
        self.master.fileEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value)
        self.master.fileHelpBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
        
        self.master.saveBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
        self.master.saveEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value)
        self.master.saveHelpBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)

        self.master.incrementerLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value, activebackground=PistachioTheme.BG.value, activeforeground=PistachioTheme.FG.value, selectcolor=PistachioTheme.ENTRY_BG.value)
        self.master.incrementerFrame.config(bg=PistachioTheme.BG.value)
        self.master.incrementerStartAtLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.incrementerStartEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.sep1.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.incrementerByLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.incrementerByEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.sep2.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.incrementerGapLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.incrementerGapEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.sep3.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.incrementerEndAtLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.incrementerEndAtEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.incrementerEndFillBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
        self.master.sep4.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)

        self.master.randomizerLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value, activebackground=PistachioTheme.BG.value, activeforeground=PistachioTheme.FG.value, selectcolor=PistachioTheme.ENTRY_BG.value)
        self.master.randomizerFrame.config(bg=PistachioTheme.BG.value)
        self.master.randomizerStartLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.randomizerStartEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.sep5.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.randomizerByLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.randomizerByEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.randomizer_.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.randomizerGapLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.randomizerGapEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.sep6.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.randomizerEndAtLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.randomizerEndAtEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.randomizerEndFillBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
        self.master.sep7.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)

        self.master.replacerLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value, activebackground=PistachioTheme.BG.value, activeforeground=PistachioTheme.FG.value, selectcolor=PistachioTheme.ENTRY_BG.value)
        self.master.replacerFrame.config(bg=PistachioTheme.BG.value)
        self.master.replacerStartLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.replacerStartEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.sep8.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.replacerByLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.replacerByEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.sep9.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.replacerGapLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.replacerGapEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.sep10.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.replacerEndAtLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.replacerEndAtEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.replacerEndFillBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
        self.master.replacerExclusiveCb.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value, activebackground=PistachioTheme.BG.value, activeforeground=PistachioTheme.FG.value, selectcolor=PistachioTheme.ENTRY_BG.value)
        self.master.replacerNonExclusiveEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)

        self.master.swapperLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value, activebackground=PistachioTheme.BG.value, activeforeground=PistachioTheme.FG.value, selectcolor=PistachioTheme.ENTRY_BG.value)
        self.master.swapperFrame.config(bg=PistachioTheme.BG.value)
        self.master.swapperStartLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.swapperStartEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.sep11.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.swapperByLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.swapperByEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.swapperGapLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.swapperGapEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.swapperEndAtLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.swapperEndAtEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.swapperEndFillBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)

        self.master.copierLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value, activebackground=PistachioTheme.BG.value, activeforeground=PistachioTheme.FG.value, selectcolor=PistachioTheme.BG.value)
        self.master.copierFrame.config(bg=PistachioTheme.BG.value)
        self.master.copierStartLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.copierStartEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.sep12.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.copierByLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.copierByEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.copierGapLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.copierGapEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.copierEndAtLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.copierEndAtEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.copierEndFillBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)

        self.master.mixerLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value, activebackground=PistachioTheme.BG.value, activeforeground=PistachioTheme.FG.value, selectcolor=PistachioTheme.BG.value)
        self.master.mixerFrame.config(bg=PistachioTheme.BG.value)
        self.master.mixerStartLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.mixerStartEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.sep13.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.fileToMixBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
        self.master.mixerByEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.mixerGapLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.mixerGapEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.mixerEndAtLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.mixerEndAtEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.mixerEndFillBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
        self.master.fileToMixLabel.config(bg=PistachioTheme.BG.value, fg=PistachioTheme.FG.value)

        self.master.bitShiftLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value, activebackground=PistachioTheme.BG.value, activeforeground=PistachioTheme.FG.value, selectcolor=PistachioTheme.BG.value)
        self.master.bitShiftFrame.config(bg=PistachioTheme.BG.value)
        self.master.bitShiftStartAtLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.bitShiftStartAtEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.bitShiftDirectionMenu.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
        self.master.bitShiftAmountMenu.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
        self.master.bitShiftGapLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.bitShiftGapEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.bitShiftEndAtLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
        self.master.bitShiftEndtAtEntry.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value, disabledbackground=PistachioTheme.ENTRY_DB.value)
        self.master.bitShiftEndFillBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)

        self.master.bottomFrame.config(bg=PistachioTheme.BG.value)
        self.master.prevPageBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
        self.master.corruptBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
        self.master.nextPageBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)

        self.isDark.set(False)
        self.isDefault.set(False)
        self.isPistachio.set(True)

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

        if self.isPistachio.get():
            presetManager.config(bg=PistachioTheme.BG.value)
            presetManager.savePathLabel.config(bg=PistachioTheme.LABEL_BG.value, fg=PistachioTheme.LABEL_FG.value)
            presetManager.presetsListBox.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value)
            presetManager.buttonsFrame.config(bg=PistachioTheme.BG.value)
            presetManager.loadPresetBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
            presetManager.delPresetBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
            presetManager.createPresetBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
            presetManager.cancelPresetBtn.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)

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
            
        if self.isPistachio.get():
            w.config(bg=PistachioTheme.BG.value)
            w.l.config(bg=PistachioTheme.BG.value, fg=PistachioTheme.LABEL_FG.value)
            w.e.config(bg=PistachioTheme.ENTRY_BG.value, fg=PistachioTheme.ENTRY_FG.value)
            w.f.config(bg=PistachioTheme.BG.value)
            w.ok.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
            w.cancel.config(bg=PistachioTheme.BTN_BG.value, fg=PistachioTheme.BTN_FG.value, activebackground=PistachioTheme.BTN_ABG.value, activeforeground=PistachioTheme.BTN_AFG.value)
