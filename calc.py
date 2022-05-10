import tkinter as tk


LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"


DEFAULT_FONT_STYLE = ("Arial", 20)
OFF_WHITE = "#F8FAFF"

WHITE = "#FFFFFF"
DIGIT_FONT_STYLE = ("Arial", 24, "bold")


LIGHT_BLUE = '#CCEDFF'

class Calculator:

#   --- Defining the constructor ---

    def __init__(self):

#   --- Creating the main window (container) ---

        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")


#   --- For Displaying the input expression ---

        #storing expression as a String
        self.total_expression=""
        self.current_expression=""

        #display frame
        self.display_frame = self.create_display_frame()

        # For total_expression(total_label) and current_expression(label)
        self.total_label, self.label = self.create_display_labels()

        # Creating a dictionary digit(key): (row,column)(value)
        self.digits= {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2,3),
            3: (3, 1), 2: (3, 2), 1: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        #operation dict
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}



        #button
        self.buttons_frame = self.create_buttons_frame()


        # For Expanding the rows and columns
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)


        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_spacial_buttons()
        self.bind_keys() # Taking keyboard input

    # '''For Taking Input from Key Board'''

    '''
    Note: When we bind keyboard buttons with the
    tkinter window, whenever we press special
    characters we will only get space while in the
    case of alphabets and numerical we will
    get actual values (in the string).
    '''
    # bind(string, method)
    def bind_keys(self):
        #binding the Enter Key
        self.window.bind("<Return>", lambda event: self.evaluate())

        for key in self.digits:
            self.window.bind(str(key), lambda event, digit= key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, oparetor= key: self.add_to_expression(oparetor))




    def create_spacial_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_square_root_button()

    #Creating the Display Label
    #total_label and label
    def create_display_labels(self):
        #Label is a widget that is used to implement display boxes where you can place text or images.
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                                   fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
            # anchor=tk.E this line will help to position the text in east side of the label

        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame,
                         text=self.current_expression,
                         anchor=tk.E,
                         bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24,
                         font=LARGE_FONT_STYLE)
            # anchor=tk.E this line will help to position the text in east side of the label

        # The Pack geometry manager packs widgets relative to the earlier widget.
        label.pack(expand=True, fill='both')

        return total_label, label



    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)

            # This will allow our frame to expand and autofill
        frame.pack(expand=True, fill="both")
        return frame


    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()




    #w = Button ( master, option=value, ... )
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),
                               bg=WHITE, fg=LABEL_COLOR,
                               font=DIGIT_FONT_STYLE,
                               borderwidth = 0,
                               command= lambda x= digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)




    def append_operator(self,operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()



    def create_operator_buttons(self):
        i=0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame,
                               text=symbol,
                               bg=OFF_WHITE, fg=LABEL_COLOR,
                               font=DEFAULT_FONT_STYLE,
                               borderwidth = 0,
                               command = lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1


    def square(self):
        self.current_expression=str(eval(f"{self.current_expression}**2"))
        self.update_label()



    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2",
                           bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0,
                           command=lambda: self.square())
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def square_root(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_square_root_button(self):
        button = tk.Button(self.buttons_frame, text="x\u221a",
                           bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0,
                           command=lambda: self.square_root())
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def clear(self):
        self.current_expression=""
        self.total_expression=""
        self.update_label()
        self.update_total_label()


    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C",
                           bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0,
                           command=lambda: self.clear())
        button.grid(row=0, column=1, sticky=tk.NSEW)



    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()

        #Exception handling ZeroDivisionError / NoInputError

        try:
            self.current_expression=str(eval(self.total_expression))
            self.total_expression = ""

        except Exception as e:
            self.current_expression="Error"

        finally:
            self.update_label()




    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=",
                           bg=LIGHT_BLUE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0,
                           command=lambda: self.evaluate())
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)


    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame


    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f" {symbol} ")

        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])
                                        #To Stop Overflowing

    def run(self):
        self.window.mainloop()
    ''' mainloop() is an infinite loop used to 
    run the application, wait for an event to 
    occur and process the event as long as the
     window is not closed.'''




if __name__ == "__main__":
    calc = Calculator()
    calc.run()


'''    

activebackground: to set the background color when button is under the cursor.
activeforeground: to set the foreground color when button is under the cursor.
bg: to set he normal background color.
command: to call a function.
font: to set the font on the button label.
image: to set the image on the button.
width: to set the width of the button.
height: to set the height of the button.

'''


