

import argparse
import kdl
import sys
import os
from pathlib import Path

def main(args):
    config_path = Path(os.getenv("SVC_CONFIG_PATH") or '/etc/svc')
    if not config_path.exists():
        config_path.mkdir(parents=True, exist_ok=True)
    
    svc_config = kdl.parse(open(config_path / 'svc.kdl', 'r').read())


if __name__ == "__main__":
    main(sys.argv[1:])
