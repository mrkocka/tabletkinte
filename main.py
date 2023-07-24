import tkinter as tk
from tkinter import ttk
import csv

def load_data(file):
    with open(file, "r") as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return data

def create_table(data, root):
    table = ttk.Treeview(root)
    table['columns'] = ('Név', 'Kor', 'Telefonszám', 'E-mail')
    table['show'] = 'headings'

    for column in table['columns']:
        table.heading(column, text=column) # let the column heading = column name

    for row in data:
        table.insert('', 'end', values=row) # insert each row

    table.pack()
    return table

root = tk.Tk()

data = load_data('./proba.csv') # replace with your filename
table = create_table(data, root)

root.mainloop()

