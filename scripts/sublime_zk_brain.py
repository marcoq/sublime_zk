import os
import pprint
import re

folder = os.path.expanduser('~/Dropbox/notes/')
f_codes = {}

root_dirs_files = os.walk(folder)
for root, dirs, files in root_dirs_files:
    for f in files:
        if f.endswith('.md'):
            try:
                f_code = int(os.path.basename(f).split(' ')[0])
                f_codes[f_code] = os.path.join(root, f)
            except ValueError:
                pass

links = dict()

root_dirs_files = os.walk(folder)
for root, dirs, files in root_dirs_files:
    for f in files:
        if f.endswith('.md'):
            f_links = [
                re.findall(
                    r'\[\[([0-9]{12})\]\] .*', l)
                for l in open(
                    os.path.join(root, f)).readlines(
                        )
                if '[[' in l and ']]' in l]
            if f_links:
                f_links = reduce(lambda a, b: a+b, f_links)
                links[f] = [
                    f_codes.get(int(f_code), None)
                    for f_code in f_links]

pprint.pprint(links)
