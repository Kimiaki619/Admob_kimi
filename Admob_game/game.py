import tkinter

def click_btn():
    pass

root = tkinter.Tk()
root.title("NV変更")
root.resizable(False,False)

canvas = tkinter.Canvas(root,width=800,height=600)
#キャンバスの配置
canvas.pack()
label = tkinter.Label(root,text="??",font=("Times New Roman",36))
label.place(x=360,y=60)
button = tkinter.Button(root,text="imeiは？",font=("Times New Roman",36),command=click_btn)
button.place(x=60, y=60)

root.mainloop()