import tkinter as tk
from tkinter import ttk
from unittype import UnitType
from converter import UnitConverter


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
        PADX = 5
        PADY = 5
        # configuration
        for i in range(6):
            self.columnconfigure(i, weight=1)

        # make some field to entry
        self.field1 = tk.Entry(self)
        self.field2 = tk.Entry(self)
        self.field1.grid(row=0, column=0, padx=PADX, pady=PADY, sticky='ew')
        self.field2.grid(row=0, column=3, padx=PADX, pady=PADY, sticky='ew')
        # text
        self.equal_text = tk.Label(self, text='=')
        self.equal_text.grid(row=0, column=2, padx=PADX,
                             pady=PADY, sticky='ew')
        # combobox
        self.combobox1 = ttk.Combobox(self, textvariable=tk.StringVar(self))
        self.combobox2 = ttk.Combobox(self, textvariable=tk.StringVar(self))
        self.combobox1.grid(row=0, column=1, padx=PADX, pady=PADY, sticky='ew')
        self.combobox2.grid(row=0, column=4, padx=PADX, pady=PADY, sticky='ew')

        # button
        self.convert_button = tk.Button(
            self, text='Convert', command=self.convert_handler)
        self.convert_button.grid(
            row=0, column=5, padx=PADX, pady=PADY, sticky='ew')

        self.clear_button = tk.Button(self, text='Clear', command=self.clear)
        self.clear_button.grid(row=0, column=6, padx=PADX, pady=PADY)

        # load unit
        self.load_units(UnitType.LENGTH)

    def clear(self) -> None:
        """This function clear field and combobox"""
        for field in [self.field1, self.field2]:
            field.delete(0, 'end')
        for combobox in [self.combobox1, self.combobox2]:
            combobox.set('')

    def load_units(self, unittype: UnitType) -> None:
        """Load units of the requested unittype into the comboboxes."""
        # get the units of the requested type
        units = self.converter.get_units(unittype)
        for combobox in [self.combobox1, self.combobox2]:
            combobox['values'] = units
            combobox['state'] = 'readonly'

    def convert_handler(self) -> None:
        """An event handler for conversion actions.
        You should call the unit converter to perform actual conversion.
        """
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

        try:
            # check whether field 1 isnt empty
            if first_amount:
                result = convert(float(first_amount),
                                 first_unit, seccod_unit)
                self.field2.delete(0, 'end')
                self.field2.insert(0, str(result))
            # check whether field 2 isnt empty
            elif second_amount:
                result = convert(float(second_amount),
                                 seccod_unit, first_unit)
                self.field1.delete(0, 'end')
                self.field1.insert(0, str(result))
            else:
                return
        except (ValueError, ZeroDivisionError, KeyError):
            # except ValueError when user input is not a number
            # except ZeroDivisionError when user input is 0 and
            # convert method has divided by 0
            # except KeyError when user input is not a unit
            self.clear()

    def run(self) -> None:
        """This method run an entire thing"""
        # start the app, wait for events
        self.mainloop()
