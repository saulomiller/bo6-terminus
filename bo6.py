import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Certifique-se de instalar o Pillow: pip install pillow

# Função para calcular e exibir os resultados
def calcular():
    try:
        x = valores['x'].get()
        y = valores['y'].get()
        z = valores['z'].get()

        expressao1 = 2 * x + 11
        expressao2 = 2 * z + y - 5
        expressao3 = y + z - x

        resultado = f"Resultado da expressão 2 * x + 11: {expressao1}\n"
        resultado += f"Resultado da expressão 2 * z + y - 5: {expressao2}\n"
        resultado += f"Resultado da expressão y + z - x: {expressao3}"
        messagebox.showinfo("Resultados", resultado)

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configurações da janela principal
janela = tk.Tk()
janela.title("Seleção de Valores e Cálculo de Expressões")
janela.geometry("400x600")

# Dicionário para armazenar os valores selecionados para x, y, e z
valores = {'x': tk.IntVar(value=0), 'y': tk.IntVar(value=0), 'z': tk.IntVar(value=0)}

# Carregar as imagens e armazená-las em um dicionário
imagens = {
    0: ImageTk.PhotoImage(Image.open("imagns/0.png").resize((50, 50))),
    10: ImageTk.PhotoImage(Image.open("imagem_10.png").resize((50, 50))),
    11: ImageTk.PhotoImage(Image.open("imagem_11.png").resize((50, 50))),
    20: ImageTk.PhotoImage(Image.open("imagem_20.png").resize((50, 50))),
    21: ImageTk.PhotoImage(Image.open("imagem_21.png").resize((50, 50))),
    22: ImageTk.PhotoImage(Image.open("imagem_22.png").resize((50, 50))),
}

# Função para criar os botões de seleção com imagens
def criar_botoes(label_text, var):
    frame = tk.Frame(janela)
    frame.pack(pady=10)
    tk.Label(frame, text=label_text).pack()

    # Criar botões de seleção usando as imagens
    for valor, img in imagens.items():
        botao = tk.Radiobutton(frame, image=img, variable=var, value=valor)
        botao.pack(side=tk.LEFT)

# Criando botões de seleção para x, y, e z com imagens
criar_botoes("Escolha o valor de x:", valores['x'])
criar_botoes("Escolha o valor de y:", valores['y'])
criar_botoes("Escolha o valor de z:", valores['z'])

# Botão para calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.pack(pady=20)

# Inicia a interface
janela.mainloop()
