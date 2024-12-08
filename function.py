import tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import sqlite3

def add_new_book():
    root = tkinter.Toplevel()
    root.title("Add New Book")
    root.geometry("900x628")
    root.resizable(width=False, height=False)
    label_color = "#c9c6c1"
    # Set a background image
    image = ImageTk.PhotoImage(file = "Image/book.png")
    my_label1 = Label(root, image=image)
    my_label1.place(x=0,y=0)
    bigFont = 'Arial 20'

    # Create Text Boxes
    n_carte = Entry(root, width=30, font=bigFont)
    n_carte.grid(row=0, column=1, padx=(0,0),pady=(30,0))
    n_autor = Entry(root, width=30, font=bigFont)
    n_autor.grid(row=1, column=1, padx=(0,0),pady=(30,0))
    an_aparitie = Entry(root, width=30, font=bigFont)
    an_aparitie.grid(row=2, column=1, padx=(0,0),pady=(30,0))
    editura = Entry(root, width=30, font=bigFont)
    editura.grid(row=3, column=1, padx=(0,0),pady=(30,0))
    tip_carte = Entry(root, width=30, font=bigFont)
    tip_carte.grid(row=4, column=1, padx=(0,0),pady=(30,0))
    cod_carte = Entry(root, width=30, font=bigFont)
    cod_carte.grid(row=5, column=1, padx=(0,0),pady=(30,0))
    # Create Text Labels
    n_carte_label = Label(root, text="Nume Carte:", font= bigFont,background=label_color)
    n_carte_label.grid(row=0, column=0, pady=(30, 0),padx=(50,10), ipadx=20)
    n_autor_label = Label(root, text="Nume Autor:", font=bigFont,background=label_color)
    n_autor_label.grid(row=1, column=0, pady=(30, 0),padx=(50,10), ipadx=20)
    an_aparitie_label = Label(root, text="An Aparitie:", font=bigFont,background=label_color)
    an_aparitie_label.grid(row=2, column=0, pady=(30, 0),padx=(50,10), ipadx=20)
    editura_label = Label(root, text="Editura:", font=bigFont,background=label_color)
    editura_label.grid(row=3, column=0, pady=(30, 0),padx=(50,10), ipadx=30)
    tip_carte_label = Label(root, text="Tip Carte:", font=bigFont,background=label_color)
    tip_carte_label.grid(row=4, column=0, pady=(30, 0),padx=(50,10), ipadx=20)
    cod_carte_label = Label(root, text="Cod Carte:", font=bigFont,background=label_color)
    cod_carte_label.grid(row=5, column=0, pady=(30, 0),padx=(50,10), ipadx=20)

    def submit():
        # Create a datebase or connect to one
        conn = sqlite3.connect('book.db')
        # Create cursor
        c = conn.cursor()

        # Insert into table
        c.execute("INSERT INTO adresses VALUES(:n_carte, :n_autor, :an_aparitie, :editura, :tip_carte, :cod_carte)",
                  {
                      'n_carte': n_carte.get(),
                      'n_autor': n_autor.get(),
                      'an_aparitie': an_aparitie.get(),
                      'editura': editura.get(),
                      'tip_carte': tip_carte.get(),
                      'cod_carte': cod_carte.get()
                  })

        # Commit Change
        conn.commit()

        # Close conection
        conn.close()
        # Create the clear the tesc boxes
        n_carte.delete(0, END)
        n_autor.delete(0, END)
        an_aparitie.delete(0, END)
        editura.delete(0, END)
        tip_carte.delete(0, END)
        cod_carte.delete(0, END)



    #Create Submit Button
    submit_btn = Button(root, text="Add New Book", font='Arial 16', command=submit,background='#965c32',activebackground='#965c32')
    submit_btn.grid(row=12,column=1, pady=(50,0), padx=(0,0), ipadx=70, ipady=5)
    root.mainloop()

def show_books():
    root = tkinter.Toplevel()
    root.title("Show Records")
    root.geometry("900x628")
    root.resizable(width=False, height=False)
    # Create a datebase or connect to one
    conn = sqlite3.connect('book.db')
    # Create cursor
    c = conn.cursor()

    #Query the datebase
    c.execute("SELECT *, oid FROM adresses")
    records = c.fetchall()
    #print(records)
    i = -1
    #Loop Thru Results
    print_records = ''
    for record in records:
        print_records += str(record[6])+"   "+str(record[0])+"   "+str(record[1])+"   "+str(record[2])+"    "+str(record[3])+"   "+str(record[4])+"   "+str(record[5])+"   "+"\n"
        i = i + 1

    query_label = Label(root, text=print_records,justify="left", font='Arial 20')
    query_label.grid(row=0, column=0, columnspan=2,pady=19,padx=10)


    # Commit Change
    conn.commit()

    # Close conection
    conn.close()
    root.mainloop()

