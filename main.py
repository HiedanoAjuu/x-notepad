
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as msg
from tkinter.filedialog import asksaveasfilename,askopenfilename
#80,35

family = ['@Fixedsys', '@MS Gothic', '@MS PGothic', '@MS UI Gothic', '@Malgun Gothic', '@Malgun Gothic Semilight', '@Microsoft JhengHei', '@Microsoft JhengHei Light', '@Microsoft JhengHei UI', '@Microsoft JhengHei UI Light', '@Microsoft YaHei UI', '@Microsoft YaHei UI Light', '@MingLiU-ExtB', '@MingLiU_HKSCS-ExtB', '@PMingLiU-ExtB', '@SimSun-ExtB', '@System', '@Terminal', '@Yu Gothic', '@Yu Gothic Light', '@Yu Gothic Medium', '@Yu Gothic UI', '@Yu Gothic UI Light', '@Yu Gothic UI Semibold', '@Yu Gothic UI Semilight', '@仿宋', '@宋体', '@微软雅黑', '@微软雅黑 Light', '@新宋体', '@方正兰亭超细黑简体', '@方正粗黑宋简体', '@楷体', '@等线', '@等线 Light', '@黑体', 'Arabic Transparent', 'Arial', 'Arial Baltic', 'Arial Black', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial Narrow', 'Arial TUR', 'Arvo', 'Bahnschrift', 'Bahnschrift Condensed', 'Bahnschrift Light', 'Bahnschrift Light Condensed', 'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiBold', 'Bahnschrift SemiBold Condensed', 'Bahnschrift SemiBold SemiConden', 'Bahnschrift SemiCondensed', 'Bahnschrift SemiLight', 'Bahnschrift SemiLight Condensed', 'Bahnschrift SemiLight SemiConde', 'Book Antiqua', 'Bookman Old Style', 'Bookshelf Symbol 7', 'Calibri', 'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light', 'Century', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Corbel Light', 'Courier', 'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'Droid Serif', 'Ebrima', 'Fixedsys', 'Franklin Gothic Medium', 'Gabriola', 'Gadugi', 'Garamond', 'Georgia', 'HoloLens MDL2 Assets', 'Impact', 'Indie Flower', 'Ink Free', 'Javanese Text', 'Leelawadee', 'Leelawadee UI', 'Leelawadee UI Semilight', 'Lobster', 'Lucida Console', 'Lucida Sans Unicode', 'MS Gothic', 'MS PGothic', 'MS Reference Sans Serif', 'MS Reference Specialty', 'MS Sans Serif', 'MS Serif', 'MS UI Gothic', 'MV Boli', 'Malgun Gothic', 'Malgun Gothic Semilight', 'Marlett', 'Microsoft Himalaya', 'Microsoft JhengHei', 'Microsoft JhengHei Light', 'Microsoft JhengHei UI', 'Microsoft JhengHei UI Light', 'Microsoft New Tai Lue', 'Microsoft PhagsPa', 'Microsoft Sans Serif', 'Microsoft Tai Le', 'Microsoft Uighur', 'Microsoft YaHei UI', 'Microsoft YaHei UI Light', 'Microsoft Yi Baiti', 'MingLiU-ExtB', 'MingLiU_HKSCS-ExtB', 'Modern', 'Mongolian Baiti', 'Monotype Corsiva', 'Myanmar Text', 'Nirmala UI', 'Nirmala UI Semilight', 'NumberOnly', 'Open Sans', 'PMingLiU-ExtB', 'Palatino Linotype', 'Poiret One', 'Raleway', 'Roboto', 'Roboto Condensed', 'Roboto Slab', 'Roman', 'Script', 'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black', 'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Semilight', 'Segoe UI Symbol', 'SimSun-ExtB', 'Sitka Banner', 'Sitka Display', 'Sitka Heading', 'Sitka Small', 'Sitka Subheading', 'Sitka Text', 'Small Fonts', 'Sylfaen', 'Symbol', 'System', 'Tahoma', 'Terminal', 'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Trebuchet MS', 'Verdana', 'Webdings', 'Wingdings', 'Wingdings 2', 'Wingdings 3', 'Yu Gothic', 'Yu Gothic Light', 'Yu Gothic Medium', 'Yu Gothic UI', 'Yu Gothic UI Light', 'Yu Gothic UI Semibold', 'Yu Gothic UI Semilight', 'icomoon', 'sonicgamer', '仿宋', '宋体', '微软雅黑', '微软雅黑 Light', '新宋体', '方正兰亭超细黑简体', '方正粗黑宋简体', '楷体', '等线', '等线 Light', '黑体']
f_size=[5,6,7,9,10,12,14,15,16,18,22,24,16,36,42,54,63,72]
shape=["normal","bold","Fine","italic","underline"]
font = ("宋体",10,"normal")
font2 = ("宋体",10,"normal")

root=tk.Tk()
file_name="无标题"
text=ScrolledText(root,undo=True)

def save():
    global file_name
    print(file_name)
    if file_name == "无标题":
        save_as()
    else:
        with open(file_name,"a")as output:
            textContent = text.get("1.0",tk.END)
            output.write(textContent)
            root.title(file_name+" - 小向记事本")

def font():
    global root2
    global lst1,lst2,lst3
    global lab
    root2 = tk.Tk()
    root2.geometry("570x540")
    lab1=tk.Label(root2,text="字体:")
    lab1.grid(row=0,column=0)
    lab2=tk.Label(root2,text="字号:")
    lab2.grid(row=0,column=1)
    lab3=tk.Label(root2,text="字形:")
    lab3.grid(row=0,column=2)
    lst1=tk.Listbox(root2)
    lst1.grid(row=1,column=0)
    for i in family:
        lst1.insert(tk.END,i)
    lst2=tk.Listbox(root2)
    lst2.grid(row=1,column=1)
    lst2=tk.Listbox(root2)
    lst2.grid(row=1,column=1)
    for i in f_size:
        lst2.insert(tk.END,i)
    lst3=tk.Listbox(root2)
    lst3.grid(row=1,column=2)
    for i in shape:
        lst3.insert(tk.END,i)
    lab = tk.Label(root2,text="Hello World 你好世界 (实例文本)",font=font2)
    lab.grid(row=2,column=1,pady=50)
    lst1.bind("<Double-Button-1>",show_font)
    lst2.bind("<Double-Button-1>",show_size)
    lst3.bind("<Double-Button-1>",show_shape)
    btn = tk.Button(root2,text="应用",command=save_font)
    btn.grid(row=3,column=1)

    root2.mainloop()
    
def show_shape(orbug):
    global font2
    font2=(font2[0],font2[1],lst3.get(lst3.curselection()))
    lab.config(font=font2)

def show_font(orbug):
    global font2
    font2=(lst1.get(lst1.curselection()),font2[1],font2[2])
    lab.config(font=font2)

def show_size(orbug):
    global font2
    font2=(font2[0],lst2.get(lst2.curselection()),font2[2])
    lab.config(font=font2)    

def save_font():
    global font,font2
    text.configure(font=font2)
    font=font2
    root2.destroy()



    
    
        
def save_as():
    global file_name
    textContent = text.get("1.0",tk.END)
    file_name = asksaveasfilename()
    if file_name == "":
        return
    with open(file_name,"a")as output:
        textContent = text.get("1.0",tk.END)
        output.write(textContent)
        root.title(file_name+" - 小向记事本")

def about_NotePad():
    msg.showinfo("关于“小向记事本”","NotePad \n ©稗田阿柔 保留所有权利 \n 支持格式:.txt等大部分文本文档格式 \n 支持编码: UTF-8")

def shellnew():
    a=msg.askokcancel("小向记事本","确定新建吗？您的窗口将会被清空。")
    if a == True:
        text.delete("1.0",tk.END)
        root.title("无标题 - 小向记事本")
        global file_name
        file_name="无标题"

def Exit():
    a=msg.askokcancel("小向记事本","确定退出吗？您所做的更改将不会被保存。")
    if a == True:
        root.destroy()

def openfile():
    global file_name
    file_name = askopenfilename()
    with open(file_name,"r",encoding="utf-8") as reader:
        txt=reader.read()
    text.delete("1.0",tk.END)
    text.insert(tk.END,txt)
    root.title(file_name+" - 小向记事本")
        
root.geometry("570x540")
root.title(file_name+" - 小向记事本")


menu1 = tk.Menu(root)
filemenu = tk.Menu(menu1)
menu1.add_cascade(label="文件(F)",menu=filemenu,underline=3)
filemenu.add_command(label="新建(N)",command=shellnew,underline=3)
filemenu.add_command(label="打开(O)",command=openfile,underline=3)
filemenu.add_command(label="保存(S)",command=save,underline=3)
filemenu.add_command(label="另存为(A)",command=save_as,underline=4)
filemenu.add_separator()
filemenu.add_command(label="退出(E)",command=Exit,underline=3)
fontmenu = tk.Menu(menu1)
menu1.add_cascade(label="格式(O)",menu=fontmenu,underline=3)
fontmenu.add_command(label="字体(F)",command=font,underline=3)
helpmenu = tk.Menu(menu1)
menu1.add_cascade(label="帮助(H)",menu=helpmenu,underline=3)
helpmenu.add_command(label="关于“小向记事本”(A)",command=about_NotePad,underline=8)
root.config(menu=menu1)
text.pack(fill=tk.BOTH,expand=True)
text.configure(font=font)

root.mainloop()
