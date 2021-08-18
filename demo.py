from tkinter import*

window=Tk()
window.title("Word Search Engine")
window.geometry('500x300')

label1=Label(window,text='Enter Sentence: ',fg='blue',font=('Times New Roman',14))
label1.grid(row=0,column=0,padx=5,pady=10)

sentence = StringVar()

textbox1=Entry(window,textvariable=sentence,fg='blue',font=('Arial',14))
textbox1.grid(row=0,column=1)

label2=Label(window,text='Enter Word: ',fg='blue',font=('Times New Roman',14))
label2.grid(row=1,column=0,padx=5,pady=10)

word = StringVar()

textbox2=Entry(window,textvariable=word,fg='blue',font=('Arial',14))
textbox2.grid(row=1,column=1)

def mySearch():

   # ans = word.get() in sentence.get()
   if word.get() in sentence.get():
        emptylabel.config(text='Word Found')
   else:
       emptylabel.config(text='Word Not Found')     
       
    
    
button1=Button(window,command=mySearch,text='Check',fg='blue',font=('Arial',14))
button1.grid(row=2,column=1,sticky=W)

emptylabel=Label(window,fg='green',font=('Arial',14))
emptylabel.grid(row=3,column=1,sticky=W,pady=10)


window.mainloop()