# cli.py
import argparse
import sys
from bitcoin_code_explainer import BitcoinCodeExplainerAgent


def main(argv=None):
    parser = argparse.ArgumentParser(description="Bitcoin Code Explainer - CLI")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-s", "--snippet", help="Pass a code snippet string to explain")
    group.add_argument("-f", "--file", help="Path to a file containing code to explain")
    parser.add_argument("-t", "--terms", action="store_true", help="List known terms")
    args = parser.parse_args(argv)

    agent = BitcoinCodeExplainerAgent()

    if args.terms:
        for k, v in agent.list_terms().items():
            print(f"{k}: {v}")
        return 0

    if args.snippet:
        text = args.snippet
    else:
        try:
            with open(args.file, "r", encoding="utf-8") as fh:
                text = fh.read()
        except Exception as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            return 2

    print(agent.explain(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
