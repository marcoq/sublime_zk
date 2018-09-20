# sublime_fixer.py

import os
import shutil

folder = os.path.expanduser('~/Dropbox/notes/ulysses/')
f_codes = {}

root_dirs_files = os.walk(folder)
for root, dirs, files in root_dirs_files:
    for f in files:
        if f.endswith('.md'):
            try:
                f_code = int(os.path.basename(f).split(' ')[0])
                f_codes[os.path.join(root, f)] = f_code
            except ValueError:
                pass

used_codes = list()

for (f, f_code) in f_codes.iteritems():
    new_f_code = f_code
    while new_f_code in used_codes:
        new_f_code += 1
    used_codes.append(new_f_code)
    if new_f_code != f_code:
        new_basename_f = ' '.join(
            os.path.basename(f).split(' ')[1:])
        if new_basename_f.startswith('# '):
            new_basename_f = new_basename_f[2:]
        new_f = "%s/%d %s" % (
            os.path.dirname(f),
            new_f_code,
            new_basename_f)
        print('mv', f, new_f)
        shutil.move(
            f,
            new_f)
