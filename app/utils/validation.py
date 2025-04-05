import re

class Validation:
    @staticmethod
    def verifier_telephone(telephone):
        return re.match(r'^\d{10}$', telephone) is not None

    @staticmethod
    def verifier_notes(note):
        return 0 <= note <= 20
