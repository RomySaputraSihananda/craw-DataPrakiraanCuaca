from argparse import ArgumentParser;

from Bmkg import Bmkg
from json import dumps
import os 


if(__name__ == '__main__'):
    argp: ArgumentParser = ArgumentParser()
    argp.add_argument("--provinsi", '-p', type=str, default='DKIJakarta')
    argp.add_argument("--output", '-o', type=str)

    args = argp.parse_args()

    bmkg: Bmkg = Bmkg()

    output = f'data' if not args.output else args.output

    if(not os.path.exists(output)):
            os.makedirs(output)

    with open(f'{output}/{args.provinsi}.json', 'w') as file:
        file.write(dumps(bmkg.execute(provinsi=args.provinsi), indent=2))