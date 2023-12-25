import argparse
import sys
from typing import Dict, Any

from bazos.main import bazos as bz

__version__ = "0.1.0"
__apiversion__ = "0.1.0"
__author__ = 'Zdenek Lapes'
__license__ = 'MIT'


def parse_cli_argument() -> Dict[str, Any]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-b', '--bazos',
        action='store_true',
        help='Use bazos'
    )
    parser.add_argument(
        '--add-only',
        action='store_true',
        help='Add only new products, not remove old ones'
    )
    parser.add_argument(
        '--print-rubrics',
        action='store_true',
        help='Print rubrics'
    )
    parser.add_argument(
        '--country',
        nargs="+",
        help="What bazos country to use",
        default=['cz', 'sk']
    )
    parser.add_argument(
        '-p', '--path',
        help='Path to products directory'
    )
    parser.add_argument(
        "--update-credentials",
        action='store_true',
        help='Update credentials'
    )
    cli_args = vars(parser.parse_args())
    return cli_args


def main():
    cli_args = parse_cli_argument()

    if cli_args['bazos']:
        bz(cli_args=cli_args)

    sys.exit()


if __name__ == '__main__':
    main()
