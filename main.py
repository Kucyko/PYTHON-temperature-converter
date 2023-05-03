from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Temperature Converter")
        self.setGeometry(100, 100, 400, 200)

        
        self.label_type = QLabel("Select type:", self)
        self.radio_celsius = QRadioButton("Celsius to Fahrenheit", self)
        self.radio_fahrenheit = QRadioButton("Fahrenheit to Celsius", self)
        self.label_temp = QLabel("Temperature:", self)
        self.text_temp = QLineEdit(self)
        self.button_convert = QPushButton("Convert", self)
        self.label_result = QLabel("", self)

        
        font = QFont()
        font.setPointSize(12)
        self.label_type.setFont(font)
        self.radio_celsius.setFont(font)
        self.radio_fahrenheit.setFont(font)
        self.label_temp.setFont(font)
        self.text_temp.setFont(font)
        self.button_convert.setFont(font)
        self.label_result.setFont(font)

        
        layout = QVBoxLayout()
        layout.addWidget(self.label_type)
        layout.addWidget(self.radio_celsius)
        layout.addWidget(self.radio_fahrenheit)
        layout.addWidget(self.label_temp)
        layout.addWidget(self.text_temp)
        layout.addWidget(self.button_convert)
        layout.addWidget(self.label_result)
        self.setLayout(layout)

        
        self.button_convert.clicked.connect(self.convert)
    def convert(self):
        try: 
            temp = int(self.text_temp.text())
            if self.radio_celsius.isChecked():
                result = str((temp * 9 / 5) + 32) + " Fahrenheits"
            elif self.radio_fahrenheit.isChecked():
                result = str((temp-32) *5/9) +" Celsius"
            else:
                result = "Invalid type of program!"
            self.label_result.setText(result)
        except ValueError:
            self.label_result.setText("You need tot ype a number!")

if __name__ == "__main__":
    app = QApplication([])
    converter = TemperatureConverter()
    converter.show()
    app.exec_()
