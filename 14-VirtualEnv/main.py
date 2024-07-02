# python -m venv myenv - Command to initialize a virtaul env
# source myenv/Scripts/activate - to activate it
#deactivate
# pip freeze > requirement.txt - to list all the packages installed in this env
# pip install -r requirement.txt - install the packages in the system

import pandas as pd

print(pd.__version__)