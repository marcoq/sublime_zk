
import os
import shutil

folder = os.path.expanduser('~/Dropbox/notes/ulysses/')

root_dirs_files = os.walk(folder)
for root, dirs, files in root_dirs_files:
    for f in files:
        if not f.endswith('.md'):
            continue
        f_path = os.path.join(root, f)
        f_code = int(os.path.basename(f).split(' ')[0])
        f_real = ' '.join(os.path.basename(f_path).split(' ')[1:])
        f_new = '/Users/marcoq/Dropbox/notes/ulysses/%s00 %s' % (
            f_code, f_real)
        shutil.move(f_path, f_new)
