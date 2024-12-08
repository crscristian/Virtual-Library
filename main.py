from tkinter import *
from tkinter.font import Font
from PIL import ImageTk,Image
import function as f

root = Tk()
root.title("Home")
root.geometry("1900x1060")
root.resizable(width=False, height=False)

bigFont = Font(
    family="Old English Text MT",
    size=60,
    weight="bold",
    slant="roman",
    underline=0,
    overstrike=0)

font_1 = Font(
    family="Impact",
    size=35,
    weight="normal",
    slant="italic",
    underline=0,
    overstrike=0)

#Set a background image
image =ImageTk.PhotoImage(Image.open("Image/book_1.png"))
my_label1 = Label(root,image=image)
my_label1.place(x=0, y=0)

my_label = Label(root, text="The Virtual Library", font=bigFont, fg="black", bg="#fbdaa5")
my_label.place(x=625, y=30)

btn_1 = Button(root, text="Add New Book", font=font_1, fg="black", bg="#ad542c",command=f.add_new_book, activebackground="#ad542c"  )
btn_1.grid(row=12,column=1, pady=(220,0), padx=(780,0), ipadx=30, ipady=5)

btn_2 = Button(root, text="Show Books", font=font_1, fg="black", bg="#ad542c",command=f.show_books_1,width=12, activebackground="#ad542c")
btn_2.grid(row=13,column=1, pady=(30,0), padx=(780,0), ipadx=35, ipady=5)

btn_3 = Button(root, text="Remove Book", font=font_1, fg="black", bg="#ad542c",command=f.delete_book, activebackground="#ad542c")
btn_3.grid(row=14,column=1, pady=(30,0), padx=(780,0), ipadx=30, ipady=5)

btn_4 = Button(root, text="Update Book", font=font_1, fg="black", bg="#ad542c",command=f.update_book,width=12, activebackground="#ad542c")
btn_4.grid(row=15,column=1, pady=(30,0), padx=(780,0), ipadx=35, ipady=5)

root.mainloop()