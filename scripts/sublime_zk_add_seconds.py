# sublime_zk_add_seconds
import os
import pprint
import re
import shutil

folder = os.path.expanduser('~/Dropbox/notes/')

failed_asserts = list()
root_dirs_files = os.walk(folder)
for root, dirs, files in root_dirs_files:
    for f in files:
        try:
            f_dir = root
            f_code = os.path.basename(f).split(' ')[0]
            assert re.match(r'[0-9]{12}', f_code)
            f_title = ' '.join(os.path.basename(f).split(' ')[1:])
            shutil.move(
                os.path.join(root, f),
                os.path.join(
                    f_dir, '%s00 %s' % (f_code, f_title)))
        except ValueError:
            print('skip', f)
        except AssertionError:
            failed_asserts.append(f)


pprint.pprint(failed_asserts)

