import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class Test(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        
        
        self.edulliset = 0
        self.maukkaat = 0

    def test_luotu_paate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_konstruktori_asettaa_kortin_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_konstruktori_asettaa_lounaat_oikein(self):
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
    
    def test_edullisen_osto_kateisella(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(300)), "60")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")
        self.assertEqual(str(self.kassapaate.edulliset), "1")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test_maukkaan_osto_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(500)), "100")

    def test_maukkaan_osto_kateisella_ja_edullisen_kortilla(self):
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(500)), "100")
        kortti = self.maksukortti
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kortilla(kortti)), "True")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
        self.assertEqual(str(self.kassapaate.edulliset), "1")
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")

    def test_edullisen_osto_kateisella_ilman_rahaa(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(100)), "100")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(100)), "100")

    def test_maukkaan_osto_kateisella_ilman_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(300)), "300")
    
    def test_lataus_kortille(self):
        kortti = self.maksukortti
        
        
        self.kassapaate.lataa_rahaa_kortille(kortti, 5000)
        self.assertEqual(str(self.maksukortti), "saldo: 60.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "105000")

    def test_lataus_kortille_nolla(self):
        kortti = self.maksukortti
        
        
        self.kassapaate.lataa_rahaa_kortille(kortti, 0)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
    
    def test_lataus_kortille_kahdesti(self):
        kortti = self.maksukortti
        
        
        self.kassapaate.lataa_rahaa_kortille(kortti, 50)
        self.kassapaate.lataa_rahaa_kortille(kortti, 250)
        self.assertEqual(str(self.maksukortti), "saldo: 13.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100300")

    def test_lataus_kortille_kahdesti_ja_osto(self):
        kortti = self.maksukortti
        
        
        self.kassapaate.lataa_rahaa_kortille(kortti, 50)
        self.kassapaate.lataa_rahaa_kortille(kortti, 250)
        self.assertEqual(str(self.maksukortti), "saldo: 13.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100300")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(self.maksukortti), "saldo: 10.6")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100300")
        self.assertEqual(str(self.kassapaate.edulliset), "1")


    def test_lataus_kortille_miinussumma(self):
            kortti = self.maksukortti
            
            
            self.kassapaate.lataa_rahaa_kortille(kortti, -5000)
            self.assertEqual(str(self.maksukortti), "saldo: 10.0")
            self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_edullisen_osto_kortilla(self):

        self.assertEqual(str(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)), "True")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "1")
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)), "True")


    def test_kahden_edullisen_osto_kortilla(self):

        self.assertEqual(str(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)), "True")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "1")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")
        

        self.assertEqual(str(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)), "True")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "2")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
        self.assertEqual(str(self.maksukortti), "saldo: 5.2")
        

    def test_maukkaan_osto_kortilla(self):

        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)), "True")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
        self.assertEqual(str(self.maksukortti.ota_rahaa(400)), "True")

    def test_edullisen_osto_kortilla_ilman_rahaa(self):
        kortti = self.maksukortti
        kortti.ota_rahaa(900)
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)), "False")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
        self.assertEqual(str(self.maksukortti.ota_rahaa(240)), "False")

    def test_maukkaan_osto_kortilla_ilman_rahaa(self):
        kortti = self.maksukortti
        kortti.ota_rahaa(700)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
        self.assertEqual(str(self.maksukortti), "saldo: 3.0")
        self.assertEqual(str(self.maksukortti.ota_rahaa(400)), "False")

    def test_kortille_voi_ladata_rahaa(self):
        kortti = self.maksukortti
        self.kassapaate.lataa_rahaa_kortille(kortti, 2500)
        self.assertEqual(str(self.maksukortti), "saldo: 35.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "102500")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        
    
    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(400)
        self.maksukortti.ota_rahaa(400)
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")



    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_edullisen_osto_kortilla_kaksi(self):
        
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "2")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")   
        self.assertEqual(str(self.maksukortti), "saldo: 5.2")

    def test_edullisen_osto_kortilla_palauttaa_true(self):
        
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)), "True")

        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "1")

        
        

    def test_maukkaan_osto_kortilla_kaksi(self):

        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.assertEqual(str(self.kassapaate.maukkaat), "2")
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
        self.assertEqual(str(self.maksukortti.ota_rahaa(200)), "True")

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = self.maksukortti
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
        self.assertEqual(str(self.kassapaate.maukkaat), "2")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(400)
        self.maksukortti.ota_rahaa(400)
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(400)
        self.maksukortti.ota_rahaa(400)
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")