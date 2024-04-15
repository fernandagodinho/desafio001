#relogio digital
from tkinter import *
from datetime import datetime

# Definindo cores
cor1 = "#3d3d3d"  # preta
cor3 = "#21c25c"  # verde

# Criando a janela
janela = Tk()
janela.title("Relógio Digital")
janela.geometry('440x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=cor1)

# Função para atualizar o relógio
def atualizar_relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")
    
    # Atualizando o label da hora
    l1.config(text=hora)
    
    # Atualizando o label da data
    l2.config(text=f"{dia_semana} {dia}/{mes}/{ano}")
    
    # Chamando a função novamente após 200ms
    l1.after(200, atualizar_relogio)

# Criando o label para a hora
l1 = Label(janela, text="10:05:05", font=('Arial', 80), bg=cor1, fg=cor3)
l1.grid(row=0, column=0, sticky=NW, padx=5)

# Criando o label para a data
l2 = Label(janela, font=('Arial', 20), bg=cor1, fg=cor3)
l2.grid(row=1, column=0, sticky=NW, padx=5)

# Iniciando o relógio
atualizar_relogio()

# Executando a aplicação
janela.mainloop()
