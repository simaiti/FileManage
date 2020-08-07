'''
Created on 2020/08/06

@author: am
'''

import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

def setDir(entry):
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    entry.set(iDirPath)
    pass

def main():
    root = Tk()
    root.title("ファイル格納アプリ")

    frame1 = ttk.Frame(root,padding=10)
    frame1.grid()

    # 「フォルダ参照」ラベルの作成
    IDirLabel1 = ttk.Label(frame1, text="フォルダ参照＞＞", padding=(5, 2))
    IDirLabel1.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry1 = StringVar()
    IDirEntry1 = ttk.Entry(frame1, textvariable=entry1, width=30)
    IDirEntry1.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    IDirButton1 = ttk.Button(frame1, text="参照", command=setDir(entry1))
    IDirButton1.pack(side=LEFT)


    frame2 = ttk.Frame(root,padding=10)
    frame2.grid()

    # 「フォルダ参照」ラベルの作成
    IDirLabel2= ttk.Label(frame2, text="フォルダ参照＞＞", padding=(5, 2))
    IDirLabel2.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry2 = StringVar()
    IDirEntry2 = ttk.Entry(frame2, textvariable=entry2, width=30)
    IDirEntry2.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    IDirButton2 = ttk.Button(frame2, text="参照", command=setDir(entry2))
    IDirButton2.pack(side=LEFT)

    root.mainloop()
    pass


if __name__ == '__main__':
    main()