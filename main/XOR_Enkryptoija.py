# Joona Niemenmaa 6/1/2024 XOR_Enkryptoija.py
###############################################
import XOR_EnkryptoijaKirjasto
MERKIT_TIEDOSTONIMI = "merkit.txt"
AVAIN_TIEDOSTONIMI = "avain.txt"
def valikko():
	print("Valitse haluamasi toiminto:")
	print("1) Käännä merkkijono XOR-enkoodauksella")
	print("2) Syötä uusi XOR-avain")
	print("0) Lopeta")
	Valinta = input("Valintasi: ")
	return Valinta
###############################################
def paaohjelma():
	print("Luetaan tarvittavat tiedot.")
	XOR_AVAIN = ""
	MERKIT = ""
	MERKIT = XOR_EnkryptoijaKirjasto.lueMerkit(MERKIT_TIEDOSTONIMI)
	XOR_AVAIN = XOR_EnkryptoijaKirjasto.lueMerkit(AVAIN_TIEDOSTONIMI)
	if (XOR_AVAIN == ""):
		print("Ei tallennettua XOR-avainta, syötä uusi avain (7 merkkiä pitkä, koostuu merkeistä '1' ja '0'.)")
		XOR_AVAIN = XOR_EnkryptoijaKirjasto.syotaUusiAvain(AVAIN_TIEDOSTONIMI)
	print("")
	print("Tämä ohjelma enkryptoi merkkijonoja XOR-enkoodauksella.")
	Tuloste = "XOR-avain on '{0}'".format(XOR_AVAIN)
	print(Tuloste)
	Valinta = None
	while (Valinta != "0"):
		Valinta = valikko()
		if (Valinta == "1"):
			Merkkijono = input("Syötä merkkijono: ")
			Merkkijono = XOR_EnkryptoijaKirjasto.kaannaMerkkijono(Merkkijono, MERKIT, XOR_AVAIN)
			print(Merkkijono)
		elif (Valinta == "2"):
			XOR_AVAIN = XOR_EnkryptoijaKirjasto.syotaUusiAvain(AVAIN_TIEDOSTONIMI)
		elif (Valinta == "0"):
			print("Lopetetaan.")
		else:
			print("Tuntematon valinta, yritä uudestaan.")
		print("")
	print("Kiitos ohjelman käytöstä.")
	return None
paaohjelma()
################################################
# EOF