#show_books()-can use for other things

def show_books_1():
    root = tkinter.Toplevel()
    root.title("Show Records")
    root.geometry("1086x264")
    root.resizable(width=False, height=False)
    # Set a background image
    image = ImageTk.PhotoImage(file="Image/balerion.png")
    my_label1 = Label(root, image=image)
    my_label1.place(x=0, y=0)
    # Create a datebase or connect to one
    conn = sqlite3.connect('book.db')
    # Create cursor
    c = conn.cursor()
    # Using treeview widget
    trv = ttk.Treeview(root, selectmode='browse')

    trv.grid(row=1, column=1, padx=20, pady=20)
    # number of columns
    trv["columns"] = ("1", "2", "3", "4", "5","6","7")

    # Defining heading
    trv['show'] = 'headings'

    # width of columns and alignment
    trv.column("1", width=30, anchor='c')
    trv.column("2", width=220, anchor='w')
    trv.column("3", width=220, anchor='w')
    trv.column("4", width=70, anchor='c')
    trv.column("5", width=220, anchor='w')
    trv.column("6", width=220, anchor='w')
    trv.column("7", width=70, anchor='c')

    # Headings
    # respective columns
    trv.heading("1", text="id")
    trv.heading("2", text="Nume_carte")
    trv.heading("3", text="Nume_autor")
    trv.heading("4", text="An_aparitie")
    trv.heading("5", text="Editura")
    trv.heading("6", text="Tip_carte")
    trv.heading("7", text="Cod_carte")
    #Query the datebase
    c.execute("SELECT *, oid FROM adresses")
    records = c.fetchall()
    #print(records)
    #Loop Thru Results
    print_records = ''
    for dt in records:
        trv.insert("", 'end', iid=dt[0], text=dt[0],
                   values=(dt[6], dt[0], dt[1], dt[2], dt[3],dt[4], dt[5]))
    # Commit Change
    conn.commit()

    # Close conection
    conn.close()
    root.mainloop()

def delete_book():
    def delete():
        # Create a datebase or connect to one
        conn = sqlite3.connect('book.db')
        # Create cursor
        c = conn.cursor()

        # Delete a record
        #c.execute("DELETE from adresses WHERE cod_carte =" + delete_box.get()) #se elimina cartea folosind codul cartii
        c.execute("DELETE from adresses WHERE oid =" + delete_box.get())
        delete_box.delete(0, END)
        # Commit Change
        conn.commit()
        # Close conection
        conn.close()

    root = tkinter.Toplevel()
    root.title("Delete Book")
    root.geometry("550x300")
    root.resizable(width=False, height=False)
    # Set a background image
    image = ImageTk.PhotoImage(file="Image/delete_record.png")
    my_label1 = Label(root, image=image)
    my_label1.place(x=0, y=0)
    bigFont = 'Arial 18'
    #Create text Boxes
    delete_box=Entry(root, width=15,font="Arial 16")
    delete_box.grid(row=0,column=1, pady=(80,0), padx=(10,0), ipadx=10, ipady=5)
    #Create Text Label
    delete_box_label = Label(root, text="ID Book:",font=bigFont,background="#854D3E")
    delete_box_label.grid(row=0,column=0,pady=(80,0), padx=(90,0), ipadx=20, ipady=2)
    # Create a Delete Button
    delete_btn = Button(root, text="Remove Book", command=delete, font="Arial 16", background="#714C43",activebackground="#714C43")
    delete_btn.grid(ipadx=30, ipady=2)
    delete_btn.place(x=195, y=150)
    root.mainloop()

