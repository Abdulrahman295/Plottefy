# Plottefy
<div align="center">
  <p align="center">A Python GUI application built with PySide2 and Matplotlib that allows users to input two mathematical functions of `x`, solves them, and plots the functions with the solution point annotated.</p>
   <p align="center">
      <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
      <img src="https://img.shields.io/badge/PySide2-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="PySide2"/>
      <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib"/>
   </p>
</div>


## ✨ Features
- **Input Two Functions:** Users can input two mathematical functions of `x` (e.g., `5*x^3 + 2*x`).
- **Supported Operators:** The program supports `+`, `-`, `/`, `*`, `^` (exponentiation), `log10()`, and `sqrt()`.
- **Input Validation:** Ensures valid input and displays helpful error messages for invalid inputs.
- **Dynamic Plotting:** Plot the function curve based on the user's input, with the solution point (intersection) annotated and centered on the graph.
- **Modern GUI:** The interface is styled using PySide2's Qt-based stylesheet support, delivering a visually appealing design.


## ☑️ Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.7 or higher


## 🗺️ Installation
1. Clone this repo:
```Bash
git clone https://github.com/Abdulrahman295/Plottefy.git
cd Plottefy
```
2. Install the required dependencies:
```Bash
pip install -r requirements.txt
```


## 💡 Usage
To start Plottefy, run the following command:
```bash
python main.py
```

Once the application is running, you can interact with the GUI to input two functions, solve them, and plot their intersection:
1. Enter Two Functions of x:
   - Supported operations: +, -, *, /, ^.
   - Supported functions: log10(), sqrt().
   - Example:
     - First function: x + 1.
     - Second function: x^2.
3. Plot the Functions and Find the Intersection:
   - Click the "Plot" button to:
     - Plot both functions on the same graph.
     - Annotate the intersection point(s) on the graph.
4. Error Handling:
   - If the input is invalid (e.g., unsupported characters), the application will display an error message to guide you.


## 📷 Screenshots

## 📰 License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
  
