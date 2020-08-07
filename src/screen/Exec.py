'''
Created on 2020/08/06

@author: am
'''

import os,sys
from tkinter import *

def setDir():
    pass

def main():
    root = Tk()
    root.title("ファイル格納アプリ")

    frame1 = ttk.Frame(root,padding=10)
    frame1.grid()

    # 「フォルダ参照」ラベルの作成
    IDirLabel = ttk.Label(frame1, text="フォルダ参照＞＞", padding=(5, 2))
    IDirLabel.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry1 = StringVar()
    IDirEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
    IDirEntry.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    IDirButton = ttk.Button(frame1, text="参照", command=setDir())
    IDirButton.pack(side=LEFT)


    frame2 = ttk.Frame(root,padding=10)
    frame2.grid()

    # 「フォルダ参照」ラベルの作成
    IDirLabel = ttk.Label(frame2, text="フォルダ参照＞＞", padding=(5, 2))
    IDirLabel.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry2 = StringVar()
    IDirEntry = ttk.Entry(frame2, textvariable=entry2, width=30)
    IDirEntry.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    IDirButton = ttk.Button(frame2, text="参照", command=setDir())
    IDirButton.pack(side=LEFT)


    pass


if __name__ == '__main__':
    main()