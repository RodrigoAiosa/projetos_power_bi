import streamlit as st
from collections import defaultdict

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Portfólio Power BI | Dashboards que Transformam Dados em Lucro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# ESTILO LANDING PAGE PREMIUM — FULL SCREEN, SEM SIDEBAR
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .main, [data-testid="stAppViewContainer"] {
    background-color: #060912 !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(0,180,216,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 80% 60%, rgba(0,100,180,0.06) 0%, transparent 50%);
}

[data-testid="stHeader"] { background: transparent !important; }

/* Remove sidebar completamente */
[data-testid="stSidebar"] { display: none !important; }
[data-testid="stSidebarCollapsedControl"] { display: none !important; }

.block-container {
    max-width: 1400px !important;
    padding: 0 2rem 4rem 2rem !important;
}

/* ===== NAVBAR FIXO ===== */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 40px;
    background: rgba(6, 9, 18, 0.8);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255,255,255,0.04);
}

.navbar-logo {
    display: flex;
    align-items: center;
    gap: 10px;
}

.navbar-logo-icon {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #00b4d8, #0077b6);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
}

.navbar-logo-text {
    font-family: 'Syne', sans-serif !important;
    color: #f0f4ff;
    font-size: 1.1rem;
    font-weight: 700;
}

.navbar-links {
    display: flex;
    gap: 32px;
    align-items: center;
}

.navbar-links a {
    color: #94a3b8;
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
    transition: color 0.3s ease;
    cursor: pointer;
}

.navbar-links a:hover {
    color: #00b4d8;
}

.navbar-cta {
    background: linear-gradient(135deg, #00b4d8, #0077b6);
    color: #ffffff !important;
    padding: 8px 20px;
    border-radius: 8px;
    font-size: 0.8rem;
    font-weight: 700;
    text-decoration: none !important;
    transition: opacity 0.3s ease;
    border: none;
    cursor: pointer;
}

.navbar-cta:hover { opacity: 0.9; }

/* ===== HERO SECTION ===== */
.hero-section {
    text-align: center;
    padding: 140px 20px 60px;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
}

.hero-badge {
    display: inline-block;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #00b4d8;
    border: 1px solid rgba(0,180,216,0.25);
    background: rgba(0,180,216,0.06);
    padding: 7px 18px;
    border-radius: 100px;
    margin-bottom: 24px;
}

.hero-title {
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(2.5rem, 5.5vw, 4.5rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -2px;
    color: #f0f4ff;
    margin-bottom: 24px;
    max-width: 900px;
}

.hero-title .accent {
    background: linear-gradient(135deg, #00b4d8 0%, #48cae4 50%, #90e0ef 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 1.15rem;
    font-weight: 300;
    color: #7b8ba8;
    max-width: 560px;
    margin-bottom: 40px;
    line-height: 1.7;
}

.hero-cta-row {
    display: flex;
    gap: 16px;
    margin-bottom: 60px;
    flex-wrap: wrap;
    justify-content: center;
}

.hero-cta-primary {
    background: linear-gradient(135deg, #00b4d8, #0077b6);
    color: #ffffff !important;
    padding: 14px 32px;
    border-radius: 12px;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700;
    font-size: 0.9rem;
    text-decoration: none !important;
    transition: all 0.3s ease;
    border: none;
    cursor: pointer;
    box-shadow: 0 8px 30px rgba(0,180,216,0.25);
}

.hero-cta-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(0,180,216,0.35);
}

.hero-cta-secondary {
    background: rgba(255,255,255,0.03);
    color: #94a3b8 !important;
    padding: 14px 32px;
    border-radius: 12px;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600;
    font-size: 0.9rem;
    text-decoration: none !important;
    transition: all 0.3s ease;
    border: 1px solid rgba(255,255,255,0.08);
    cursor: pointer;
}

.hero-cta-secondary:hover {
    border-color: rgba(0,180,216,0.3);
    color: #00b4d8 !important;
}

/* ===== STATS BAR ===== */
.stats-bar {
    display: flex;
    justify-content: center;
    gap: 60px;
    flex-wrap: wrap;
    padding: 30px 20px;
    background: rgba(255,255,255,0.015);
    border: 1px solid rgba(255,255,255,0.04);
    border-radius: 20px;
    max-width: 800px;
    width: 100%;
    backdrop-filter: blur(10px);
}

.stat-item { text-align: center; }
.stat-number {
    font-family: 'Syne', sans-serif !important;
    font-size: 2.2rem;
    font-weight: 800;
    color: #00b4d8;
    line-height: 1;
}
.stat-label {
    font-size: 0.7rem;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 8px;
}

/* ===== SECTION HEADERS ===== */
.section-header {
    text-align: center;
    padding: 80px 20px 40px;
}

.section-label {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #00b4d8;
    margin-bottom: 12px;
}

.section-title {
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(1.8rem, 3vw, 2.8rem);
    font-weight: 800;
    color: #f0f4ff;
    line-height: 1.2;
    margin-bottom: 16px;
}

.section-desc {
    font-size: 1rem;
    color: #64748b;
    max-width: 500px;
    margin: 0 auto;
    line-height: 1.6;
}

/* ===== CATEGORY TABS ===== */
.category-tabs {
    display: flex;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
    padding: 0 20px 40px;
}

/* ===== CARDS GRID ===== */
[data-testid="stHorizontalBlock"] {
    align-items: stretch !important;
}

[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    display: flex !important;
    flex-direction: column !important;
}

[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] > [data-testid="stVerticalBlockBorderWrapper"],
[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] > div {
    height: 100% !important;
    flex: 1 !important;
}

.ux-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.035) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 20px;
    padding: 28px;
    height: 100%;
    min-height: 340px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
}

.ux-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,216,0.3), transparent);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.ux-card:hover {
    transform: translateY(-8px);
    border-color: rgba(0,180,216,0.25);
    box-shadow: 0 20px 50px rgba(0,180,216,0.08);
}

