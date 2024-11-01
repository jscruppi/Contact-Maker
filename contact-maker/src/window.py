"""

Window Class for Gui implementation of Contact-Maker
To be implemented with the tkinter module

Last Updated: October 22, 2024
Authors: Joe Scruppi

"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from .contact_process import *
import sys
import os

class Window:
    def __init__(self):

        #create and initilize the window
        self.root = tk.Tk()
        self.root.geometry('400x300')
        self.root.title('Contact-Maker')

        #initilize the empty fields that store filepath info
        self.input_file_path = ''
        self.output_file_path = ''

        #output file generation flag
        self.is_file_generated = False

        #create the buttons and labels
        self.open_button = tk.Button(self.root, text='Select .csv file', command=self.setInputFilePath)
        self.open_button.pack()
        self.input_file_label = tk.Label(self.root, text='')
        self.input_file_label.pack(pady=30)

        self.gen_button = tk.Button(self.root, text='Generate Contact File')#command=s.genFile(self.output_file_path,  self.input_file_path))
        self.gen_button.pack()

        #set the icon image
        icon_image = sys.path[0] + '/data/laptop.png'
        self.root.iconphoto(False, tk.PhotoImage(file=icon_image))


    def getInputFile(self):
        return self.input_file_path
    
    def getOutputFile(self):
        
        #prompt user to create the output filepath
        entry = tk.filedialog.asksaveasfilename(defaultextension='.vcf',
                                                title='Save As')
        self.output_file_path = entry

        return self.output_file_path 

    def setInputFilePath(self):
    
        self.input_file_path = filedialog.askopenfilename()
        if self.input_file_path:
            #display input path on the window screen
            self.input_file_label.config(text=self.shorten_path(self.input_file_path))

            #enable genFile button to function now that we have the loaded path
            #the lambda call makes it so command will only activate once the button is clicked
            self.gen_button.config(command= lambda: self.createOutput())
        else:
            messagebox.showwarning("No file Selected", "You did not choose the CSV file")

    #called whenever genFile is preshed
    #will genFile() and output a messagebox of the omitted names
    def createOutput(self):
        
        genFile(self.getOutputFile(), self.input_file_path)

       #see if any names were ommitted
        if(self.output_file_path):
            with open(sys.path[0] + '/data/omit_names.txt', mode='r') as omit_log:
                content = omit_log.readlines()

                if(len(content) != 0):
                    self.showOmitLog(content)

                omit_log.close()


        self.is_file_generated = True

    def showOmitLog(self, omit_log):
        #omit log comes in as a list of strings
        #need to change to all one string
        output = ''
        for x in range(len(omit_log)):
            output += omit_log[x]

        tk.messagebox.showinfo('Omitted Names', output)
    
    def shorten_path(self, path, num_parts=2):
        parts = path.split(os.sep)
        shortened = os.sep.join(parts[-num_parts:])
        return shortened

    def run(self):
        self.root.mainloop()

