from tkinter import *
root=Tk()
root.title("Train Route")
root.minsize(400,600)
root.maxsize(400,600)
root.configure(background="#00a65a")

label1=Label(root,text="Train Route",bg="#00a65a",fg="#fff")
label1.configure(font=("Constantia",22,"bold"))
label1.pack(pady=(30,10))

trainNo=Entry(root)
trainNo.pack(ipadx=40,ipady=5)

click=Button(root,text="Fetch Station",bg="#fff",fg="#000",width=15,height=2)
click.configure(font=("Constantia",10))
click.pack(pady=(10,20))

result=Label(root,text="",bg="#00a65a",fg="#fff")
result.configure(font=("Constantia",14))
result.pack(pady=(5,10))

root.mainloop()
