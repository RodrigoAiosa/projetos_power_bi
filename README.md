# 📊 PBI Portfolio

> Portfólio moderno e minimalista para exibição de dashboards Power BI, construído com Python + Streamlit.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)

---

## 🎨 Paleta de Cores - Autoridade Power BI

| Cor | Hex | Uso |
|-----|-----|-----|
| **Power BI Yellow** | `#F2C811` | Destaques, botões ativos, acentos |
| **Gold Deep** | `#EAAA00` | Gradientes, hover |
| **Dark Navy** | `#1A1A2E` | Fundo sidebar |
| **Deep Black** | `#0F0F1A` | Fundo principal |
| **Surface** | `#16213E` | Cards, elementos elevados |
| **Cyan** | `#00B4D8` | Categorias, links |
| **Text Primary** | `#FFFFFF` | Títulos |
| **Text Secondary** | `#A0AEC0` | Descrições |
| **Text Muted** | `#718096` | Labels, footer |

---

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/pbi-portfolio.git
cd pbi-portfolio
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o app
```bash
streamlit run app.py
```

O app estará disponível em `http://localhost:8501`

---

## 📁 Estrutura do Projeto

```
pbi-portfolio/
├── app.py                    # Aplicação principal Streamlit
├── requirements.txt          # Dependências Python
├── README.md                 # Documentação
├── .streamlit/
│   └── config.toml          # Configurações de tema
└── assets/
    └── (imagens e recursos)
```

---

## 🎯 Funcionalidades

- ✅ **Sidebar colapsável** com botão customizado
- ✅ **Menu com submenus** (Estudantes, Professores, Finanças)
- ✅ **Grid de projetos** com cards interativos
- ✅ **Filtros por categoria**
- ✅ **Embed Power BI** diretamente no app
- ✅ **Design moderno e minimalista**
- ✅ **Paleta de cores profissional** com autoridade no tema
- ✅ **Responsivo** para diferentes tamanhos de tela

---

## 📝 Adicionar Novos Projetos

Edite a lista `PBI_PROJECTS` no arquivo `app.py`:

```python
{
    "title": "Nome do Dashboard",
    "icon": "📊",
    "category": "Categoria",
    "url": "https://app.powerbi.com/view?r=...",
    "desc": "Descrição do projeto"
}
```

### Categorias disponíveis:
- `Operações & Logística`
- `Estratégico & Financeiro`
- `RH & People Analytics`
- `Setor Público & Geral`

---

## 🌐 Deploy no Streamlit Cloud

1. Faça push do código para o GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu repositório
4. O deploy será feito automaticamente!

---

## 📄 Licença

MIT License - Livre para uso pessoal e comercial.

---

<div align="center">
  <p>Feito com 💛 e Python</p>
  <p><strong>Power BI</strong> • <strong>Streamlit</strong> • <strong>Data Visualization</strong></p>
</div>
