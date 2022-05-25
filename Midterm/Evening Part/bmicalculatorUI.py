import tkinter as tk
from tkinter import ttk

from bmicalculator import ENGLISH, METRIC


class BMICalculatorUI(tk.Tk):

    def __init__(self, calculator):
        super().__init__()
        self.calculator = calculator
        self.unit = METRIC
        self.initcomponents()

    def initcomponents(self):
        options = {'padx': 5, 'pady': 5, 'sticky': tk.EW}

        self.title('BMI Calculator')
        self.style = ttk.Style(self)
        self.style.configure('TRadiobutton', foreground='#8BFFF6')
        self.style.configure(
            'TEntry', background='#181A20', foreground='#E6F137', font=('Menlo', 17))
        self.style.configure('TLabel', font=('Menlo', 17))

        # tk variable
        self.radio_var = tk.StringVar()
        self.height_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        self.bmi_var = tk.StringVar()
        self.height_entry_var = tk.StringVar()
        self.weight_entry_var = tk.StringVar()
        self.health_var = tk.StringVar()

        # label
        self.input_label = tk.Label(self, text="InputUnits")
        self.bmi_label = tk.Label(self, text='BMI')
        self.height_unit_label = tk.Label(self, textvariable=self.height_var)
        self.weight_unit_label = tk.Label(self, textvariable=self.weight_var)
        self.bmi_ans_label = tk.Label(
            self, textvariable=self.bmi_var, bg='#011627', fg='#39FF14', anchor=tk.W)
        self.health_label = tk.Label(
            self, textvariable=self.health_var, font=("Menlo", 10))

        # Entry
        self.height_entry = tk.Entry(self, textvariable=self.height_entry_var)
        self.weight_entry = tk.Entry(self, textvariable=self.weight_entry_var)

        # button
        self.radbutton1 = ttk.Radiobutton(
            self, text=ENGLISH, variable=self.radio_var, value=ENGLISH, command=lambda: self.loadunits(ENGLISH))
        self.radbutton2 = ttk.Radiobutton(
            self, text=METRIC, variable=self.radio_var, value=METRIC, command=lambda: self.loadunits(METRIC))
        self.calc_button = tk.Button(
            self, text="Calculate BMI", command=self.calculate_handler)
        self.clear_button = tk.Button(self, text="Clear", command=self.clear)

        # grid
        self.input_label.grid(row=0, column=0, columnspan=2, **options)
        self.radbutton1.grid(row=0, column=3, **options)
        self.radbutton2.grid(row=0, column=2, **options)
        self.height_unit_label.grid(row=1, column=0, columnspan=2, **options)
        self.height_entry.grid(row=1, column=2, columnspan=2, **options)
        self.weight_unit_label.grid(row=2, column=0, columnspan=2, **options)
        self.weight_entry.grid(row=2, column=2, columnspan=2, **options)
        self.calc_button.grid(row=3, column=0, columnspan=2, **options)
        self.clear_button.grid(row=3, column=2, columnspan=2, **options)
        self.bmi_label.grid(row=4, column=1, **options)
        self.bmi_ans_label.grid(row=4, column=2, columnspan=2, **options)
        self.health_label.grid(row=5, column=0, columnspan=4, **options)


        # configuration
        self.radio_var.set(self.unit)
        rows, cols = self.grid_size()
        for row in range(rows):
            self.rowconfigure(row, weight=1)
        for col in range(cols):
            self.columnconfigure(col, weight=1)
        self.loadunits(self.unit)

    def loadunits(self, units):
        if units in (ENGLISH, METRIC):
            height, weight = units.split('-')
            self.height_var.set(f"Height ({height})")
            self.weight_var.set(f"Weight ({weight})")
        self.clear()

    def clear(self):
        tk_var_list = [self.height_entry_var,
                       self.weight_entry_var, self.bmi_var, self.health_var]

        for var in tk_var_list:
            var.set("")

    def calculate_handler(self):
        try:
            height = float(self.height_entry_var.get())
            weight = float(self.weight_entry_var.get())
            if height < 0 or weight < 0:
                raise ValueError("height or weight can't be negative")
            units = self.radio_var.get()
            bmi = self.calculator.bmi(height, weight, units)
            health_status = self.calculator.health_assessment(bmi)
            self.bmi_var.set(f'{bmi:.1f}')
            self.health_var.set(health_status)
        except (ValueError, TypeError, ZeroDivisionError):
            self.clear()

    def run(self):
        self.mainloop()
