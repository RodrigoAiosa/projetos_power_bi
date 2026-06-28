import streamlit as st
from streamlit.components.v1 import html
from collections import defaultdict

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
COLORS = {
    "primary": "#F2C811",
    "secondary": "#EAAA00",
    "dark": "#1A1A2E",
    "darker": "#0F0F1A",
    "surface": "#16213E",
    "text_primary": "#FFFFFF",
    "text_secondary": "#A0AEC0",
    "text_muted": "#718096",
    "accent": "#00B4D8",
    "border": "#2D3748",
    "card_bg": "#1E293B",
    "hover": "#2D3748",
}

# ============================================================
# CSS CUSTOMIZADO
# ============================================================
custom_css = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {{ font-family: 'Inter', sans-serif !important; }}
    
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {COLORS["dark"]} 0%, {COLORS["darker"]} 100%) !important;
        border-right: 1px solid {COLORS["border"]} !important;
        min-width: 320px !important;
        max-width: 320px !important;
    }}
    
    [data-testid="stSidebar"] > div:first-child {{
        background: transparent !important;
        padding-top: 0 !important;
    }}
    
    [data-testid="stSidebar"] button[kind="headerNoPadding"] {{
        display: none !important;
    }}
    
    .main .block-container {{
        padding: 2rem 3rem !important;
        max-width: 1400px !important;
        background: {COLORS["darker"]} !important;
    }}
    
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
    
    .sidebar-logo {{
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 1.5rem 1rem;
        margin-bottom: 0.5rem;
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
    
    .menu-section-label {{
        color: {COLORS["text_muted"]};
        font-size: 0.65rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        padding: 1rem 1rem 0.5rem 1rem;
        margin-top: 0.5rem;
    }}
    
    .main-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.5rem;
        padding-bottom: 1.5rem;
        border-bottom: 1px solid {COLORS["border"]};
    }}
    
    .main-header h1 {{
        font-size: 1.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, {COLORS["primary"]}, {COLORS["accent"]});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    
    .main-header p {{
        color: {COLORS["text_muted"]} !important;
        font-size: 0.95rem;
        margin-top: 0.25rem;
    }}
    
    .embed-container {{
        position: relative;
        width: 100%;
        height: 85vh;
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid {COLORS["border"]};
        background: {COLORS["card_bg"]};
    }}
    
    .embed-container iframe {{
        width: 100%;
        height: 100%;
        border: none;
    }}
    
    .sidebar-footer {{
        position: sticky;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 1rem;
        border-top: 1px solid {COLORS["border"]};
        background: {COLORS["darker"]};
        text-align: center;
        margin-top: auto;
    }}
    
    .sidebar-footer p {{
        color: {COLORS["text_muted"]} !important;
        font-size: 0.7rem;
        margin: 0;
    }}
    
    ::-webkit-scrollbar {{ width: 5px; }}
    ::-webkit-scrollbar-track {{ background: {COLORS["darker"]}; }}
    ::-webkit-scrollbar-thumb {{ background: {COLORS["border"]}; border-radius: 3px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: {COLORS["primary"]}; }}
    
    header[data-testid="stHeader"] {{ display: none !important; }}
    footer {{ display: none !important; }}
    
    @media (max-width: 768px) {{
        .main .block-container {{ padding: 1rem !important; }}
        .main-header h1 {{ font-size: 1.4rem; }}
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
        "title": "Controle de Pedidos BNZ",
        "icon": "📦",
        "category": "Operações & Logística",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZDZlNzViNzMtODllZS00OTVlLWI4MWQtNzBhZmU5ZTkxY2E0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Níveis de estoque e giro de produtos atualizados. Ideal para evitar rupturas de prateleira e excessos de capital imobilizado."
    },
    {
        "title": "Relatório Borelli",
        "icon": "🚀",
        "category": "Operações & Logística",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZTY5YmEzZmQtZDVhMS00N2QyLWJhY2QtMDNhMWFmMDRjMjNmIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Mapeamento minucioso do ciclo de produção industrial. Identificação ágil de gargalos e taxas de ociosidade de maquinário."
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
        "title": "Análise Dados Estratégica",
        "icon": "📈",
        "category": "Estratégico & Financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Visão unificada para C-Level. Consolidação ágil de múltiplos vetores de crescimento e gaps de eficiência organizacional interna."
    },
    {
        "title": "Financeiro — Beocean Resort",
        "icon": "🏖️",
        "category": "Estratégico & Financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9",
        "desc": "Fluxo de caixa corporativo adaptado para redes de hotelaria. Gestão centralizada de canais de receita direta e custos operacionais fixos."
    },
    {
        "title": "Monitoramento de Vagas — Bradesco",
        "icon": "👔",
        "category": "RH & People Analytics",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMjQxN2Q4NGYtNWRmNy00NWVjLWE4YmQtNWMyNWYwNGYyZDUzIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Visão consolidada do fluxo interno de contratações do banco. Mapeamento por praças regionais, perfis técnicos de entrada e status de posições."
    },
    {
        "title": "People Analytics (RH)",
        "icon": "👥",
        "category": "RH & People Analytics",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Inteligência de departamento pessoal: Funil de R&S, turnover, custos associados a comissões e bonificações integradas por performance."
    },
]

# Agrupa projetos por categoria
projects_by_category = defaultdict(list)
for p in PBI_PROJECTS:
    projects_by_category[p["category"]].append(p)

CATEGORY_ICONS = {
    "Operações & Logística": "⚙️",
    "Estratégico & Financeiro": "💹",
    "RH & People Analytics": "👤",
    "Setor Público & Geral": "🏛️",
}

# ============================================================
# ESTADO DA SESSÃO
# ============================================================
if "selected_project" not in st.session_state:
    st.session_state.selected_project = None

if "expanded_categories" not in st.session_state:
    st.session_state.expanded_categories = set(projects_by_category.keys())

# ============================================================
# BOTÃO COLLAPSE (JavaScript)
# ============================================================
collapse_js = """
<script>
    function toggleSidebar() {
        const sidebar = window.parent.document.querySelector('[data-testid="stSidebar"]');
        const btn = window.parent.document.querySelector('.collapse-btn');
        if (sidebar) {
            const isExpanded = sidebar.style.marginLeft !== '-320px';
            if (isExpanded) {
                sidebar.style.marginLeft = '-320px';
                sidebar.style.width = '0px';
                if (btn) btn.innerHTML = '☰';
            } else {
                sidebar.style.marginLeft = '0px';
                sidebar.style.width = '320px';
                if (btn) btn.innerHTML = '✕';
            }
        }
    }
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
    setTimeout(createCollapseButton, 500);
    setInterval(createCollapseButton, 2000);
</script>
"""
html(collapse_js, height=0)

# ============================================================
# SIDEBAR - CATEGORIAS E PROJETOS
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
    
    # Label de seção
    st.markdown('<div class="menu-section-label">📁 Categorias</div>', unsafe_allow_html=True)
    
    # Renderiza cada categoria e seus projetos
    for cat_name, projects in projects_by_category.items():
        cat_icon = CATEGORY_ICONS.get(cat_name, "📁")
        is_expanded = cat_name in st.session_state.expanded_categories
        
        # Botão da categoria (toggle expand)
        cat_label = f"{cat_icon} {cat_name}"
        if st.button(
            f"{cat_label} ({len(projects)})",
            key=f"cat_{cat_name}",
            use_container_width=True,
            type="secondary" if not is_expanded else "primary"
        ):
            if is_expanded:
                st.session_state.expanded_categories.discard(cat_name)
            else:
                st.session_state.expanded_categories.add(cat_name)
            st.rerun()
        
        # Se expandido, mostra os projetos
        if is_expanded:
            for proj in projects:
                proj_idx = PBI_PROJECTS.index(proj)
                is_selected = st.session_state.selected_project == proj_idx
                
                btn_type = "primary" if is_selected else "secondary"
                if st.button(
                    f"{proj['icon']} {proj['title']}",
                    key=f"proj_{proj_idx}",
                    use_container_width=True,
                    type=btn_type
                ):
                    st.session_state.selected_project = proj_idx
                    st.rerun()
    
    # Footer
    st.markdown("""
    <div class="sidebar-footer">
        <p>© 2026 PBI Portfolio • Powered by Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# CONTEÚDO PRINCIPAL
# ============================================================
if st.session_state.selected_project is not None:
    project = PBI_PROJECTS[st.session_state.selected_project]
    
    # Header com botão voltar
    col1, col2 = st.columns([1, 12])
    with col1:
        if st.button("←", use_container_width=True, help="Voltar para lista"):
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
    # Página inicial
    st.markdown("""
    <div class="main-header">
        <div>
            <h1>📊 Portfólio Power BI</h1>
            <p>Selecione um dashboard no menu lateral para visualizar</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Grid de projetos
    cols_per_row = 3
    for i in range(0, len(PBI_PROJECTS), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, col in enumerate(cols):
            idx = i + j
            if idx < len(PBI_PROJECTS):
                proj = PBI_PROJECTS[idx]
                with col:
                    with st.container():
                        st.markdown(f"### {proj['icon']} {proj['title']}")
                        st.caption(f"🏷️ {proj['category']}")
                        st.write(proj['desc'])
                        if st.button("▶️ Abrir Dashboard", key=f"open_{idx}", use_container_width=True):
                            st.session_state.selected_project = idx
                            st.rerun()
                        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    # Estatísticas
    st.markdown("---")
    stats = st.columns(4)
    stats[0].metric("📊 Total", len(PBI_PROJECTS))
    stats[1].metric("📁 Categorias", len(projects_by_category))
    stats[2].metric("⚙️ Operações", len(projects_by_category.get("Operações & Logística", [])))
    stats[3].metric("💹 Financeiro", len(projects_by_category.get("Estratégico & Financeiro", [])))
