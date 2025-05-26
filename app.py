# -*- coding: utf-8 -*-
"""
Created on Mon May 26 13:23:17 2025

@author: gig
"""

import streamlit as st
import random
import time

# Türkçe harfler listesi
turkce_harfler = list("ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ")

# Global skorlar
if "dogru" not in st.session_state:
    st.session_state.dogru = 0
    st.session_state.yanlis = 0
    st.session_state.bos = 0
    st.session_state.soru_index = 1
    st.session_state.dizi_gosterildi = False

# Başlık
st.title("🧠 Zihinsel Egzersiz Arayüzü")

# Soru fonksiyonları
def rastgele_rakamlar(adet):
    return random.sample(range(1, 10), adet)

def temiz_dizi(elemanlar):
    return '-'.join(str(e) for e in elemanlar if str(e).isalnum())

def soru1():
    dizi = rastgele_rakamlar(2)
    return temiz_dizi(dizi), f"{dizi[1]}'ten önceki sayıyı yaz.", str(dizi[0])

def soru2():
    dizi = rastgele_rakamlar(3)
    return temiz_dizi(dizi), f"{dizi[1]}'den önceki sayıyı yaz.", str(dizi[0])

def soru3():
    dizi = rastgele_rakamlar(4)
    return temiz_dizi(dizi), f"{dizi[3]}'den iki önceki sayıyı yaz.", str(dizi[1])

def soru4():
    dizi = rastgele_rakamlar(4)
    return temiz_dizi(dizi), "1. ve 4. sayıların toplamını yaz.", str(dizi[0] + dizi[3])

def soru5():
    dizi = rastgele_rakamlar(5)
    return temiz_dizi(dizi), "Üçüncü sıradaki sayıyı yaz.", str(dizi[2])

def soru6():
    dizi = rastgele_rakamlar(5)
    return temiz_dizi(dizi), "4. sayıdan 3 önceki sayıyı yaz.", str(dizi[0])

def soru7():
    dizi = rastgele_rakamlar(6)
    return temiz_dizi(dizi), "2. ve 5. sayıların çarpımını yaz.", str(dizi[1] * dizi[4])

def soru8():
    while True:
        dizi = rastgele_rakamlar(7)
        if dizi[0] + dizi[1] > dizi[-2] + dizi[-1]:
            break
    return temiz_dizi(dizi), "İlk iki sayının toplamından son iki sayının toplamını çıkar.", str((dizi[0] + dizi[1]) - (dizi[-2] + dizi[-1]))

def soru9():
    harfler = random.sample(turkce_harfler, 3)
    sayilar = rastgele_rakamlar(4)
    dizi = [harfler[0], sayilar[0], harfler[1], harfler[2], sayilar[1], sayilar[2], sayilar[3]]
    toplam = sum(x for x in dizi if isinstance(x, int))
    return temiz_dizi(dizi), "Sayıların toplamını yaz.", str(toplam)

def soru10():
    harfler = random.sample(turkce_harfler, 3)
    sayilar = rastgele_rakamlar(4)
    dizi = [harfler[0], sayilar[0], sayilar[1], harfler[1], sayilar[2], harfler[2], sayilar[3]]
    harfler_ = [c for c in dizi if isinstance(c, str)]
    return temiz_dizi(dizi), "Alfabetik olarak önce gelen harfi yaz.", sorted(harfler_)[0]

sorular = [soru1, soru2, soru3, soru4, soru5, soru6, soru7, soru8, soru9, soru10]

# Oturum sonuysa
if st.session_state.soru_index > 10:
    st.markdown("### 🏁 Tüm sorular tamamlandı!")
    st.success(f"✅ Doğru: {st.session_state.dogru}  ❌ Yanlış: {st.session_state.yanlis}  ⏺️ Boş: {st.session_state.bos}")
    if st.button("🔄 Yeniden Başla"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
else:
    if not st.session_state.dizi_gosterildi:
        dizi, soru, cevap = sorular[st.session_state.soru_index - 1]()
        st.session_state.dizi = dizi
        st.session_state.soru = soru
        st.session_state.gercek_cevap = cevap
        st.session_state.dizi_gosterildi = True
        st.write("### 🔢 Dizi:")
        st.markdown(f"## {dizi}")
        st.info("⏳ 10 saniye sonra soru gelecek...")
        time.sleep(10)

    st.markdown("### ❓ Soru:")
    st.markdown(f"## {st.session_state.soru}")

    cevap_input = st.text_input("✍️ Cevabınızı giriniz", key="cevap_input")

    if st.button("✅ Gönder"):
        girilen = cevap_input.strip()
        if girilen == "":
            st.session_state.bos += 1
        elif girilen == st.session_state.gercek_cevap:
            st.session_state.dogru += 1
        else:
            st.session_state.yanlis += 1
        st.session_state.soru_index += 1
        st.session_state.dizi_gosterildi = False
        st.experimental_rerun()
