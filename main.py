from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

photoCell = QLabel()

fileButton = QPushButton("Папка")
steerLeftButton = QPushButton("Вліво")
steerRightButton = QPushButton("Вправо")
mirrorButton = QPushButton("Дзеркало")
sharpnessButton = QPushButton("Різкість")
BWButton = QPushButton("Ч/Б")

listFileButton = QListWidget()

mainLine = QHBoxLayout()
extraLine1 = QVBoxLayout()
extraLine2 = QVBoxLayout()
extraLine3 = QHBoxLayout()

extraLine1.addWidget(fileButton)
extraLine1.addWidget(listFileButton)
mainLine.addLayout(extraLine1)

extraLine2.addWidget(photoCell)
mainLine.addLayout(extraLine2)

extraLine3.addWidget(steerLeftButton)
extraLine3.addWidget(steerRightButton)
extraLine3.addWidget(mirrorButton)
extraLine3.addWidget(sharpnessButton)
extraLine3.addWidget(BWButton)
extraLine2.addLayout(extraLine3)

window.setLayout(mainLine)
window.show()
app.exec()