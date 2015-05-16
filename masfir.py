#!/usr/bin/env python
# -*- Coding: utf-8 -*-

"""
" Movie And Series FIlename Renamer
"
" author: Claude Muller
"
"""

try:
    # Try python 3.+ libs
    from tkinter import Tk, Menu, Listbox, Button, filedialog, Label, StringVar, OptionMenu
    from tkinter import END, RIGHT, LEFT, TOP, BOTTOM, BOTH, N, W, E, S, X
except (ImportError):
    # Or python 2.7+ libs
    from Tkinter import Tk, Menu, Listbox, Button, tkFileDialog, Label, StringVar, OptionMenu
    from Tkinter import END, RIGHT, LEFT, TOP, BOTTOM, BOTH, N, W, E, S, X
from ttk import Frame, Style
import os
import dirmuncher

class Masfir(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self._initUI()

    def _initUI(self):
        """ Initialise the UI """
        self.parent.title("Masfir v0.1")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self._createMenu()
        self._createUIElements()

    def _createMenu(self):
        """ Create the menu """

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        # File Menu
        mnuFile = Menu(menubar)
        mnuFile.add_command(label="Exit", underline=1, command=self._onMenuFileExit)
        menubar.add_cascade(label="File", underline=0, menu=mnuFile)

        # Help Menu
        mnuHelp = Menu(menubar)
        mnuHelp.add_command(label="About", underline=0, command=self._onMenuHelpAbout)
        menubar.add_cascade(label="Help", underline=0, menu=mnuHelp)

    def _createUIElements(self):
        """ Create the main frame's UI elements """

        # Top frame with the Load Directory controls
        frmLoadDir = Frame(self)
        frmLoadDir.pack(side=TOP, anchor=N, fill=X)

        self.sLoadDirVar = StringVar()
        lblLoadDir = Label(frmLoadDir, text="<Empty Directory>", textvariable=self.sLoadDirVar)
        lblLoadDir.pack(side=LEFT)

        btnLoadDir = Button(frmLoadDir, text="Load Directory", command=self._onBtnLoadDir)
        btnLoadDir.pack(side=RIGHT)

        # Dropdown with list of series (directories) detected
        frmSeriesSelector = Frame(self)
        frmSeriesSelector.pack(side=TOP, anchor=N, fill=X)

        self.sSeriesVar = StringVar()
        self.optSeries = OptionMenu(frmSeriesSelector, self.sSeriesVar, 'one', 'two', 'three', 'Loading', command=self._onBtnSeriesSelected)
        self.optSeries.pack(side=LEFT)

        # The two diff-style listboxes containing original and new episode list names
        frmListBoxes = Frame(self)
        frmListBoxes.pack(fill=BOTH, expand=1)

        self.lstOrgFiles = Listbox(frmListBoxes)
        self.lstOrgFiles.bind("<<ListboxSelect>>", self._onListOrgFiles)
        self.lstOrgFiles.pack(side=LEFT, fill=BOTH, expand=1, anchor=W)

        self.lstNewFiles = Listbox(frmListBoxes)
        self.lstNewFiles.bind("<<ListboxSelect>>", self._onListNewFiles)
        self.lstNewFiles.pack(side=RIGHT, fill=BOTH, expand=1, anchor=E)

        # Bottom buttons
        frmFinal = Frame(self)
        frmFinal.pack(side=BOTTOM, anchor=S, fill=X)

        btnRename = Button(frmFinal, text="Rename", command=self._onBtnRename)
        btnRename.pack(side=LEFT)

        btnExit = Button(frmFinal, text="Exit", command=self._onBtnExit)
        btnExit.pack(side=RIGHT)

    def _onBtnLoadDir(self):
        selectedDirectory = filedialog.askdirectory()

        self.optSeries['menu'].delete(0, END)
        # self.optSeries['menu'].insert('one', 'two', 'three')
        self.sSeriesVar.set('two')

        self.sLoadDirVar.set(selectedDirectory)
        # Populate listbox
        self.lstOrgFiles.delete(0, END)
        for item in os.listdir(selectedDirectory):
            self.lstOrgFiles.insert(END, item)

    def _onBtnExit(self):
        self._exit()

    def _onListOrgFiles(self):
        pass

    def _onListNewFiles(self):
        pass

    def _onBtnSeriesSelected(self):
        pass

    def _onBtnRename(self):
        pass

    def _onMenuFileExit(self):
        """ Jump to _exit() if Exit is clicked """
        self._exit()

    def _onMenuHelpAbout(self):
        """ Something here """
        pass

    def _exit(self):
        """ Exit the app """
        self.quit()


def main():
    root = Tk()
    root.geometry("800x600+100+100")
    app = Masfir(root)
    root.mainloop()

if __name__ == "__main__":
    main()
