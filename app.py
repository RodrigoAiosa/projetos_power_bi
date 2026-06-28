import streamlit as st
import json
from streamlit.components.v1 import html

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Portfólio Power BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# PALETA DE CORES - AUTORIDADE POWER BI
# ============================================================
# Cores inspiradas no branding Microsoft/Power BI com tom profissional
COLORS = {
    "primary": "#F2C811",        # Power BI Yellow (destaque)
    "secondary": "#EAAA00",      # Gold mais profundo
    "dark": "#1A1A2E",           # Azul escuro profundo (fundo sidebar)
    "darker": "#0F0F1A",         # Quase preto
    "surface": "#16213E",         # Azul superfície
    "text_primary": "#FFFFFF",   # Texto principal
    "text_secondary": "#A0AEC0", # Texto secundário
    "text_muted": "#718096",     # Texto suave
    "accent": "#00B4D8",         # Cyan (contraste)
    "success": "#48BB78",        # Verde
    "border": "#2D3748",         # Bordas
    "card_bg": "#1E293B",        # Fundo cards
    "hover": "#2D3748",          # Hover
}

# ============================================================
# CSS CUSTOMIZADO - SIDEBAR MODERNA E MINIMALISTA
# ============================================================
custom_css = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    * {{
        font-family: 'Inter', sans-serif !important;
    }}

    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {COLORS["dark"]} 0%, {COLORS["darker"]} 100%) !important;
        border-right: 1px solid {COLORS["border"]} !important;
    }}

    [data-testid="stSidebar"] > div:first-child {{
        background: transparent !important;
    }}

    /* Esconde o toggle padrão do Streamlit */
    [data-testid="stSidebar"] button[kind="headerNoPadding"] {{
        display: none !important;
    }}

    /* ===== MAIN AREA ===== */
    .main .block-container {{
        padding: 2rem 3rem !important;
        max-width: 1400px !important;
        background: {COLORS["darker"]} !important;
    }}

    /* ===== TIPOGRAFIA ===== */
    h1, h2, h3, h4, h5, h6 {{
        color: {COLORS["text_primary"]} !important;
        font-weight: 700 !important;
    }}

    p, span, div {{
        color: {COLORS["text_secondary"]} !important;
    }}

    /* ===== BOTÃO COLLAPSE CUSTOM ===== */
    .collapse-btn {{
        position: fixed;
        top: 1rem;
        left: 1rem;
        z-index: 999999;
        background: {COLORS["surface"]};
        border: 1px solid {COLORS["border"]};
        border-radius: 8px;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        color: {COLORS["text_primary"]};
        font-size: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}

    .collapse-btn:hover {{
        background: {COLORS["primary"]};
        color: {COLORS["dark"]};
        transform: scale(1.05);
    }}

    /* ===== CARDS DE PROJETO ===== */
    .pbi-card {{
        background: {COLORS["card_bg"]};
        border: 1px solid {COLORS["border"]};
        border-radius: 16px;
        padding: 1.5rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }}

    .pbi-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, {COLORS["primary"]}, {COLORS["accent"]});
        opacity: 0;
        transition: opacity 0.3s ease;
    }}

    .pbi-card:hover {{
        transform: translateY(-4px);
        border-color: {COLORS["primary"]};
        box-shadow: 0 20px 40px rgba(242, 200, 17, 0.1);
    }}

    .pbi-card:hover::before {{
        opacity: 1;
    }}

    .pbi-card-icon {{
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }}

    .pbi-card-title {{
        color: {COLORS["text_primary"]} !important;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }}

    .pbi-card-desc {{
        color: {COLORS["text_muted"]} !important;
        font-size: 0.85rem;
        line-height: 1.5;
        margin-bottom: 1rem;
    }}

    .pbi-card-category {{
        display: inline-block;
        background: {COLORS["surface"]};
        color: {COLORS["accent"]} !important;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 500;
        border: 1px solid {COLORS["border"]};
    }}

    /* ===== HEADER ===== */
    .main-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2rem;
        padding-bottom: 1.5rem;
        border-bottom: 1px solid {COLORS["border"]};
    }}

    .main-header h1 {{
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, {COLORS["primary"]}, {COLORS["accent"]});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}

    .main-header p {{
        color: {COLORS["text_muted"]} !important;
        font-size: 1rem;
        margin-top: 0.25rem;
    }}

    /* ===== FILTROS ===== */
    .filter-container {{
        display: flex;
        gap: 1rem;
        margin-bottom: 2rem;
        flex-wrap: wrap;
    }}

    .filter-pill {{
        background: {COLORS["card_bg"]};
        border: 1px solid {COLORS["border"]};
        color: {COLORS["text_secondary"]};
        padding: 8px 20px;
        border-radius: 25px;
        cursor: pointer;
        transition: all 0.2s ease;
        font-size: 0.85rem;
        font-weight: 500;
    }}

    .filter-pill:hover {{
        border-color: {COLORS["primary"]};
        color: {COLORS["primary"]};
    }}

    .filter-pill.active {{
        background: {COLORS["primary"]};
        color: {COLORS["dark"]} !important;
        border-color: {COLORS["primary"]};
        font-weight: 600;
    }}

    /* ===== SIDEBAR LOGO ===== */
    .sidebar-logo {{
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 1.5rem 1rem;
        margin-bottom: 1rem;
        border-bottom: 1px solid {COLORS["border"]};
    }}

    .sidebar-logo-icon {{
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, {COLORS["primary"]}, {COLORS["secondary"]});
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
    }}

    .sidebar-logo-text {{
        color: {COLORS["text_primary"]} !important;
        font-size: 1.3rem;
        font-weight: 700;
    }}

    .sidebar-logo-sub {{
        color: {COLORS["text_muted"]} !important;
        font-size: 0.75rem;
    }}

    /* ===== MENU ITEMS ===== */
    .menu-item {{
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px 16px;
        margin: 2px 8px;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.2s ease;
        color: {COLORS["text_secondary"]};
        font-size: 0.9rem;
        font-weight: 500;
    }}

    .menu-item:hover {{
        background: {COLORS["hover"]};
        color: {COLORS["text_primary"]};
    }}

    .menu-item.active {{
        background: linear-gradient(135deg, {COLORS["primary"]}20, {COLORS["accent"]}10);
        color: {COLORS["primary"]};
        border-left: 3px solid {COLORS["primary"]};
    }}

    .menu-item-icon {{
        font-size: 1.2rem;
        width: 24px;
        text-align: center;
    }}

    /* ===== SUBMENU ===== */
    .submenu {{
        margin-left: 2rem;
        border-left: 2px solid {COLORS["border"]};
        padding-left: 0.5rem;
    }}

    .submenu-item {{
        padding: 8px 16px;
        color: {COLORS["text_muted"]};
        font-size: 0.85rem;
        cursor: pointer;
        transition: all 0.2s ease;
        border-radius: 6px;
    }}

    .submenu-item:hover {{
        color: {COLORS["text_primary"]};
        background: {COLORS["hover"]};
    }}

    .submenu-item.active {{
        color: {COLORS["primary"]};
    }}

    /* ===== IFRAME EMBED ===== */
    .embed-container {{
        position: relative;
        width: 100%;
        height: 85vh;
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid {COLORS["border"]};
    }}

    .embed-container iframe {{
        width: 100%;
        height: 100%;
        border: none;
    }}

    /* ===== FOOTER SIDEBAR ===== */
    .sidebar-footer {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 1rem;
        border-top: 1px solid {COLORS["border"]};
        text-align: center;
    }}

    .sidebar-footer p {{
        color: {COLORS["text_muted"]} !important;
        font-size: 0.75rem;
    }}

    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar {{
        width: 6px;
    }}

    ::-webkit-scrollbar-track {{
        background: {COLORS["darker"]};
    }}

    ::-webkit-scrollbar-thumb {{
        background: {COLORS["border"]};
        border-radius: 3px;
    }}

    ::-webkit-scrollbar-thumb:hover {{
        background: {COLORS["primary"]};
    }}

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {{
        .main .block-container {{
            padding: 1rem !important;
        }}

        .main-header h1 {{
            font-size: 1.5rem;
        }}
    }}

    /* Esconde elementos padrão do Streamlit que atrapalham */
    header[data-testid="stHeader"] {{
        display: none !important;
    }}

    footer {{
        display: none !important;
    }}

    /* Ajusta o espaço do topo quando sidebar está colapsada */
    .stApp {{
        margin-top: 0 !important;
    }}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ============================================================
