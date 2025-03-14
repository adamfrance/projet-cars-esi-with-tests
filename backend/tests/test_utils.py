import sys
import os
from unittest.mock import patch, MagicMock

# Ensure the utils module can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_report_pipeline_with_direct_mocks():
    """Test report_pipeline with direct mocking approach"""
    # Import inside test to ensure path is set up
    from utils.report import report_pipeline
    from utils.report_query import make_query
    from utils.send_report import send_report
    
    # Create mocks for the functions we want to patch
    original_make_query = make_query
    original_send_report = send_report
    
    try:
        # Replace with mocks
        make_query_mock = MagicMock(return_value="<html>Test HTML</html>")
        send_report_mock = MagicMock()
        
        # Monkey patch the functions
        sys.modules['utils.report_query'].make_query = make_query_mock
        sys.modules['utils.report'].send_report = send_report_mock
        
        # Call the function
        report_pipeline("test@example.com", 10)
        
        # Check that make_query was called with correct args
        make_query_mock.assert_called_once_with(10)
        
        # Check that send_report was called with correct args
        send_report_mock.assert_called_once()
        args, kwargs = send_report_mock.call_args
        assert kwargs["email"] == "test@example.com"
        assert kwargs["subject"] == "FARM Cars Report"
        assert kwargs["HTMLcontent"] == "<html>Test HTML</html>"
        
    finally:
        # Restore original functions
        sys.modules['utils.report_query'].make_query = original_make_query
        sys.modules['utils.report'].send_report = original_send_report