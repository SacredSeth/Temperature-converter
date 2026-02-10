from tkinter import *


class Converter:
    """
    temperature converter
    """
    def __init__(self):

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_help_button = Button(self.temp_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial", "14", "bold"), width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, padx=5, pady=5)


    def to_help(self):
        DisplayHelp()


class DisplayHelp:

    def __init__(self):

        # setup dialogue box
        self.help_box = Toplevel()

        bg_colour = "#FFE6CC"
        self.help_frame = Frame(self.help_box, width=300, height=200, bg=bg_colour)
        self.help_frame.grid()

        self.help_heading = Label(self.help_frame,
                                  text="Help / Information",
                                  font=("Arial", "14", "bold"),
                                  bg=bg_colour)
        self.help_heading.grid(row=0)

        help_instructions = ("To use the program, simply enter the temperature "
                             "you wish to convert and then choose to convert to "
                             "either degrees Celsius (centigrade) or Fahrenheit."
                             "\n\n"
                             "Note that -273 degrees C (-459 F) is absolute zero "
                             "(the coldest possible temperature). If you try to "
                             "convert a temperature that is less than -273 degrees "
                             "C, you will get an error message. \n\n"
                             "To see your "
                             "calculation history and export it to a text file, please "
                             "click the 'History / Export' button.")
        self.help_text = Label(self.help_frame,
                               text=help_instructions,
                               wraplength=350,
                               justify="left",
                               bg=bg_colour)
        self.help_text.grid(row=1, padx=10)

        self.close_button = Button(self.help_frame, text="Close",
                                   bg="#CC6600", fg="#FFFFFF",
                                   font=("Arial", "12", "bold"),
                                   command=self.close_help)
        self.close_button.grid(row=2, padx=10, pady=10)



    def close_help(self):
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()