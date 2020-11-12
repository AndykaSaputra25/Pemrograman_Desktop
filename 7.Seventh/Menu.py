import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import QtGui 

from Rumus_Kecepatan import *
from Kalkulator_Terbatas import *

class Window():
    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)
        self.mWin = QMainWindow()
        self.win1 = QWidget()
        self.mWin.setWindowTitle("Kumpulan Rumus Matematika")
        self.mWin.setWindowIcon(QtGui.QIcon('pythonLogo.png')) 
        self.windows()

    def windows(self):
        self.bar = self.mWin.menuBar()
        self.file1 = self.bar.addMenu('File')
        self.transaksi = self.bar.addMenu('Help')

        self.save = QAction('Save')
        self.about = QAction('About')
        more1a = QAction('New')
        more1b = QAction('Rumus Kecepatan')
        more1c = QAction('Kalkulator Sederhana')

        more1 = self.file1.addMenu('More')
        
        self.file1.addAction(self.save)
        self.file1.addAction(self.about)
        more1.addAction(more1a)
        more1.addAction(more1b)
        more1.addAction(more1c)

        self.save.setShortcut('Ctrl+S')
        more1a.setShortcut('Ctrl+N')

        more1a.triggered.connect(self.more1_action)
        more1b.triggered.connect(self.more1b_action)
        more1c.triggered.connect(self.more1c_action)

        self.mWin.show()
        sys.exit(self.app.exec_())

    def more1_action(self):
        self.win1.setWindowTitle('Window1')
        self.win1.setGeometry(100, 100, 200, 300)
        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap('mtk.jpg'))
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl)
        self.win1.setLayout(vbox)
        self.win1.show()

    def more1b_action(self):
        self.kpn = Kecepatan()
        self.kpn.show()

    def more1c_action(self):
        self.katas = KalkulatorTerbatas()
        self.katas.show()


if __name__ == '__main__':
    Window()  