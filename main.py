"""
ATENÇÃO:
Para evitar erros, recomendo verificar com atenção cada modulo que deverá ser instalado
Todos os requisitos para essa aplicação funcionar está no fim desta pagina!
"""

# Importações dos modulos da interfase grafica:
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# Adicionando a Tkinter a uma variavel:
master = tk.Tk()

# Config pricipais da janela:
# Título do banco:
master.title('Py_Bank')
# Tamanho da nossa tela:
master.geometry('315x676+558+76')
# Travar o redicionamento da tela:
master.wm_resizable(width=False,height=False)
# -------------------------------------------


# Importações de imagens:
# Imagem pricipal:
Imagem_Pricipal = tk.PhotoImage(file='imagens/Tela_inicial.png') # Importando a imagem em uma variavel
#  Imagem do botão ENTRAR:
Imagem_Botao_Entrar = tk.PhotoImage(file='imagens/Botao_Entrar.png')


# Criação da Label
TelaPricipal = ttk.Label(master,image=Imagem_Pricipal) # Criando label para imagem pricipal
TelaPricipal.place(x=0,y=0)


# Função onde esconde a senha a gosto do usuario:
def VerSenha():
    if senha.get() == 1:
        Entrada_Senha.config(show='*')
    if senha.get() == 0:
        Entrada_Senha.config(show='')
senha = tk.IntVar()
#_____________________________________


# Criação das entradas:
Ent_testes = tk.Entry(master)
Entrada_Nome = ttk.Entry(master,bootstyle="light")
Entrada_Senha = ttk.Entry(master,bootstyle="light",validate="key",foreground='#A112D1')
Botao_Ent = tk.Button(master,image=Imagem_Botao_Entrar,borderwidth=0)
Mostrar_Senha = ttk.Checkbutton(bootstyle="success-round-toggle",onvalue=1,offvalue=0,variable=senha,command=VerSenha)
# Config de cada botão:
Entrada_Nome.place(x=73,y=388,width=190,height=34) # Config caixa de entrada nome.
Entrada_Senha.place(x=73,y=453,width=190,height=34) # Config Caixa de entrada senha.
Botao_Ent.place(x=49,y=510) # Config do botão de entrar.
Mostrar_Senha.place(x=49,y=43) # Config da caixa de seleção do checkbutton
Ent_testes.grid()

""""
Esta função não e usada no algoritmo, apenas foi criada para mapear a tela
e assim ajudar onde irá ficar cada itém, ao clicar no botão do meio do SCROOL do mouse
e printado no terminal onde está localizado o mouse no momento, assim ajudando nas conf. 
dos botões, como (X= e Y=).
'"""
# ---------------------------------------
# Função Clique do mouse
def clique_do_mouse(retorno):
    print(f'X:{retorno.x} |  Y:{retorno.y} Geo: {master.geometry()}')
# Evento do mouse
# Tecla usada e a do meio do mouse, no scroll
master.bind("<Button-2>",clique_do_mouse) 
# ---------------------------------------


# Codigo obrigatorio do Tkinter, para não fechar a janela atual
master.mainloop()


"""

Requisitos:
Tkinter: 
    Caso não tenha instalado execulte o comando no terminal:   pip install tkinter

Tkinter boosttrap:
    Irá cuidar da parte visual em algumas partes do codigo, mais informaçoes de como instalar no site:
    https://ttkbootstrap.readthedocs.io/    
     
"""