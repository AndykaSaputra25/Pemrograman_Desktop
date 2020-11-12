import sys
from PyQt5.QtWidgets import *

class Kecepatan(QWidget):
    def __init__(self, parent = None):
        super(Kecepatan, self).__init__(parent)
        self.setWindowTitle("Perhitungan Matematika Dasar")
        self.setStyleSheet("font-size: 15px")
        self.windows()

    def windows(self):
        self.teks1 = QLabel('Rumus Kecepatan')
        self.teks2 = QLabel('(Klik Operator yang Akan Digunakan)')
        self.hasil = QLabel()
        self.user = QLabel()

    #__Menu Pilihan
        self.speed = QPushButton('Kecepatan')
        self.distance = QPushButton('Jarak')
        self.time = QPushButton('Waktu')

    #__Support Halaman
        self.angka1 = QLabel('Kecepatan (m/s)   :')
        self.angka2 = QLabel('Jarak (m)             :')
        self.angka3 = QLabel('Waktu (s)             :')
        self.bil1 = QLineEdit()
        self.bil2 = QLineEdit()
        self.bil3 = QLineEdit()
        self.nama = QLineEdit('Nama Anda')
        self.hitung = QPushButton('HITUNG !!!')

        self.teks1.setStyleSheet("font-size: 24px; background: gold; margin: 10px 15px 25px 15px")

    #__Koneksikan
        self.speed.clicked.connect(self.kecepatan)
        self.distance.clicked.connect(self.jarak)
        self.time.clicked.connect(self.waktu)

    #__Posisi
        self.gL = QGridLayout()
        self.gL.addWidget(self.teks1, 0, 0, 1, 0)
        self.gL.addWidget(self.angka1, 1, 0)
        self.gL.addWidget(self.bil1, 1, 1)
        self.gL.addWidget(self.angka2, 2, 0)
        self.gL.addWidget(self.bil2, 2, 1)
        self.gL.addWidget(self.angka3, 3, 0)
        self.gL.addWidget(self.bil3, 3, 1)
        self.gL.addWidget(self.nama, 4, 0)
        self.gL.addWidget(self.teks2, 5, 0, 1, 0)
        self.gL.addWidget(self.speed, 6, 0)
        self.gL.addWidget(self.distance, 6, 1)
        self.gL.addWidget(self.time, 7, 0, 1, 0)
        self.gL.addWidget(self.user, 8, 0, 1, 0)
        self.gL.addWidget(self.hasil, 9, 0, 1, 0)
        self.setLayout(self.gL)

    def kecepatan(self):
        try:
            dua = float(self.bil2.text())
        except ValueError:
            self.hasil.setText("Gunakan Angka")
        else:
            try:
                tiga = float(self.bil3.text())
            except ValueError:
                self.hasil.setText("Gunakan Angka")
            else:
                try:
                    nama = self.nama.text()
                except ValueError:
                    self.nama.setText("inputkan dengan benar")
                else:
                    hsl = dua / tiga
                    self.user.setText('__Kecepatan__ Halo Selamat Datang, ' + nama)
                    self.hasil.setText('Jarak' + ' / ' + 'Waktu' + ' = ' + str(hsl) + ' m/s ')

    def jarak(self):
        try:
            satu = float(self.bil1.text())
        except ValueError:
            self.hasil.setText("Gunakan Angka")
        else:
            try:
                tiga = float(self.bil3.text())
            except ValueError:
                self.hasil.setText("Gunakan Angka")
            else:
                try:
                    nama = self.nama.text()
                except ValueError:
                    self.nama.setText("inputkan dengan benar")
                else:
                    hsl = satu * tiga
                    self.user.setText('__Jarak__ Halo Selamat Datang, ' + nama)
                    self.hasil.setText('Kecepatan' + ' * ' + 'Waktu' + ' = ' + str(hsl) + ' m ')

    def waktu(self):
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
                    hsl = dua / satu
                    self.user.setText('__Waktu__ Halo Selamat Datang, ' + nama)
                    self.hasil.setText('Jarak' + ' / ' + 'Kecepatan' + ' = ' + str(hsl) + ' s ')

def main():
    app = QApplication(sys.argv)
    win = Kecepatan()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()         