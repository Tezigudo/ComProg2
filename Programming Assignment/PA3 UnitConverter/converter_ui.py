import tkinter as tk
from time import sleep
from tkinter import Label, ttk

from converter import UnitConverter
from unittype import UnitType


class ConverterUI(tk.Tk):
    """User Interface for a unit converter.

    The UI displays units and handles user interaction.  It invokes
    a UnitConverter object to perform actual unit conversions.
    """

    def __init__(self, converter: UnitConverter) -> None:
        super().__init__()
        # save a reference to the unit converter
        self.converter = converter
        # configure initial thing
        self.title('God\'s Unit Converter')

        # to access values of the comboboxes and input fields

        self.init_components()

    def init_components(self) -> None:
        """Create components and layout the UI."""

        options = {'padx': 5, 'pady': 5, 'sticky': tk.EW}
        font_opt = {'font': {'Menlo', 20}, 'bg': '#011627', 'fg': '#39FF14'}

        # create a menu
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        self.unit_change_bar = tk.Menu(self.menu)
        self.menu.add_cascade(label='Unit', menu=self.unit_change_bar)

        for unit in UnitType:
            self.unit_change_bar.add_command(label=str(unit), command=lambda arg=unit: self.load_units(
                arg), activebackground='#011627', activeforeground='#39FF14')

        self.unit_change_bar.add_separator()

        # exit_menu
        self.unit_change_bar.add_command(label='Exit', command=self.destroy)

        # make some field to entry
        self.field1 = tk.Entry(self)
        self.field2 = tk.Entry(self)
        # combobox
        self.combobox1 = ttk.Combobox(
            self, textvariable=tk.StringVar(self), state='readonly')
        self.combobox2 = ttk.Combobox(
            self, textvariable=tk.StringVar(self), state='readonly')
        # text
        self.equal_text = tk.Label(self, text='=', **font_opt)
        # button
        self.convert_button = tk.Button(
            self, text='Convert', command=self.convert_handler)
        # clear button
        self.clear_button = tk.Button(self, text='Clear', command=self.clear)

        # configuration
        for i in range(6):
            self.columnconfigure(i, weight=1)
        self.config(bg='#011627')

        for field in (self.field1, self.field2):
            # colorize
            field.config(**font_opt)

        # grid a component
        component_list = [self.field1, self.combobox1, self.equal_text,
                          self.field2, self.combobox2, self.convert_button, self.clear_button]

        for index, component in enumerate(component_list):
            component.grid(row=0, column=index, **options)

    def clear(self) -> None:
        """This function clear field and combobox"""
        for field in [self.field1, self.field2]:
            field.delete(0, tk.END)
        for combobox in [self.combobox1, self.combobox2]:
            combobox.set('')

    def load_units(self, unittype: UnitType) -> None:
        """Load units of the requested unittype into the comboboxes."""
        # get the units of the requested type
        units = self.converter.get_units(unittype)
        for combobox in [self.combobox1, self.combobox2]:
            combobox['values'] = units
        self.clear()  # clear all the entry and field

    def convert_handler(self) -> None:
        """An event handler for conversion actions.
        You should call the unit converter to perform actual conversion.
        """
        try:
            # select which unit to display
            first_unit = self.combobox1.get()
            seccod_unit = self.combobox2.get()

            convert = self.converter.convert
            # check whether user choose some choice on combobox
            if first_unit is None or seccod_unit is None:
                return

            # get the value from the input field
            first_amount = self.field1.get()
            second_amount = self.field2.get()

            # check whether field 1 isnt empty
            if first_amount:
                result = convert(float(first_amount), first_unit, seccod_unit)
                self.field2.delete(0, 'end')
                self.field2.insert(0, str(result))
            # check whether field 2 isnt empty
            elif second_amount:
                result = convert(float(second_amount), seccod_unit, first_unit)
                self.field1.delete(0, 'end')
                self.field1.insert(0, str(result))
        except (ValueError, ZeroDivisionError, KeyError):
            # except ValueError when user input is not a number
            # except ZeroDivisionError when user input is 0 and
            # convert method has divided by 0
            # except KeyError when user input is not a unit
            self.clear()

    def is_valid(self, field) -> None:
        """change color of the field if it is valid or not
        if it not valid change into a red else change into a green"""
        other = self.field1 if field == self.field2 else self.field2
        entry = field.get()
        try:
            if entry:
                float(entry)
            field.config(fg='#39FF14')
        except ValueError:
            field.config(fg='red')
            other.delete(0, tk.END)

    def colorize_valid(self) -> None:
        """check all field and change it to all color"""
        for field in [self.field1, self.field2]:
            self.is_valid(field)

    def update(self) -> None:
        """Update the UI to reflect the current state of the unit converter."""
        DELAY = 10
        self.colorize_valid()
        self.after(DELAY, self.update)

    def run(self) -> None:
        """
        this function run all thing
        """
        # start the app, wait for events
        self.update()
        self.mainloop()
