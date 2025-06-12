from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image

# Importando ------
import requests
import json


# cores
co0 = "#444466"  # Preta / black
co1 = "#feffff"  # branca / white 
co2 = "#6f9fbd"  # azul / blue

fundo = "#484f60" # background

# criando janela ------

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

# Dividindo a janela em dois frames ------
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)


frame_cima = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=320, height=300, bg=fundo, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)

# Função para pegar dados

def info():
    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CBRL'

    # -- HTTP requests
    response = requests.get(api_link)

    # -- Convertendo os dados em dicionário
    dados = response.json()

    # -- Valor em USD
    valor_usd = float(dados['USD'])
    valor_formatado_usd = "$ {:,.3f}".format(valor_usd)
    l_p_usd['text'] = valor_formatado_usd

     # -- Valor em EURO
    valor_euro = float(dados['EUR'])
    valor_formatado_euro = "€ {:,.3f}".format(valor_euro)
    l_p_euro['text'] = valor_formatado_euro

     # -- Valor em REAL
    valor_real = float(dados['BRL'])
    valor_formatado_real = "R$ {:,.3f}".format(valor_real)
    l_p_real['text'] = valor_formatado_real

    frame_baixo.after(1000, info)



# Configurando o frame cima-------
imagem = Image.open('imagens/bit4.png')
imagem = imagem.resize((30, 30), Image.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image=imagem, compound=LEFT, bg=co1, relief=FLAT)
l_icon.place(x=10, y=10)


l_nome = Label(frame_cima, text='Bitcoin Price Tracker', bg=co1, fg=co2, relief=FLAT, anchor='center', font=('Arial 20'))
l_nome.place(x=50, y=5)


# Configurando o frame baixo ----
l_p_usd = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 20'))
l_p_usd.place(x=10, y=50)

l_p_euro = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_p_euro.place(x=11, y=130)

l_p_real = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_p_real.place(x=12, y=160)



info()


janela.mainloop()
