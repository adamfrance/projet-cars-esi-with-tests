import sys
import os
import importlib
from unittest.mock import patch, MagicMock

def test_report_pipeline_simplified():
    """Test une version simplifiée de report_pipeline"""
    from utils.report_test import report_pipeline
    
    result = report_pipeline("test@example.com", 10)
    assert result["email"] == "test@example.com"
    assert result["cars_number"] == 10