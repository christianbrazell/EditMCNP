from utils.MCFRTank import MCFRTank
import argparse

# set command line arguments
# -c CONFIG -o OUTPUT -r REFERENCE
parser = argparse.ArgumentParser()

parser.add_argument("-c", "--config", dest="config", help="config deck edits")
parser.add_argument("-o", "--output", dest="output", help="output deck filename")
parser.add_argument("-r", "--reference", dest="reference", help="reference deck filename")

args = parser.parse_args()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    MCFR = MCFRTank(config=args.config)
    MCFR.update_deck(args.output, deck=args.reference)



