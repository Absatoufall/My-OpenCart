from tkinter import *
import tkinter as tk
import mysql.connector

# Fonction pour récupérer et afficher All customers
def get_customer_count():
 clear_result_label() # Effacer le texte précédent
 cursor.execute("SELECT COUNT(*) FROM oc_customer")
 customer_count = cursor.fetchone()[0]
 result_label.config(text="All customers: {}".format(customer_count))

# Fonction pour récupérer et afficher le Customers_connected
def get_online_user_count():
 clear_result_label() # Effacer le texte précédent
 cursor.execute("SELECT COUNT(*) FROM oc_customer_online")
 online_user_count = cursor.fetchone()[0]
 result_label.config(text="Customers_connected: {}".format(online_user_count))

# Fonction pour récupérer et afficher la Products_List
def get_product_list():
 clear_result_label() # Effacer le texte précédent
 cursor.execute("SELECT model FROM oc_product")
 products = cursor.fetchall()
 product_list = '\n'.join([product[0] for product in products])
 result_label.config(text="Products_List:\n{}".format(product_list))

# Fonction pour effacer le texte de l'étiquette result_label
def clear_result_label():
 result_label.config(text="")

# Connexion à la base de données OpenCart
connection = mysql.connector.connect(
host="localhost",
 user="root",
 password="",
 database="opencart"
)
cursor = connection.cursor()

# Création de la fenêtre Tkinter

root = tk.Tk()
root.title("Monitoring_OpenCart")



# Création des boutons pour afficher différentes options
customer_button = tk.Button(root, text="All customers", command=get_customer_count)
customer_button.pack(pady=5)

online_user_button = tk.Button(root, text="Customers_connected", command=get_online_user_count)
online_user_button.pack(pady=5)

product_list_button = tk.Button(root, text="Products_List", command=get_product_list)
product_list_button.pack(pady=5)

# Étiquette pour afficher le résultat
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Exécution de la boucle principale Tkinter
root.mainloop()

#Hi I am Absatou
#Salut