# Version modifiée de report.py pour les tests
def report_pipeline(email, cars_number):
    """Version de test qui ne dépend pas de MongoDB"""
    return {"email": email, "cars_number": cars_number}