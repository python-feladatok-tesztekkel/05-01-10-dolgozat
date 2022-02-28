from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok


class Szogek04(TestCase):
    def test_feladat(self):
        aktualis = feladatok.szog(91)
        elvart = "tompaszög"
        self.assertEqual(elvart, aktualis, elvart+" szöget rosszul határozta meg!")
    def test_feladat1(self):
        aktualis = feladatok.szog(179)
        elvart = "tompaszög"
        self.assertEqual(elvart, aktualis, elvart+" szöget rosszul határozta meg!")
