import tkinter
import tkinter.messagebox

def main():
    flag = True
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!') if flag  else  ('blue', 'Goodbye, world!')
        lable1.config(text = msg,fg = color)


    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示','确定要取消吗'):
            top.quit()


    top = tkinter.Tk()
    top.geometry('240x160')
    top.title = '小游戏'
    lable1 = tkinter.Label(top,text = 'Hello, world!',font='Arial -32', fg='red')
    lable1.pack(expand=1)
    panel = tkinter.Frame()
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()


if __name__ == '__main__':
    main()
