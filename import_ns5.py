# Imports
import os
import sys
import regex as re
from neuroport_dbs.ImportNS5FeaturesGUI import NS5OfflinePlayback

if __name__ == '__main__':
    from qtpy.QtWidgets import QApplication

    qapp = QApplication(sys.argv)

    id_re = re.compile(r"(?P<Date>\d{4}[-_]?\d{2}[-_]?\d{2})[_-]+(?P<Id>\d+)[-_]?(?P<Proc>\d+).ns5")

    base_dir = '/tmp/data/'
    files_dict = {}

    for root, dirs, files in os.walk(base_dir, topdown=False):
        ns5 = [x for x in files if x.endswith('.ns5')]
        if ns5:
            for n in ns5:
                matches = id_re.match(n)
                subject_id = matches.group('Id')
                proc_id = matches.group('Proc')

                if subject_id not in files_dict:
                    files_dict[subject_id] = []
                files_dict[subject_id].append([proc_id, os.path.join(root, n.replace('.ns5', ''))])

    # select file
    for sub, ns in files_dict.items():
        for p, f in ns:
            NS5OfflinePlayback(sub, p, f)
