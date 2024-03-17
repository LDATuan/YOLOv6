import gdown
import argparse
import zipfile

def load(args):
    file_name = gdown.download(id=args.id)
    if zipfile.is_zipfile(file_name):
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall('data')

def get_arg_parser():
    parser = argparse.ArgumentParser(description='Download Training Data', add_help=True)
    parser.add_argument('--id', type=str, help='id of gg drive file')
    return parser

if __name__ == '__main__':
    args = get_arg_parser().parse_args()
    load(args)



