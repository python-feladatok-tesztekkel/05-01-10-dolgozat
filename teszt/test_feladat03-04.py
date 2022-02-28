from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok



class TestEBetukSzama4(TestCase):
    def test_feladat04(self):
        aktualis = feladatok.ebetuk_szama("abcdfghé")
        elvart = 1
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg az e vagy é betűk számát")
