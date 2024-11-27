"""

Main file for contact-maker
Launches the program 

Authors: Joe Scruppi

"""

from src import window

def main():

    #create the window
    w = window.Window()

    #run the mainloop
    w.run()

#when script is run
if __name__ == '__main__':
    main()

