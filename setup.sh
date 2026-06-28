#!/bin/bash
# setup.sh - Script de configuração inicial do projeto

echo "🚀 Configurando PBI Portfolio..."

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Por favor, instale o Python 3.10+"
    exit 1
fi

# Cria ambiente virtual
echo "📦 Criando ambiente virtual..."
python3 -m venv venv

# Ativa ambiente
echo "⚡ Ativando ambiente virtual..."
source venv/bin/activate

# Instala dependências
echo "📥 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup completo!"
echo ""
echo "Para iniciar o app, execute:"
echo "  source venv/bin/activate"
echo "  streamlit run app.py"
echo ""
echo "Acesse: http://localhost:8501"
