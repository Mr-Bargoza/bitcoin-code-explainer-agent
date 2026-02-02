# Minimal implementation of the BitcoinCodeExplainerAgent
# Adds a simple keyword-based explainer to satisfy tests and CLI usage.

import re
from typing import Dict, List, Optional


class BitcoinCodeExplainerAgent:
    def __init__(self, terms: Optional[Dict[str, str]] = None):
        # default terms; extend as needed
        self._terms: Dict[str, str] = terms or {
            "transaction": "A transaction transfers value between addresses.",
            "transactions": "A transaction transfers value between addresses.",
            "signature": "A cryptographic signature proving ownership.",
            "block": "A block contains a set of transactions and metadata.",
            "verification": "The process of checking validity (signatures, rules).",
        }

    def explain(self, text: str) -> str:
        if not text:
            return "Generic: no input provided."

        lowered = text.lower()
        matches: List[str] = []

        # simple word-boundary search to avoid accidental substring matches
        for term, explanation in self._terms.items():
            pattern = r"\b" + re.escape(term.lower()) + r"\b"
            if re.search(pattern, lowered):
                matches.append(f"{term}: {explanation}")

        if matches:
            return "\n".join(matches)
        return "Generic explanation: no known bitcoin terms found."

    def add_term(self, term: str, explanation: str) -> None:
        if not term:
            raise ValueError("term must be non-empty")
        self._terms[term] = explanation

    def remove_term(self, term: str) -> None:
        self._terms.pop(term, None)

    def list_terms(self) -> Dict[str, str]:
        # return a shallow copy to avoid accidental external mutation
        return dict(self._terms)