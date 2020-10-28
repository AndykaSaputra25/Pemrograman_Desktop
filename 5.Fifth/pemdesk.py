import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laundry Andyka")
        self.windows()
        self.setGeometry(400, 50, 400, 500)
        self.setStyleSheet("font-size: 15px")
    
    def windows(self):
        #__Menu-Label
        cekBox1 = QCheckBox("Disable widgets (non aktifkan inputan)")
        title = QLabel('Andyka Laundry')
        nama = QLabel('Nama:')
        alamat = QLabel('Alamat:')
        nomor = QLabel('Nomor WhatsApp/HP:')
        berat = QLabel('Berat (kg):')
        kode = QLabel('Kode jenis (cb/ck/cs/s):')
        total = QLabel('Total yang Harus di Bayar:')
        self.hasil = QLabel()
        self.hak = QLabel('Copyright (c) Pemrograman Desktop 2020')


        #__waktu
        dateTimeEdit = QDateTimeEdit(self)
        dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        
        #__RadioButton
        cb = QRadioButton('CB (Cuci Basah)')
        ck = QRadioButton('CK (Cuci Kering)')
        cs = QRadioButton('CS (Cuci Setrika)')
        s = QRadioButton('S (Setrika)')

        #__Memberi tempat input
        inputNama = QLineEdit()
        inputAlamat = QLineEdit()
        inputNomor = QLineEdit()
        self.inputBerat = QLineEdit()
        self.inputKode = QLineEdit()

        #__Label-Harga
        hcb = QLabel('Rp. 3,000/kg')
        hck = QLabel('Rp. 4,000/kg')
        hcs = QLabel('Rp. 5,500/kg')
        hs = QLabel('Rp. 4,000/kg')

        lanjut = QPushButton("H I T U N G")
        lanjut.clicked.connect(self.hitung)

        #__Kalender
        self.kalender = QCalendarWidget()
        self.kalender.setGridVisible(True)

        #__Disable Inputan
        cekBox1.toggled.connect(self.inputBerat.setDisabled)
        cekBox1.toggled.connect(inputNama.setDisabled)
        cekBox1.toggled.connect(self.inputKode.setDisabled)
        cekBox1.toggled.connect(inputAlamat.setDisabled)
        cekBox1.toggled.connect(inputNomor.setDisabled)

        #__style
        title.setStyleSheet("font-size: 45px; color: blue; background: gold; font-weight: bold")
        total.setStyleSheet("font-size: 21px; font-weight: bold")
        self.hak.setAlignment(Qt.AlignCenter)

        gL = QGridLayout()
        #__Mengatur posisi
        gL.addWidget(title, 0, 0)
        gL.addWidget(cekBox1, 0, 1)

        gL.addWidget(nama, 1, 0)
        gL.addWidget(inputNama, 1, 1)

        gL.addWidget(alamat, 2, 0)
        gL.addWidget(inputAlamat, 2, 1)

        gL.addWidget(nomor, 3, 0)
        gL.addWidget(inputNomor, 3, 1)

        gL.addWidget(cb, 4, 0)
        gL.addWidget(hcb, 4, 1)

        gL.addWidget(ck, 5, 0)
        gL.addWidget(hck, 5, 1)

        gL.addWidget(cs, 6, 0)
        gL.addWidget(hcs, 6, 1)

        gL.addWidget(s, 7, 0)
        gL.addWidget(hs, 7, 1)

        gL.addWidget(kode, 8, 0)
        gL.addWidget(self.inputKode, 8, 1)

        gL.addWidget(berat, 9, 0)
        gL.addWidget(self.inputBerat, 9, 1)

        gL.addWidget(dateTimeEdit, 10, 0)
        gL.addWidget(lanjut, 10, 1)

        gL.addWidget(total, 11, 0)
        gL.addWidget(self.hasil, 11, 1)

        gL.addWidget(self.kalender, 12, 0, 1, 0)

        gL.addWidget(self.hak, 13, 0, 1, 0)

        #__Mengatur tampilan ke GridLayout
        self.setLayout(gL)

    def hitung(self):
        try:
            bil1 = float(self.inputBerat.text())
        except ValueError:
            self.hasil.setText("Inputan Salah")
        else:
            try:
                bil2 = str(self.inputKode.text())
            except ValueError:
                self.hasil.setText("Kode Tidak Ditemukan")
            else:
                    if bil2 == 'cb' or bil2 == 'CB':
                        hsl = bil1 * 3000
                        self.hasil.setText('Rp. ' + str(hsl))
                    elif bil2 == 'ck' or bil2 == 'CK' or bil2 == 's' or bil2 =='S':
                        hsl = bil1 * 4000
                        self.hasil.setText('Rp. ' + str(hsl))
                    elif bil2 == 'cs' or bil2 == 'CS':
                        hsl = bil1 * 5500
                        self.hasil.setText('Rp. ' + str(hsl))


def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 