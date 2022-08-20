import os, tkinter, tkinter.filedialog, tkinter.messagebox
from main import mosaic,color_to_16,draw_mc
#https://shizenkarasuzon.hatenablog.com/entry/2020/03/21/002600
#参考元です!
class MyApp1(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.Button1 = tkinter.Button(self, bg='#000000', fg='#ffffff', width=12, height = 5)
        self.Button1["text"] = "SELECT FILE" #ボタンのテキスト
        self.Button1["command"] = self.Button1_Func #割り込み関数
        self.Button1.pack(side="top")
        
        self.Button2 = tkinter.Button(self, bg='#000000', fg='#ffffff', width=12, height = 5)
        self.Button2["text"] = "RunIN MC"
        self.Button2["command"] = self.Button2_Func
        self.Button2.pack(side="top")

        self.ButtonQuit = tkinter.Button(self, bg='#000000', fg='#ffffff', width=12, height = 5)
        self.ButtonQuit["text"] = "QUIT"
        self.ButtonQuit["command"] = self.QuitApp
        self.ButtonQuit.pack(side="top")
        self.selected_file_path = ""
        self.img16_path = ''
        
    def Button1_Func(self):
        fTyp = [("","*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        self.selected_file_path = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        print(self.selected_file_path)
        self.img16_path = color_to_16(mosaic(self.selected_file_path,0.5))

    def Button2_Func(self):
        if self.img16_path == '':
            print("check the path!!")
        else:
            draw_mc(self.img16_path)
        
    def QuitApp(self):
        print("quit this App")
        self.master.destroy()
        
        
root = tkinter.Tk()
root.geometry("100x260")
app = MyApp1(master=root)
app.mainloop()