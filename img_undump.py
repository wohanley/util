import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('source', help="the file to read raw image data from")
args = parser.parse_args()

data = open(args.source + '.dump', 'rb').read()
meta = open(args.source + '.meta').readlines()

output = Image.frombytes('RGB', (int(meta[0]), int(meta[1])), data)
