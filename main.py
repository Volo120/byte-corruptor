from tkinter import *
from tkinter.filedialog import *
import os, random
import sub_functions as sf
import special_widgets as sw
import dynamic_widgets as dw
import themes as t
import preset_manager as pm
import menu_items as mi

class AppClass(Tk):
    def __init__(self):
        super().__init__()
        self.v = "v4.0.0"
        self.title(f"Byte Corruptor {self.v}")
        self.resizable(0, 0)
        self.iconbitmap(os.path.join(os.environ["WINDIR"], "System32", "systeminfo.exe")) # default windows executable icon

        self.selectedFilePath = None
        self.savePath = None

        self.fileToMixWith = None

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

        mi.init_menuItems(self, pm, dw, sf, t, os, sw)

        # inits
        dw.autoDisableAndEnable(self)
        dw.exclusiveToggle(self)
        dw.prevAndNextSwitch(self, 0)

    def runCorruption(self):
        if not sf.checkEntriesValuesType(
            self=self,
            var=self.var.get(),
            incr=self.incrementerColl.register(),
            rand=self.randomizerColl.register(),
            repl=self.replacerColl.register(),
            swap=self.swapperColl.register(),
            copy=self.copierColl.register(),
            mixe=self.mixerColl.register()
        ): return

        incStartAt, incEndAt, incGap, incInc = None, None, None, None
        rStartAt, rEndAt, rGap, rMinMax = None, None, None, None
        reStartAt, reEndAt, reGap, reOriginalNew, reNonExclusive = None, None, None, None, None
        sStartAt, sEndAt, sGap, sIndex = None, None, None, None
        cStartAt, cEndAt, cGap, cIndex = None, None, None, None
        mStartAt, mEndAt, mGap = None, None, None

        if self.var.get() == 1:
            incStartAt = self.incrementerStartEntry.get()
            incEndAt = self.incrementerEndAtEntry.get()
            incGap = self.incrementerGapEntry.get()
            incInc = self.incrementerByEntry.get()
            
        if self.var.get() == 2:
            rStartAt = self.randomizerStartEntry.get()
            rEndAt = self.randomizerEndAtEntry.get()
            rGap = self.randomizerGapEntry.get()
            rMinMax = self.randomizerByEntry.get("/")
            
        if self.var.get() == 3:
            reStartAt = self.replacerStartEntry.get()
            reEndAt = self.replacerEndAtEntry.get()
            reGap = self.replacerGapEntry.get()
            reOriginalNew = self.replacerByEntry.get("/")
            reNonExclusive = self.replacerNonExclusiveEntry.get()
            
        if self.var.get() == 4:
            sStartAt = self.swapperStartEntry.get()
            sEndAt = self.swapperEndAtEntry.get()
            sGap = self.swapperGapEntry.get()
            sIndex = self.swapperByEntry.get()

        if self.var.get() == 5:
            cStartAt = self.copierStartEntry.get()
            cEndAt = self.copierEndAtEntry.get()
            cGap = self.copierGapEntry.get()
            cIndex = self.copierByEntry.get()

        if self.var.get() == 6:
            mStartAt = self.mixerStartEntry.get()
            mEndAt = self.mixerEndAtEntry.get()
            mGap = self.mixerGapEntry.get()
            
        byteArray = []
        byteArray.clear()
        file = open(self.selectedFilePath, "rb+")
        for i in range(0, os.path.getsize(self.selectedFilePath)):
            file.seek(i)
            currentByte = file.read(1)
            intByte = int.from_bytes(currentByte, "big")
            byteArray.append(intByte)

        reversedArray = []
        reversedArray.clear()
        
        if self.reversedArray.get() and self.var.get() == 1:
            for b in byteArray[int(incStartAt):int(incEndAt)]:
                reversedArray.append(b)
            reversedArray.reverse()
            byteArray[int(incStartAt):int(incEndAt)] = reversedArray

        if self.reversedArray.get() and self.var.get() == 2:
            for b in byteArray[int(rStartAt):int(rEndAt)]:
                reversedArray.append(b)
            reversedArray.reverse()
            byteArray[int(rStartAt):int(reEndAt)] = reversedArray

        if self.reversedArray.get() and self.var.get() == 3:
            for b in byteArray[int(reStartAt):int(reEndAt)]:
                reversedArray.append(b)
            reversedArray.reverse()
            byteArray[int(reStartAt):int(reEndAt)] = reversedArray

        if self.reversedArray.get() and self.var.get() == 4:
            for b in byteArray[int(sStartAt):int(sEndAt)]:
                reversedArray.append(b)
            reversedArray.reverse()
            byteArray[int(sStartAt):int(sEndAt)] = reversedArray

        if self.var.get() == 1:
            if int(incGap) <= 0: incGap = 1
            for i in range(int(incStartAt), int(incEndAt), int(incGap)):
                if self.randomizedOperators.get():
                    op = random.choice(["+", "-"])
                    if op == "+":
                        byteArray[i] += int(incInc)
                    elif op == "-":
                        byteArray[i] -= int(incInc)
                else:
                    byteArray[i] += int(incInc)
                if byteArray[i] > 255 or byteArray[i] < 0:
                    byteArray[i] %= 255

        if self.var.get() == 2:
            if int(rGap) <= 0: rGap = 1
            for i in range(int(rStartAt), int(rEndAt), int(rGap)):
                if self.randomizedOperators.get():
                    op = random.choice(["+", "-"])
                    if op == "+":
                        byteArray[i] += random.randint(int(rMinMax[0]), int(rMinMax[1]))
                    elif op == "-":
                        byteArray[i] -= random.randint(int(rMinMax[0]), int(rMinMax[1]))
                else:
                    byteArray[i] += random.randint(int(rMinMax[0]), int(rMinMax[1]))

                if byteArray[i] > 255 or byteArray[i] < 0:
                    byteArray[i] %= 255

        if self.var.get() == 3:
            if int(reGap) <= 0: reGap = 1
            if self.exclusive.get():
                for i in range(int(reStartAt), int(reEndAt), int(reGap)):
                    if byteArray[i] == int(reOriginalNew[0]):
                        byteArray[i] = int(reOriginalNew[1])
                    if byteArray[i] > 255 or byteArray[i] < 0:
                        byteArray[i] %= 255
            else:
                for i in range(int(reStartAt), int(reEndAt), int(reGap)):
                    byteArray[i] = int(reNonExclusive)
                    if byteArray[i] > 255 or byteArray[i] < 0:
                        byteArray[i] %= 255
        
        if self.var.get() == 4:
            if int(sGap) <= 0: sGap = 1
            for i in range(int(sStartAt), int(sEndAt), int(sGap)):
                try:
                    j = i + int(sIndex)
                    obHolder = byteArray[i]
                    nbHolder = byteArray[j]
                    byteArray[i] = nbHolder
                    byteArray[i + j] = obHolder
                except IndexError: # ignore this :)
                    pass

        if self.var.get() == 5:
            if int(cGap) <= 0: cGap = 1
            if int(cIndex) > len(byteArray): return sf.user32MessageBox(message="the byte you chose is out of bounds", style=sf.MB_OK | sf.MB_ICONSTOP)
            for i in range(int(cStartAt), int(cEndAt), int(cGap)):
                byteArray[i] = byteArray[int(cIndex)]

        if self.var.get() == 6:
            if self.fileToMixWith == None: return sf.user32MessageBox(message="you haven't selected a mixing file", style=sf.MB_OK | sf.MB_ICONSTOP)

            mixBytes = []
            mixBytes.clear()
            mixIndex = 0
            mixFile = open(self.fileToMixWith, "rb+")
            for i in range(0, os.path.getsize(self.fileToMixWith)):
                mixFile.seek(i)
                mixByte = mixFile.read(1)
                intMixByte = int.from_bytes(mixByte, "big")
                mixBytes.append(intMixByte)

            if int(mGap) <= 0: mGap = 1
            for i in range(int(mStartAt), int(mEndAt), int(mGap)):
                if mixIndex > len(mixBytes)-1:
                    mixIndex = 0
                byteArray[i] = mixBytes[mixIndex]
                mixIndex += 1

        newFile = open(self.savePath, "wb+")
        
        for b in byteArray:
            byte = b.to_bytes(1, "big")
            newFile.write(byte)

        file.close()
        newFile.close()
        byteArray.clear()

if __name__ == "__main__":
    AppClass().mainloop()
