from PySide2 import QtCore, QtWidgets
from src.model.Solver import Solver
from src.model.Plotter import Plotter
from src.controller.InputController import InputController


class OutputController:
    """Controller class responsible for handling output-related actions in the application."""

    def __init__(self, ui, main_window):
        self.ui = ui
        self.main_window = main_window
        self.inputController = InputController(ui, main_window)
        self.set_output_handlers()

    def set_output_handlers(self):
        """
        Binds output event handlers.

        Args:
            self: The OutputController instance

        Returns:
            None
        """
        self.ui.plotBtn.clicked.connect(self.plot_action)
        self.ui.errorDisplay.mousePressEvent = self.show_error_popup

    def plot_action(self):
        """
        Validates the input functions and plots the functions and their intersections.

        Args:
            self: The OutputController instance

        Returns:
            None
        """
        validation_result = self.inputController.validate_functions()
        print("validation_result", validation_result)
        if not validation_result["is_valid"]:
            self.show_errors(validation_result["error_message"])
            return

        func1_expr = self.inputController.get_function1()
        func2_expr = self.inputController.get_function2()
        solver = Solver(func1_expr, func2_expr)
        solution_result = solver.find_intersections()
        print("solution_result", solution_result)
        if solution_result["error"]:
            self.show_errors(solution_result["error"])
            return

        plotter = Plotter(func1_expr, func2_expr, solution_result["intersections"])
        self.show_errors("")
        self.ui.figure.clear()
        plotter.plot(ax=self.ui.figure.add_subplot(111))
        self.ui.canvas.draw()

    def show_errors(self, error_message: str):
        """
        Displays the provided error message in the UI's error display widget.

        Args:
            error_message (str): The error message to be displayed.

        Returns:
            None
        """
        self.ui.figure.clear()
        self.ui.canvas.draw()

        if error_message:
            self.ui.errorDisplay.setText(error_message)
        else:
            no_errors_message = "No errors found. Form submitted successfully!"
            html_text = f'<font face="Arial" color="#61bf81" font-size = "18px" border-color= "#61bf81">{no_errors_message}</font>'
            self.ui.errorDisplay.setHtml(html_text)

    def show_error_popup(self, _):
        """
        Displays a custom error popup dialog with detailed error messages.

        Args:
            self: The OutputController instance
            _: Unused event argument

        Returns:
            None
        """
        # Create a custom QDialog to replace QMessageBox
        error_dialog = QtWidgets.QDialog()
        error_dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        error_dialog.setMinimumWidth(500)  # Make the dialog wider

        # Apply the same QSS styling to the QDialog
        error_dialog.setStyleSheet(
            """
            QDialog {
                background-color: #2e3440;  /* Dark blue-gray background */
                color: #d8dee9;             /* Light gray text */
                font-size: 14px;
                border: 2px solid #4c566a;  /* Light blue-gray border */
                border-radius: 10px;        /* Rounded corners */
            }
            QLabel {
                color: #d8dee9;             /* Light gray text */
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton {
                padding: 10px;
                font-size: 14px;
                background-color: #81a1c1;  /* Light blue background */
                color: #2e3440;             /* Dark blue-gray text */
                border-radius: 10px;        /* More rounded corners */
                border: 2px solid #81a1c1;  /* Light blue border */
            }
            QPushButton:hover {
                background-color: #88c0d0;  /* Light cyan on hover */
                border: 2px solid #88c0d0;
            }
            QPushButton:pressed {
                background-color: #5e81ac;  /* Darker blue on press */
                border: 2px solid #5e81ac;
            }
        """
        )

        # Create a custom title bar
        title_bar = QtWidgets.QWidget()
        title_bar.setStyleSheet(
            "background-color: #4c566a; border-top-left-radius: 10px; border-top-right-radius: 10px;"
        )
        title_bar_layout = QtWidgets.QHBoxLayout()

        # Add a title label
        title_label = QtWidgets.QLabel("Detailed Errors")
        title_label.setStyleSheet("color: #d8dee9; font-size: 16px; font-weight: bold;")
        title_bar_layout.addWidget(title_label)
        title_bar.setLayout(title_bar_layout)

        # Add a QLabel to display the error message
        error_message = self.ui.errorDisplay.toPlainText()
        error_message = (
            "• " + error_message.replace("\n", "\n• ") if error_message else ""
        )
        error_message, error_message_2 = error_message.split("\n")
        error_label = QtWidgets.QLabel(error_message)
        error_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        error_label.setWordWrap(True)  # Enable word wrap for long text

        error_label2 = QtWidgets.QLabel(error_message_2)
        error_label2.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        error_label2.setWordWrap(True)

        # Add a close button at the bottom
        bottom_close_button = QtWidgets.QPushButton("Close")
        bottom_close_button.clicked.connect(error_dialog.close)

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(title_bar)
        layout.addWidget(error_label)
        layout.addWidget(error_label2)
        layout.addWidget(bottom_close_button, alignment=QtCore.Qt.AlignCenter)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        error_dialog.setLayout(layout)

        # Show the dialog
        error_dialog.exec_()
