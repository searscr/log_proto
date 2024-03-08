from mantid.simpleapi import CreateSampleWorkspace
from mantid.kernel import amend_config

import settings
from log_test import test_logging

import argparse
import sys



def bool_to_mtd_str(arg: bool) -> str:
    """mantid.kernel.ConfigService does not understand bool, but does understand
    the strings "0" and "1". This method converts things
    """
    return "1" if arg else "0"

def main(args=None):
    settings.init()
    parser = argparse.ArgumentParser(
        prog="garnet", description="Single Crystal Diffraction", epilog="https://garnet-neutrons.readthedocs.io/"
    )
    parser.add_argument("-v", "--version", action="version", version="0.1.0")
    # parser.add_argument("--debug", action="store_true", help="enable debug logging")
    parser.add_argument("--garnet-only", action="store_true", help="enable garnet-only logging")
    parser.add_argument("--checkfornewmantid", action="store_true", help="check for new mantid version on startup")
    parser.add_argument(
        "--updateinstruments", action="store_true", help="update user's cache of mantid instrument definitions"
    )
    options, _ = parser.parse_known_args(args)
    if options.garnet_only:
        settings.update(True)
        print("garnet-only logging enabled")
    
    with settings.set_log_level(2):
        test_logging()
    

if __name__ == "__main__":
    main(sys.argv)
