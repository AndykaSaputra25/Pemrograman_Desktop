import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WidgetsGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styles")
        self.gunakanPalette = QApplication.palette()       #__rubah warna
        self.windows()
    
    def windows(self):
#__Opening
        lbl = QLabel("Style:")
        #__ComboBox
        comBox = QComboBox()
        comBox.addItems(['Data Science', 'Data Analysis', 'Data Enginering'])
        #__CeckBox
        self.cekBox = QCheckBox("Use style's standard palette")
        self.cekBox.setChecked(True)
        cekBox1 = QCheckBox("Disable widgets")

    #__Fungsi yang akan di tampilkan
        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createProgressBar()

    #__Toggled  memancarkan sinyal respon ke changePalette
        self.cekBox.toggled.connect(self.changePalette)
        cekBox1.toggled.connect(self.topLeftGroupBox.setDisabled)
        cekBox1.toggled.connect(self.topRightGroupBox.setDisabled)
        cekBox1.toggled.connect(self.bottomRightGroupBox.setDisabled)
        cekBox1.toggled.connect(self.bottomLeftTabWidget.setDisabled)

    #__Horizontal
        topLayout = QHBoxLayout()
        topLayout.addWidget(lbl)
        topLayout.addWidget(comBox)
        topLayout.addStretch(1)             #__item spaccer
        topLayout.addWidget(self.cekBox)
        topLayout.addWidget(cekBox1)

    #__posisi GridLayout
        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        self.setLayout(mainLayout)

    #__jenis style yang di inginkan
        self.changeStyle('Fusion')
        
#__Group-1
    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Group 1")

        radioButton1 = QRadioButton("radio button 1")
        radioButton2 = QRadioButton("radio button 2")
        radioButton3 = QRadioButton("radio button 3")
        radioButton1.setChecked(True)

        checkbox = QCheckBox("Tri-state check box")
        checkbox.setTristate(True)                  #__status Ekslusif/Netral
        checkbox.setCheckState(Qt.PartiallyChecked) #__item di centang sebagian
    #__Vertikal
        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addWidget(checkbox)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)  


#__Group-2
    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Group 2")

        defaultPushButton = QPushButton("Default Push Button")
        defaultPushButton.setDefault(True)

        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)     #__setel tombol (sakelar)
        
        flatPushButton = QPushButton("Flat Push Button")
        flatPushButton.setFlat(True)
    #__Vertikal
        layout = QVBoxLayout()
        layout.addWidget(defaultPushButton)
        layout.addWidget(togglePushButton)
        layout.addWidget(flatPushButton)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

#__Group-3
    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()

        tab1 = QWidget()
    #__set Baris * Kolom
        tableWidget = QTableWidget(15, 10) 

        tab2 = QWidget()
        textEdit = QTextEdit()

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        textEdit.setPlainText("Nama :   Moch. Andyka Saputra\n"
                            "NIM  :   190411100070\n" 
                            "Univ :   Universitas Trunojoyo\n"
                            "Asal :   Sidoarjo\n")
        
        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab1, "Table")
        self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")


#__Group-4
    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Group 3")
        self.bottomRightGroupBox.setCheckable(True)

        lineEdit = QLineEdit('HaloSemuaSayaDisini')
        lineEdit.setEchoMode(QLineEdit.Password)

        spinBox = QSpinBox(self.bottomRightGroupBox)
        spinBox.setValue(50)

        dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
        dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
        slider.setValue(20)

        scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
        scrollBar.setValue(30)
        
        dial = QDial(self.bottomRightGroupBox)
        dial.setValue(30)
        dial.setNotchesVisible(True) 

        layout = QGridLayout()
        layout.addWidget(lineEdit, 0, 0, 1, 2)
        layout.addWidget(spinBox, 1, 0, 1, 2)
        layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
        layout.addWidget(slider, 3, 0)
        layout.addWidget(scrollBar, 4, 0)
        layout.addWidget(dial, 3, 1, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)

#__Group-5
    def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0,100)
        self.progressBar.setValue(82)

#__Sinyal respon dan merubah style dari window app
    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()
    def changePalette(self):
        if (self.cekBox.isChecked()):
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.gunakanPalette)


def main():
    app = QApplication(sys.argv)
    win = WidgetsGUI()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()    
