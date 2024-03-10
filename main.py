from tkinter import *
from tkinter.filedialog import *
import os, random
import sub_functions as sf
import special_widgets as sw
import dynamic_widgets as dw
import themes as t
import preset_manager as pm
import app_widgets as aw

class AppClass(Tk):
    def __init__(self):
        super().__init__()
        self.v = "v4.1.2"
        self.title(f"Byte Corruptor {self.v}")
        self.resizable(0, 0)
        self.iconbitmap(os.path.join(os.environ["WINDIR"], "System32", "systeminfo.exe")) # windows executable icon

        self.selectedFilePath = ""
        self.savePath = None

        self.fileToMixWith = None

        # init (defaults)
        aw.init_appWidgets(self, pm, dw, sf, t, os, sw)
        dw.autoDisableAndEnable(self)
        dw.exclusiveToggle(self)
        dw.prevAndNextSwitch(self, None)

    def runCorruption(self):
        if not sf.checkEntriesValuesType(
            self=self,
            var=self.var.get(),
            incr=self.incrementerColl.register(),
            rand=self.randomizerColl.register(),
            repl=self.replacerColl.register(),
            swap=self.swapperColl.register(),
            copy=self.copierColl.register(),
            mixe=self.mixerColl.register(),
            bits=self.bitShifterColl.register()
        ): return

        if self.var.get() == 1:
            iStartAt = self.incrementerStartEntry.get()
            iEndAt = self.incrementerEndAtEntry.get()
            iGap = self.incrementerGapEntry.get()
            iInc = self.incrementerByEntry.get()
            
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

        if self.var.get() == 7:
            bsStartAt = self.bitShiftStartAtEntry.get()
            bsShiftDirection = self.bitShiftDirectionVar.get()
            bsShiftAmount = self.bitShiftAmount.get()
            bsGap = self.bitShiftGapEntry.get()
            bsEndAt = self.bitShiftEndtAtEntry.get()
            
        byteArray = []
        byteArray.clear()

        file = open(self.selectedFilePath, "rb+")
        newFile = open(self.savePath, "wb+")

        for i in range(0, os.path.getsize(self.selectedFilePath)):
            file.seek(i)
            currentByte = file.read(1)
            intByte = int.from_bytes(currentByte, "big")
            byteArray.append(intByte)

        reversedArray = []
        reversedArray.clear()
        
        if self.reversedArray.get() and self.var.get() == 1:
            byteArray[int(iStartAt):int(iEndAt)] = sf.reverseBytes(byteArray, iStartAt, iEndAt)

        if self.reversedArray.get() and self.var.get() == 2:
            byteArray[int(rStartAt):int(rEndAt)] = sf.reverseBytes(byteArray, rStartAt, rEndAt)

        if self.reversedArray.get() and self.var.get() == 3:
            byteArray[int(reStartAt):int(reEndAt)] = sf.reverseBytes(byteArray, reStartAt, reEndAt)

        if self.reversedArray.get() and self.var.get() == 4:
            byteArray[int(sStartAt):int(sEndAt)] = sf.reverseBytes(byteArray, sStartAt, sEndAt)

        if self.reversedArray.get() and self.var.get() == 5:
            byteArray[int(cStartAt):int(cEndAt)] = sf.reverseBytes(byteArray, cStartAt, cEndAt)

        if self.reversedArray.get() and self.var.get() == 6:
            byteArray[int(mStartAt):int(mEndAt)] = sf.reverseBytes(byteArray, mStartAt, mEndAt)
        
        if self.reversedArray.get() and self.var.get() == 7:
            byteArray[int(bsStartAt):int(bsEndAt)] = sf.reverseBytes(byteArray, bsStartAt, bsEndAt)

        if self.var.get() == 1:
            if int(iGap) <= 0: iGap = 1
            for i in range(int(iStartAt), int(iEndAt), int(iGap)):
                if self.randomizedOperators.get():
                    op = random.choice(["+", "-"])
                    if op == "+":
                        byteArray[i] += int(iInc)
                    elif op == "-":
                        byteArray[i] -= int(iInc)
                else:
                    byteArray[i] += int(iInc)
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
            if int(sIndex) > len(byteArray): return sf.user32MessageBox(message="the byte you chose is out of bounds", style=sf.MB_OK | sf.MB_ICONSTOP)
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
                if mixIndex == len(mixBytes):
                    mixIndex = 0
                byteArray[i] = mixBytes[mixIndex]
                mixIndex += 1

            mixFile.close()

        if self.var.get() == 7:
            if int(bsGap) <= 0: bsGap = 1
            for i in range(int(bsStartAt), int(bsEndAt), int(bsGap)):
                if bsShiftDirection == "left":
                    byteArray[i] = byteArray[i] << bsShiftAmount
                if bsShiftDirection == "right":
                    byteArray[i] = byteArray[i] >> bsShiftAmount
                if byteArray[i] > 255 or byteArray[i] < 0:
                    byteArray[i] %= 255

        for b in byteArray:
            byte = b.to_bytes(1, "big")
            newFile.write(byte)

        file.close()
        newFile.close()
        byteArray.clear()

if __name__ == "__main__":
    AppClass().mainloop()
