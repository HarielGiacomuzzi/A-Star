#!/usr/bin/env python
# Four spaces as indentation [no tabs]

uploadfolder = "http://moodle.pucrs.br/mod/assign/view.php?id=649085"

if __name__ == '__main__':
    import os
    zipname = raw_input('Student ID (e.g. 09123456): ')
    os.system("zip -r s" + zipname + ".zip *.py maps sprites readme.txt")
    print("You can now upload '"+zipname+".zip' to "+uploadfolder)