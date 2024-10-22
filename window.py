"""

Window Class for Gui implementation of Contact-Maker
To be implemented with the tkinter module

Last Updated: October 22, 2024
Authors: Joe Scruppi

"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import scripts as s

class Window:
    def __init__(self):

        #create and initilize the window
        self.root = tk.Tk()
        self.root.geometry('400x300')
        self.root.title('Contact-Maker')

        #initilize the empty fields that store filepath info
        self.input_file_path = ''
        self.output_file_path = 'output.vcf'

        #create the buttons and labels
        self.open_button = tk.Button(self.root, text='Select .csv file', command=self.setInputFilePath)
        self.open_button.pack()
        self.input_file_label = tk.Label(self.root, text='')
        self.input_file_label.pack(pady=30)


        self.gen_button = tk.Button(self.root, text='Generate Contact File')#command=s.genFile(self.output_file_path,  self.input_file_path))
        self.gen_button.pack()
        self.output_file_label = tk.Label(self.root, text=self.output_file_path)
        self.output_file_label.pack()


    def getInputFile(self):
        return self.input_file_path
    
    def getOutputFile(self):
        return self.output_file_path
    
    def setInputFilePath(self):
    
        self.input_file_path = filedialog.askopenfilename()
        if self.input_file_path:
            #display input path on the window screen
            self.input_file_label.config(text=f'{self.input_file_path}')
        else:
            messagebox.showwarning("No file Selected", "You did not choose the CSV file")

    def run(self):
        self.root.mainloop()

