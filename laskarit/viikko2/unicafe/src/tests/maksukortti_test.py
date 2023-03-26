import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luodun_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")
    
    def test_ota_rahaa_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")

    def test_ota_rahaa_ei_mene_miinukselle(self):
        kortti = Maksukortti(200)
        kortti.ota_rahaa(300)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_ota_rahaa_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.50 euroa")

    def test_ota_rahaa_ei_mene_miinukselle(self):
        self.kortti = Maksukortti(200)
        self.kortti.ota_rahaa(300)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2.00 euroa")
