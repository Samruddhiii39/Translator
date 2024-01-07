from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type",source="English",destination="Hindi"):
    text1 = text
    src = source
    dest = destination
    trans = Translator()
    trans1 =trans.translate(text,source=src,destination=dest)
    return trans1.text

def data():
    sou = combo1.get()
    des = combo2.get()
    message = sorce_txt.get(1.0,END)
    get_text =change(text=message,source=sou,destination=des)
    trans_txt.delete(1.0,END)
    trans_txt.insert(END,get_text)

window = Tk()
window.title("TRANSLATOR")
window.geometry("700x700")
window.config(bg='Green')

text_lab = Label(window,text="TRANSLATOR",font=("Calligrapher",30,"bold"))
text_lab.place(x=200,y=30,height=70,width=300)

frame_1 = Frame(window).pack(side=BOTTOM)

text_lab = Label(window,text="SOURCE",font=("Calligrapher",15,"bold"))
text_lab.place(x=200,y=110,height=25,width=300)

sorce_txt = Text(frame_1,font=("Calligrapher",15,"bold"),wrap=WORD)
sorce_txt.place(x=20,y=145,height=200,width=650)

list_txt = list(LANGUAGES.values())

combo1 = ttk.Combobox(frame_1,value=list_txt)
combo1.place(x=20,y=370,height=45,width=200)
combo1.set("Engilsh")

button = Button(frame_1,text="Translate",relief=RAISED,command=data)
button.place(x=260,y=370,height=45,width=200)

combo2 = ttk.Combobox(frame_1,value=list_txt)
combo2.place(x=490,y=370,height=45,width=200)
combo2.set("Engilsh")

trans_txt = Text(frame_1,font=("Calligrapher",15,"bold"),wrap=WORD)
trans_txt.place(x=20,y=480,height=200,width=650)

text_lab = Label(window,text="DESTINATION",font=("Calligrapher",15,"bold"))
text_lab.place(x=200,y=440,height=25,width=300)

window.mainloop()