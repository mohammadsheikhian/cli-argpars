import argparse


my_parser = argparse.ArgumentParser()
my_parser.add_argument(
    '-i',
    '--input',
    default=0,
    action='store',
    type=int,
)
subparser = my_parser.add_subparsers(
	title="sub commands",
	prog='cliargpars',
	dest="command",
)


def jwt_command(args):
    print(args)


def db_command(args):
    print(args)


def create_jwt_subcommand(subparser):
    parser = subparser.add_parser(
    	'jwt',
    	help='JWT command managers',
    )

    jwt_subparsers = parser.add_subparsers(
        title='JWT management',
        dest='jwt_command',
    )

    jwt_parser = jwt_subparsers.add_parser(
        'create',
        help='Create a new initial jwt.'
    )

    jwt_parser.set_defaults(func=jwt_command)

    jwt_parser.add_argument(
        '-e', '--expire-in',
        default=3600,
        type=int,
        help='the max age, default: 3600 (one hour).'
    )

    jwt_parser.add_argument(
        'payload',
        default='{}',
        nargs='?',
        help= \
            'A JSON parsable string to treat as payload. for example: '
            '{"a": "b"}'
    )


def create_db_subcommand(subparser):
    db_parser = subparser.add_parser(
        'db',
        help='DB command managers',
    )

    db_parser.set_defaults(func=db_command)

    db_parser.add_argument(
        '-n',
        '--name',
        default='No name',
        type=str,
    )


def main():
    create_jwt_subcommand(subparser)
    create_db_subcommand(subparser)

    args = my_parser.parse_args()
    args.func(args)

