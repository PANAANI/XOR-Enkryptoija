# Joona Niemenmaa 7/1/2024 XOR_EnkryptoijaKirjasto.py
#######################################################
import sys
XOR_AVAIN_PITUUS = 7
def lueMerkit(TiedostoNimi):
	try:
		Tiedosto = open(TiedostoNimi, "r", encoding="UTF-8")
		Merkkijono = Tiedosto.readline()
		Tiedosto.close()
		Tuloste = "Tiedosto '{0}' luettu.".format(TiedostoNimi)
		print(Tuloste)
	except OSError:
		Tuloste = "Tiedoston '{0}' käsittelyssä virhe, lopetetaan.".format(TiedostoNimi)
		print(Tuloste)
		sys.exit(0)
	return Merkkijono
#######################################################
def syotaUusiAvain(TiedostoNimi):
	HyvaksyMerkkijono = False
	while (HyvaksyMerkkijono == False):
		Syote = input("Syötä XOR-avain: ")
		if (len(Syote) != XOR_AVAIN_PITUUS):
			Tuloste = "Syöte ei ole {0} merkkiä pitkä, yritä uudestaan.".format(XOR_AVAIN_PITUUS)
			print(Tuloste)
			continue
		Tarkista = True
		for i in range(len(Syote)):
			if (Syote[i] != "1" and Syote[i] != "0"):
				print("Syötteen tulee koostua merkeistä '1' tai '0', yritä uudestaan.")
				Tarkista = False
				break
		if (Tarkista == True):
			HyvaksyMerkkijono = True
	try:
		Tiedosto = open(TiedostoNimi, "w", encoding="UTF-8")
		Tiedosto.write(Syote + "\n")
		Tiedosto.close()
	except OSError:
		Tuloste = "Tiedoston '{0}' käsittelyssä virhe, lopetetaan.".format(TiedostoNimi)
		print(Tuloste)
		sys.exit(0)
	Tuloste = "XOR-avain on nyt '{0}' ja se on tallennettu.".format(Syote)
	print(Tuloste)
	return Syote
##########################################################
def desimaaliBinaariksi(Desimaali, Pituus):
	Binaari = ""
	Jakojaannos = None
	while (Desimaali != 0):
		Jakojaannos = Desimaali % 2
		Desimaali = Desimaali // 2
		if (Jakojaannos == 0):
			Binaari = "0" + Binaari
		elif (Jakojaannos == 1):
			Binaari = "1" + Binaari
	while (len(Binaari) < Pituus):
		Binaari = "0" + Binaari
	return Binaari
##########################################################
def binaariDesimaaliksi(Binaari):
	Desimaali = 0
	for i in range(len(Binaari)):
		Desimaali = Desimaali + 2**i * int(Binaari[len(Binaari) - i - 1])
	return Desimaali
##########################################################
def kaannaMerkkijono(Merkkijono, MERKIT, XOR_AVAIN):
	Tulos = ""
	for i in range(len(Merkkijono)):
		KaannettyBinaari = ""
		Binaari = desimaaliBinaariksi(MERKIT.index(Merkkijono[i]), len(XOR_AVAIN))
		for j in range(len(Binaari)):
			if (Binaari[j] != XOR_AVAIN[j]):
				KaannettyBinaari = KaannettyBinaari + "1"
			else:
				KaannettyBinaari = KaannettyBinaari + "0"
		Tulos = Tulos + MERKIT[binaariDesimaaliksi(KaannettyBinaari)] 
	return Tulos
##########################################################
# EOF
