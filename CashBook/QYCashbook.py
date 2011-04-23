#!/usr/bin/python

import os.path
import wx
import wx.grid
from datetime import datetime

class CashbookFrame(wx.Frame):
    def __init__(self, parent, id, title):
        # New a frame using base class initializer
        wx.Frame.__init__(self, parent, id, title)
        # Create a frame status bar(bottom) using built-in method
        self.CreateStatusBar()
        # Create a menu bar using user-defined method
        self.createMenuBar()
        # Create entry header like 'Date' 'Expense' 'Comment' 'Total'
        self.createGrid()
        # Create instance of Cashbook
        self.cb = Cashbook()
    
    def createMenuBar(self):
        # Create a frame menu bar(top)
        self.menuBar = wx.MenuBar()
        self.createFileMenu()
        self.createEditMenu()
        self.createHelpMenu()
        self.SetMenuBar(self.menuBar)

    def createFileMenu(self):
        self.fileMenu = wx.Menu()
        self.menuBar.Append(self.fileMenu, 'File')
        # Add menu item to File menu
        openItem = self.fileMenu.Append(wx.ID_OPEN, 'Open', 'Open an existing cashbook file')
        saveItem = self.fileMenu.Append(wx.ID_SAVE, 'Save', 'Save these entries into a file')
        closeItem = self.fileMenu.Append(wx.ID_CLOSE, 'Close', 'Close the current cashbook file')
        exitItem = self.fileMenu.Append(wx.ID_EXIT, 'Exit', 'Exit Cashbook')
        # Bind event handler to event in File menu
        self.Bind(wx.EVT_MENU, self.onOpen, openItem)
        self.Bind(wx.EVT_MENU, self.onSave, saveItem)
        self.Bind(wx.EVT_MENU, self.onClose, closeItem)
        self.Bind(wx.EVT_MENU, self.onExit, exitItem)

    def createEditMenu(self):
        self.editMenu = wx.Menu()
        self.menuBar.Append(self.editMenu, 'Edit')
        # Add menu item to Edit menu
        newItem = self.editMenu.Append(wx.ID_NEW, 'New Entry', 'Create a new consumption entry')
        deleteItem = self.editMenu.Append(wx.ID_DELETE, 'Delete Entry', 'Delte an entry')
        # Bind event handler to event in Edit menu
        self.Bind(wx.EVT_MENU, self.onNew, newItem)
        self.Bind(wx.EVT_MENU, self.onDelete, deleteItem)
    
    def createHelpMenu(self):
        self.helpMenu = wx.Menu()
        self.menuBar.Append(self.helpMenu, 'Help')
        # Add menu item to Help menu
        aboutItem = self.helpMenu.Append(wx.ID_ABOUT, 'About', 'About Cashbook')
        helpItem = self.helpMenu.Append(wx.ID_HELP, 'Help', 'Show Cashbook help details')
        # Bind event handler to event in Help menu
        self.Bind(wx.EVT_MENU, self.onAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.onHelp, helpItem)
    
    def createGrid(self):
        self.grid = wx.grid.Grid(self, -1)
        self.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.onChange)
        self.grid.CreateGrid(0, 4)
        self.grid.SetRowLabelSize(45)
        self.grid.SetColLabelSize(20)
        self.grid.SetColLabelValue(0, 'Date')
        self.grid.SetColLabelValue(1, 'Expense')
        self.grid.SetColLabelValue(2, 'Comment')
        self.grid.SetColLabelValue(3, 'Total')
        self.grid.SetColMinimalAcceptableWidth(150)
        self.grid.SetColSize(0, 150)
        self.grid.SetColSize(1, 150)
        self.grid.SetColSize(2, 300)
        self.grid.SetColSize(3, 150)
        #self.grid.SetSize((500, 300))

    # Display updated grid
    def onShow(self, cb):
        for i in range(len(cb)):
            self.grid.SetCellValue(i, 1, str(cb[i].getExpense()))
            self.grid.SetCellValue(i, 2, cb[i].getComment())
            self.grid.SetCellValue(i, 3, str(cb[i].getTotal()))
    
    def onChange(self, event):
        row = event.GetRow()
        col = event.GetCol()
        if col == 0:
            date = self.grid.GetCellValue(row, col)
            self.cb[row].setDate(date)
        elif col == 1:
            expense = int(self.grid.GetCellValue(row, col))
            self.cb[row].setExpense(expense)
            if row == 0:
                self.cb[row].setTotal(expense)
                for i in range(row + 1, self.grid.GetNumberRows()):
                    self.cb[i].setTotal(self.cb[i - 1].getTotal() + self.cb[i].getExpense())
            else:
                self.cb[row].setTotal(int(self.cb[row - 1].getTotal()) + expense)
                for i in range(row + 1, self.grid.GetNumberRows()):
                    self.cb[i].setTotal(self.cb[i - 1].getTotal() + self.cb[i].getExpense())
            for i in range(row, self.grid.GetNumberRows()):
                self.grid.SetCellValue(i, 3, str(self.cb[i].getTotal()))
        elif col == 2:
            comment = self.grid.GetCellValue(row, col)
            self.cb[row].setComment(comment)
        self.cb.isSaved = False

    def onOpen(self, event):
        self.cb.isFromFile = True
        dlg = wx.FileDialog(self, 'Open', '', '', '*.txt', wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            fileName = dlg.GetFilename()
            dir = dlg.GetDirectory()
            filePath = os.path.join(dir, fileName)
            with open(filePath, 'r') as f:
                lines = f.readlines()
            for i in lines:
                l = i.split('\n')[0].split('+++')
                expense = l[0]
                comment = l[1]
                total = l[2]
                ent = Entry()
                ent.setExpense(expense)
                ent.setComment(comment)
                ent.setTotal(total)
                self.cb.appendEntry(ent)
            self.grid.AppendRows(len(self.cb))
            self.grid.SetCellValue(0, 0, fileName.rstrip('.txt'))
            self.onShow(self.cb)

    def onSave(self, event):
        if not self.cb.isFromFile:
            fileName = str(datetime.now()).split()[0] + '.txt'
            with open(fileName, 'w') as f:
                for i in range(len(self.cb)):
                    f.write(str(self.cb[i].getExpense()) + \
                            '+++' + self.cb[i].getComment() + \
                            '+++' + str(self.cb[i].getTotal()) + '\n')
        else:
            fileName = self.grid.GetCellValue(0, 0) + '.txt'
            with open(fileName, 'w') as f:
                for i in range(len(self.cb)):
                    f.write(str(self.cb[i].getExpense()) + \
                            '+++' + self.cb[i].getComment() + \
                            '+++' + str(self.cb[i].getTotal()) + '\n')
        self.cb.isSaved = True

    def onClose(self, event):
        if self.cb.isSaved == True:
            self.grid.DeleteRows(0, self.grid.GetNumberRows())
            self.cb = Cashbook()
        else:
            dlg = wx.MessageDialog(self, 'Do you want to save the current file?', 'Close File', wx.YES_NO|wx.CANCEL)
            if dlg.ShowModal() == wx.ID_CANCEL:
                pass
            elif dlg.ShowModal() == wx.ID_YES:
                self.onSave()
                self.grid.DeleteRows(0, self.grid.GetNumberRows())
                self.cb = Cashbook()
            else:
                self.grid.DeleteRows(0, self.grid.GetNumberRows())
                self.cb = Cashbook()
            dlg.Destroy()

    def onExit(self, event):
        self.Close()

    def onNew(self, event):
        self.grid.AppendRows()
        self.cb.appendEntry(Entry())

    def onDelete(self, event):
        row = self.grid.GetGridCursorRow()
        if row < 0: return
        dlg = wx.MessageDialog(self, 'Are you sure to delete entry %d?' % row, 'Delete Entry', wx.YES_NO)
        if dlg.ShowModal() == wx.ID_YES:
            expense = int(self.cb[row].getExpense())
            for i in range(row + 1, self.grid.GetNumberRows()):
                self.cb[i].setTotal(int(self.cb[i].getTotal()) - expense)
            self.grid.DeleteRows(row)
            del self.cb[row]
            self.onShow(self.cb)
        dlg.Destroy()

    def onAbout(self, event):
        aboutString = 'This is Qionger\'s Cashbook written by little fur fur using lovely Python'
        dlg = wx.MessageDialog(self, aboutString, 'Qionger\'s Cashbook', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def onHelp(self, event):
        wx.LaunchDefaultBrowser('https://github.com/JasonSun/Misc/tree/master/CashBook')

class Cashbook:
    def __init__(self):
        self.entries = []
        self.isFromFile = False
        self.isSaved = False

    def __getitem__(self,i):
        return self.entries[i]
    
    def __delitem__(self, i):
        del self.entries[i]

    def __len__(self):
        return len(self.entries)

    def appendEntry(self, entry):
        self.entries.append(entry)

class Entry:
    def __init__(self):
        self.date = ''
        self.expense = 0
        self.comment = ''
        # entry.total means total expense as far
        self.total = 0

    def setDate(self, date):
        self.date = date

    def setExpense(self, expense):
        self.expense = expense

    def setComment(self, comment):
        self.comment = comment

    def setTotal(self, total):
        self.total = total
    
    def getComment(self):
        return self.comment

    def getExpense(self):
        return self.expense

    def getTotal(self):
        return self.total

if __name__ == '__main__':
    app = wx.App()
    frame = CashbookFrame(None, wx.ID_ANY, "Qionger's Cashbook")
    frame.Show()
    app.MainLoop()
