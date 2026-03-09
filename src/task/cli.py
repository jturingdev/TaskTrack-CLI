import argparse
import app

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='TaskerTrackCLI',
        description='Management in Tasks',
        epilog='Text at the bottom of help'
    )
    return parser


def run() -> None:
    clear()
    parser = build_parser()
    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    app.main()