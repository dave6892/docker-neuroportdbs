import sys
import qtpy.QtCore
from qtpy.QtWidgets import QApplication
from qtpy.QtCore import QTimer
from neuroport_dbs.FeaturesGUI import FeaturesGUI

def main():
    _ = QApplication(sys.argv)
    window = FeaturesGUI()
    window.show()
    timer = QTimer()
    timer.timeout.connect(window.update)
    timer.start(100)

    if (sys.flags.interactive != 1) or not hasattr(qtpy.QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()


if __name__ == '__main__':
    main()
