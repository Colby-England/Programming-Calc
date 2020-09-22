from tkinter import *
from conversions import bin_to_dec, dec_to_bin, hex_to_dec, dec_to_hex, bin_to_hex, hex_to_bin


class App:
    """Class to hold gui elements for programming calc app."""

    def __init__(self, master):
        """Initializes an instance of App with all of the relevant gui widgets"""

        frame = Frame(master)
        frame.pack()

        # Building option menu for selecting what type of conversion will be performed, option menu strings are mapped
        # to their corresponding functions from conversions.py
        self.options = {"Bin to Dec": bin_to_dec, "Dec to Bin": dec_to_bin, "Hex to Dec": hex_to_dec,
                        "Dec to Hex": dec_to_hex, "Bin to Hex": bin_to_hex, "Hex to Bin": hex_to_bin}
        self.start_conversion = StringVar(frame)
        self.start_conversion.set("Bin to Dec")  # Initial value for conversion type
        self.option = OptionMenu(frame, self.start_conversion, *self.options.keys())
        self.option.grid(row=0)

        # Building entry box for the initial unconverted value
        self.initial_value_text = Entry(frame)
        self.initial_value_text.grid(row=1, columnspan=2, sticky=W+E+N+S)

        # Building entry box for the converted value and set initial value to empty string
        self.converted_value_text = StringVar("")
        self.converted_value = Entry(frame, textvariable=self.converted_value_text)
        self.converted_value.grid(row=2, columnspan=2, sticky=W + E + N + S)

        # Building button that will call convert_value
        self.button = Button(frame, text="Convert", command=self.convert_value)
        self.button.grid(row=0, column=1)

    def convert_value(self):
        """Calls the appropriate function from conversions.py and updates the converted value entry box"""

        # Get the conversion type and initial value from the GUI elements
        conversion_type = self.start_conversion.get()
        initial_value = self.initial_value_text.get()

        # Retrieve function from self.options based on conversion type selected, then call the selected function
        conversion_function = self.options[conversion_type]
        conversion = conversion_function(initial_value)

        # Set converted value entry box to the calculated converted value
        self.converted_value_text.set(str(conversion))


def main():
    root = Tk()
    root.geometry("160x75")
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
