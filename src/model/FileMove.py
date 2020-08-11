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
from tkinter import scrolledtext
from tkinter.scrolledtext import ScrolledText
from _datetime import datetime

def fileMove(fromDir, searchword, toDir, mergeCheck):

    print(searchword)
    print(mergeCheck)

    if mergeCheck == 1 :
        dstDir = toDir + "/" + searchword
        os.makedirs(dstDir, exist_ok=True)
    else:
        dstDir = toDir

    searchword = fromDir + "/*" + searchword + "*"
    print(searchword)

    moveList = glob.glob(searchword)
    for l in moveList:
        print(l)

    for target in moveList:
        shutil.move(target, dstDir)

    showList(dstDir,moveList)
    writeLog(dstDir, moveList)

def writeLog(dstDir,moveList):
    txtname = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".txt"
    file = open(txtname, "w",  encoding ="UTF-8")
    file.write("ファイル移動先：" + dstDir +"\n")
    file.write("\n")
    for f in moveList:
        file.write(f + "\n")
    file.close

def showList(dstDir,moveList):
    root = Tk()
    root.title("実行結果")

    dstDirFrame = ttk.Frame(root,padding=10)
    dstDirFrame.grid()

    dstDirLabel = ttk.Label(dstDirFrame,text="移動先：")
    dstDirLabel.pack(side=LEFT)

    dstDirLabel2 = ttk.Label(dstDirFrame,text=dstDir)
    dstDirLabel2.pack(side=LEFT)

    listFrame = ttk.Frame(root,padding=10,)
    listFrame.grid()

    listLabel = ttk.Label(listFrame,text="対象ファイル一覧")
    listLabel.pack()

    sc = ScrolledText(listFrame)
    sc.pack()
    num = 1.0
    for p in moveList:
        sc.insert(num,p + "\n")
        num += 1.0
    sc.configure(state="disabled")