from tkinter import *
from tkinter import ttk


#cores   #usei o color piker (google)
cor1 = "#3b3b3b" # preta
cor2 = "#feffff" # branca
cor3 = "#38576b" # azul escuro
cor4 = "#eceff1" # cinza claro
cor5 = "#ffab40" # laranja

# inicio da janela
janela = Tk()
janela.title("Calculadora Facul")
janela.geometry("240x325")  #240x310
janela.config(bg=cor1)

#variaveis para logica
valor_texto = StringVar()
entradas = ""

# criando os frames
frame_digitado = Frame(janela, width=240, height=60, bg=cor3)
frame_digitado.grid(row=0, column=0)

frame_corpo = Frame(janela, width=240, height=265)
frame_corpo.grid(row=1, column=0)

# Criando LABEL
calc_label = Label(frame_digitado, textvariable=valor_texto, width=13, height=2, font=("Roboto 20 bold"), padx=7, relief=FLAT, anchor="e", justify=RIGHT, bg=cor3, fg=cor4)
calc_label.place(x=0, y=0)

by = Label(frame_corpo, text="Felipe Lamata", bg=cor4, fg=cor1, font=("Roboto 8 bold"))
by.place(x=80, y=248)


## logica
##Funções

def entrada_de_valores(itens):
    global entradas
    entradas = entradas + str(itens)
    valor_texto.set(entradas)   #passando valor para uma variavel de string variavel
  
def calcular():                 #função q executa a expressão q esta guardada na variavel "entradas" pela funão EVAL
   global entradas   
   resultado = eval(entradas)   #A função eval() analisa o argumento da expressão e o avalia como uma expressão python
   valor_texto.set(resultado)
   entradas=str(resultado)
      
def apagar_tudo():              #função para apagar tudo Variaveis + tela
    global entradas
    entradas=''
    valor_texto.set('')    
    

# botões da calc
# botões primeira linha
b_C = Button(frame_corpo, command=apagar_tudo, text="C", width=11, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE) 
b_C.place(x=0, y=0)

b_P = Button(frame_corpo, command=lambda: entrada_de_valores('%'), text="%", width=5, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_P.place(x=120, y=0)

b_D = Button(frame_corpo, command=lambda: entrada_de_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_D.place(x=180, y=0)

# botões segunda linha 7/8/9/*
b_7 = Button(frame_corpo, command=lambda: entrada_de_valores('7'), text="7", width=5, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE) 
b_7.place(x=0, y=50)

b_8 = Button(frame_corpo, command=lambda: entrada_de_valores('8'), text="8", width=5, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=60, y=50)

b_9 = Button(frame_corpo, command=lambda: entrada_de_valores('9'), text="9", width=5, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=120, y=50)

b_mult = Button(frame_corpo, command=lambda: entrada_de_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_mult.place(x=180, y=50)

# botões terceura linha 4/5/6/-
b_4 = Button(frame_corpo, command=lambda: entrada_de_valores('4'), text="4", width=5, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE) 
b_4.place(x=0, y=100)

b_5 = Button(frame_corpo, command=lambda: entrada_de_valores('5'), text="5", width=5, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=100)

b_6 = Button(frame_corpo, command=lambda: entrada_de_valores('6'), text="6", width=5, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=100)

b_sub = Button(frame_corpo, command=lambda: entrada_de_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_sub.place(x=180, y=100)

# botões quarta linha 1/2/3/+
b_1 = Button(frame_corpo, command=lambda: entrada_de_valores('1'), text="1", width=5, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE) 
b_1.place(x=0, y=150)

b_2 = Button(frame_corpo, command=lambda: entrada_de_valores('2'), text="2", width=5, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=60, y=150)

b_3 = Button(frame_corpo, command=lambda: entrada_de_valores('3'), text="3", width=5, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=120, y=150)

b_soma = Button(frame_corpo, command=lambda: entrada_de_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_soma.place(x=180, y=150)

# botões quinta linha 0/./=
b_0 = Button(frame_corpo, command=lambda: entrada_de_valores('0'), text="0", width=11, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE) 
b_0.place(x=0, y=200)

b_ponto = Button(frame_corpo, command=lambda: entrada_de_valores('.'), text=".", width=5, height=2, bg=cor4, fg=cor1, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_ponto.place(x=120, y=200)


b_igual = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=("Roboto 13 bold"), relief=RAISED, overrelief=RIDGE)
b_igual.place(x=180, y=200)



janela.mainloop()           #manterá a janela aberta por loop