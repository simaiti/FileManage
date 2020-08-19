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

def fileMove(fromDir, searchward, toDir, mergeCheck):

    print(fromDir)
    print(searchward)
    print(mergeCheck)
    print(toDir)

    if fromDir == "":
        outError(0)
        return

    if toDir == "":
        outError(2)
        return

    if searchward == "":
        if outError(1) == "no":
            return

    if mergeCheck == 1 :
        dstDir = toDir + "/" + searchward
        os.makedirs(dstDir, exist_ok=True)
    else:
        dstDir = toDir

    searchward = fromDir + "/*" + searchward + "*"
    print(searchward)

    moveList = glob.glob(searchward)
    for l in moveList:
        print(l)

    for target in moveList:
        shutil.move(target, dstDir)

    showList(dstDir,moveList)
    writeLog(dstDir, moveList)

def outError(code):
    if code == 0:
        messagebox.showwarning("エラー", "検索元フォルダが指定されていません")
    elif code == 1:
        return messagebox.askquestion("実行前確認", "検索ワードが指定されていない為、移動元フォルダ内をすべて移動してもよろしいですか？")
    elif code == 2:
        messagebox.showwarning("エラー", "移動先フォルダが指定されていません")

def writeLog(searchward,dstDir,moveList):
    txtname = searchward + datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f') + ".txt"
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