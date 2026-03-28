import tkinter as tk
from tkinter import filedialog, messagebox
#main window code
root = tk.Tk()
root.title("simple text editor")
root.geometry("800x600")

#create a text area
text= tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica",18)
)
text.pack(expand=True,fill=tk.BOTH)
 
#main logic start now
#Function 1 to create a new file  
def new_file():
    text.delete(1.0,tk.END)

#function2 to open a new file 
def open_file():
   #open a file dialog to select a file 
    file_path = filedialog.askopenfilename(
       defaultextension=".txt",
       filetypes=[("Text Files","*.txt")]
    ) 

    if file_path:
       #open selected file 
       with open(file_path,"r")as file:
              text.delete(1.0,tk.END)
              text.insert(tk.END,file.read())
#function 3 to save a file 
def save_file():
     #open aa file dialog to select a file 
    file_path=filedialog.asksaveasfilename(
          defaultextension=".txt",
            filetypes=[("Text Files","*.txt")]
    )
    if file_path:
          with open(file_path,"w")as file:
               file.write(text.get(1.0,tk.END))
          messagebox.showinfo("Info","File saved successfully")

#menu

menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)

#new file , open , save , exit
menu.add_cascade(label="File",menu=file_menu)


file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="open",command=open_file)
file_menu.add_command(label="save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)


#start and keep the windoe open 
root.mainloop()
