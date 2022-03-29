import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class Test(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.edulliset = 0
        self.maukkaat = 0

    def test_luotu_paate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kassapaate), self.kassapaate.kassassa_rahaa)
    
    def test_edullisen_osto_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa 100060")
        self.assertEqualstr(str(self.kassapaate.edulliset), "1")

    def test_maukkaan_osto_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa 100100")
        self.assertEqualstr(str(self.kassapaate.maukkaat), "1")
    
    def test_edullisen_osto_kateisella_ilman_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(str(self.kassapaate), "kassassa rahaa 100000")
        self.assertEqualstr(str(self.kassapaate.edulliset), "0")

    def test_maukkaan_osto_kateisella_ilman_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(str(self.maksukortti), "kassassa rahaa 100000")
        self.assertEqualstr(str(self.kassapaate.maukkaat), "0")
    
    def test_lataus_kortille(self):
        self.maksukortti.lataa_rahaa(5000)
        self.assertEqual(str(self.maksukortti), "saldo: 50.0")
        self.assertEqual(str(self.kassapaate), "kassassa rahaa 1050.0")

    def test_edullisen_osto_kortilla(self):
        self.maksukortti.ota_rahaa(250)
