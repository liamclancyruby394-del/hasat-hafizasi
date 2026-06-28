
import streamlit as st
from PIL import Image
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Hasat Hafızası",
    page_icon="🌾",
    layout="wide"
)
st.set_page_config(
    page_title="Hasat Hafızası",
    page_icon="🌾",
    layout="wide"
)

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    stDeployButton {display:none;}
    .stDeployButton {display: none !important;}
    </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown("TARERAL Takımı")
st.sidebar.markdown("**basvuru id:** `#4518395`  \n**Kategori:** Tarım ve Hayvansal Üretim Veri Analitiği")
st.sidebar.markdown("---")

st.sidebar.subheader("yıllar")
secilen_yil = st.sidebar.selectbox(
    "incelemek istediginiz yılı seciniz::",
    list(range(2014, 2025)),
    help="yılı değistirdiğinizde grafik harita ve yorumlar yılların verilerine göre değisir"
)


st.title("hasat hafızası bilgi sistemi")
st.markdown("#### *cukurova bolgesi 10 yıllık dijital tarım arsivi*")


col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="incelenen süre", value="10 Yıl", delta="2014 - 2024" , delta_arrow="off")
with col_m2:
    st.metric(label="saha doğruluk oranı", value="%90", delta="optimum uyum" , delta_arrow="off")
with col_m3:
    st.metric(label="donanım maliyeti", value="0 ₺", delta="tamamen açık kaynaklardan yararlanıldı" , delta_arrow="off")

st.markdown("---")

st.header(f" {secilen_yil} yılı incelemesi")

grafik_yolu = f"graph_{secilen_yil}.png"
harita_yolu = f"map_{secilen_yil}.png"
lejant_yolu = "ndvi_legend.png"

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ndvi urun deseni haritası")
    if os.path.exists(harita_yolu):
        harita_img = Image.open(harita_yolu)
        st.image(harita_img, caption=f"{secilen_yil} - Sentinel-2 ve Landsat uydularından elde edilen görüntü", use_container_width=True)

    
    st.markdown("#### NDVI Renk Skalası ")
    if os.path.exists(lejant_yolu):
        lejant_img = Image.open(lejant_yolu)
        st.image(lejant_img, caption=" düşük değerler kırmızı sarı|yüksek değerler yeşil falan", width=400)

with col2:
    st.markdown("### aylık ortalama yağış grafiği")
    if os.path.exists(grafik_yolu):
        grafik_img = Image.open(grafik_yolu)
        st.image(grafik_img, caption=f"{secilen_yil} - meteoroloji genel müdürlüğü yağış grafiği (mm)", use_container_width=True)
st.markdown("---")


yorumlar = {
    2014: "2014 yılı yorum metin at buraya",
    2015: "2015 yılı yorum metin",
    2016: "2016 yorum metin",
    2017: "2017 yorum metin",
    2018: "2018 yorum metni",
    2019: "2019 yorum metni",
    2020: "2020 yorum merni",
    2021: "2021 yorum metin",
    2022: "2022 yorum",
    2023: "2023 metin",
    2024: "2024 yorum geelecek",
}

st.markdown("### yorumlar buraya gelebilir")
st.info(yorumlar.get(secilen_yil,))

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("TEKNOFEST 2026 Tarım Teknolojileri Yarışması")

