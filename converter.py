import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox

valut = {
    'рубль': 1,
    'доллар': 70,
    'евро': 80
}


class window(QWidget):
    def __init__(self):
        super(window, self).__init__()
        self.setWindowTitle('конвертор валют')
        self.setFixedSize(270, 90)

        self.input_value = QLineEdit(self)
        self.input_value.move(10, 10)
        self.input_value.resize(100, 30)

        self.input_type = QComboBox(self)
        self.input_type.move(10, 50)
        self.input_type.resize(100, 30)
        self.input_type.addItems(valut.keys())

        self.convert_button = QPushButton(self)
        self.convert_button.setText('->')
        self.convert_button.move(120, 10)
        self.convert_button.resize(30, 70)
        self.convert_button.clicked.connect(self.convert)

        self.output_value = QLineEdit(self)
        self.output_value.setEnabled(False)
        self.output_value.move(160, 10)
        self.output_value.resize(100, 30)

        self.output_type = QComboBox(self)
        self.output_type.move(160, 50)
        self.output_type.resize(100, 30)
        self.output_type.addItems(valut.keys())

    def convert(self):
        input = float(self.input_value.text()) * valut[
            self.input_type.currentText()]
        output = input / valut[self.output_type.currentText()]
        self.output_value.setText(f'{output:.2f}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec_())
