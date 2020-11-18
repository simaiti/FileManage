'''
Created on 2020/08/06

@author: am
'''

import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from model.FileMove import moveCheck



def setDir(entry):
    dirPath = os.path.abspath(os.path.dirname(__file__))
    Path = filedialog.askdirectory(initialdir=dirPath)
    entry.set(Path)


def setFile(sl):
    dirPath = os.path.abspath(os.path.dirname(__file__))
    filetype = [("テキスト","*.txt")]
    Path = filedialog.askopenfilename(filetypes = filetype)
    sl.set(Path)


def changeStatus(arg,arg2,slButton):
    if str(arg["state"]) == "normal":
        print("change dis")
        arg["state"] ="disabled"
        arg2["state"] ="normal"
        slButton["state"] ="normal"
    else:
        print("change normal")
        arg["state"] ="normal"
        arg2["state"] ="disabled"
        slButton["state"] ="disabled"


def main():
    root = Tk()
    root.title("ファイル格納アプリ")

    frameOfFrom = ttk.Frame(root, padding=10)
    frameOfFrom.grid()

    # 「フォルダ参照」ラベルの作成
    Label1 = ttk.Label(frameOfFrom, text="検索元フォルダ：", width=14, padding=(5, 2))
    Label1.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry1 = StringVar()
    Entry1 = ttk.Entry(frameOfFrom, textvariable=entry1, width=100)
    Entry1.pack(fill="x", side=LEFT)

    # 「フォルダ参照」ボタンの作成
    Button1 = ttk.Button(frameOfFrom, text="参照", command=lambda:setDir(entry1))
    Button1.pack(side=LEFT)

    searchWardFrame = ttk.Frame(root, padding=10)
    searchWardFrame.grid(sticky="w")

    swLabel = ttk.Label(searchWardFrame, text="検索用ワード ：", width=14, padding=(5, 2))
    swLabel.pack(side=LEFT)

    swEntry = StringVar()
    Entry2 = ttk.Entry(searchWardFrame, textvariable=swEntry, width=100)
    Entry2.pack(fill="x", side=LEFT)

    searchListFrame = ttk.Frame(root, padding=10)
    searchListFrame.grid(sticky="w")

    slLabel = ttk.Label(searchListFrame, text="検索用リスト：", width=14, padding=(5, 2))
    slLabel.pack(side=LEFT)

    sl = StringVar()
    slEntry = ttk.Entry(searchListFrame, textvariable=sl, width=100,state="disabled")
    slEntry.pack(fill="x", side=LEFT)

    slButton = ttk.Button(searchListFrame,text="参照",command=lambda:setFile(sl),state="disabled")
    slButton.pack(side=LEFT)

    frameOfTo = ttk.Frame(root, padding=10)
    frameOfTo.grid()

    # 「フォルダ参照」ラベルの作成
    Label3 = ttk.Label(frameOfTo, text="移動先フォルダ：", width=14, padding=(5, 2))
    Label3.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry3 = StringVar()
    print(entry3)
    Entry3 = ttk.Entry(frameOfTo, textvariable=entry3, width=100)
    Entry3.pack(fill="x", side=LEFT)

    # 「フォルダ参照」ボタンの作成
    Button3 = ttk.Button(frameOfTo, text="参照", command=lambda:setDir(entry3))
    Button3.pack(side=LEFT)

    listCheckBoxFrame = ttk.Frame(root, padding=10)
    listCheckBoxFrame.grid(sticky="w")

    lcBox = IntVar()
    listUseCheck = ttk.Checkbutton(listCheckBoxFrame,
                                   text="検索ワードのリストを指定して実行する",
                                   variable=lcBox,
                                   command=lambda:changeStatus(Entry2,slEntry,slButton))
    listUseCheck.pack(side=LEFT)

    mcBoxFrame = ttk.Frame(root, padding=10)
    mcBoxFrame.grid(sticky="w")

    mCheck = IntVar()
    mergeCheck = ttk.Checkbutton(mcBoxFrame, text="移動先に検索ワードでフォルダを作成しますか？", variable=mCheck)
    mergeCheck.pack()

    actionFrame = ttk.Frame(root, padding=10)
    actionFrame.grid()

    execButton = ttk.Button(actionFrame,
                            text="実行",
                            command=lambda:moveCheck(entry1.get(), swEntry.get(), entry3.get(), mCheck.get(),sl.get(),lcBox.get()))
    execButton.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