# DADOS DOS PROJETOS POWER BI
# ============================================================
PBI_PROJECTS = [
    {
        "title": "Transporte - Travel Company",
        "icon": "🚛",
        "category": "Operações & Logística",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiNjY5NThlNjctZWY1Ny00YjA0LTk0MjEtNzhiNjgzZjdjZjA2IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Transforme dados logísticos em vantagem competitiva. Analise indicadores de performance operacional, identifique ineficiências e otimize custos."
    },
    {
        "title": "Dashboard ANATEL - Reclamações",
        "icon": "📞",
        "category": "Operações & Logística",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZjBjMjg2NWItMWY5Yi00MDYwLThhZTUtOTBjZWMzZGM2MjIyIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Monitoramento de reclamações gerais da ANATEL. Perfeito para identificar gargalos de atendimento, tendências e disparadores de insatisfação."
    },
    {
        "title": "Dashboard OEE - Eficiência Industrial",
        "icon": "🏭",
        "category": "Operações & Logística",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2YxN2NhZmQtMTg4My00YTgwLWJhOGQtZmRkNGZkNTM1ZDM0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Acompanhe disponibilidade, desempenho e qualidade de produção industrial em tempo real, mitigando as perdas ocultas do chão de fábrica."
    },
    {
        "title": "Portal da Transparência - Ilhéus",
        "icon": "🏛️",
        "category": "Setor Público & Geral",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTM2ZWFlM2QtOTc2NC00NDQ2LTg2ZTctOGY5Nzc4YTk2YWM1IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Auditoria de dados públicos municipais simplificada. Transparência visual clara de receitas, despesas empenhadas e investimentos de Ilhéus."
    },
    {
        "title": "DRE Estratégico — Finanças",
        "icon": "💰",
        "category": "Estratégico & Financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiOWE0ZmU3ZTMtYzAyYi00NDE1LTg3YWItYjcxZTE2ZWI2OWRjIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Demonstrativo de Resultados estruturado com análises vertical e horizontal automáticas. Avalie margens de contribuição e lucratividade real."
    },
    {
        "title": "Monitoramento de Vagas — Bradesco",
        "icon": "👔",
        "category": "RH & People Analytics",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMjQxN2Q4NGYtNWRmNy00NWVjLWE4YmQtNWMyNWYwNGYyZDUzIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Visão consolidada do fluxo interno de contratações do banco. Mapeamento por praças regionais, perfis técnicos de entrada e status de posições."
    },
    {
        "title": "Relatório STONE - Faturamento B2B",
        "icon": "💳",
        "category": "Estratégico & Financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Acompanhamento granular de performance de adquirência de cartões. Métricas de Ticket Médio, faturamento bruto e fatias de mercado."
    },
    {
        "title": "Vendas Meta vs Realizado",
        "icon": "🎯",
        "category": "Estratégico & Financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Gestão comercial cirúrgica. Identifique rapidamente quais filiais ou vendedores estão performando abaixo da linha de corte esperada."
    },
    {
        "title": "Controle de Pedidos BNZ",
        "icon": "📦",
        "category": "Operações & Logística",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZDZlNzViNzMtODllZS00OTVlLWI4MWQtNzBhZmU5ZTkxY2E0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Níveis de estoque e giro de produtos atualizados. Ideal para evitar rupturas de prateleira e excessos de capital imobilizado."
    },
    {
        "title": "Análise Dados Estratégica",
        "icon": "📈",
        "category": "Estratégico & Financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Visão unificada para C-Level. Consolidação ágil de múltiplos vetores de crescimento e gaps de eficiência organizacional interna."
    },
    {
        "title": "People Analytics (RH)",
        "icon": "👥",
        "category": "RH & People Analytics",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Inteligência de departamento pessoal: Funil de R&S, turnover, custos associados a comissões e bonificações integradas por performance."
    },
    {
        "title": "Relatório Borelli",
        "icon": "🚀",
        "category": "Operações & Logística",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZTY5YmEzZmQtZDVhMS00N2QyLWJhY2QtMDNhMWFmMDRjMjNmIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Mapeamento minucioso do ciclo de produção industrial. Identificação ágil de gargalos e taxas de ociosidade de maquinário."
    },
    {
        "title": "Financeiro — Beocean Resort",
        "icon": "🏖️",
        "category": "Estratégico & Financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9",
        "desc": "Fluxo de caixa corporativo adaptado para redes de hotelaria. Gestão centralizada de canais de receita direta e custos operacionais fixos."
    }
]

