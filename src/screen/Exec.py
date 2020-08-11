'''
Created on 2020/08/06

@author: am
'''

import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from model.FileMove import fileMove
from idlelib.idle_test.test_configdialog import root


def setDir(entry):
    dirPath = os.path.abspath(os.path.dirname(__file__))
    Path = filedialog.askdirectory(initialdir=dirPath)
    entry.set(Path)



def main():
    root = Tk()
    root.title("ファイル格納アプリ")

    frameOfFrom = ttk.Frame(root, padding=10)
    frameOfFrom.grid()

    # 「フォルダ参照」ラベルの作成
    Label1 = ttk.Label(frameOfFrom, text="検索元フォルダ：", padding=(5, 2))
    Label1.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry1 = StringVar()
    Entry1 = ttk.Entry(frameOfFrom, textvariable=entry1, width=100)
    Entry1.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    Button1 = ttk.Button(frameOfFrom, text="参照", command=lambda:setDir(entry1))
    Button1.pack(side=LEFT)

    searchWardFrame = ttk.Frame(root, padding=10)
    searchWardFrame.grid(sticky="w")

    Label2 = ttk.Label(searchWardFrame, text="検索用ワード ：", padding=(5, 2))
    Label2.pack(side=LEFT)

    entry2 = StringVar()
    Entry2 = ttk.Entry(searchWardFrame, textvariable=entry2, width=100)
    Entry2.pack(side=LEFT)

    frameOfTo = ttk.Frame(root, padding=10)
    frameOfTo.grid()

    # 「フォルダ参照」ラベルの作成
    Label3 = ttk.Label(frameOfTo, text="移動先フォルダ：", padding=(5, 2))
    Label3.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry3 = StringVar()
    Entry3 = ttk.Entry(frameOfTo, textvariable=entry3, width=100)
    Entry3.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    Button3 = ttk.Button(frameOfTo, text="参照", command=lambda:setDir(entry3))
    Button3.pack(side=LEFT)

    cBoxFrame = ttk.Frame(root, padding=10)
    cBoxFrame.grid(sticky="w")

    mCheck = IntVar()
    mergeCheck = ttk.Checkbutton(cBoxFrame, text="移動先に検索ワードでフォルダを作成しますか？",variable=mCheck)
    mergeCheck.pack()

    actionFrame = ttk.Frame(root, padding=10)
    actionFrame.grid()

    execButton = ttk.Button(actionFrame, text="実行", command=lambda:fileMove(entry1.get(), entry2.get(), entry3.get(),mCheck.get()))
    execButton.pack()

    root.mainloop()


if __name__ == '__main__':
    main()


