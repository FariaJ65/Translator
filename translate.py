from fnmatch import translate
from tkinter import *
from tkinter import ttk,messagebox
import googletrans 
from googletrans import Translator


root=Tk()
root.title("Google Translate")
root.geometry("1080x400")
root.resizable(False,False)
root.configure(bg="white")
#icon
root.iconbitmap("trans.ico")


def label_change():
    c1=combo1.get()
    c2=combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000,label_change)

def translate_now():
    text_=text1.get(1.0,END)
    t1=Translator()
    trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
    trans_text=trans_text.text

    text2.delete(1.0,END)
    text2.insert(END,trans_text)


#image
mid_image = PhotoImage(file="C:/Users/ahnaf/Documents/Pycharm Projects/Translator/trans2.png")
image_label=Label(root,image=mid_image,width=150)
image_label.place(x=460,y=50)



language = googletrans.LANGUAGES
languageV= list(language.values())
lang1=language.keys()


#first Text Box
combo1=ttk.Combobox(root ,values=languageV ,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("English")

label1=Label(root,text="English",font="segoe 30 bold",bg="white",width=18,bd=5 ,relief=GROOVE)
label1.place(x=10,y=50)

# first text box frame
f1=Frame(root,bg="Black",bd=5)
f1.place(x=10,y=118,width=440,height=210)

text1=Text(f1,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)


scrolibar1=Scrollbar(f1)
scrolibar1.pack(side="right",fill="y")

scrolibar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrolibar1.set)


# 2nd Text Box
combo2=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo2.place(x=730,y=20)
combo2.set("select your language")

label2=Label(root,text="English",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

# 2nd text box frame
f2=Frame(root,bg="Black",bd=5)
f2.place(x=620,y=118,width=440,height=210)

text2=Text(f2,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)


scrolibar2=Scrollbar(f2)
scrolibar2.pack(side="right",fill="y")

scrolibar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrolibar2.set)


#translate_button
translate=Button(root,text="Translate",font=("Roboto",15),
                activebackground="lightblue",cursor="hand2",bd=1,width=10,height=2,
                bg="lightgreen",fg="white",command= translate_now)
translate.place(x=480,y=250)                

label_change()

root.mainloop()