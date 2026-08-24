import random
import tkinter as tk
from tkinter import messagebox


class JogoAdivinhacao:

    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação - Modo Aprendizagem")
        self.root.geometry("450x400")
        self.root.resizable(False, False)

       
        self.cor_fundo_creme = "#BBBBDB"
        self.cor_azul_marinho = "#000080"

        
        self.root.configure(bg=self.cor_fundo_creme)

        
        self.max_tentativas = 6
        self.numero_secreto = 0
        self.tentativas_restantes = 0

        
        self.criar_widgets()
        self.novo_jogo()

    def criar_widgets(self):
        
        self.lbl_titulo = tk.Label(
            self.root,
            text="Adivinhe o Número (1 a 24)",
            font=("Arial", 16, "bold italic"),
            bg=self.cor_fundo_creme,
        )
        self.lbl_titulo.pack(pady=10)

        
        self.lbl_modo = tk.Label(
            self.root,
            text="Modo Aprendizagem Ativo",
            font=("Arial", 10, "italic"),
            fg="green",
            bg=self.cor_fundo_creme,
        )
        self.lbl_modo.pack()

        
        self.lbl_tentativas = tk.Label(
            self.root,
            text="",
            font=("Arial", 11, "bold italic"),
            bg=self.cor_fundo_creme,
        )
        self.lbl_tentativas.pack(pady=10)

       
        self.entry_palpite = tk.Entry(
            self.root, font=("Arial", 14, "italic"), justify="center", width=10
        )
        self.entry_palpite.pack(pady=5)
        self.entry_palpite.bind("<Return>", lambda event: self.verificar_palpite())

        
        self.btn_enviar = tk.Button(
            self.root,
            text="Tentar Palpite",
            font=("Arial", 11, "bold italic"),
            bg=self.cor_azul_marinho,
            fg="white",
            activebackground="#080863",
            activeforeground="white",
            command=self.verificar_palpite,
        )
        self.btn_enviar.pack(pady=5)

        
        self.lbl_dica = tk.Label(
            self.root,
            text="",
            font=("Arial", 11, "italic"),
            bg=self.cor_fundo_creme,
            relief="groove",
            width=45,
            height=6,
            wraplength=350,
        )
        self.lbl_dica.pack(pady=15)

        
        self.btn_reiniciar = tk.Button(
            self.root,
            text="Novo Jogo",
            font=("Arial", 10, "italic"),
            command=self.novo_jogo,
        )
        self.btn_reiniciar.pack(pady=5)

    def novo_jogo(self):
        self.numero_secreto = random.randint(1, 24)
        self.tentativas_restantes = self.max_tentativas
        self.lbl_tentativas.config(
            text=f"Tentativas restantes: {self.tentativas_restantes}"
        )
        self.lbl_dica.config(
            text="Digite um número de 1 a 24 e clique em 'Tentar Palpite'!"
        )
        self.entry_palpite.delete(0, tk.END)
        self.entry_palpite.config(state="normal")
        self.btn_enviar.config(state="normal")

    def gerar_dica_aprendizagem(self, palpite):
        dicas = []

    
        diferenca = abs(self.numero_secreto - palpite)
        if palpite < self.numero_secreto:
            direcao = "MAIOR"
        else:
            direcao = "MENOR"

        if diferenca >= 10:
            distancia = "Você está MUITO LONGE!"
        elif diferenca >= 5:
            distancia = "Você está LONGE."
        else:
            distancia = "Você está PERTO!"

        dicas.append(f"• O número secreto é {direcao} que {palpite}.")
        dicas.append(f"• Proximidade: {distancia}")


        if self.numero_secreto % 2 == 0:
            paridade = "PAR"
        else:
            paridade = "ÍMPAR"
        dicas.append(f"• Dica de Aprendizado: O número secreto é {paridade}.")

        if self.numero_secreto % 3 == 0:
            dicas.append("• Dica Extra: O número é múltiplo de 3.")
        elif self.numero_secreto % 5 == 0:
            dicas.append("• Dica Extra: O número é múltiplo de 5.")

        return "\n".join(dicas)

    def verificar_palpite(self):
        entrada = self.entry_palpite.get()

       
        if not entrada.isdigit():
            messagebox.showwarning(
                "Aviso", "Por favor, digite um número inteiro válido!"
            )
            return

        palpite = int(entrada)

        if palpite < 1 or palpite > 24:
            messagebox.showwarning(
                "Aviso", "O número precisa estar entre 1 e 24!"
            )
            return

        self.tentativas_restantes -= 1
        self.lbl_tentativas.config(
            text=f"Tentativas restantes: {self.tentativas_restantes}"
        )

      
        if palpite == self.numero_secreto:
            self.lbl_dica.config(
                text=f"Parabéns! Você acertou o número {self.numero_secreto}!"
            )
            messagebox.showinfo(
                "Vitória!",
                f"Você acertou o número {self.numero_secreto}!",
            )
            self.finalizar_jogo()
            return

        
        if self.tentativas_restantes == 0:
            self.lbl_dica.config(
                text=f"Fim de jogo! O número secreto era {self.numero_secreto}."
            )
            messagebox.showinfo(
                "Fim de Jogo",
                f"Suas tentativas acabaram! O número era {self.numero_secreto}.",
            )
            self.finalizar_jogo()
            return

        # Exibir dicas se ainda tiver tentativas
        texto_dica = self.gerar_dica_aprendizagem(palpite)
        self.lbl_dica.config(text=texto_dica)
        self.entry_palpite.delete(0, tk.END)

    def finalizar_jogo(self):
        self.entry_palpite.config(state="disabled")
        self.btn_enviar.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = JogoAdivinhacao(root)
    root.mainloop()