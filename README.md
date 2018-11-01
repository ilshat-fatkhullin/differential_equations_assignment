# Plot builder
Plot builder for differential equations course assignment.

### Installation:
1. Install Python 3.6 or later.
2. Install matplotlib:
`pip install matplotlib`
3. Install tkinter:
`pip install tkinter`
4. Clone a repository. 
5. Execute the following terminal command in a root folder of the cloned repository:
`python3 main.py`

### Main technology stack:
- Python 3.6
- PyCharm
- MatPlotLib
- TKinter
- GitHub

### Development patterns:
- Source version control
- Singleton principles

### Implementation details:
- `main.py`. It is a root script, which is responsible for front-end part of the application. Contains GUI implementation and links it with back-end.
- `plot_builder.py`. Consists of a class `PlotBuilder`, which is responsible for show of computed plots.
- `calculator.py`. Consists of a class `Calculator`, which provides the following features:
  - additional functions for calculations.
  - general solution of the equation.
  - patterns for computing results and errors by computation methods (e.g. Euler, Improves Euler, Runge Kutta).
- `methods` folder contains implementation of all computation methods.