.ux-card:hover::before {
    opacity: 1;
}

.card-top { display: flex; gap: 16px; align-items: flex-start; margin-bottom: 20px; }
.card-icon-box {
    font-size: 32px;
    background: rgba(0,180,216,0.06);
    padding: 12px;
    border-radius: 14px;
    border: 1px solid rgba(0,180,216,0.1);
    line-height: 1;
    flex-shrink: 0;
}
.ux-card-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.15rem;
    font-weight: 700;
    color: #f0f4ff;
    line-height: 1.3;
    margin-top: 4px;
}

.card-category-tag {
    display: inline-block;
    font-size: 0.65rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #00b4d8;
    background: rgba(0,180,216,0.08);
    padding: 4px 10px;
    border-radius: 6px;
    margin-bottom: 12px;
    border: 1px solid rgba(0,180,216,0.15);
}

.ux-card-desc {
    font-size: 0.88rem;
    color: #94a3b8;
    line-height: 1.65;
    margin-bottom: 24px;
    flex-grow: 1;
}

.card-actions { display: flex; flex-direction: column; gap: 14px; margin-top: auto; }

.btn-direct {
    background: linear-gradient(135deg, #00b4d8, #0077b6);
    color: #ffffff !important;
    padding: 14px;
    border-radius: 12px;
    text-align: center;
    text-decoration: none !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700;
    font-size: 0.85rem;
    letter-spacing: 0.5px;
    transition: all 0.3s ease;
    display: block;
    border: none;
    cursor: pointer;
    width: 100%;
}

.btn-direct:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,180,216,0.3);
}

.share-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255,255,255,0.04);
    padding-top: 14px;
}

