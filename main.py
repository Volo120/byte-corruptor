from tkinter import Tk
import dynamic_widgets as dw
import app_widgets as aw

class Corruptor(Tk):
    def __init__(self):
        super().__init__()
        aw.init_windowAttributes(self)
        aw.init_appWidgets(self)
        dw.autoDisableAndEnable(self)
        dw.exclusiveToggle(self)
        dw.prevAndNextSwitch(self, None)

if __name__ == "__main__":
    Corruptor().mainloop()
