import sys
from PySide2 import QtWidgets, QtGui

from src.utils.common import add_fonts
from src.view.mainWindow import Ui_MainWindow
from src.controller.OutputController import OutputController

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    database = QtGui.QFontDatabase()
    add_fonts(database)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    oc = OutputController(ui, MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())