.share-txt { font-size: 0.72rem; color: #475569; font-weight: 500; }
.share-links { display: flex; gap: 8px; }

.share-btn-item {
    display: flex;
    align-items: center;
    gap: 5px;
    padding: 6px 10px;
    border-radius: 6px;
    font-size: 0.72rem;
    font-weight: 600;
    text-decoration: none !important;
    transition: all 0.2s;
}
.share-btn-item.wa {
    background: rgba(37, 211, 102, 0.08);
    color: #25D366 !important;
    border: 1px solid rgba(37, 211, 102, 0.15);
}
.share-btn-item.wa:hover { background: rgba(37, 211, 102, 0.15); }
.share-btn-item.li {
    background: rgba(10, 102, 194, 0.08);
    color: #0A66C2 !important;
    border: 1px solid rgba(10, 102, 194, 0.15);
}
.share-btn-item.li:hover { background: rgba(10, 102, 194, 0.15); }

/* ===== SEARCH BAR ===== */
div[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.03) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(0,180,216,0.15) !important;
    border-radius: 14px !important;
    padding: 14px 24px !important;
    font-size: 0.95rem !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: rgba(0,180,216,0.5) !important;
    background: rgba(0,180,216,0.02) !important;
    box-shadow: 0 0 20px rgba(0,180,216,0.1);
}

/* ===== EMBED VIEW ===== */
.embed-view {
    padding-top: 80px;
}

.embed-header {
    display: flex;
    align-items: center;
    gap: 20px;
    margin-bottom: 24px;
    padding-bottom: 20px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}

.embed-back-btn {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    color: #94a3b8;
    padding: 10px 18px;
    border-radius: 10px;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 6px;
}

.embed-back-btn:hover {
    border-color: rgba(0,180,216,0.3);
    color: #00b4d8;
}

.embed-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.6rem;
    font-weight: 800;
    color: #f0f4ff;
}

.embed-container {
    position: relative;
    width: 100%;
    height: 82vh;
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(255,255,255,0.015);
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}
.embed-container iframe {
    width: 100%;
    height: 100%;
    border: none;
}

/* ===== FOOTER ===== */
.landing-footer {
    text-align: center;
    padding: 60px 20px 40px;
    border-top: 1px solid rgba(255,255,255,0.04);
    margin-top: 60px;
}

.landing-footer p {
    color: #475569;
    font-size: 0.8rem;
}

.landing-footer .footer-brand {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.2rem;
    font-weight: 700;
    color: #f0f4ff;
    margin-bottom: 8px;
}

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #060912; }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.08); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(0,180,216,0.4); }

