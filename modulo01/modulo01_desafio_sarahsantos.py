import tkinter as tk
from tkinter import messagebox, ttk


class AcaiteriaGUI:

  def __init__(self, root):
    self.root = root
    self.root.title("Açaiteria - Sistema de Vendas")
    self.root.geometry("720x600")
    self.root.resizable(False, False)

    # Configuração de Cores Principais (Tema Açai)
    self.COLOR_BG = "#F4EFEA"  # Fundo suave
    self.COLOR_PURPLE_DARK = "#3B1443"  # Roxo Açai Escuro
    self.COLOR_PURPLE_MED = "#5C2269"  # Roxo Médio
    self.COLOR_ACCENT = "#8E24AA"  # Destaque
    self.COLOR_TEXT_LIGHT = "#FFFFFF"

    self.root.configure(bg=self.COLOR_BG)

    # Configuração dos Estilos TTK
    self.style = ttk.Style()
    self.style.theme_use("clam")
    self._setup_styles()

    # Dados dos produtos (vagas 1 a 5)
    self.produtos = [
        {
            "vaga": 1,
            "nome": "Açaí comum",
            "estoque": 120,
            "preco": 14.99,
            "validade": "02/07/2027",
            "descricao": "Açaí comum, ideal para quem precisa do básico.",
        },
        {
            "vaga": 2,
            "nome": "Açaí premium",
            "estoque": 90,
            "preco": 19.99,
            "validade": "02/11/2027",
            "descricao": "Açaí premium, qualidade superior.",
        },
        {
            "vaga": 3,
            "nome": "Açaí personalizável",
            "estoque": 150,
            "preco": 18.99,
            "validade": "08/06/2027",
            "descricao": (
                "Açaí personalizável, monte com acompanhamentos."
            ),
        },
        {
            "vaga": 4,
            "nome": "Açaí puro",
            "estoque": 80,
            "preco": 10.99,
            "validade": "05/10/2027",
            "descricao": "Açaí puro e denso da Amazônia.",
        },
        {
            "vaga": 5,
            "nome": "Açaí com Morango",
            "estoque": 60,
            "preco": 15.99,
            "validade": "20/08/2027",
            "descricao": "Açaí batido com toque fresco de fruta.",
        },
    ]

    # Variáveis de Checkout
    self.produto_selecionado = None
    self.forma_pagamento_var = tk.StringVar(value="Pix")

    # Header de Título
    header_frame = tk.Frame(self.root, bg=self.COLOR_PURPLE_DARK, height=60)
    header_frame.pack(fill="x")

    lbl_header = tk.Label(
        header_frame,
        text="🍧 Açaiteria - Sistema de Vendas",
        font=("Segoe UI", 16, "bold"),
        bg=self.COLOR_PURPLE_DARK,
        fg=self.COLOR_TEXT_LIGHT,
    )
    lbl_header.pack(pady=12)

    # Container Principal com Abas
    self.notebook = ttk.Notebook(self.root)
    self.notebook.pack(fill="both", expand=True, padx=15, pady=15)

    # Configuração das Abas
    self.tab_cardapio = ttk.Frame(self.notebook, style="Main.TFrame")
    self.tab_cadastro = ttk.Frame(self.notebook, style="Main.TFrame")
    self.tab_venda = ttk.Frame(self.notebook, style="Main.TFrame")

    self.notebook.add(self.tab_cardapio, text="📋 Cardápio / Estoque")
    self.notebook.add(self.tab_cadastro, text="✏️ Cadastrar Produto")
    self.notebook.add(self.tab_venda, text="🛒 Realizar Venda")

    self._setup_cardapio()
    self._setup_cadastro()
    self._setup_venda()

  def _setup_styles(self):
    # Estilo dos Frames
    self.style.configure("Main.TFrame", background=self.COLOR_BG)

    # Estilo do Notebook (Abas)
    self.style.configure(
        "TNotebook", background=self.COLOR_BG, borderwidth=0
    )
    self.style.configure(
        "TNotebook.Tab",
        font=("Segoe UI", 10, "bold"),
        padding=[12, 6],
        background="#E0D6E3",
        foreground="#333333",
    )
    self.style.map(
        "TNotebook.Tab",
        background=[("selected", self.COLOR_PURPLE_MED)],
        foreground=[("selected", self.COLOR_TEXT_LIGHT)],
    )

    # Estilo da Treeview (Tabela)
    self.style.configure(
        "Treeview",
        font=("Segoe UI", 10),
        rowheight=26,
        background="#FFFFFF",
        fieldbackground="#FFFFFF",
    )
    self.style.configure(
        "Treeview.Heading",
        font=("Segoe UI", 10, "bold"),
        background=self.COLOR_PURPLE_DARK,
        foreground=self.COLOR_TEXT_LIGHT,
    )
    self.style.map("Treeview.Heading", background=[("active", self.COLOR_PURPLE_MED)])

    # Estilo dos Botões
    self.style.configure(
        "Primary.TButton",
        font=("Segoe UI", 10, "bold"),
        background=self.COLOR_PURPLE_MED,
        foreground=self.COLOR_TEXT_LIGHT,
        padding=[10, 6],
    )
    self.style.map(
        "Primary.TButton",
        background=[("active", self.COLOR_ACCENT)],
        foreground=[("active", self.COLOR_TEXT_LIGHT)],
    )

    # Estilo dos LabelFrames
    self.style.configure(
        "TLabelframe", background=self.COLOR_BG, borderwidth=1
    )
    self.style.configure(
        "TLabelframe.Label",
        font=("Segoe UI", 10, "bold"),
        foreground=self.COLOR_PURPLE_DARK,
        background=self.COLOR_BG,
    )

    # Estilo dos Labels e Radiobuttons
    self.style.configure(
        "TLabel", font=("Segoe UI", 10), background=self.COLOR_BG
    )
    self.style.configure(
        "TRadiobutton", font=("Segoe UI", 10), background=self.COLOR_BG
    )

  # --- ABA 1: CARDÁPIO E LISTAGEM ---
  def _setup_cardapio(self):
    columns = ("vaga", "nome", "preco", "estoque", "validade")
    self.tree = ttk.Treeview(
        self.tab_cardapio, columns=columns, show="headings", height=8
    )

    self.tree.heading("vaga", text="Vaga")
    self.tree.heading("nome", text="Nome")
    self.tree.heading("preco", text="Preço (R$)")
    self.tree.heading("estoque", text="Estoque")
    self.tree.heading("validade", text="Validade")

    self.tree.column("vaga", width=60, anchor="center")
    self.tree.column("nome", width=200)
    self.tree.column("preco", width=110, anchor="center")
    self.tree.column("estoque", width=90, anchor="center")
    self.tree.column("validade", width=110, anchor="center")

    self.tree.pack(fill="x", padx=15, pady=15)

    # Frame de Detalhes
    frame_detalhes = ttk.LabelFrame(self.tab_cardapio, text=" Detalhes ")
    frame_detalhes.pack(fill="x", padx=15, pady=5)

    lbl_detalhe_title = ttk.Label(
        frame_detalhes,
        text="Descrição do Produto Selecionado:",
        font=("Segoe UI", 10, "bold"),
    )
    lbl_detalhe_title.pack(anchor="w", padx=10, pady=(8, 2))

    self.lbl_descricao = ttk.Label(
        frame_detalhes,
        text="Selecione um produto acima para ver os detalhes.",
        wraplength=620,
        foreground="#666666",
        font=("Segoe UI", 10, "italic"),
    )
    self.lbl_descricao.pack(anchor="w", padx=10, pady=(0, 10))

    self.tree.bind("<<TreeviewSelect>>", self._exibir_detalhes)
    self.atualizar_tabela()

  def atualizar_tabela(self):
    for item in self.tree.get_children():
      self.tree.delete(item)
    for prod in self.produtos:
      self.tree.insert(
          "",
          "end",
          values=(
              prod["vaga"],
              prod["nome"],
              f"R$ {prod['preco']:.2f}",
              prod["estoque"],
              prod["validade"],
          ),
      )

  def _exibir_detalhes(self, event):
    selected = self.tree.selection()
    if selected:
      item = self.tree.item(selected[0])
      vaga = item["values"][0]
      prod = next(p for p in self.produtos if p["vaga"] == vaga)
      self.lbl_descricao.config(
          text=prod["descricao"], foreground="#000000", font=("Segoe UI", 10)
      )

  # --- ABA 2: CADASTRO E EDIÇÃO ---
  def _setup_cadastro(self):
    frame_form = ttk.LabelFrame(
        self.tab_cadastro, text=" Formulário de Cadastro "
    )
    frame_form.pack(fill="both", expand=True, padx=15, pady=15)

    grid_opts = {"sticky": "w", "padx": 15, "pady": 8}

    ttk.Label(frame_form, text="Vaga (1 a 5):").grid(
        row=0, column=0, **grid_opts
    )
    self.combo_vaga = ttk.Combobox(
        frame_form, values=[1, 2, 3, 4, 5], state="readonly", width=8
    )
    self.combo_vaga.current(0)
    self.combo_vaga.grid(row=0, column=1, **grid_opts)

    ttk.Label(frame_form, text="Nome do Produto:").grid(
        row=1, column=0, **grid_opts
    )
    self.ent_nome = ttk.Entry(frame_form, width=38)
    self.ent_nome.grid(row=1, column=1, **grid_opts)

    ttk.Label(frame_form, text="Estoque:").grid(row=2, column=0, **grid_opts)
    self.ent_estoque = ttk.Entry(frame_form, width=15)
    self.ent_estoque.grid(row=2, column=1, **grid_opts)

    ttk.Label(frame_form, text="Preço (R$):").grid(
        row=3, column=0, **grid_opts
    )
    self.ent_preco = ttk.Entry(frame_form, width=15)
    self.ent_preco.grid(row=3, column=1, **grid_opts)

    ttk.Label(frame_form, text="Validade:").grid(row=4, column=0, **grid_opts)
    self.ent_validade = ttk.Entry(frame_form, width=15)
    self.ent_validade.grid(row=4, column=1, **grid_opts)

    ttk.Label(frame_form, text="Descrição:").grid(
        row=5, column=0, **grid_opts
    )
    self.ent_descricao = ttk.Entry(frame_form, width=38)
    self.ent_descricao.grid(row=5, column=1, **grid_opts)

    btn_salvar = ttk.Button(
        frame_form,
        text="💾 Salvar / Atualizar Produto",
        style="Primary.TButton",
        command=self._salvar_produto,
    )
    btn_salvar.grid(row=6, column=0, columnspan=2, pady=20, padx=15)

  def _salvar_produto(self):
    try:
      vaga = int(self.combo_vaga.get())
      nome = self.ent_nome.get().strip()
      estoque = int(self.ent_estoque.get())
      preco = float(self.ent_preco.get().replace(",", "."))
      validade = self.ent_validade.get().strip()
      descricao = self.ent_descricao.get().strip()

      if not nome or not validade:
        messagebox.showwarning(
            "Atenção", "Preencha todos os campos obrigatórios!"
        )
        return

      # Atualiza no estoque
      for prod in self.produtos:
        if prod["vaga"] == vaga:
          prod.update({
              "nome": nome,
              "estoque": estoque,
              "preco": preco,
              "validade": validade,
              "descricao": descricao,
          })
          break

      self.atualizar_tabela()
      self._atualizar_combo_vendas()
      messagebox.showinfo("Sucesso", f"Produto salvo na vaga {vaga}!")

    except ValueError:
      messagebox.showerror(
          "Erro", "Estoque e Preço devem conter valores numéricos válidos!"
      )

  # --- ABA 3: REALIZAR VENDA ---
  def _setup_venda(self):
    frame_venda = ttk.LabelFrame(self.tab_venda, text=" Finalizar Venda ")
    frame_venda.pack(fill="both", expand=True, padx=15, pady=15)

    ttk.Label(
        frame_venda,
        text="Selecione o Produto:",
        font=("Segoe UI", 10, "bold"),
    ).pack(anchor="w", padx=15, pady=(15, 2))
    self.combo_produtos_venda = ttk.Combobox(
        frame_venda, state="readonly", width=45, font=("Segoe UI", 10)
    )
    self.combo_produtos_venda.pack(anchor="w", padx=15, pady=5)
    self._atualizar_combo_vendas()

    ttk.Label(
        frame_venda,
        text="Forma de Pagamento:",
        font=("Segoe UI", 10, "bold"),
    ).pack(anchor="w", padx=15, pady=(20, 2))
    frame_pagamento = ttk.Frame(frame_venda, style="Main.TFrame")
    frame_pagamento.pack(anchor="w", padx=15, pady=5)

    for opcao in ["Pix", "Cartão", "Dinheiro"]:
      ttk.Radiobutton(
          frame_pagamento,
          text=opcao,
          value=opcao,
          variable=self.forma_pagamento_var,
      ).pack(side="left", padx=10)

    btn_confirmar = ttk.Button(
        frame_venda,
        text="🎉 Confirmar & Realizar Venda",
        style="Primary.TButton",
        command=self._confirmar_venda,
    )
    btn_confirmar.pack(anchor="w", padx=15, pady=30)

  def _atualizar_combo_vendas(self):
    opcoes = [
        f"{p['vaga']} - {p['nome']} (R$ {p['preco']:.2f})" for p in self.produtos
    ]
    self.combo_produtos_venda["values"] = opcoes
    if opcoes:
      self.combo_produtos_venda.current(0)

  def _confirmar_venda(self):
    selecao = self.combo_produtos_venda.get()
    if not selecao:
      messagebox.showwarning("Atenção", "Selecione um produto!")
      return

    vaga = int(selecao.split(" - ")[0])
    prod = next(p for p in self.produtos if p["vaga"] == vaga)
    pagamento = self.forma_pagamento_var.get()

    if prod["estoque"] <= 0:
      messagebox.showerror(
          "Erro", f"Produto '{prod['nome']}' sem estoque disponível!"
      )
      return

    resposta = messagebox.askyesno(
        "Confirmar Venda",
        f"Produto: {prod['nome']}\nPreço: R$ {prod['preco']:.2f}\nPagamento:"
        f" {pagamento}\n\nDeseja confirmar a compra?",
    )

    if resposta:
      prod["estoque"] -= 1
      self.atualizar_tabela()
      messagebox.showinfo(
          "Venda Concluída",
          f"🌟 Venda realizada com sucesso!\nEstoque atual de '{prod['nome']}':"
          f" {prod['estoque']}",
      )


if __name__ == "__main__":
  root = tk.Tk()
  app = AcaiteriaGUI(root)
  root.mainloop()