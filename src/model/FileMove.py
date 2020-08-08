'''
Created on 2020/08/08

@author: am
'''

import os, glob
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Treeview

def fileMove(fromDir, searchward, toDir, mergeCheck):

    print(searchward)
    print(mergeCheck)

    if mergeCheck == 1 :
        dstDir = toDir + "/" + searchward
        os.makedirs(dstDir, exist_ok=True)
    else:
        dstDir = toDir

    seachward = fromDir + "/*" + searchward + "*"
    print(seachward)

    moveList = glob.glob(seachward)
    for l in moveList:
        print(l)

    for target in moveList:
        shutil.move(target, dstDir)

    showList(dstDir,moveList)

def showList(dstDir,moveList):
    root = Tk()
    root.title("実行結果")

    dstDirFrame = ttk.Frame(root,padding=10)
    dstDirFrame.grid()

    dstDirLabel = ttk.Label(dstDirFrame,text="移動先：")
    dstDirLabel.pack(side=LEFT)

    dstDirLabel2 = ttk.Label(dstDirFrame,text=dstDir)
    dstDirLabel2.pack(side=LEFT)

    listFrame = ttk.Frame(root,padding=10)
    listFrame.grid()

    listLabel = ttk.Label(listFrame,text="対象ファイル一覧")
    listLabel.pack()

    treebox = Treeview(listFrame)
    treebox["show"] = "headings"
    for p in moveList:
        treebox.insert("", "end", values=p)
    treebox.pack()

