import customtkinter as ctk
import subprocess as spr
import tkinter as tk
from tkinter import messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.geometry("323x300")
app.title("Agendamento")

def cancelar_agendamento():
    spr.Popen(["python", "cancelar.py"])

def agendado():
    tk.messagebox.showinfo("Concluido!!")


opção=ctk.IntVar()

ctk.CTkLabel(app,text="Faça seu agendamento:").pack(pady=5)
ctk.CTkRadioButton(app, text="Consulta",variable=opção, value=1).pack(pady=5)
ctk.CTkRadioButton(app, text="Exame",variable=opção, value=2).pack(pady=5)
ctk.CTkRadioButton(app, text="Retorno",variable=opção, value=3).pack(pady=5)
ctk.CTkLabel(app,text="Data do agendamento:").pack(pady=5)
ctk.CTkEntry(app).pack(pady=5)
ctk.CTkButton(app,text="Agendar",command=agendado).pack(pady=5)
ctk.CTkButton(app, text="Cancelar Agendamento", command=cancelar_agendamento).pack(pady=5)


app.mainloop()


