import unittest
from app.models import Etudiant

class TestEtudiant(unittest.TestCase):
    def test_moyenne(self):
        etudiant = Etudiant("Ndiaye", "Bouba", "779856321", "L3 Physique", 17, 18, 16)
        self.assertEqual(etudiant.moyenne(), 17)

if __name__ == '__main__':
    unittest.main()