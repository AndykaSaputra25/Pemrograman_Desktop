import sys
from PyQt5.QtWidgets import *

#__Membuat class tampilan
class Window(QWidget):
	#__Constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Biodata')
        self.setGeometry(400, 200, 500, 350)
        self.setStyleSheet("background-color: gray; color: #fffff0; font-size: 14px")
        self.window()
        self.show()
    
    def window(self):
        #__Menu-Label
        title = QLabel('Input Biodata')
        name = QLabel('Name')
        address = QLabel('Address')
        hobby = QLabel('Hobby')
        status = QLabel('Status')

        #__style title nya
        title.setStyleSheet("font-size: 30px; color: white; background: black; font-weight: bold")

        #__Memberi tempat input
        inputName = QLineEdit()
        inputAddres1 = QLineEdit()
        inputAddres2 = QLineEdit()

        #__checkBox
        boxHobby1 = QCheckBox('Makan')
        boxHobby2 = QCheckBox('Tidur')
        boxHobby3 = QCheckBox('Main')

        #__RadioButton
        rdb1 = QRadioButton('Pelajar')
        rdb2 = QRadioButton('Pegawai')
        rdb3 = QRadioButton('Wiraswasta')

        gL = QGridLayout()
        #__menyesuaikan jika window besar/kecil
        gL.setRowStretch(10, 2)
        #__Jarak antar paragraf
        gL.setSpacing(15)

        #__Mengatur posisi
        gL.addWidget(title, 0, 0, 1, 0)   #__(name, baris, kolom, colspan, rowspan)

        gL.addWidget(name, 1, 0)          #__(name, baris, kolom)
        gL.addWidget(inputName, 1, 1)

        gL.addWidget(address, 2, 0)
        gL.addWidget(inputAddres1, 2, 1)
        gL.addWidget(inputAddres2, 3, 1)
        
        gL.addWidget(hobby, 4, 0)
        gL.addWidget(boxHobby1, 4, 1)
        gL.addWidget(boxHobby2, 5, 1)
        gL.addWidget(boxHobby3, 6, 1)

        gL.addWidget(status, 7, 0)
        gL.addWidget(rdb1, 7, 1)
        gL.addWidget(rdb2, 8, 1)
        gL.addWidget(rdb3, 9, 1)

        #__Mengatur tampilan ke GridLayout
        self.setLayout(gL)

def main():
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()