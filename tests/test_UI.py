import pytest
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Qt
from src.view.mainWindow import Ui_MainWindow
from src.controller.InputController import InputController
from src.controller.OutputController import OutputController

@pytest.fixture
def app(qtbot):
    return QApplication.instance() or QApplication([])

@pytest.fixture
def main_window(app):
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    return window, ui

@pytest.fixture
def input_controller(main_window):
    window, ui = main_window
    return InputController(ui, window)

@pytest.fixture
def output_controller(main_window):
    window, ui = main_window
    return OutputController(ui, window)

def test_empty_inputs(input_controller, qtbot):
    input_controller.ui.firstFnInput.setText("")
    input_controller.ui.secondFnInput.setText("")
    assert not input_controller.ui.plotBtn.isEnabled()

def test_filled_inputs(input_controller, qtbot):
    input_controller.ui.firstFnInput.setText("x^2")
    input_controller.ui.secondFnInput.setText("x")
    assert input_controller.ui.plotBtn.isEnabled()

def test_valid_function_validation(input_controller):
    input_controller.ui.firstFnInput.setText("x^2")
    input_controller.ui.secondFnInput.setText("x")
    result = input_controller.validate_functions()
    assert result["is_valid"]
    assert result["error_message"] == ""

def test_invalid_function_validation(input_controller):
    input_controller.ui.firstFnInput.setText("invalid")
    input_controller.ui.secondFnInput.setText("x")
    result = input_controller.validate_functions()
    assert not result["is_valid"]
    assert "Invalid character" in result["error_message"]

def test_plot_action_valid_input(output_controller, qtbot):
    output_controller.ui.firstFnInput.setText("x^2")
    output_controller.ui.secondFnInput.setText("x")
    qtbot.mouseClick(output_controller.ui.plotBtn, Qt.LeftButton)
    assert (
        output_controller.ui.errorDisplay.toPlainText()
        == "No errors found. Form submitted successfully!"
    )

def test_plot_action_invalid_input(output_controller, qtbot):
    output_controller.ui.firstFnInput.setText("invalid")
    output_controller.ui.secondFnInput.setText("x")
    qtbot.mouseClick(output_controller.ui.plotBtn, Qt.LeftButton)
    assert "Invalid character" in output_controller.ui.errorDisplay.toPlainText()

def test_close_action(input_controller, qtbot):
    window = input_controller.main_window
    window.show()
    qtbot.addWidget(window)
    qtbot.waitExposed(window)

    # Click close button
    qtbot.mouseClick(input_controller.ui.closeBtn, Qt.LeftButton)
    qtbot.wait(100)  # Small wait to process events

    # Close window and process events
    window.close()
    QApplication.processEvents()

    # Verify window is closed
    assert not window.isVisible()