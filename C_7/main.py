import mysql.connector
import tkinter as tk
import tkinter.ttk as ttk

def connection():
    database = mysql.connector.connect(host="db4free.net", user="z01berg", password="234680234680", database="book_shell")
    return database

def fetch_data():
    db = connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def load_data():
    data = fetch_data()
    treeview.delete(*treeview.get_children())
    for row in data:
        treeview.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))

def add_book():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj nową książkę")

    title_label = ttk.Label(new_window, text="Tytuł:")
    title_label.pack()
    title_entry = ttk.Entry(new_window)
    title_entry.pack()

    author_label = ttk.Label(new_window, text="Autor:")
    author_label.pack()
    author_entry = ttk.Entry(new_window)
    author_entry.pack()

    price_label = ttk.Label(new_window, text="Cena:")
    price_label.pack()
    price_entry = ttk.Entry(new_window)
    price_entry.pack()

    category_label = ttk.Label(new_window, text="Kategoria:")
    category_label.pack()
    category_entry = ttk.Entry(new_window)
    category_entry.pack()

    def add_new():
        new_title = title_entry.get()
        new_author = author_entry.get()
        new_price = price_entry.get()
        new_category = category_entry.get()

        db = connection()
        sql = "INSERT INTO books(title, author, price, category) VALUES (%s, %s, %s, %s)"
        params = (new_title, new_author, new_price, new_category)
        cursor = db.cursor()
        cursor.execute(sql, params)
        db.commit()
        cursor.close()
        db.close()
        load_data()
        new_window.destroy()

    add_button = ttk.Button(new_window, text="Dodaj", command=add_new)
    add_button.pack()

def delete_book():
    selected_item = treeview.focus()
    if selected_item:
        item_values = treeview.item(selected_item)["values"]
        book_id = item_values[0]

        db = connection()
        cursor = db.cursor()
        sql = "DELETE FROM books WHERE id = %s"
        params = (book_id,)
        cursor.execute(sql, params)
        db.commit()
        cursor.close()
        db.close()
        load_data()

def update_book():
    selected_item = treeview.focus()
    if selected_item:
        item_values = treeview.item(selected_item)["values"]
        book_id = item_values[0]

        new_window = tk.Toplevel(root)
        new_window.title("Edytuj książkę")

        title_label = ttk.Label(new_window, text="Tytuł:")
        title_label.pack()
        title_entry = ttk.Entry(new_window)
        title_entry.insert(0, item_values[1])
        title_entry.pack()

        author_label = ttk.Label(new_window, text="Autor:")
        author_label.pack()
        author_entry = ttk.Entry(new_window)
        author_entry.insert(0, item_values[2])
        author_entry.pack()

        price_label = ttk.Label(new_window, text="Cena:")
        price_label.pack()
        price_entry = ttk.Entry(new_window)
        price_entry.insert(0, item_values[3])
        price_entry.pack()

        category_label = ttk.Label(new_window, text="Kategoria:")
        category_label.pack()
        category_entry = ttk.Entry(new_window)
        category_entry.insert(0, item_values[4])
        category_entry.pack()

        def update():
            new_title = title_entry.get()
            new_author = author_entry.get()
            new_price = price_entry.get()
            new_category = category_entry.get()

            db = connection()
            sql = "UPDATE books SET title=%s, author=%s, price=%s, category=%s WHERE id=%s"
            params = (new_title, new_author, new_price, new_category, book_id)
            cursor = db.cursor()
            cursor.execute(sql, params)
            db.commit()
            cursor.close()
            db.close()
            load_data()
            new_window.destroy()

        update_button = ttk.Button(new_window, text="Aktualizuj", command=update)
        update_button.pack()

def open_details_window(event):
    selected_item = treeview.focus()
    if selected_item:
        item_values = treeview.item(selected_item)["values"]
        book_id = item_values[0]

        details_window = tk.Toplevel(root)
        details_window.title("Szczegóły")

        index_label = ttk.Label(details_window, text="Id:")
        index_label.pack()
        index_entry = ttk.Entry(details_window)
        index_entry.insert(0, book_id)
        index_entry.config(state="disabled")
        index_entry.pack()

        title_label = ttk.Label(details_window, text="Tytuł:")
        title_label.pack()
        title_entry = ttk.Entry(details_window)
        title_entry.insert(0, item_values[1])
        title_entry.pack()

        author_label = ttk.Label(details_window, text="Autor:")
        author_label.pack()
        author_entry = ttk.Entry(details_window)
        author_entry.insert(0, item_values[2])
        author_entry.pack()

        price_label = ttk.Label(details_window, text="Cena:")
        price_label.pack()
        price_entry = ttk.Entry(details_window)
        price_entry.insert(0, item_values[3])
        price_entry.pack()

        category_label = ttk.Label(details_window, text="Kategoria:")
        category_label.pack()
        category_entry = ttk.Entry(details_window)
        category_entry.insert(0, item_values[4])
        category_entry.pack()

        edit_button = tk.Button(details_window, text="Edytuj", command=update_book)
        delete_button = tk.Button(details_window, text="Usuń", command=delete_book)
        edit_button.pack()
        delete_button.pack()

root = tk.Tk()
root.title("Baza książek")
root.iconbitmap("bookshelf.ico")

treeview = ttk.Treeview(root)
treeview["columns"] = ("id", "title", "author", "price", "category")
treeview.column("#0", width=0)
treeview.heading("id", text="ID")
treeview.heading("title", text="Tytuł")
treeview.heading("author", text="Autor")
treeview.heading("price", text="Cena")
treeview.heading("category", text="Kategoria")
treeview.bind("<Double-1>", open_details_window)
treeview.pack()

add_new_book_button = tk.Button(root, text="Dodaj nową książkę", command=add_book)
add_new_book_button.pack(side="left")

load_data()
root.mainloop()
