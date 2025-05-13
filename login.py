import customtkinter as ctk
import subprocess as spr

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x300")
app.title("TecMed")

def abrir_agendamento():
    spr.Popen(["python", "agendamento.py"])

ctk.CTkLabel(app,text= "Fazer Login:").pack(pady=5)
ctk.CTkLabel(app,text= "CPF cadastrado:").pack(pady=5)
ctk.CTkEntry(app).pack(pady=5)
ctk.CTkButton(app, text="Ir Para Agendamento", command= abrir_agendamento).pack(pady=5)




app.mainloop()