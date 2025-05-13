import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x300")
app.title("Cancelar")

def cancelamento():
    tk.messagebox.showwarning("Concluido")


ctk.CTkLabel(app,text= "Cancele aqui: ").pack(pady=5)
ctk.CTkButton(app, text="cancelar", command=cancelamento).pack(pady=5)


app.mainloop()