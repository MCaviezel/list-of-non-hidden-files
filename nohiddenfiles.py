@author: marcocaviezel

import os
import re

def nohiddenfiles(path = os.listdir()):
    import os
    import re
    regex = re.compile(r'^\.')
    selected_files = [s for s in path if not regex.match(s) ]
    return selected_files