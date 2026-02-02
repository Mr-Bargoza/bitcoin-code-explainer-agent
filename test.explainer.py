# test_explainer.py
import pytest
from bitcoin_code_explainer import BitcoinCodeExplainerAgent


def test_matches_transaction_and_signature():
    agent = BitcoinCodeExplainerAgent()
    out = agent.explain("VerifyTransaction(tx); // check signature")
    o = out.lower()
    assert "transaction" in o
    assert "signature" in o


def test_no_matches_returns_generic():
    agent = BitcoinCodeExplainerAgent()
    out = agent.explain("int add(int a, int b) { return a + b; }")
    assert "generic" in out.lower()


def test_add_and_remove_term():
    agent = BitcoinCodeExplainerAgent()
    agent.add_term("foobar", "example term")
    assert "foobar" in agent.list_terms()
    agent.remove_term("foobar")
    assert "foobar" not in agent.list_terms()
