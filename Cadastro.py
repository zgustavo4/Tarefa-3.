import customtkinter as ctk
import tkinter as tk
import subprocess as spr
from tkinter import messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x800")
app.title("TecMed")
l = ctk.LEFT
r = ctk.RIGHT


def abrir_login():
    spr.Popen(["python", "login.py"])

def login():
    tk.messagebox.showwarning("Concluido")
    

opção=ctk.IntVar()



ctk.CTkLabel(app,text= "Já é cadastrado?").pack(pady=5)
ctk.CTkButton(app, text="Login",command=abrir_login).pack(pady=5)
ctk.CTkLabel(app,text= "Não é cadastrado? Cadastre AQUI EM BAIXO:").pack(pady=5)
nome = ctk.CTkLabel(app,text= "Nome:").pack(pady=5)
ctk.CTkEntry(app).pack(pady=5)
data = ctk.CTkLabel(app,text= "Data de Nascimento:").pack(pady=5)
ctk.CTkEntry(app).pack(pady=5)
cpf = ctk.CTkLabel(app,text= "CPF:").pack(pady=5)
ctk.CTkEntry(app).pack(pady=5)
rg = ctk.CTkLabel(app,text= "RG:").pack(pady=5)
ctk.CTkEntry(app).pack(pady=5)
numero = ctk.CTkLabel(app,text= "Numero de Contato:").pack(pady=5)
ctk.CTkEntry(app).pack(pady=5)
ctk.CTkLabel(app,text= "Sexo:").pack(pady=5)

ctk.CTkRadioButton(app, text="Masculino",variable=opção, value=1).pack(pady=5)
ctk.CTkRadioButton(app, text="Feminino",variable=opção, value=2).pack(pady=5)
ctk.CTkButton(app, text="Finalizar", command= login).pack(pady=5)




app.mainloop()

