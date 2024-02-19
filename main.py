from tkinter import *
from tkinter.filedialog import *
import os, random
import sub_functions as sf
import special_widgets as sw

class AppClass(Tk):
    def __init__(self):
        super().__init__()
        self.v = "2.0.0"
        self.title(f"V's Byte Corruptor {self.v}")
        self.geometry("770x530")
        self.resizable(0, 0)

        self.selectedFilePath = ""
        self.savePath = ""

        self.incrementerColl = sw.EntryCollection()
        self.randomizerColl  = sw.EntryCollection()
        self.replacerColl    = sw.EntryCollection()
        self.swapperColl     = sw.EntryCollection()
        
        self.randomizedOperators = BooleanVar()
        self.exclusive = BooleanVar()
        self.var = IntVar()

        self.exclusive.set(True)
        self.var.set(1)

        self.menuBar = Menu(self)
        self.optionMenu = Menu(self.menuBar, tearoff=0)
        self.optionMenu.add_checkbutton(label="Randomized Add/Sub Operators", variable=self.randomizedOperators)
        self.menuBar.add_cascade(label="Options", menu=self.optionMenu)
        self.config(menu=self.menuBar)

        self.topFrame = Frame(self, width=700, height=300)
        self.topFrame.pack()

        self.fileBtn = Button(self.topFrame, text="open..", command=self.selectFile)
        self.fileBtn.grid(row=0, column=0, pady=5)

        self.fileEntry = Text(self.topFrame, width=50, height=1, state=DISABLED)
        self.fileEntry.grid(row=0, column=1, padx=5)

        self.fileHelpBtn = Button(self.topFrame, text="?", command=lambda: sf.info(buttonType="add file"))
        self.fileHelpBtn.grid(row=0, column=2, padx=5)
        
        self.saveBtn = Button(self.topFrame, text="save to..", command=self.saveToPath)
        self.saveBtn.grid(row=1, column=0, pady=5)

        self.saveEntry = Text(self.topFrame, width=50, height=1, state=DISABLED)
        self.saveEntry.grid(row=1, column=1, padx=5)

        self.saveHelpBtn = Button(self.topFrame, text="?", command=lambda: sf.info(buttonType="save file"))
        self.saveHelpBtn.grid(row=1, column=2, padx=5)

        # **********
        self.incrementerLabel = Radiobutton(self, text="Incrementer", value=1, variable=self.var, command=lambda: sf.autoDisableAndEnable(self))
        self.incrementerLabel.pack(pady=5)

        self.incrementerFrame = Frame(self)
        self.incrementerFrame.pack(pady=5)

        self.incrementerStartAtLabel = Label(self.incrementerFrame, text="start at", cursor="hand2")
        self.incrementerStartAtLabel.grid(row=0, column=0, padx=5)
        self.incrementerStartAtLabel.bind("<Button-1>", lambda x=None: sf.info("start at"))

        self.incrementerStartEntry = Entry(self.incrementerFrame, width=9)
        self.incrementerStartEntry.grid(row=0, column=1)

        self.sep1 = Label(self.incrementerFrame)
        self.sep1.grid(row=0, column=2)

        self.incrementerByLabel = Label(self.incrementerFrame, text="increment by", cursor="hand2")
        self.incrementerByLabel.grid(row=0, column=3, padx=5)
        self.incrementerByLabel.bind("<Button-1>", lambda x=None: sf.info("inc by"))

        self.incrementerByEntry = Entry(self.incrementerFrame, width=7)
        self.incrementerByEntry.grid(row=0, column=4)

        self.sep2 = Label(self.incrementerFrame)
        self.sep2.grid(row=0, column=5)

        self.incrementerGapLabel = Label(self.incrementerFrame, text="gap size", cursor="hand2")
        self.incrementerGapLabel.grid(row=0, column=6, padx=5)
        self.incrementerGapLabel.bind("<Button-1>", lambda x=None: sf.info("gap"))

        self.incrementerGapEntry = Entry(self.incrementerFrame, width=9)
        self.incrementerGapEntry.grid(row=0, column=7)

        self.sep3 = Label(self.incrementerFrame)
        self.sep3.grid(row=0, column=8)

        self.incrementerEndAtLabel = Label(self.incrementerFrame, text="end at", cursor="hand2")
        self.incrementerEndAtLabel.grid(row=0, column=9, padx=5)
        self.incrementerEndAtLabel.bind("<Button-1>", lambda x=None: sf.info("end at"))

        self.incrementerEndAtEntry = Entry(self.incrementerFrame, width=9)
        self.incrementerEndAtEntry.grid(row=0, column=10)

        self.incrementerEndFillBtn = Button(self.incrementerFrame, text="very last byte", command=lambda: (self.incrementerEndAtEntry.delete(0, END), self.incrementerEndAtEntry.insert(END, os.path.getsize(self.selectedFilePath))) if len(self.selectedFilePath) > 0 else sf.windowsMessageBox("you haven't selected a file yet.", style=sf.MB_ICONEXCLAMATION))
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
        self.randomizerLabel = Radiobutton(self, text="Randomizer", value=2, variable=self.var, command=lambda: sf.autoDisableAndEnable(self))
        self.randomizerLabel.pack(pady=5)

        self.randomizerFrame = Frame(self)
        self.randomizerFrame.pack(pady=5)

        self.randomizerStartLabel = Label(self.randomizerFrame, text="start at", cursor="hand2")
        self.randomizerStartLabel.grid(row=0, column=0, padx=5)
        self.randomizerStartLabel.bind("<Button-1>", lambda x=None: sf.info("start at"))

        self.randomizerStartEntry = Entry(self.randomizerFrame, width=9)
        self.randomizerStartEntry.grid(row=0, column=1)

        self.sep5 = Label(self.randomizerFrame)
        self.sep5.grid(row=0, column=2)

        self.randomizerByLabel = Label(self.randomizerFrame, text="min/max", cursor="hand2")
        self.randomizerByLabel.grid(row=0, column=3, padx=5)
        self.randomizerByLabel.bind("<Button-1>", lambda x=None: sf.info("min/max"))

        self.randomizerByEntry = sw.Entry(self.randomizerFrame, width=9, hasSpecialCharacters=True)
        self.randomizerByEntry.grid(row=0, column=4)
        self.randomizerByEntry.insert(END, "0/255")

        Label(self.randomizerFrame).grid(row=0, column=5)

        self.randomizerGapLabel = Label(self.randomizerFrame, text="gap size", cursor="hand2")
        self.randomizerGapLabel.grid(row=0, column=6, padx=5)
        self.randomizerGapLabel.bind("<Button-1>", lambda x=None: sf.info("gap"))

        self.randomizerGapEntry = Entry(self.randomizerFrame, width=9)
        self.randomizerGapEntry.grid(row=0, column=7)

        self.sep6 = Label(self.randomizerFrame)
        self.sep6.grid(row=0, column=8)

        self.randomizerEndAtLabel = Label(self.randomizerFrame, text="end at", cursor="hand2")
        self.randomizerEndAtLabel.grid(row=0, column=9, padx=5)
        self.randomizerEndAtLabel.bind("<Button-1>", lambda x=None: sf.info("end at"))

        self.randomizerEndAtEntry = Entry(self.randomizerFrame, width=9)
        self.randomizerEndAtEntry.grid(row=0, column=10)

        self.randomizerEndFillBtn = Button(self.randomizerFrame, text="very last byte", command=lambda: (self.randomizerEndAtEntry.delete(0, END), self.randomizerEndAtEntry.insert(END, os.path.getsize(self.selectedFilePath))) if len(self.selectedFilePath) > 0 else sf.windowsMessageBox("you haven't selected a file yet.", style=sf.MB_ICONEXCLAMATION))
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

        self.replacerLabel = Radiobutton(self, text="Replacer", value=3, variable=self.var, command=lambda: sf.autoDisableAndEnable(self))
        self.replacerLabel.pack(pady=5)

        self.replacerFrame = Frame(self)
        self.replacerFrame.pack(pady=5)

        self.replacerStartLabel = Label(self.replacerFrame, text="start at", cursor="hand2")
        self.replacerStartLabel.grid(row=0, column=0, padx=5)
        self.replacerStartLabel.bind("<Button-1>", lambda x=None: sf.info("start at"))

        self.replacerStartEntry = Entry(self.replacerFrame, width=9)
        self.replacerStartEntry.grid(row=0, column=1)

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
        self.sep10 = Label(self.replacerFrame)
        self.sep10.grid(row=0, column=8)

        self.replacerEndAtLabel = Label(self.replacerFrame, text="end at", cursor="hand2")
        self.replacerEndAtLabel.grid(row=0, column=9, padx=5)
        self.replacerEndAtLabel.bind("<Button-1>", lambda x=None: sf.info("end at"))

        self.replacerEndAtEntry = Entry(self.replacerFrame, width=9)
        self.replacerEndAtEntry.grid(row=0, column=10)

        self.replacerEndFillBtn = Button(self.replacerFrame, text="very last byte", command=lambda: (self.replacerEndAtEntry.delete(0, END), self.replacerEndAtEntry.insert(END, os.path.getsize(self.selectedFilePath))) if len(self.selectedFilePath) > 0 else sf.windowsMessageBox("you haven't selected a file yet.", style=sf.MB_ICONEXCLAMATION))
        self.replacerEndFillBtn.grid(row=0, column=11, padx=15)

        self.replacerExclusiveCb = Checkbutton(self, text="Exclusive bytes", variable=self.exclusive, command=lambda: sf.exclusiveToggle(self))
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

        self.swapperLabel = Radiobutton(self, text="swapper", value=4, variable=self.var, command=lambda: sf.autoDisableAndEnable(self))

        self.swapperFrame = Frame(self)

        self.swapperStartLabel = Label(self.swapperFrame, text="start at", cursor="hand2")
        self.swapperStartLabel.bind("<Button-1>", lambda x=None: sf.info("start at"))

        self.swapperStartEntry = Entry(self.swapperFrame, width=9)

        self.sep11 = Label(self.swapperFrame)

        self.swapperByLabel = Label(self.swapperFrame, text="swap with next/prev", cursor="hand2")
        self.swapperByLabel.bind("<Button-1>", lambda x=None: sf.info("swap with"))

        self.swapperByEntry = Entry(self.swapperFrame, width=8)

        self.swapperGapLabel = Label(self.swapperFrame, text="gap size", cursor="hand2")
        self.swapperGapLabel.bind("<Button-1>", lambda x=None: sf.info("gap"))

        self.swapperGapEntry = Entry(self.swapperFrame, width=8)

        self.swapperEndAtLabel = Label(self.swapperFrame, text="end at", cursor="hand2")
        self.swapperEndAtLabel.bind("<Button-1>", lambda x=None: sf.info("end at"))

        self.swapperEndAtEntry = Entry(self.swapperFrame, width=9)

        self.swapperEndFillBtn = Button(self.swapperFrame, text="very last byte", command=lambda: (self.swapperEndAtEntry.delete(0, END), self.swapperEndAtEntry.insert(END, os.path.getsize(self.selectedFilePath))) if len(self.selectedFilePath) > 0 else sf.windowsMessageBox("you haven't selected a file yet.", style=sf.MB_ICONEXCLAMATION))

        self.swapperColl.setEntry(
            self.swapperStartEntry,
            self.swapperByEntry,
            self.swapperGapEntry,
            self.swapperEndAtEntry
        )

        # **********

        self.bottomFrame = Frame(self)
        self.bottomFrame.pack(pady=10, side="bottom")

        self.prevPageBtn = Button(self.bottomFrame, text="<<<", font=("Helvetica", 15, "bold"), state=NORMAL, command=lambda: sf.prevAndNextSwitch(self, 0))
        self.prevPageBtn.grid(row=0, column=0, padx=5)

        self.runBtn = Button(self.bottomFrame, text="Run", font=("Helvetica", 20, "bold"), state=DISABLED, command=self.run)
        self.runBtn.grid(row=0, column=1)

        self.nextPageBtn = Button(self.bottomFrame, text=">>>", font=("Helvetica", 15, "bold"), state=NORMAL, command=lambda: sf.prevAndNextSwitch(self, 1))
        self.nextPageBtn.grid(row=0, column=2, padx=5)

        # **********

        # initials
        sf.autoDisableAndEnable(self)
        sf.exclusiveToggle(self)
        sf.prevAndNextSwitch(self, 0)

    def selectFile(self):
        try: self.selectedFilePath = askopenfile().name
        except AttributeError: return
        self.fileEntry.config(state=NORMAL)
        self.fileEntry.delete("1.0", END)
        self.fileEntry.insert(END, "../"+self.selectedFilePath.split("/")[-2]+"/"+self.selectedFilePath.split("/")[-1])
        self.fileEntry.config(state=DISABLED)
        self.saveBtn.config(state=NORMAL)

    def saveToPath(self):
        if not self.selectedFilePath: return
        self.saveBtn.config(state=NORMAL)
        try: self.savePath = asksaveasfile(initialfile=self.selectedFilePath).name
        except AttributeError: return
        self.saveEntry.config(state=NORMAL)
        self.saveEntry.delete("1.0", END)
        self.saveEntry.insert(END, "../"+self.savePath.split("/")[-2]+"/"+self.savePath.split("/")[-1])
        self.saveEntry.config(state=DISABLED)
        self.incrementerEndFillBtn.config(state=NORMAL)
        self.runBtn.config(state=NORMAL)

    def run(self):
        if not sf.checkEntriesValuesType(
            self,
            var=self.var.get(),
            incr=self.incrementerColl.register(),
            rand=self.randomizerColl.register(),
            repl=self.replacerColl.register(),
            swap=self.swapperColl.register()
        ): return

        incStartAt, incEndAt, incGap, incInc = None, None, None, None
        rStartAt, rEndAt, rGap, rMinMax = None, None, None, None
        reStartAt, reEndAt, reGap, reOriginalNew, reExclusive = None, None, None, None, None
        sStartAt, sEndAt, sGap, sIndex = None, None, None, None

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
            reExclusive = self.replacerNonExclusiveEntry.get()

        if self.var.get() == 4:
            sStartAt = self.swapperStartEntry.get()
            sEndAt = self.swapperEndAtEntry.get()
            sGap = self.swapperGapEntry.get()
            sIndex = self.swapperByEntry.get()

        byteArray = []
        byteArray.clear()
        file = open(self.selectedFilePath, "rb+")
        for i in range(0, os.path.getsize(self.selectedFilePath)):
            file.seek(i)
            currentByte = file.read(1)
            intByte = int.from_bytes(currentByte, "big")
            byteArray.append(intByte)

        if self.var.get() == 1:
            if int(incGap) <= 0: incGap = 1
            for i in range(int(incStartAt), int(incEndAt), int(incGap)):
                if i != 0:
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
                if i != 0:
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
                    if i != 0:
                        if byteArray[i] == int(reOriginalNew[0]):
                            byteArray[i] = int(reOriginalNew[1])
                        if byteArray[i] > 255 or byteArray[i] < 0:
                            byteArray[i] %= 255
            else:
                for i in range(int(reStartAt), int(reEndAt), int(reGap)):
                    if i != 0:
                        byteArray[i] = int(reExclusive)
                        if byteArray[i] > 255 or byteArray[i] < 0:
                            byteArray[i] %= 255

        if self.var.get() == 4:
            if int(sGap) <= 0: sGap = 1
            for i in range(int(sStartAt), int(sEndAt), int(sGap)):
                if i != 0:
                    if byteArray[i] != b"":
                        try:
                            byteArray[i], byteArray[i+int(sIndex)] = byteArray[i+int(sIndex)], byteArray[i]
                        except:
                            sf.user32MessageBox(f"out of bounds, adjust gap size")

        newFile = open(self.savePath, "wb+")
        
        for i in byteArray:
            byte = i.to_bytes(1, "big")
            newFile.write(byte)

        file.close()
        newFile.close()
        byteArray.clear()

if __name__ == "__main__":
    AppClass().mainloop()
