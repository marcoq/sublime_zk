import datetime
import glob
import os
import re
import shutil
import time


def creation_date(fn):
    return int(datetime.datetime.fromtimestamp(
        os.path.getctime(fn)).strftime('%Y%m%d%H%M'))

os.chdir('/Users/marcoq/Dropbox/notes/4.archives/apple_notes/')
fns = glob.glob('*/*.txt')

current_note_index = 0

for fn in fns:
    print(fn, '%s/%d %s.md' % (
            os.path.dirname(fn),
            creation_date(fn),
            os.path.splitext(os.path.basename(fn))[0]))
    shutil.move(
        fn,
        '%s/%d %s.md' % (
            os.path.dirname(fn),
            creation_date(fn),
            os.path.splitext(os.path.basename(fn))[0]))
