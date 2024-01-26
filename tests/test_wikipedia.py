#tests/test_wikipedia.py
import pytest
from python_luqinhas import wikipedia

def test_random_page_uses_given_languagee(mock_requests_get):
	wikipedia.random_page(language="de")
	args, _ = mock_requests_get.call_args
	assert "de.wikipedia.org" in args[0]