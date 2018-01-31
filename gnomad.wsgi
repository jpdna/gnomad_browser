
# INC3340060

activate_this = '/data01/gnomad_browser/default/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.append("/data01/gnomad_browser/default")
from exac import app as application

if __name__ == "__main__":
    application.run()
