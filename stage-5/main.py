"""
This module defines what will happen in stage-1.
"""
import sys

import requests


def main() -> None:
    response = requests.get('http://bodywork-demo-project--stage-4:5000/v2/predict')
    if response.ok:
        print(response.text)
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
