import pytest
from unittest.mock import MagicMock, patch
from utils.report import report_pipeline
from utils.report_query import make_query

@patch('utils.report_query.make_query')
@patch('utils.report.send_report')
def test_report_pipeline(mock_send_report, mock_make_query):
    # Setup mocks
    mock_make_query.return_value = "<html>Test HTML</html>"
    
    # Call the function
    report_pipeline("test@example.com", 10)
    
    # Assertions
    mock_make_query.assert_called_once_with(10)
    mock_send_report.assert_called_once_with(
        email="test@example.com", 
        subject="FARM Cars Report", 
        HTMLcontent="<html>Test HTML</html>"
    )