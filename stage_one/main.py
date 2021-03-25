"""
This module defines what will happen in stage_1.
"""
import sys
from datetime import datetime


def main() -> None:
    now = datetime.now()
    print(f'now={now}')
    try:
        sys.argv[1]
        sys.argv[2]
        sys.exit(0)
    except Exception:
        sys.exit(1)


if __name__ == '__main__':
    main()
