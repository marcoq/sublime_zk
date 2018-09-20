import datetime
import glob
import os
import re
import shutil
import time


def creation_date(fn):
    return int(datetime.datetime.fromtimestamp(
        os.path.getctime(fn)).strftime('%Y%m%d%H%M'))

ndir = '/Users/marcoq/Dropbox/notes/ulysses'
os.chdir(ndir)
fns = glob.glob('*/*.md')
print(fns)
current_note_index = 0

for fn in fns:
    shutil.move(
        fn,
        '%s/%d00 %s.md' % (
            ndir,
            creation_date(fn),
            os.path.splitext(fn.split('/')[-2])[0]))
    #shutil.move(
    #    fn,
    #    '%s/%d %s.md' % (
    #        os.path.dirname(fn),
    #        creation_date(fn),
    #        os.path.splitext(os.path.basename(fn))[0]))
