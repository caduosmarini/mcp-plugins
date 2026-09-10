import copy
import json
import unittest
from pathlib import Path
from validate_project import validate


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.d=json.loads((Path(__file__).parent.parent/'assets/exemplo-minimo.json').read_text())
    def test_fixture(self):
        self.assertEqual(validate(self.d),[])
    def test_double_band_deduction(self):
        self.d['parts'][0]['raw'][0]-=1
        self.assertTrue(any('deduction' in e for e in validate(self.d)))
    def test_duplicate_physical_piece(self):
        self.d['sheets'][0]['placements'].append(copy.deepcopy(self.d['sheets'][0]['placements'][0]))
        self.assertTrue(any('exactly once' in e for e in validate(self.d)))
    def test_overlap(self):
        p=copy.deepcopy(self.d['parts'][0]);p['id']='P02';self.d['parts'].append(p)
        self.d['sheets'][0]['placements'].append({'id':'P02','x':11,'y':11})
        self.assertTrue(any('overlap' in e for e in validate(self.d)))
    def test_trim(self):
        self.d['sheets'][0]['placements'][0]['x']=0
        self.assertTrue(any('outside' in e for e in validate(self.d)))
    def test_forbidden_rotation(self):
        self.d['parts'][0]['rotation_allowed']=False
        self.d['sheets'][0]['placements'][0]['rotated']=True
        self.assertTrue(any('forbidden' in e for e in validate(self.d)))
    def test_nonfinite(self):
        self.d['parts'][0]['raw'][0]=float('nan')
        self.assertTrue(validate(self.d))


if __name__=='__main__':
    unittest.main()
