from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok




class Jeles03(TestCase):
    def test_feladat03(self):
        szamok=[5,3,5]
        aktualis = feladatok.hany_targybol_jeles(szamok)
        elvart = 2
        self.assertEqual(elvart, aktualis, "Nem megfelelően határozta meg a jelesek számát!")

