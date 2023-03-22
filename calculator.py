
from ast import operator
import tkinter as tk
from tkinter.font import BOLD

OPERATOR_FONT_STYLE=('Arial','20')
DIGITS_FONT_STYLE=('Arial',24,BOLD)
LARGE_FONT=('Arial',40)
SMALL_FONT=('Arial',16)

LIGHT_BLUE='#CCEDFF'
OFF_WHITE='#F8FAFF'
GRAY='#F5F5F5'
LABEL_COLOR='#25265E'
WHITE='#FFFFFF'
class Calculator:

    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry('375x667')
        self.window.resizable(0,0)
        self.window.title('calculator')
        self.total_expression=""
        self.current_expression=""
        self.digits={
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            '.':(4,1),0:(4,2)
        }
        self.operators={'/':'\u00F7','*':'\u00D7','-':'-','+':'+'}
     
        self.display_frame = self.create_display_frame()
        self.total_label ,self.label=self.create_display_labels()
        self.button_frame=self.create_button_frame()
        
        self.button_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.button_frame.rowconfigure(x,weight=1)
            self.button_frame.columnconfigure(x,weight=1)

        self.create_digit_buttons()
        self.create_operator_button()
        self.special_buttons()
        self.bind_keys()

    def special_buttons(self):
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_square_root_button()

    def bind_keys(self):
        self.window.bind("<Return>",lambda event:self.evaluate())
        for key in self.digits:
            self.window.bind(str(key),lambda event,value=key:self.add_to_expression(value))
        for key in self.operators:
            self.window.bind(key,lambda event ,operator=key:self.append_operator(operator))

    def add_to_expression(self,value):
        self.current_expression+=str(value)
        self.update_label()

    def append_operator(self,operator):
        self.current_expression+=operator
        self.total_expression+=self.current_expression
        self.current_expression=''
        self.update_total_label()
        self.update_label()

    def clear(self):
        self.current_expression=''
        self.total_expression=''
        self.update_total_label()
        self.update_label()

    def create_display_labels(self):
        total_label=tk.Label(self.display_frame,text=self.total_expression,anchor=tk.E,bg=GRAY,fg=LABEL_COLOR,padx=24,font=SMALL_FONT)
        total_label.pack(expand=True,fill="both")

        label=tk.Label(self.display_frame,text=self.current_expression,anchor=tk.E,bg=GRAY,fg=LABEL_COLOR,padx=24,font=LARGE_FONT)
        label.pack(expand=True,fill="both")
        
        return total_label,label
    
    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            buton=tk.Button(self.button_frame,text=str(digit),bg=WHITE,fg=LABEL_COLOR,font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda x=digit:self.add_to_expression(x))
            buton.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression+=self.current_expression
        self.update_total_label()
        try:
         self.current_expression=str(eval(self.total_expression))
         self.total_expression=''

        except Exception as e:
         self.current_expression='Error'
        
        finally:
         self.update_label()

    def create_operator_button(self):
        i=0
        for operator,symbol in self.operators.items():
            btn=tk.Button(self.button_frame,text=symbol,bg=OFF_WHITE,font=OPERATOR_FONT_STYLE,fg=LABEL_COLOR,borderwidth=0,command=lambda x=operator:self.append_operator(x))
            btn.grid(row=i,column=4,sticky=tk.NSEW)
     
            i+=1

    def square(self):
        self.current_expression=str(eval(f'{self.current_expression}**2'))
        self.update_label()


    def create_square_button(self):
        btn=tk.Button(self.button_frame,text='x\u00b2',bg=OFF_WHITE,font=OPERATOR_FONT_STYLE,fg=LABEL_COLOR,borderwidth=0,command=self.square)
        btn.grid(row=0,column=2,sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression=str(eval(f'{self.current_expression}**0.5'))
        self.update_label()

    def create_square_root_button(self):
        btn=tk.Button(self.button_frame,text='\u221ax',bg=OFF_WHITE,font=OPERATOR_FONT_STYLE,fg=LABEL_COLOR,borderwidth=0,command=self.sqrt)
        btn.grid(row=0,column=3,sticky=tk.NSEW)

    def create_clear_button(self):
        btn=tk.Button(self.button_frame,text='c',bg=OFF_WHITE,font=OPERATOR_FONT_STYLE,fg=LABEL_COLOR,borderwidth=0,command=self.clear)
        btn.grid(row=0,column=1,sticky=tk.NSEW)

    def create_equal_button(self):
         btn=tk.Button(self.button_frame,text='=',bg=LIGHT_BLUE,font=OPERATOR_FONT_STYLE,fg=LABEL_COLOR,borderwidth=0,command=self.evaluate)
         btn.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)

    def create_display_frame(self):

        frame=tk.Frame(self.window,height=221,bg=GRAY)
        frame.pack(expand=True,fill="both")
        return frame
   
    def create_button_frame(self):
        frame =tk.Frame(self.window)
        frame.pack(expand=True,fill='both')
        return frame

    def update_total_label(self):
        expression=self.total_expression
        for operator,symbol in self.operators.items():
            expression=expression.replace(operator,f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:10])
 
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    calculator=Calculator()
    calculator.run()