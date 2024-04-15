from cProfile import label
from tkinter import*
from datetime import datetime

cor1 ="#3d3d3d"
cor2 = "#fafcff"
cor3 = "#21c25c"
cor4 =" #eb463b"
cor5 = "#dedcdc"
cor6 = "#3080f0"

janela = tk()
janela.title ("")
janela.geometry ("400x180")
janela.resizable(widt=false, height= false)
janela.configure(background=cor1)

def atulizar_relogio():
    tempo = datetime.now()
    hora = tempo.strptime("%H:%M:S")
    dia_semana= tempo. strptime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%y")

l1.config(text=hora)
l2.config(text=f"{dia_semana }\u00a0{dia}\{mes}\{ano} " )

l1.after(200,atulizar_relogio)

l1 = label(janela, text="15:05:05", font=('ariel',80),bg=cor1 fg=cor6 )
l1 = Grid( row=0 , column=0,sticky=NW, padx = 5)
l2 =label(janela,font=('ariel,20'), bg=cor1 fg=cor3 )
l2 =Grid (row=1 ,column =0, sticky=NW, padx=5 )
atulizar_relogio()
janela mainloop

        