/* ===== HIDE STREAMLIT ELEMENTS ===== */
footer { display: none !important; }

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
    .navbar { padding: 12px 20px; }
    .navbar-links { display: none; }
    .hero-section { padding: 100px 16px 40px; }
    .block-container { padding: 0 1rem 2rem 1rem !important; }
    .stats-bar { gap: 30px; padding: 20px; }
    .stat-number { font-size: 1.6rem; }
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# DADOS DOS PROJETOS
# ============================================================
pbi_projects = [
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

# Agrupa por categoria
projects_by_category = defaultdict(list)
for p in pbi_projects:
    projects_by_category[p["category"]].append(p)

CATEGORY_ICONS = {
    "Operações & Logística": "⚙️",
    "Estratégico & Financeiro": "💹",
    "RH & People Analytics": "👤",
    "Setor Público & Geral": "🏛️",
}

CATEGORY_ORDER = ["Estratégico & Financeiro", "Operações & Logística", "RH & People Analytics", "Setor Público & Geral"]

# ============================================================
# ESTADO DA SESSÃO
# ============================================================
if "selected_project" not in st.session_state:
    st.session_state.selected_project = None

if "active_category" not in st.session_state:
    st.session_state.active_category = "Todos"

# ============================================================
# FUNÇÃO: RENDERIZAR CARD
# ============================================================
def render_card(p, idx):
    import urllib.parse

    mensagem_whatsapp = (
        f"Olá! Veja que excelente dashboard de Power BI:\n\n"
        f"📊 *{p['title']}*\n"
        f"ℹ️ {p['desc']}\n\n"
        f"🔗 Aceda ao painel completo aqui: {p['url']}"
    )
    wa_link = f"https://wa.me/?text={urllib.parse.quote(mensagem_whatsapp)}"

    li_base = "https://www.linkedin.com/shareArticle?mini=true"
    li_title = urllib.parse.quote(p['title'])
    li_summary = urllib.parse.quote(f"Solução de BI: {p['desc']}")
    li_url = urllib.parse.quote(p['url'])
    li_link = f"{li_base}&url={li_url}&title={li_title}&summary={li_summary}"

    st.markdown(f"""
    <div class="ux-card">
        <div style="display:flex; flex-direction:column; flex-grow:1;">
            <div class="card-top">
                <div class="card-icon-box">{p['icon']}</div>
                <div>
                    <div class="card-category-tag">{p['category']}</div>
                    <div class="ux-card-title">{p['title']}</div>
                </div>
            </div>
            <div class="ux-card-desc">{p['desc']}</div>
        </div>
        <div class="card-actions">
            <div class="share-row">
                <span class="share-txt">Compartilhar</span>
                <div class="share-links">
                    <a href="{wa_link}" target="_blank" class="share-btn-item wa">
                        <span>📱</span> WhatsApp
                    </a>
                    <a href="{li_link}" target="_blank" class="share-btn-item li">
                        <span>💼</span> LinkedIn
                    </a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("▶️ Visualizar Dashboard", key=f"open_{idx}", use_container_width=True):
        st.session_state.selected_project = idx
        st.rerun()

# ============================================================
# VIEW: DASHBOARD EMBED
# ============================================================
if st.session_state.selected_project is not None:
    project = pbi_projects[st.session_state.selected_project]

    # Navbar minimal no embed
    st.markdown("""
    <div class="navbar">
        <div class="navbar-logo">
            <div class="navbar-logo-icon">📊</div>
            <div class="navbar-logo-text">PBI Portfolio</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="embed-view">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 12])
    with col1:
        if st.button("← Voltar", use_container_width=True):
            st.session_state.selected_project = None
            st.rerun()
    with col2:
        st.markdown(f"""
        <div class="embed-header">
            <div class="embed-title">{project['icon']} {project['title']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="embed-container">
        <iframe src="{project['url']}" frameborder="0" allowFullScreen="true"></iframe>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# VIEW: LANDING PAGE
# ============================================================
else:
    # --- NAVBAR ---
    st.markdown("""
    <div class="navbar">
        <div class="navbar-logo">
            <div class="navbar-logo-icon">📊</div>
            <div class="navbar-logo-text">PBI Portfolio</div>
        </div>
        <div class="navbar-links">
            <a href="#projetos">Projetos</a>
            <a href="#sobre">Sobre</a>
            <a href="#contato">Contato</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    total = len(pbi_projects)
    st.markdown(f"""
    <div class="hero-section">
        <div class="hero-badge">📊 Portfólio de Alta Performance</div>
        <h1 class="hero-title">Dashboards que transformam<br><span class="accent">Dados em Lucro</span></h1>
        <p class="hero-subtitle">Arquitetura de BI de nível corporativo. Explore soluções segmentadas por verticais de negócio e tome decisões baseadas em dados.</p>
        <div class="hero-cta-row">
            <a href="#projetos" class="hero-cta-primary">Explorar Projetos</a>
            <a href="#sobre" class="hero-cta-secondary">Saiba Mais</a>
        </div>
        <div class="stats-bar">
            <div class="stat-item">
                <div class="stat-number">{total}</div>
                <div class="stat-label">Painéis Ativos</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">4</div>
                <div class="stat-label">Verticais</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">100%</div>
                <div class="stat-label">Foco em Decisão</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">+20</div>
                <div class="stat-label">Anos de Experiência</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- SEARCH BAR ---
    st.markdown('<div id="projetos"></div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)

    col_s1, col_s2, col_s3 = st.columns([1, 2, 1])
    with col_s2:
        search_query = st.text_input(
            label="Buscar",
            placeholder="Busque por: RH, Financeiro, Logística, Vendas...",
            key="search_pbi",
            label_visibility="collapsed"
        )

    # --- CATEGORY FILTERS ---
    st.markdown('<div class="category-tabs">', unsafe_allow_html=True)

    cats = ["Todos"] + CATEGORY_ORDER
    filter_cols = st.columns(len(cats))
    for i, cat in enumerate(cats):
        with filter_cols[i]:
            is_active = st.session_state.active_category == cat
            btn_type = "primary" if is_active else "secondary"
            count = total if cat == "Todos" else len(projects_by_category.get(cat, []))
            label = f"{cat} ({count})" if cat != "Todos" else f"📁 Todos ({count})"
            if st.button(label, key=f"filter_{cat}", use_container_width=True, type=btn_type):
                st.session_state.active_category = cat
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    # --- SECTION HEADER ---
    st.markdown("""
    <div class="section-header">
        <div class="section-label">Portfólio</div>
        <h2 class="section-title">Soluções por Categoria</h2>
        <p class="section-desc">Cada dashboard foi desenvolvido com foco em resolver problemas reais de negócio.</p>
    </div>
    """, unsafe_allow_html=True)

    # --- RENDER PROJECTS ---
    if search_query:
        search_terms = search_query.lower().split()
        filtered = []
        for p in pbi_projects:
            text = f"{p['title']} {p['desc']} {p['category']} {p['icon']}".lower()
            if all(t in text for t in search_terms):
                filtered.append(p)

        if filtered:
            st.markdown(f"<p style='color:#64748b; text-align:center; margin-bottom:30px;'>🔍 {len(filtered)} resultado(s) encontrado(s)</p>", unsafe_allow_html=True)
            for i in range(0, len(filtered), 3):
                cols = st.columns(3)
                for j in range(3):
                    idx = i + j
                    if idx < len(filtered):
                        with cols[j]:
                            real_idx = pbi_projects.index(filtered[idx])
                            render_card(filtered[idx], real_idx)
        else:
            st.markdown("""
            <div style="text-align:center; padding: 60px 20px; color: #64748b;">
                <p style="font-size:3rem; margin-bottom:16px;">🔍</p>
                <h3 style="color:#f0f4ff; font-family:'Syne',sans-serif; margin-bottom:8px;">Nenhum resultado encontrado</h3>
                <p>Tente buscar por termos mais amplos ou verifique a ortografia.</p>
            </div>
            """, unsafe_allow_html=True)

    else:
        # Filtra por categoria ativa
        cats_to_show = CATEGORY_ORDER if st.session_state.active_category == "Todos" else [st.session_state.active_category]

        for cat_name in cats_to_show:
            cat_projects = [p for p in pbi_projects if p["category"] == cat_name]
            if not cat_projects:
                continue

            cat_icon = CATEGORY_ICONS.get(cat_name, "📁")
            st.markdown(f"""
            <div style="margin: 50px 0 24px; padding-left: 12px; border-left: 3px solid #00b4d8;">
                <h3 style="font-family:'Syne',sans-serif !important; font-size:1.3rem; font-weight:700; color:#f0f4ff; margin:0;">
                    {cat_icon} {cat_name}
                </h3>
                <p style="color:#64748b; font-size:0.85rem; margin:4px 0 0 0;">{len(cat_projects)} projeto(s) nesta categoria</p>
            </div>
            """, unsafe_allow_html=True)

            for i in range(0, len(cat_projects), 3):
                cols = st.columns(3)
                for j in range(3):
                    idx_proj = i + j
                    if idx_proj < len(cat_projects):
                        with cols[j]:
                            real_idx = pbi_projects.index(cat_projects[idx_proj])
                            render_card(cat_projects[idx_proj], real_idx)

    # --- FOOTER ---
    st.markdown("""
    <div class="landing-footer">
        <div class="footer-brand">📊 PBI Portfolio</div>
        <p>Dashboards Power BI de alta performance para decisões estratégicas.</p>
        <p style="margin-top:16px; font-size:0.7rem; color:#334155;">© 2026 PBI Portfolio • Todos os direitos reservados</p>
    </div>
    """, unsafe_allow_html=True)
