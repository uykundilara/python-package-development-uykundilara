import unittest
import sys
import os

from geometri import mesafe_hesapla, dik_uzaklik_hesapla

class TestGeometri(unittest.TestCase):
    
    def test_mesafe(self):
        # (0,0) ile (3,4) noktaları arası mesafe 5 olmalı (3-4-5 üçgeni)
        self.assertEqual(mesafe_hesapla(0, 0, 3, 4), 5.0)
        # Aynı noktalar arası mesafe 0 olmalı
        self.assertEqual(mesafe_hesapla(1, 1, 1, 1), 0.0)

    def test_dik_uzaklik(self):
        # (0,0) noktasının 3x + 4y - 10 = 0 doğrusuna uzaklığı 2 olmalı
        # Hesap: |3*0 + 4*0 - 10| / kök(3^2 + 4^2) = 10 / 5 = 2
        self.assertEqual(dik_uzaklik_hesapla(0, 0, 3, 4, -10), 2.0)

if __name__ == '__main__':
    unittest.main()
    def test_alan_hesapla(self):
        # 2x2'lik bir karenin alanı 4 olmalı
        kare = [(0, 0), (2, 0), (2, 2), (0, 2)]
        self.assertEqual(alan_hesapla(kare), 4.0)
        
        # 3-4-5 üçgeni (dik kenarlar 3 ve 4 birim) alanı 6 olmalı
        ucgen = [(0, 0), (3, 0), (0, 4)]
        self.assertEqual(alan_hesapla(ucgen), 6.0)