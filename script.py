from files_helper_functions import remove_first_line, analyze_input_files
from download_from_dbox import download_from_dbox
from name_to_db import name_to_db
from title_to_db import title_to_db
from known_for_to_db import known_for_to_db
import os.path



title_url = "https://www.dropbox.com/s/3do9bu0awq048uh/title.basics.tsv.gz?dl=1"
title_file = "title.tsv"
name_url = "https://www.dropbox.com/s/xaidig3yw2viyym/name.basics.tsv.gz?dl=1"  # dl=1 - download
name_file = "name.tsv"
known_for_file = "known_for.tsv"


print("Script started...")

if not os.path.isfile(title_file):
    print("Downloading " + title_file)
    download_from_dbox(title_url,title_file)

if not os.path.isfile(name_file):
    print("Downloading " + name_file)
    download_from_dbox(name_url,name_file)

print(title_file + " and " + name_file + " downloaded.")

analyze_input_files(name_file,title_file,known_for_file)
title_to_db(title_file)
name_to_db(name_file)
known_for_to_db(known_for_file)

print("Script ended succesfully!")
