"""Entry point for Streamlit Cloud deployment."""
import streamlit as st

from ui import setup_page

setup_page("Báo cáo CSKH MB")

pg = st.navigation(
    {
        "Dữ liệu": [
            st.Page("pages/1_tai_du_lieu.py", title="Tải dữ liệu"),
        ],
        "Báo cáo": [
            st.Page("pages/2_tao_bao_cao.py", title="Tạo báo cáo"),
        ],
    }
)
pg.run()
