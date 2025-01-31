import matplotlib

matplotlib.use("Qt5Agg")

from PySide2 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from src.utils.common import get_styles_path


class Ui_MainWindow(object):
    """Ui_MainWindow is a class that sets up the user interface for the main window of the application."""

    def setupUi(self, MainWindow):
        """
        Sets up the UI for the main window.

        Args:
            MainWindow (QMainWindow): The main window instance.

        Returns:
            None
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(802, 590)
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        with open(get_styles_path(), "r") as file:
            stylesheet = file.read()
            MainWindow.setStyleSheet(stylesheet)

        #  central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        # plot button
        self.plotBtn = QtWidgets.QPushButton(self.centralwidget)
        self.plotBtn.setGeometry(QtCore.QRect(170, 390, 91, 51))
        self.plotBtn.setObjectName("plotBtn")
        self.plotBtn.setDisabled(True)

        # close button
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setGeometry(QtCore.QRect(50, 390, 93, 51))
        self.closeBtn.setObjectName("closeBtn")

        # first function input
        self.firstFnInput = QtWidgets.QLineEdit(self.centralwidget)
        self.firstFnInput.setGeometry(QtCore.QRect(40, 180, 231, 49))
        self.firstFnInput.setStyleSheet("")
        self.firstFnInput.setObjectName("firstFnInput")

        # second function input
        self.secondFnInput = QtWidgets.QLineEdit(self.centralwidget)
        self.secondFnInput.setGeometry(QtCore.QRect(40, 290, 231, 49))
        self.secondFnInput.setObjectName("secondFnInput")

        # second function label
        self.secondFnLabel = QtWidgets.QLabel(self.centralwidget)
        self.secondFnLabel.setGeometry(QtCore.QRect(70, 250, 161, 31))
        self.secondFnLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.secondFnLabel.setObjectName("secondFnLabel")

        # first function Label
        self.firstFnLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstFnLabel.setGeometry(QtCore.QRect(70, 130, 161, 41))
        self.firstFnLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.firstFnLabel.setObjectName("firstFnLabel")

        # plot area
        self.plotArea = QtWidgets.QWidget(self.centralwidget)
        self.plotArea.setGeometry(QtCore.QRect(329, 89, 441, 331))
        self.plotArea.setObjectName("plotArea")

        # plot area layout
        self.plotLayout = QtWidgets.QVBoxLayout(self.plotArea)
        self.plotArea.setLayout(self.plotLayout)

        # matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.plotLayout.addWidget(self.canvas)

        # Lines
        self.verticalLine = QtWidgets.QFrame(self.centralwidget)
        self.verticalLine.setGeometry(QtCore.QRect(300, 10, 2, 551))
        self.verticalLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLine.setObjectName("verticalLine")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 10, 691, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(100, 10, 691, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLine_2 = QtWidgets.QFrame(self.centralwidget)
        self.verticalLine_2.setGeometry(QtCore.QRect(790, 10, 2, 551))
        self.verticalLine_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalLine_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLine_2.setObjectName("verticalLine_2")
        self.verticalLine_3 = QtWidgets.QFrame(self.centralwidget)
        self.verticalLine_3.setGeometry(QtCore.QRect(10, 10, 2, 551))
        self.verticalLine_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalLine_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLine_3.setObjectName("verticalLine_3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(100, 560, 691, 2))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 560, 691, 2))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        # Error display label
        self.errorDisplayLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorDisplayLabel.setGeometry(QtCore.QRect(320, 450, 141, 16))
        self.errorDisplayLabel.setObjectName("errorDisplayLabel")

        # Error display Area
        self.errorDisplay = QtWidgets.QTextEdit(self.centralwidget)
        self.errorDisplay.setGeometry(QtCore.QRect(320, 480, 461, 49))
        self.errorDisplay.setText("")
        self.errorDisplay.setReadOnly(True)
        self.errorDisplay.setObjectName("errorDisplay")
        MainWindow.setCentralWidget(self.centralwidget)

        # Small label below the error display
        self.errorInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorInfoLabel.setGeometry(
            QtCore.QRect(320, 530, 200, 16)
        )  # Adjust position
        self.errorInfoLabel.setObjectName("errorInfoLabel")
        self.errorInfoLabel.setText("Click for more info")
        self.errorInfoLabel.setStyleSheet("color: gray; font-size: 10px;")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Sets text and tooltips for UI elements.

        Args:
            MainWindow (QMainWindow): The main window instance.

        Returns:
            None
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plotBtn.setText(_translate("MainWindow", "Plot"))
        self.closeBtn.setText(_translate("MainWindow", "Close"))
        self.secondFnInput.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Enter the Second Function</p></body></html>",
            )
        )
        second_function_label = (
            '<span style="font-family: Anime Inept; font-size: 18px; '
            'border: 2px solid #61bf81;">Second Function</span>'
        )
        self.secondFnLabel.setText(second_function_label)
        first_function_label = (
            '<span style="font-family: Anime Inept; font-size: 18px; '
            'border: 2px solid #61bf81;">First Function</span>'
        )
        self.firstFnLabel.setText(first_function_label)
        self.firstFnInput.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Enter the First Function</p></body></html>",
            )
        )
        self.errorDisplayLabel.setText(_translate("MainWindow", "Errors"))
