from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok


class Szogek03(TestCase):
    def test_feladat(self):
        aktualis = feladatok.szog(90)
        elvart = "derékszög"
        self.assertEqual(elvart, aktualis, elvart+" szöget rosszul határozta meg!")
