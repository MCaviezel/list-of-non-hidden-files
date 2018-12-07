"""@author: marcocaviezel
"""
import os
import re

def ignorehiddenfiles(path = os.listdir()):
"""
Ignore hidden files \n
This is a handy function to get the list of all variables in a folder, without hidden files (starting with a dot, e.g. .DS_store).\n
Use \n
clean_list_of_pwd = nohiddenfiles()\n
to get the list of the pwd (as default). \n
Alternatively you can enter a path to another directory.
"""
    import os
    import re
    regex = re.compile(r'^\.')
    selected_files = [s for s in path if not regex.match(s) ]
    return selected_files