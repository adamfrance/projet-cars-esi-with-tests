import sys
import os
from unittest.mock import patch, MagicMock

def test_report_pipeline_with_direct_mocks():
    """Test report_pipeline with direct mocking approach"""
    # Import dans le test pour s'assurer que les chemins sont corrects
    from utils.report import report_pipeline
    
    # Utiliser un mock pour remplacer les fonctions
    with patch('utils.report_query.make_query') as mock_make_query:
        with patch('utils.report.send_report') as mock_send_report:
            # Configuration des mocks
            mock_make_query.return_value = "<html>Test HTML</html>"
            
            # Appel de la fonction
            report_pipeline("test@example.com", 10)
            
            # Vérifications
            mock_make_query.assert_called_once_with(10)
            mock_send_report.assert_called_once()
            # Vérifie les arguments
            args = mock_send_report.call_args[1]  # Récupère les kwargs
            assert args["email"] == "test@example.com"
            assert args["subject"] == "FARM Cars Report"
            assert args["HTMLcontent"] == "<html>Test HTML</html>"