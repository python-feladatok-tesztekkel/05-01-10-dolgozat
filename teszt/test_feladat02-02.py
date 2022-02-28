from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok




class Jeles02(TestCase):
    def test_feladat02(self):
        szamok=[3]
        aktualis = feladatok.hany_targybol_jeles(szamok)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem megfelelően határozta meg a jelesek számát!")

