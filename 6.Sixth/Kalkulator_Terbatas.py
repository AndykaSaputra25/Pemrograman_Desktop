import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Perhitungan Matematika Dasar")
        self.setStyleSheet("font-size: 15px")
        self.windows()

    def windows(self):
        self.teks1 = QLabel('Kalkulator Terbatas')
        self.teks2 = QLabel('(Klik Operator yang Akan Digunakan)')
        self.hasil = QLabel()
        self.user = QLabel()

    #__Menu Pilihan
        self.plus = QPushButton('TAMBAH (+)')
        self.minus = QPushButton('KURANG (-)')
        self.kali = QPushButton('KALI (*)')
        self.bagi = QPushButton('Bagi (/)')
        self.pangkat = QPushButton('PANGKAT (**)')
        self.mod = QPushButton('MODULUS (%)')

    #__Support Halaman
        self.angka1 = QLabel('Angka 1 : ')
        self.angka2 = QLabel('Angka 2 : ')
        self.bil1 = QLineEdit()
        self.bil2 = QLineEdit()
        self.nama = QLineEdit('Nama Anda')
        self.hitung = QPushButton('HITUNG !!!')

        self.teks1.setStyleSheet("font-size: 24px; background: gold; margin: 10px 15px 25px 15px")

    #__Koneksikan
        self.plus.clicked.connect(self.penambahan)
        self.minus.clicked.connect(self.pengurangan)
        self.kali.clicked.connect(self.pengkalian)
        self.bagi.clicked.connect(self.pembagian)
        self.pangkat.clicked.connect(self.pemangkatan)
        self.mod.clicked.connect(self.pemodulusan)

    #__Posisi
        self.gL = QGridLayout()
        self.gL.addWidget(self.teks1, 0, 0, 1, 0)
        self.gL.addWidget(self.angka1, 1, 0)
        self.gL.addWidget(self.bil1, 1, 1)
        self.gL.addWidget(self.angka2, 2, 0)
        self.gL.addWidget(self.bil2, 2, 1)
        self.gL.addWidget(self.nama, 3, 0)
        self.gL.addWidget(self.teks2, 4, 0, 1, 0)
        self.gL.addWidget(self.plus, 5, 0)
        self.gL.addWidget(self.minus, 5, 1)
        self.gL.addWidget(self.kali, 6, 0)
        self.gL.addWidget(self.bagi, 6, 1)
        self.gL.addWidget(self.pangkat, 7, 0)
        self.gL.addWidget(self.mod, 7, 1)
        self.gL.addWidget(self.user, 8, 0, 1, 0)
        self.gL.addWidget(self.hasil, 9, 0, 1, 0)
        self.setLayout(self.gL)

    def penambahan(self):
        try:
            satu = float(self.bil1.text())
        except ValueError:
            self.hasil.setText("Gunakan Angka")
        else:
            try:
                dua = float(self.bil2.text())
            except ValueError:
                self.hasil.setText("Gunakan Angka")
            else:
                try:
                    nama = self.nama.text()
                except ValueError:
                    self.nama.setText("inputkan dengan benar")
                else:
                    hsl = satu + dua
                    self.user.setText('Halo Selamat Datang, ' + nama)
                    self.hasil.setText(str(satu) + ' + ' + str(dua) + ' = ' + str(hsl))

    def pengurangan(self):
        try:
            satu = float(self.bil1.text())
        except ValueError:
            self.hasil.setText("Gunakan Angka")
        else:
            try:
                dua = float(self.bil2.text())
            except ValueError:
                self.hasil.setText("Gunakan Angka")
            else:
                try:
                    nama = self.nama.text()
                except ValueError:
                    self.nama.setText("inputkan dengan benar")
                else:
                    hsl = satu - dua
                    self.user.setText('Halo Selamat Datang, ' + nama)
                    self.hasil.setText(str(satu) + ' - ' + str(dua) + ' = ' + str(hsl))

    def pengkalian(self):
        try:
            satu = float(self.bil1.text())
        except ValueError:
            self.hasil.setText("Gunakan Angka")
        else:
            try:
                dua = float(self.bil2.text())
            except ValueError:
                self.hasil.setText("Gunakan Angka")
            else:
                try:
                    nama = self.nama.text()
                except ValueError:
                    self.nama.setText("inputkan dengan benar")
                else:
                    hsl = satu * dua
                    self.user.setText('Halo Selamat Datang, ' + nama)
                    self.hasil.setText(str(satu) + ' * ' + str(dua) + ' = ' + str(hsl))

    def pembagian(self):
        try:
            satu = float(self.bil1.text())
        except ValueError:
            self.hasil.setText("Gunakan Angka")
        else:
            try:
                dua = float(self.bil2.text())
            except ValueError:
                self.hasil.setText("Gunakan Angka")
            else:
                try:
                    nama = self.nama.text()
                except ValueError:
                    self.nama.setText("inputkan dengan benar")
                else:
                    hsl = satu / dua
                    self.user.setText('Halo Selamat Datang, ' + nama)
                    self.hasil.setText(str(satu) + ' / ' + str(dua) + ' = ' + str(hsl))
    
    def pemangkatan(self):
        try:
            satu = float(self.bil1.text())
        except ValueError:
            self.hasil.setText("Gunakan Angka")
        else:
            try:
                dua = float(self.bil2.text())
            except ValueError:
                self.hasil.setText("Gunakan Angka")
            else:
                try:
                    nama = self.nama.text()
                except ValueError:
                    self.nama.setText("inputkan dengan benar")
                else:
                    hsl = satu ** dua
                    self.user.setText('Halo Selamat Datang, ' + nama)
                    self.hasil.setText(str(satu) + ' ** ' + str(dua) + ' = ' + str(hsl))

    def pemodulusan(self):
        try:
            satu = float(self.bil1.text())
        except ValueError:
            self.hasil.setText("Gunakan Angka")
        else:
            try:
                dua = float(self.bil2.text())
            except ValueError:
                self.hasil.setText("Gunakan Angka")
            else:
                try:
                    nama = self.nama.text()
                except ValueError:
                    self.nama.setText("inputkan dengan benar")
                else:
                    hsl = satu % dua
                    self.user.setText('Halo Selamat Datang, ' + nama)
                    self.hasil.setText(str(satu) + ' % ' + str(dua) + ' = ' + str(hsl))

def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()         