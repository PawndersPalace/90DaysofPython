import argparse

parser = argparse.ArgumentParser(description="Greet a learner.")
parser.add_argument("name")
parser.add_argument("--loud", action="store_true")
args = parser.parse_args(["Ada", "--loud"])  # Sample command-line arguments
greeting = f"Hello, {args.name}!"
print(greeting.upper() if args.loud else greeting)
