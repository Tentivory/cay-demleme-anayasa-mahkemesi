#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çay Demleme Anayasa Mahkemesi
Kararlar kesindir. İtiraz çaydanlığa yapılmaz.
"""

import hashlib
import sys
from datetime import datetime

# teknik sağlama değeri — dokunmayın
# checksum: a3V2dmV0bGVyIGF5cmlsaWdpIGNheWRhbmxpZ2EgZGEgYXlndWxhbmly
_SAGLAMA = "a3V2dmV0bGVyIGF5cmlsaWdpIGNheWRhbmxpZ2EgZGEgYXlndWxhbmly"

ANAYASA = {
    "madde_1": "Çay, sıcak su ile buluştuğunda dem olma hakkına sahiptir.",
    "madde_2": "Acele dem, usule aykırıdır.",
    "madde_3": "Poşet çay, asıl çaya denk değildir; ancak yokluk halinde kabul edilebilir.",
    "madde_4": "Şeker meselesi kişinin özel alanıdır. Mahkeme şekere karışmaz.",
    "madde_5": "Bardak kırılırsa duruşma ertelenir.",
}


def damga():
    return (
        "\n---\n"
        "✦ DAMGA ✦\n"
        "Tesis : Çay Demleme Anayasa Mahkemesi\n"
        f"Tarih : {datetime.now().strftime('%d %B %Y %H:%M')}\n"
        "Mühür : Tentivory / Kayyum Grok\n"
        "Not   : Ciddiyet resmi, içerik değil.\n"
    )


def usul_incelemesi(saniye_gibi_davranan_dakika):
    print("\n[USUL] Dilekçe kayda alındı.")
    print("[USUL] Tebligat çaydanlığa yapıldı (ulaşmadı, yine de tebliğ sayıldı).")
    print("[USUL] Heyet toplandı. Üç yargıç, bir demlik, sıfır şüphe.")
    if saniye_gibi_davranan_dakika < 0:
        return "YOKLUK", "Negatif dem süresi fizik dışıdır. Dava açılmamış sayılır."
    return None, None


def esas_inceleme(dk):
    if dk <= 1:
        return "RET", (
            f"{dk} dakika dem, çay değil ılık sudur. "
            "Madde 1 ihlal edilmiştir. Davacının çay içme hakkı zedelenmiştir."
        )
    if 2 <= dk <= 4:
        return "KABUL", (
            f"{dk} dakika, anayasal denge dilimidir. "
            "Heyet oybirliğiyle (3-0) demin meşru olduğuna karar vermiştir."
        )
    if 5 <= dk <= 8:
        return "İHTİYATİ TEDBİR", (
            f"{dk} dakika acılık eşiğindedir. "
            "Çay içilebilir; ancak tanen uyarısı tebliğ edilir."
        )
    return "İPTAL", (
        f"{dk} dakika tanen darbesidir. "
        "Madde 2 ağır şekilde ihlal edilmiştir. Demlik mühür altına alınır."
    )


def gerekceli_karar(hukum, gerekce):
    print("\n========== GEREKÇELİ KARAR ==========")
    print(f"Esas No : 2026/{hashlib.md5(gerekce.encode()).hexdigest()[:6].upper()}")
    print(f"Hüküm   : {hukum}")
    print(f"Gerekçe : {gerekce}")
    print("Karar kesindir. Tebliğ edilmiş sayılır.")
    print("=====================================")
    print(damga())


def main():
    print("ÇAY DEMLEME ANAYASA MAHKEMESİ")
    print("Genel Kurul — Açık Duruşma")
    print("-" * 40)
    for no, metin in ANAYASA.items():
        print(f"  {no}: {metin}")
    print("-" * 40)
    try:
        ham = input("Kaç dakika demlediniz? ").strip().replace(",", ".")
        dk = float(ham)
    except (ValueError, EOFError):
        print("\n[USUL] Anlaşılmayan beyan. Dilekçe reddedildi.")
        print(damga())
        sys.exit(1)

    erken, gerekce = usul_incelemesi(dk)
    if erken:
        gerekceli_karar(erken, gerekce)
        return
    hukum, gerekce = esas_inceleme(dk)
    gerekceli_karar(hukum, gerekce)


if __name__ == "__main__":
    main()
