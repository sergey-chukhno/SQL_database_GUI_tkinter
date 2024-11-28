from tkinter import *
from PIL import ImageTk, Image 
import sqlite3

root = Tk()
root.title('Database')
root.iconbitmap('Desktop/Python course/Tkinter_course/tic_tac_toe_icon.py')
root.geometry('600x600')




#On cree le tableau (lignes et colonnes)
# с.execute("""CREATE TABLE addresses(
          # first_name text,
          # last_name text, 
          # address text, 
          # city text, 
          # zip integer)""")

#On cree la fonction submit

def save():

  conn = sqlite3.connect('address_book.db') #On cree une variable de connexion a notre database sqlite.Entre parentheses on ecrit le nom d'une base de donnees qu'on veut creer. Si cette basse de donnees n'existe pas encore, cette commande va la creer et elle sera sauvegardee dans notre dossier actuel. 

  c = conn.cursor() #on cree le curseur

  record_id = delete_box.get()
  c.execute("""UPDATE addresses SET
            first_name = :first,
            last_name = :last, 
            address = :address, 
            city = :city, 
            zip = :zip

            WHERE oid = :oid""",
            {
              'first': first_name.get(),
              'last': last_name.get(), 
              'address': address.get(),
              'city': city.get(),
              'zip': zip.get(), 

              'oid': record_id 
            })



  conn.commit() #Pour sauvegarder les changements qu'on fait dans notre base de donnees

  conn.close() #Pour terminer la connextion a notre base de donnees

  editor.destroy() 

  




#Create Edit function
def update(): 

  global editor
  editor = Tk()
  editor.title('Update a Record')
  editor.iconbitmap('Desktop/Python course/Tkinter_course/tic_tac_toe_icon.py')
  editor.geometry('400x400')

  conn = sqlite3.connect('address_book.db') #On cree une variable de connexion a notre database sqlite.Entre parentheses on ecrit le nom d'une base de donnees qu'on veut creer. Si cette basse de donnees n'existe pas encore, cette commande va la creer et elle sera sauvegardee dans notre dossier actuel. 

  c = conn.cursor() #on cree le curseur

  
  #Create global variables for text box names
  global first_name
  global last_name
  global address
  global city
  global zip




  record_id = delete_box.get()
  #Query the database
  c.execute("SELECT * FROM addresses WHERE oid = " + record_id) 
  records = c.fetchall()


  first_name = Entry(editor, width=30)
  first_name.grid(row=0, column=1, padx=20, pady=(10,0))

  last_name = Entry(editor, width=30)
  last_name.grid(row=1, column=1, padx=20)

  address = Entry(editor, width=30)
  address.grid(row=2, column=1, padx=20)

  city = Entry(editor, width=30)
  city.grid(row=3, column=1, padx=20)

  zip = Entry(editor, width=30)
  zip.grid(row=4, column=1, padx=20)



  #On cree les text box labels
  first_name_label = Label(editor, text='First Name')
  first_name_label.grid(row=0, column=0)

  last_name_label = Label(editor, text='Last Name')
  last_name_label.grid(row=1, column=0)

  address_label = Label(editor, text='Address')
  address_label.grid(row=2, column=0)

  city_label = Label(editor, text='City')
  city_label.grid(row=3, column = 0)

  zip_label = Label(editor, text='Zip code')
  zip_label.grid(row=4, column=0)

  #Loop through results/Inserting the results of the query into the fields so that we can update them
  for record in records: 
    first_name.insert(0, record[0])
    last_name.insert(0, record[1])
    address.insert(0, record[2])
    city.insert(0, record[3])
    zip.insert(0, record[4])


  #Create a Save Button to Save Updated Record
  update_button = Button(editor, text='Save Record', command=save)
  update_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)



def delete():
   
  conn = sqlite3.connect('address_book.db') #On cree une variable de connexion a notre database sqlite.Entre parentheses on ecrit le nom d'une base de donnees qu'on veut creer. Si cette basse de donnees n'existe pas encore, cette commande va la creer et elle sera sauvegardee dans notre dossier actuel. 

  c = conn.cursor() #on cree le curseur

  #Delete a record
  c.execute('DELETE from addresses WHERE oid= ' + delete_box.get())

  conn.commit() #Pour sauvegarder les changements qu'on fait dans notre base de donnees

  conn.close() #Pour terminer la connextion a notre base de donnees 



def submit():

  conn = sqlite3.connect('address_book.db') #On cree une variable de connexion a notre database sqlite.Entre parentheses on ecrit le nom d'une base de donnees qu'on veut creer. Si cette basse de donnees n'existe pas encore, cette commande va la creer et elle sera sauvegardee dans notre dossier actuel. 

  c = conn.cursor() #on cree le curseur

  #Inserer les donnees dans le tableau
  c.execute(
    "INSERT INTO addresses (first_name, last_name, address, city, zip) VALUES (:first_name, :last_name, :address, :city, :zip)",
            {
              'first_name': first_name.get(),
              'last_name': last_name.get(),
              'address': address.get(),
              'city': city.get(),
              'zip': zip.get()
            }
  )

    #Clear the textboxes
  first_name.delete(0, END)
  last_name.delete(0, END)
  address.delete(0, END)
  city.delete(0, END)
  zip.delete(0, END)

  conn.commit() #Pour sauvegarder les changements qu'on fait dans notre base de donnees

  conn.close() #Pour terminer la connextion a notre base de donnees 

def query():
   
  conn = sqlite3.connect('address_book.db') #On cree une variable de connexion a notre database sqlite.Entre parentheses on ecrit le nom d'une base de donnees qu'on veut creer. Si cette basse de donnees n'existe pas encore, cette commande va la creer et elle sera sauvegardee dans notre dossier actuel. 

  c = conn.cursor() #on cree le curseur

  #Query the database
  c.execute("SELECT *, oid FROM addresses") 
  records = c.fetchall()
  print(records)

  #Loop through records
  print_records = ''
  for record in records: 
    print_records += str(record) + "\n"

  query_label = Label(root, text=print_records)
  query_label.grid(row=12, column=0, columnspan=2)

  conn.commit() #Pour sauvegarder les changements qu'on fait dans notre base de donnees

  conn.close() #Pour terminer la connextion a notre base de donnees 






#on cree entry widget - a text box ou on va introduire le first_name, last_name, etc
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20, pady=(10,0))

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

zip = Entry(root, width=30)
zip.grid(row=4, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

#On cree les text box labels
first_name_label = Label(root, text='First Name')
first_name_label.grid(row=0, column=0)

last_name_label = Label(root, text='Last Name')
last_name_label.grid(row=1, column=0)

address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)

city_label = Label(root, text='City')
city_label.grid(row=3, column = 0)

zip_label = Label(root, text='Zip code')
zip_label.grid(row=4, column=0)

delete_label = Label(root, text='Select ID')
delete_label.grid(row=9, column=0)

#On cree le submit button
submit_button = Button(root, text = 'Add record to database', command = submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create a Query Button
query_button = Button(root, text='Show records', command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create a Delete Button
delete_button = Button(root, text='Delete record', command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create an Update Button 
update_button = Button(root, text='Update a Record', command=update)
update_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=130)



root.mainloop()