# ============================================================
# ESTADO DA SIDEBAR
# ============================================================
if "sidebar_collapsed" not in st.session_state:
    st.session_state.sidebar_collapsed = False

if "selected_project" not in st.session_state:
    st.session_state.selected_project = None

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "Todos"

# ============================================================
# BOTÃO DE COLLAPSE/EXPAND (JavaScript injetado)
# ============================================================
collapse_js = """
<script>
    // Função para alternar sidebar
    function toggleSidebar() {
        const sidebar = window.parent.document.querySelector('[data-testid="stSidebar"]');
        const btn = window.parent.document.querySelector('.collapse-btn');

        if (sidebar) {
            const isExpanded = sidebar.getAttribute('aria-expanded') === 'true';

            if (isExpanded) {
                sidebar.setAttribute('aria-expanded', 'false');
                sidebar.style.marginLeft = '-350px';
                sidebar.style.width = '0px';
                if (btn) btn.innerHTML = '☰';
            } else {
                sidebar.setAttribute('aria-expanded', 'true');
                sidebar.style.marginLeft = '0px';
                sidebar.style.width = '350px';
                if (btn) btn.innerHTML = '✕';
            }
        }
    }

    // Cria o botão de collapse
    function createCollapseButton() {
        let btn = window.parent.document.querySelector('.collapse-btn');
        if (!btn) {
            btn = document.createElement('button');
            btn.className = 'collapse-btn';
            btn.innerHTML = '✕';
            btn.title = 'Toggle Sidebar';
            btn.onclick = toggleSidebar;
            window.parent.document.body.appendChild(btn);
        }
    }

    // Executa após carregar
    setTimeout(createCollapseButton, 500);

    // Recria se necessário
    setInterval(createCollapseButton, 2000);
</script>
"""

