from src.model.Validator import Validator


class InputController:
    """Controller class responsible for handling input-related actions in the application."""

    def __init__(self, ui, main_window):
        self.ui = ui
        self.main_window = main_window
        self.set_input_handlers()

    def set_input_handlers(self):
        """Binds input event handlers.

        Args:
            self: The InputController instance

        Returns:
            None
        """
        self.ui.firstFnInput.textChanged.connect(self.check_empty_inputs)
        self.ui.secondFnInput.textChanged.connect(self.check_empty_inputs)
        self.ui.closeBtn.clicked.connect(self.close_action)

    def check_empty_inputs(self):
        """
        Checks if the input fields are empty.
        If either of the input fields is empty, disables the plot button.

        Args:
            self: The InputController instance

        Returns:
            None
        """
        if (
            not self.ui.firstFnInput.text().strip()
            or not self.ui.secondFnInput.text().strip()
        ):
            self.ui.plotBtn.setDisabled(True)
        else:
            self.ui.plotBtn.setEnabled(True)

    def close_action(self):
        """
        Closes the main application window.

        Args:
            self: The InputController instance

        Returns:
            None
        """
        self.main_window.close()

    def check_errors(self, func_expr: str) -> str:
        """
        Checks for errors in the given function expression using the Validator class.

        Args:
            self: The InputController instance
            func_expr (str): The function expression to be validated.

        Returns:
            str: A string containing the error messages if the expression is invalid,
                 otherwise an empty string.
        """
        validator = Validator()
        validation_result = validator.validate_expr(func_expr)
        return (
            "\n".join(validation_result["errors"])
            if not validation_result["is_valid"]
            else ""
        )

    def get_function1(self) -> str:
        """
        Retrieves the text from the first function input field in the UI.

        Args:
            self: The InputController instance

        Returns:
            str: The trimmed text from the first function input field.
        """
        return self.ui.firstFnInput.text().strip()

    def get_function2(self) -> str:
        """
        Retrieves the text from the second function input field in the UI.

        Args:
            self: The InputController instance

        Returns:
            str: The trimmed text from the second function input field.
        """
        return self.ui.secondFnInput.text().strip()

    def validate_functions(self) -> dict:
        """
        Retrieves the expressions for two functions and checks for any errors in them.

        Args:
            self: The InputController instance

        Returns:
            dict: A dictionary with the following keys:
                - is_valid (bool): True if no errors are found, False otherwise.
                - error_message (str): "No errors found" if no errors are found, otherwise the error messages.
        """
        error_message = self.check_errors(self.get_function1())
        second_func_error = self.check_errors(self.get_function2())
        if second_func_error:
            error_message += '\n' + second_func_error
        return {
            "is_valid": True if not error_message else False,
            "error_message": "" if not error_message else error_message,
        }
