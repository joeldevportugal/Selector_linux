# Importar as bibliotecas a usar
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename

# Função copiar
def copiar_codigo():
    # Limpa o conteúdo atual da área de transferência
    janela.clipboard_clear()
    
    # Pega todos os itens da Listbox Lcodico
    itens = Lcodico.get(0, tk.END)
    
    # Se a lista estiver vazia, exibe uma mensagem de aviso e retorna
    if not itens:
        messagebox.showwarning("Aviso", "Nenhum código para copiar.")
        return
    
    # Concatena todos os itens em uma única string
    codigo = "\n".join(itens)
    
    # Adiciona o código à área de transferência
    janela.clipboard_append(codigo)
    
    # Exibe uma mensagem de sucesso
    messagebox.showinfo("Sucesso", "Código copiado para a área de transferência.")

# Função atualizar cor
def atualiza_cor(*args):
    # Pega os valores atuais dos sliders
    r = Svermelho.get()
    g = Sverde.get()
    b = SAzul.get()
    
    # Converte os valores para uma string hexadecimal
    cor_hex = f'#{r:02x}{g:02x}{b:02x}'
    
    # Atualiza o fundo de LCor com a nova cor
    LCor.config(bg=cor_hex)
    
    # Atualiza o campo EHexa com o valor hexadecimal da cor
    EHexa.delete(0, tk.END)
    EHexa.insert(0, cor_hex)

# Função carregar cor
def carregar_cor():
    # Pega os valores dos campos Enome e EHexa
    nome = Enome.get()
    hexa = EHexa.get()
    
    # Verifica se os campos não estão vazios
    if nome and hexa:
        # Adiciona os valores à Listbox Lcodico
        Lcodico.insert(tk.END, f'{nome} {hexa}')
        
        # Opcional: limpa os campos após adicionar
        Enome.delete(0, tk.END)
        EHexa.delete(0, tk.END)
    else:
        messagebox.showinfo('Informação',"Nome da cor ou valor hexadecimal está vazio!")

# Função salvar cores
def salvar_cores():
    # Abre a janela de diálogo para o usuário escolher onde salvar o arquivo
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not filepath:  # Se o usuário cancelar, retorna sem fazer nada
        return
    with open(filepath, 'w') as arquivo:
        for item in Lcodico.get(0, tk.END):
            arquivo.write(item + '\n')
    messagebox.showinfo("Cores",f"Cores salvas com sucesso em {filepath}!")

# Função limpar campos
def limpar_campos():
    # Limpa o conteúdo de Lcor
    LCor.config(bg='#000000')
    
    # Define os valores dos sliders para zero
    Svermelho.set(0)
    Sverde.set(0)
    SAzul.set(0)
    
    # Limpa os campos Enome e EHexa
    Enome.delete(0, tk.END)
    EHexa.delete(0, tk.END)
    
    # Limpa o conteúdo de Lcodico
    Lcodico.delete(0, tk.END)    

# Definir cores a usar neste projeto
co0 ='#ffffff'  # cor branco para fundo
co1 = '#000000' # cor preto para painel
co2 = '#fffbf5' # amarelo claro entrys
co3 = '#f8f9f7' # azul claro para botões 
co4 = '#f8f8ee' # amarelo claro para ListBox

# Configurar a janela
janela = tk.Tk()
janela.geometry('650x450+100+100')
janela.resizable(False, False)
janela.title('Selector de Cores Hexadecimal Dev Joel 2024 Portugal ©')
janela.configure(bg=co0)

# Criar o label para exibir a cor preta
LCor = tk.Label(janela, bg=co1, width=30, height=15)
LCor.place(x=5, y=0)

# Criar o label controle Vermelho, Verde, Azul
Vermelho = tk.Label(janela, text='Vermelho', font=('arial 14'), bg=co0)
Vermelho.place(x=260, y=0)
Verde = tk.Label(janela, text='Verde', font=('arial 14'), bg=co0)
Verde.place(x=260, y=75)
Azul = tk.Label(janela, text='Azul', font=('arial 14'), bg=co0)
Azul.place(x=260, y=155)

# Criar o Slider Vermelho, Verde, Azul
Svermelho = tk.Scale(janela, orient=tk.HORIZONTAL, length=365, bg=co0, from_=0, to=255, command=atualiza_cor)
Svermelho.place(x=260, y=30)
Sverde = tk.Scale(janela, orient=tk.HORIZONTAL, length=365, bg=co0, from_=0, to=255, command=atualiza_cor)
Sverde.place(x=260, y=105)
SAzul = tk.Scale(janela, orient=tk.HORIZONTAL, length=365, bg=co0, from_=0, to=255, command=atualiza_cor)
SAzul.place(x=260, y=185)

# Criar as entrys Referencia e codigo
Enome = tk.Entry(janela, bg=co2, width=10, font=('arial 14'))
Enome.place(x=5, y=265)
EHexa = tk.Entry(janela, bg=co2, font=('arial 14'), width=10)
EHexa.place(x=125, y=265)

# Criar os Botões
BtnCarregar = tk.Button(janela, text='Carregar codigo', font=('arial 12'), relief=tk.RAISED, overrelief=tk.RIDGE, command=carregar_cor, bg=co3)
BtnCarregar.place(x=320, y=305)
BtnGuardar = tk.Button(janela, text='Guardar', font=('arial 12'), relief=tk.RAISED, overrelief=tk.RIDGE, command=salvar_cores, bg=co3)
BtnGuardar.place(x=5, y=305)
BtnCopiar = tk.Button(janela, text='Copiar codigo', font=('arial 12'), relief=tk.RAISED, overrelief=tk.RIDGE, command=copiar_codigo, bg=co3)
BtnCopiar.place(x=100, y=305)
BtnLimpar = tk.Button(janela, text='Limpar', font=('arial 12'), relief=tk.RAISED, overrelief=tk.RIDGE, command=limpar_campos, bg=co3)
BtnLimpar.place(x=235, y=305)

# Criar a Listbox
Lcodico = tk.Listbox(janela, font=('arial 12'),height=4, width=70, bg=co4)
Lcodico.place(x=5, y=350)

# Iniciar a janela
janela.mainloop()
