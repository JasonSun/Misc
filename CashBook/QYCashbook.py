#!/usr/bin/python

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
        # Cashbook instance
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
        saveItem = self.fileMenu.Append(wx.ID_SAVE, 'Save', 'Save these entries into a file')
        saveasItem = self.fileMenu.Append(wx.ID_SAVEAS, 'Save As', 'Save these entries into a new file')
        exitItem = self.fileMenu.Append(wx.ID_EXIT, 'Exit', 'Exit Cashbook')
        # Bind event handler to event in File menu
        self.Bind(wx.EVT_MENU, self.onSave, saveItem)
        self.Bind(wx.EVT_MENU, self.onSaveas, saveasItem)
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

    def onChange(self, event):
        row = event.GetRow()
        col = event.GetCol()
        entry = self.cb[row]
        if col == 0:
            date = self.grid.GetCellValue(row, col)
            entry.setDate(date)
        elif col == 1:
            expense = int(self.grid.GetCellValue(row, col))
            entry.setExpense(expense)
            if row == 0:
                entry.setTotal(expense)
                for i in range(row + 1, self.grid.GetNumberRows()):
                    self.cb[i].setTotal(self.cb[i - 1].getTotal() + self.cb[i].getExpense())
            else:
                entry.setTotal(self.cb[row - 1].getTotal() + expense)
                for i in range(row + 1, self.grid.GetNumberRows()):
                    self.cb[i].setTotal(self.cb[i - 1].getTotal() + self.cb[i].getExpense())
            for i in range(row, self.grid.GetNumberRows()):
                self.grid.SetCellValue(i, 3, str(self.cb[i].getTotal()))
        elif col == 2:
            comment = self.grid.GetCellValue(row, col)
            entry.setComment(comment)

    def onSave(self, event):
        fileName = str(datetime.now()).split()[0] + '.txt'
        with open(fileName, 'w') as f:
            for i in range(len(self.cb)):
                f.write(str(self.cb[i].getExpense()) + \
                        '+++' + self.cb[i].getComment() + \
                        '+++' + str(self.cb[i].getTotal()) + '\n')

    def onSaveas(self, event):
        pass

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
            expense = self.cb[row].getExpense()
            for i in range(row + 1, self.grid.GetNumberRows()):
                self.cb[i].setTotal(self.cb[i].getTotal() - expense)
                self.grid.SetCellValue(i, 3, str(self.cb[i].getTotal()))
            self.grid.DeleteRows(row)
            del self.cb[row]
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
