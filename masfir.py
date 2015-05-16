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
    from tkinter import Tk, Menu, Listbox, Button, filedialog
    from tkinter import END, RIGHT, LEFT, TOP, BOTH, N, W, X
except (ImportError):
    # Or python 2.7+ libs
    from Tkinter import Tk, Menu, Listbox, Button, tkFileDialog
    from Tkinter import END, RIGHT, LEFT, TOP, BOTH, N, W, X
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

        frmButtons = Frame(self)
        frmButtons.pack(side=RIGHT, anchor=N+W)

        btnLoadDirectory = Button(frmButtons, text="Load Directory", command=self._onBtnLoadDirectory)
        btnLoadDirectory.pack(side=TOP, fill=X)

        btnExit = Button(frmButtons, text="Exit", command=self._onBtnExit)
        btnExit.pack(side=TOP, fill=X)

        # Create the listbox
        self.lstFilesAndFolders = Listbox(self)

        self.lstFilesAndFolders.bind("<<ListboxSelect>>", self._onListFilesAndFolders)
        self.lstFilesAndFolders.pack(side=LEFT, fill=BOTH, expand=1)

    def _onBtnLoadDirectory(self):
        selectedDirectory = filedialog.askdirectory()

        # Populate listbox
        for item in os.listdir(selectedDirectory):
            self.lstFilesAndFolders.insert(END, item)

    def _onBtnExit(self):
        self._exit()

    def _onListFilesAndFolders(self):
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
