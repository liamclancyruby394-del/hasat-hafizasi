import streamlit as st
from PIL import Image
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="Hasat Hafızası", page_icon="🧑🏻‍🌾", layout="wide")

st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display: none !important;}
    div.stButton > button {
        width: 100% !important; height: 50px !important; border-radius: 10px !important;
        font-weight: bold !important; transition: all 0.3s ease; margin-bottom: 10px;
    }
    div.stButton > button:hover { background-color: #4CAF50 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown("### HASAT HAFIZASI\n---")

if 'sayfa' not in st.session_state:
    st.session_state.sayfa = "Ana Sayfa"

# Sayfa Geçiş Butonları
if st.sidebar.button("Ana Sayfa"): st.session_state.sayfa = "Ana Sayfa"
if st.sidebar.button("Hakkımızda & İletişim"): st.session_state.sayfa = "Hakkımızda & İletişim"
if st.sidebar.button("Yıllar Veri Arşivi"): st.session_state.sayfa = "Yıllar Veri Arşivi"
if st.sidebar.button("Geleceğe Yönelik Tahmin"): st.session_state.sayfa = "Geleceğe Yönelik Tahmin"

# Takım adını alta sabitlemek için boşluk
st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><hr><h3 style='text-align: center; color: #4CAF50;'>TARERAL Takımı</h3>", unsafe_allow_html=True)

veri_sozlugu = {
    2014: [65.812, 24.485, 82.101, 22.986, 49.822, 41.518, 6.668, 5.8, 58.072, 61.435, 85.453, 106.193],
    2015: [140.516, 150.821, 104.782, 30.624, 48.481, 15.008, 3.719, 11.322, 26.377, 56.15, 27.263, 23.45],
    2016: [135.255, 60.362, 65.98, 26.886, 63.721, 30.986, 3.503, 7.873, 28.071,  13.624, 43.145, 170.795],
    2017: [84.31, 13.416, 85.898, 61.427, 55.045, 26.468, 3.224, 3.46, 13.333, 34.222, 101.598, 73.212],
    2018: [257.2611, 76.956, 54.638, 39.19, 62.94, 54.791, 6.321, 3.761, 15.843, 82.798, 66.689, 262.577],
    2019: [212.705, 99.016, 95.286, 52.861, 28.076, 37.254, 18.608, 3.504, 12.439,  27.682, 38.807, 255.154],
    2020: [130.5, 81.246, 77.525, 34.736, 58.409, 19.384, 4.22, 3.329, 7.085, 20.156, 72.068, 55.62],
    2021: [192.07, 32.287, 69.944, 49.221, 21.581, 12.416,  8.099, 9.372, 21.365,  14.061, 64.934, 154.676],
    2022: [176.25, 66.9, 107.385, 34.146, 31.625, 32.474, 3.222, 5.285, 11.478, 32.914, 84.508, 40.922],
    2023: [47.228, 49.085, 84.656, 63.414, 63.023, 31.983, 9.553, 6.999, 11.478,  40.314, 95.484, 92.339],
    2024: [133.984, 44.887, 58.073, 30.407, 76.163, 12.894, 15.036, 6.074, 24.801, 18.94, 91.56, 129.632]
}
aylar = ["Ocak  ", "Şubat  ", "Mart  ", "Nisan  ", "Mayıs  ", "Haziran  ", "Temmuz  ", "Ağustos  ", "Eylül  ", "Ekim  ", "Kasım  ", "Aralık  "]

if st.session_state.sayfa == "Ana Sayfa":
    st.title("Hasat Hafızası Bilgi Sistemi")
    st.markdown("#### *Çukurova Bölgesi 10 Yıllık Dijital Tarım Arşivi*")
    st.markdown("**Sloganımız:** Toprağın geçmişi, tarımın geleceği: Hasat Hafızası")
    st.markdown("---")
    
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("incelenen süre", "10 Yıl", "2014 - 2024")
    col_m2.metric("Saha doğruluk oranı", "%90", "optimum uyum")
    col_m3.metric("donanım maliyeti", "0 ₺", "açık kaynak")

elif st.session_state.sayfa == "Hakkımızda & İletişim":
    st.title("Hakkımızda & İletişim")
    st.subheader("Projede Çözüm Yaklaşımımız")
    st.info("İklim krizi ve yanlış ekim alışkanlıklarınedeniyle topraklarımızda yaşanan verim kaybını, karmaşık yazım dilleriyle boğuşmak yerine Avrupa Uzay Ajansı (ESA) ve NASA’nın sağladığı ücretsiz uydu görüntülerini kullanarak analiz ediyoruz. NDVI dediğimiz bitki sağlığı indeksini temel alarak, tarlalardaki su stresini ve bitki gelişimini sayısal verilere döküyoruz. Böylece bölgenin 2014-2024 yılları arasındaki ürün deseni haritasını çıkarıp, toprağın nerede yorulduğunu ve nerede verim kaybı yaşandığını somut bir şekilde görselleştiriyoruz.")
    st.markdown("---")
    st.subheader("İletişim Bilgileri")
    st.markdown("* **E-posta:\n* **Telefon:\n* **Adres:")

elif st.session_state.sayfa == "Yıllar Veri Arşivi":
    st.title("Geçmiş Yılların Veri Arşivi (2014 - 2024)")
    secilen_yil = st.selectbox("İncelemek istediğiniz geçmiş yılı seçiniz:", list(range(2014, 2025)))
    
    st.header(f"📅 {secilen_yil} Yılı İncelemesi")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### NDVI Ürün Deseni Haritası")
        if os.path.exists(f"map_{secilen_yil}.png"): st.image(f"map_{secilen_yil}.png", use_container_width=True)
        
        st.markdown("#### NDVI Renk Skalası")
        if os.path.exists("ndvi_legend.png"): st.image("ndvi_legend.png", width=300)
            
    with col2:
        st.markdown("### Aylık Yağış Grafiği")
        if os.path.exists(f"graph_{secilen_yil}.png"): 
            st.image(f"graph_{secilen_yil}.png", use_container_width=True)
        else:
            fig, ax = plt.subplots(figsize=(6, 3.5))
            ax.bar(aylar, veri_sozlugu[secilen_yil], color='skyblue', edgecolor='gray')
            st.pyplot(fig)
            
    st.markdown("---")
    yorumlar = {2014: "2014-2015 yıllarında yüksek NDVI değerlerinin geniş alanlara yayıldığı görülmektedir. Bölgede sağlıklı bitki örtüsünün bulunduğunu göstermektedir. Yaz aylarında yağışların azalmasına rağmen tarım alanlarında ciddi bir kuruma gözlenmemiştir. Bu durum sulama yapılmasının göstergesi olabilir.", 
                2015: "2014-2015 yıllarında yüksek NDVI değerlerinin geniş alanlara yayıldığı görülmektedir. Bölgede sağlıklı bitki örtüsünün bulunduğunu göstermektedir. Yaz aylarında yağışların azalmasına rağmen tarım alanlarında ciddi bir kuruma gözlenmemiştir. Bu durum sulama yapılmasının göstergesi olabilir. ", 
                2016: "2016-2018 döneminde bazı tarım alanlarında NDVI değerlerinde düşüş gözlenmiştir. Haritalarda açık yeşil ve sarı tonların artması, bitki gelişiminde önceki yıllara göre azalma yaşandığını göstermektedir. Özellikle 2017 yılında yağış grafiğinde dikkat çekici bir düşüş mevcuttur. Kasım ayı dışında diğer aylarda yağış 100mm geçmemiştir. Bu durum yöntemimizin doğruluğunu kanıtlar nitelikte NDVI haritasına yansımıştır. 2018 yılında ise Ocak ve Aralık ayları dışında oldukça düşük yağış almıştır. NDVI haritasında dalgalanmalar oluşmuş, haritanın sol tarafında geniş tarım parsellerinin rengi açık yeşile geçmiştir. Bu durum toprağın nem dengesini korumasında zorluk yaşadığını gösterebilir.", 
                2017: "2016-2018 döneminde bazı tarım alanlarında NDVI değerlerinde düşüş gözlenmiştir. Haritalarda açık yeşil ve sarı tonların artması, bitki gelişiminde önceki yıllara göre azalma yaşandığını göstermektedir. Özellikle 2017 yılında yağış grafiğinde dikkat çekici bir düşüş mevcuttur. Kasım ayı dışında diğer aylarda yağış 100mm geçmemiştir. Bu durum yöntemimizin doğruluğunu kanıtlar nitelikte NDVI haritasına yansımıştır. 2018 yılında ise Ocak ve Aralık ayları dışında oldukça düşük yağış almıştır. NDVI haritasında dalgalanmalar oluşmuş, haritanın sol tarafında geniş tarım parsellerinin rengi açık yeşile geçmiştir. Bu durum toprağın nem dengesini korumasında zorluk yaşadığını gösterebilir.", 
                2018: "2016-2018 döneminde bazı tarım alanlarında NDVI değerlerinde düşüş gözlenmiştir. Haritalarda açık yeşil ve sarı tonların artması, bitki gelişiminde önceki yıllara göre azalma yaşandığını göstermektedir. Özellikle 2017 yılında yağış grafiğinde dikkat çekici bir düşüş mevcuttur. Kasım ayı dışında diğer aylarda yağış 100mm geçmemiştir. Bu durum yöntemimizin doğruluğunu kanıtlar nitelikte NDVI haritasına yansımıştır. 2018 yılında ise Ocak ve Aralık ayları dışında oldukça düşük yağış almıştır. NDVI haritasında dalgalanmalar oluşmuş, haritanın sol tarafında geniş tarım parsellerinin rengi açık yeşile geçmiştir. Bu durum toprağın nem dengesini korumasında zorluk yaşadığını gösterebilir.", 
                2019: "2019 yılında NDVI değerlerinde yeniden artış görülmektedir. Bu durum yıllara bağlı olarak iklim koşulları, yağış miktarı, sulama uygulamaları veya ürün desenindeki değişimlerden kaynaklanmış olabilir.", 
                2020: "2020 yılında bir önceki yıla göre yağış miktarı aylara göre düzensizleşmiş ve  tarım arazilerinin genelinde yeşil tonların canlılığını kaybetmeye başladığı görülmektedir.  ", 
                2021: "2021 yılında Ocak ayındaki zirve yağışın ardından Şubat ayında ani bir düşüş ve yıl boyu kurak bir dönem yaşanmıştır. Ani iklimsel dalgalanma NDVI haritasına doğrudan yansımıştır. Haritanın sol üst ve alt kısımları ile sarı ve açık yeşil alanlar da artış görülmektedir. Bitki canlılığı azalmıştır.", 
                2022: "2022 yılında NDVI haritası incelendiğinde, bitki örtüsünün yağış etkisiyle toparlandığı ancak bazı parsellerde toprağın yorulduğu verim kaybı yaşandığı alanlarda bu durumun kalıcılaşmaya başladığı görülmektedir.", 
                2023: "İncelediğimiz dönemler  içerinde 2023 sarı tonlarının en belirgin olduğu yıllardan biridir. Yıl boyu yağış miktarı düşüktür(100mm civarı) . Haritanın sol ve orta kısımlarında verimliliğin azalarak bitki örtüsünün gerilediği bitki sağlığı düşüşüne işaret etmektedir. ", 
                2024: "2024 yılında ise NDVI haritasında yeşil tonların artışı bir önceki yıla göre görülse de geçmiş yılların toprak yorgunluğu ve su stresi etkisiyle haritanın kuzey bölgelerinde kahverengi/sarı tonlara yakın alanların somut bir şekilde arttığı görülmektedir. "}
    st.markdown("### 📝 Yıl Değerlendirmesi")
    st.info(yorumlar.get(secilen_yil, "Yorum bulunamadı."))

elif st.session_state.sayfa == "Geleceğe Yönelik Tahmin":
    st.title("Makine öğrenimi ile geleceğe yönelik tahmin")
    tahmin_yili = st.selectbox("Tahmin yılı seçiniz:", [2026, 2027, 2028])
    tahmin_sonuclari = []
    yillar_X = np.array(list(veri_sozlugu.keys())).reshape(-1, 1)
    
    for i in range(12):
        aylik_veri_y = [veri_sozlugu[yil][i] for yil in veri_sozlugu.keys()]
        
        model = LinearRegression()
        model.fit(yillar_X, aylik_veri_y)
        
        tahmin = model.predict(np.array([[tahmin_yili]]))[0]
        tahmin_sonuclari.append(max(0, round(tahmin, 1)))

    st.subheader(f"{tahmin_yili} ")
    col_g1, col_g2 = st.columns([2, 1])
    
    with col_g1:
        fig, ax = plt.subplots(figsize=(7, 3.5))
        ax.plot(aylar, tahmin_sonuclari, color='green', marker='o', linestyle='--')
        ax.set_ylabel("Yağış (mm)")
        ax.grid(True, linestyle=':', alpha=0.6)
        st.pyplot(fig)
        
    with col_g2:
        st.dataframe(pd.DataFrame({"Ay": aylar, "tahmin (mm)": tahmin_sonuclari}), use_container_width=True, hide_index=True)
        
    st.info(f"**Not:** bu grafik sistemdeki 2014-2024 verilerinin matematiksel hesaplamalarını yapıp {tahmin_yili} yılı için tahmini değerleri yansıtmaktadır.")
