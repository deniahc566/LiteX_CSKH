"""LiteX design system — shared theme tokens and CSS for all pages."""
from pathlib import Path

import streamlit as st

ASSETS = Path(__file__).parent / "assets"
LOGO = ASSETS / "logo.png"
ICON = ASSETS / "icon.png"

BRAND = "#0D87E1"
GRAD_L = "#004DBF"
GRAD_R = "#18BCFF"
TEXT = "#212121"
MUTED = "#888888"
BORDER = "#E8E8E8"
SURFACE = "#FFFFFF"
BG = "#F5F6FA"

_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600;700&display=swap');
html, body, [class*="css"], .stApp {{
  font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Arial, sans-serif;
  color: {TEXT};
}}
.stApp {{ background: {BG}; }}
h1 {{ font-size: 30px !important; font-weight: 700 !important; letter-spacing: -.01em; }}
h2, h3 {{ font-size: 20px !important; font-weight: 600 !important; }}
.lx-eyebrow {{ font-family: 'Outfit', sans-serif; font-weight: 600; text-transform: uppercase;
  letter-spacing: .14em; font-size: 12px; color: {BRAND}; margin-bottom: -6px; }}
.lx-sub {{ color: {MUTED}; font-size: 14px; margin-top: -8px; margin-bottom: 8px; }}
.lx-gradbar {{ height: 4px; border-radius: 4px; margin: 4px 0 18px;
  background: linear-gradient(90deg, {GRAD_L}, {GRAD_R}); }}

/* Buttons */
.stButton > button, .stDownloadButton > button {{
  border-radius: 10px; padding: 9px 18px; font-weight: 500;
  border: 1px solid {BORDER}; background: {SURFACE}; color: {BRAND};
}}
.stButton > button[kind="primary"], .stDownloadButton > button[kind="primary"] {{
  border: none; color: #fff;
  background-image: linear-gradient(90deg, {GRAD_L}, {GRAD_R});
  box-shadow: 0 8px 20px 0 #0C83DF66;
}}
.stButton > button[kind="primary"]:disabled {{ opacity: .45; box-shadow: none; }}

/* Inputs */
.stTextInput input, .stNumberInput input, .stDateInput input, .stTextArea textarea {{
  border-radius: 10px !important;
}}

/* Cards: bordered containers, metrics, expanders, status */
div[data-testid="stVerticalBlockBorderWrapper"]:has(> div > div[data-testid="stVerticalBlock"]) {{
  border-radius: 12px;
}}
div[data-testid="stMetric"] {{
  background: {SURFACE}; border: 1px solid {BORDER}; border-radius: 12px;
  box-shadow: 0 6px 16px rgba(0,0,0,.08); padding: 16px 18px;
}}
div[data-testid="stMetricLabel"] p {{ font-size: 13px; color: {MUTED}; }}
div[data-testid="stMetricValue"] {{ font-weight: 700; font-variant-numeric: tabular-nums; }}
div[data-testid="stExpander"] details {{
  background: {SURFACE}; border: 1px solid {BORDER}; border-radius: 12px;
}}

/* File drop zone */
section[data-testid="stFileUploaderDropzone"] {{
  border-radius: 15px; border: 1.5px dashed {BRAND}55; background: {SURFACE};
}}

/* Alerts */
div[data-testid="stAlert"] {{ border-radius: 10px; }}

/* Sidebar */
section[data-testid="stSidebar"] {{ background: {SURFACE}; border-right: 1px solid {BORDER}; }}
</style>
"""


def setup_page(title: str) -> None:
    """Call once from the entry point: page config, logo, global CSS."""
    st.set_page_config(page_title=title, page_icon=str(ICON), layout="wide")
    st.logo(str(LOGO), icon_image=str(ICON))
    st.markdown(_CSS, unsafe_allow_html=True)


def page_header(title: str, eyebrow: str = "", subtitle: str = "") -> None:
    if eyebrow:
        st.markdown(f'<div class="lx-eyebrow">{eyebrow}</div>', unsafe_allow_html=True)
    st.title(title)
    if subtitle:
        st.markdown(f'<div class="lx-sub">{subtitle}</div>', unsafe_allow_html=True)
    st.markdown('<div class="lx-gradbar"></div>', unsafe_allow_html=True)
