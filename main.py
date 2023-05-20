from tkinter import *

master = Tk()

# Título do banco
master.title('Py_Bank')
# Tamanho da nossa tela
master.geometry('314x674+335+-8')
# Travar o redicionamento da tela
master.wm_resizable(width=False,height=False)

# Importações de imagens
Imagem_Pricipal = PhotoImage(file='tela_inicial.png') # Importando a imagem em uma variavel

# Criação da Label
TelaPricipal = Label(master,image=Imagem_Pricipal) # Criando label para imagem pricipal
TelaPricipal.place(x=0,y=0)


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

#alteração teste