def update_book():
    root = tkinter.Toplevel()
    root.title("Update Info Book")
    root.geometry("550x300")
    root.resizable(width=False, height=False)
    # Set a background image
    image = ImageTk.PhotoImage(file="Image/delete_record.png")
    my_label1 = Label(root, image=image)
    my_label1.place(x=0, y=0)
    bigFont = 'Arial 18'

    def edit():
        global editor
        global n_carte_editor
        global n_autor_editor
        global an_aparitie_editor
        global editura_editor
        global tip_carte_editor
        global cod_carte_editor
        editor = Tk()
        editor.title("Update Book")
        editor.geometry("800x600")
        editor.resizable(width=False, height=False)
        label_color = "#c9c6c1"

        # Create a datebase or connect to one
        conn = sqlite3.connect('book.db')
        # Create cursor
        c = conn.cursor()

        record_id = delete_box.get()
        # Query the datebase
        c.execute("SELECT * FROM adresses WHERE oid=" + record_id)
        records = c.fetchall()

        # Create Global Variables for text box names
        n_carte_editor = Entry(editor, width=30, font=bigFont)
        n_carte_editor.grid(row=0, column=1, padx=(0, 0), pady=(30, 0))
        n_autor_editor = Entry(editor, width=30, font=bigFont)
        n_autor_editor.grid(row=1, column=1, padx=(0, 0), pady=(30, 0))
        an_aparitie_editor = Entry(editor, width=30, font=bigFont)
        an_aparitie_editor.grid(row=2, column=1, padx=(0, 0), pady=(30, 0))
        editura_editor = Entry(editor, width=30, font=bigFont)
        editura_editor.grid(row=3, column=1, padx=(0, 0), pady=(30, 0))
        tip_carte_editor= Entry(editor, width=30, font=bigFont)
        tip_carte_editor.grid(row=4, column=1, padx=(0, 0), pady=(30, 0))
        cod_carte_editor = Entry(editor, width=30, font=bigFont)
        cod_carte_editor.grid(row=5, column=1, padx=(0, 0), pady=(30, 0))
        # Create Text Labels
        n_carte_label = Label(editor, text="Nume Carte:", font=bigFont, background=label_color)
        n_carte_label.grid(row=0, column=0, pady=(30, 0), padx=(50, 10), ipadx=20)
        n_autor_label = Label(editor, text="Nume Autor:", font=bigFont, background=label_color)
        n_autor_label.grid(row=1, column=0, pady=(30, 0), padx=(50, 10), ipadx=20)
        an_aparitie_label = Label(editor, text="An Aparitie:", font=bigFont, background=label_color)
        an_aparitie_label.grid(row=2, column=0, pady=(30, 0), padx=(50, 10), ipadx=20)
        editura_label = Label(editor, text="Editura:", font=bigFont, background=label_color)
        editura_label.grid(row=3, column=0, pady=(30, 0), padx=(50, 10), ipadx=30)
        tip_carte_label = Label(editor, text="Tip Carte:", font=bigFont, background=label_color)
        tip_carte_label.grid(row=4, column=0, pady=(30, 0), padx=(50, 10), ipadx=20)
        cod_carte_label = Label(editor, text="Cod Carte:", font=bigFont, background=label_color)
        cod_carte_label.grid(row=5, column=0, pady=(30, 0), padx=(50, 10), ipadx=20)

        # loop thrus results
        for record in records:
            n_carte_editor.insert(0, record[0])
            n_autor_editor.insert(0, record[1])
            an_aparitie_editor.insert(0, record[2])
            editura_editor.insert(0, record[3])
            tip_carte_editor.insert(0, record[4])
            cod_carte_editor.insert(0, record[5])

        # Create a Save Edit Button
        save_btn = Button(editor, text="Save Edit ", command=update,font="Arial 16", background="#714C43",width=20,activebackground="#714C43")
        save_btn.grid( ipadx=30, ipady=2)
        save_btn.place(x=250,y=440)
        editor.mainloop()

    def update():
        # Create a datebase or connect to one
        conn = sqlite3.connect('book.db')
        # Create cursor
        c = conn.cursor()

        record_id = delete_box.get()
        delete_box.delete(0, END)
        c.execute(""" UPDATE adresses SET 
            nume_carte = :carte,
            nume_autor = :autor,
            an_aparitie = :aparitie,
            editura = :editura,
            tip_carte = :tip,
            cod_carte = :cod

            WHERE oid = :oid""",
                  {'carte': n_carte_editor.get(),
                   'autor': n_autor_editor.get(),
                   'aparitie': an_aparitie_editor.get(),
                   'editura': editura_editor.get(),
                   'tip': tip_carte_editor.get(),
                   'cod': cod_carte_editor.get(),
                   'oid': record_id
                   })
        # Commit Change
        conn.commit()
        # Close conection
        conn.close()


    #Create text Boxes
    delete_box=Entry(root, width=15,font="Arial 16")
    delete_box.grid(row=0,column=1, pady=(80,0), padx=(10,0), ipadx=10, ipady=5)
    #Create Text Label
    update_box_label = Label(root, text="Cod Book:",font=bigFont,background="#854D3E")
    update_box_label.grid(row=0,column=0,pady=(80,0), padx=(90,0), ipadx=20, ipady=2)
    # Create a Delete Button
    update_btn = Button(root, text="Update Book", command=edit, font="Arial 16", background="#714C43",activebackground="#714C43")
    update_btn.grid(ipadx=30, ipady=2)
    update_btn.place(x=195, y=150)



    root.mainloop()


'''
#Create a datebase or connect to one
conn = sqlite3.connect('book.db')
# Create cursor
c = conn.cursor()
#Create table
c.execute("""CREATE TABLE adresses(
            nume_carte text,
            nume_autor  text,
            an_aparitie text,
            editura text,
            tip_carte text, 
            cod_carte integer
)""")
'''

