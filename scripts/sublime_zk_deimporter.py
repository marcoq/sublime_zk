import datetime
import glob
import os
import re
import shutil
import time


def sublime_zk_cut_after_note_id(text):
    """
    Tries to find the 12/14 digit note ID (at beginning) in text.
    """
    note_ids = re.findall('[0-9.]{12,18}', text)
    if note_ids:
        if note_ids[-1].endswith('.'):
            return note_ids[-1][:-1]
        return note_ids[-1]
    return None

os.chdir('/Users/marcoq/Dropbox/notes')
fns = glob.glob('*/*/*.md')

for fn in fns:
    note_id = sublime_zk_cut_after_note_id(fn)
    assert note_id
    dn_ = os.path.dirname(fn)
    fn_ = os.path.basename(fn)
    new_fn_ = os.path.join(
        dn_,
        note_id + ' ' + fn_[:-len(' 201808081212.md')] + '.md')
    print('mv', fn, new_fn_)
    shutil.move(fn, new_fn_)