html(collapse_js, height=0)

# ============================================================
# SIDEBAR - MENU E SUBMENUS
# ============================================================
with st.sidebar:
    # Logo
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-icon">📊</div>
        <div>
            <div class="sidebar-logo-text">PBI Portfolio</div>
            <div class="sidebar-logo-sub">Power BI Dashboards</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Menu Principal
    st.markdown("<div style='color: #718096; font-size: 0.7rem; font-weight: 600; padding: 0 1rem; margin-bottom: 0.5rem; letter-spacing: 1px;'>MENU PRINCIPAL</div>", unsafe_allow_html=True)

    menu_items = [
        ("🏠", "Dashboard", "dashboard"),
        ("🏢", "Instituição", "institution"),
    ]

    for icon, label, key in menu_items:
        active = st.session_state.get("menu_selected", "dashboard") == key
        css_class = "menu-item active" if active else "menu-item"
        st.markdown(f"""
        <div class="{css_class}" onclick="window.parent.postMessage({{type: 'menu_click', key: '{key}'}}, '*')">
            <span class="menu-item-icon">{icon}</span>
            <span>{label}</span>
        </div>
        """, unsafe_allow_html=True)

    # Menu com Submenu - Estudantes
    st.markdown("<div style='height: 1rem;'></div>")
    st.markdown("<div style='color: #718096; font-size: 0.7rem; font-weight: 600; padding: 0 1rem; margin-bottom: 0.5rem; letter-spacing: 1px;'>GESTÃO</div>", unsafe_allow_html=True)

    # Expanders para submenus (estilo acordeão)
    with st.expander("👥 Gerenciar Estudantes", expanded=False):
        st.markdown("""
        <div class="submenu">
            <div class="submenu-item">📋 Informações dos Estudantes</div>
            <div class="submenu-item">💰 Pagamentos dos Estudantes</div>
            <div class="submenu-item">📊 Transações dos Estudantes</div>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("👨‍🏫 Gerenciar Professores", expanded=False):
        st.markdown("""
        <div class="submenu">
            <div class="submenu-item">📋 Informações dos Professores</div>
            <div class="submenu-item">💵 Salários dos Professores</div>
            <div class="submenu-item">📊 Transações dos Professores</div>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("💼 Gerenciar Finanças", expanded=False):
        st.markdown("""
        <div class="submenu">
            <div class="submenu-item">📈 Relatórios Financeiros</div>
            <div class="submenu-item">💳 Contas a Pagar</div>
            <div class="submenu-item">💰 Contas a Receber</div>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="sidebar-footer">
        <p>© 2026 PBI Portfolio</p>
        <p style="font-size: 0.65rem;">Powered by Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# CONTEÚDO PRINCIPAL
# ============================================================

# Se um projeto foi selecionado, mostra o embed
if st.session_state.selected_project is not None:
    project = PBI_PROJECTS[st.session_state.selected_project]

    # Header com botão voltar
    col1, col2 = st.columns([1, 10])
    with col1:
        if st.button("← Voltar", use_container_width=True):
            st.session_state.selected_project = None
            st.rerun()
    with col2:
        st.markdown(f"""
        <div class="main-header" style="margin-bottom: 1rem;">
            <div>
                <h1>{project["icon"]} {project["title"]}</h1>
                <p>{project["category"]} • Power BI Embedded</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Embed do Power BI
    st.markdown(f"""
    <div class="embed-container">
        <iframe 
            src="{project["url"]}" 
            frameborder="0" 
            allowFullScreen="true">
        </iframe>
    </div>
    """, unsafe_allow_html=True)

else:
    # Página inicial - Grid de projetos
    st.markdown("""
    <div class="main-header">
        <div>
            <h1>📊 Portfólio Power BI</h1>
            <p>Dashboards interativos e relatórios estratégicos</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Filtros por categoria
    categories = ["Todos"] + sorted(list(set(p["category"] for p in PBI_PROJECTS)))

    cols = st.columns(len(categories))
    for i, cat in enumerate(categories):
        with cols[i]:
            is_active = st.session_state.selected_category == cat
            btn_style = "primary" if is_active else "secondary"
            if st.button(cat, key=f"cat_{cat}", use_container_width=True, type=btn_style):
                st.session_state.selected_category = cat
                st.rerun()

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

    # Filtra projetos
    filtered = PBI_PROJECTS if st.session_state.selected_category == "Todos" else [
        p for p in PBI_PROJECTS if p["category"] == st.session_state.selected_category
    ]

    # Grid de cards
    cols_per_row = 3
    for i in range(0, len(filtered), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, col in enumerate(cols):
            idx = i + j
            if idx < len(filtered):
                project = filtered[idx]
                with col:
                    card_html = f"""
                    <div class="pbi-card" onclick="window.parent.postMessage({{type: 'project_click', index: {PBI_PROJECTS.index(project)}}}, '*')">
                        <div class="pbi-card-icon">{project["icon"]}</div>
                        <div class="pbi-card-title">{project["title"]}</div>
                        <div class="pbi-card-desc">{project["desc"]}</div>
                        <div class="pbi-card-category">{project["category"]}</div>
                    </div>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)

                    # Botão invisível para capturar clique
                    if st.button("Abrir Dashboard", key=f"btn_{idx}", use_container_width=True):
                        st.session_state.selected_project = PBI_PROJECTS.index(project)
                        st.rerun()

    # Estatísticas
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    st.markdown("---")

    stats_cols = st.columns(4)
    with stats_cols[0]:
        st.metric("Total de Projetos", len(PBI_PROJECTS))
    with stats_cols[1]:
        st.metric("Categorias", len(set(p["category"] for p in PBI_PROJECTS)))
    with stats_cols[2]:
        st.metric("Operações & Logística", len([p for p in PBI_PROJECTS if p["category"] == "Operações & Logística"]))
    with stats_cols[3]:
        st.metric("Financeiro", len([p for p in PBI_PROJECTS if p["category"] == "Estratégico & Financeiro"]))
