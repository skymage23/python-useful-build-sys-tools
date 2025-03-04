import pathlib
import sys

modules_dir = (pathlib.Path(__file__).parent / "modules")

def initialize():
    sys.path.append(modules_dir.__str__())