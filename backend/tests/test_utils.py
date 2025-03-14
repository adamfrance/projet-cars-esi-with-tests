import sys
import os
import importlib
from unittest.mock import patch, MagicMock

def test_report_pipeline_with_direct_mocks():
    """Test report_pipeline with direct mocking approach"""
    # Créer une version modifiée pour les tests qui ne dépend pas de MongoDB
    def mock_make_query(cars_number):
        return "<html>Test HTML</html>"
    
    def mock_send_report(email, subject, HTMLcontent):
        return True
    
    # Sauvegarder les fonctions originales
    from utils.report_query import make_query as original_make_query
    from utils.report import send_report as original_send_report
    
    # Appliquer les mocks
    import utils.report_query
    import utils.report
    utils.report_query.make_query = mock_make_query
    utils.report.send_report = mock_send_report
    
    try:
        # Réimporter pour appliquer les mocks
        importlib.reload(utils.report)
        
        # Importer après avoir appliqué les mocks
        from utils.report import report_pipeline
        
        # Créer des spies pour suivre les appels
        make_query_spy = MagicMock(side_effect=mock_make_query)
        send_report_spy = MagicMock(side_effect=mock_send_report)
        
        # Remplacer par les spies
        utils.report_query.make_query = make_query_spy
        utils.report.send_report = send_report_spy
        
        # Exécuter la fonction
        report_pipeline("test@example.com", 10)
        
        # Vérifier les appels
        make_query_spy.assert_called_once_with(10)
        send_report_spy.assert_called_once()
        args, kwargs = send_report_spy.call_args
        assert kwargs["email"] == "test@example.com"
        assert kwargs["subject"] == "FARM Cars Report"
        assert kwargs["HTMLcontent"] == "<html>Test HTML</html>"
    
    finally:
        # Restaurer les fonctions originales
        utils.report_query.make_query = original_make_query
        utils.report.send_report = original_send_report