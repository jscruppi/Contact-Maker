"""

Main file for contact-maker
Launches the program 

Authors: Joe Scruppi

"""

from src import window, contact_process
import sys

def main() -> None:

    if len(sys.argv) == 1:
        #create the window
        w = window.Window()

        #run the mainloop
        w.run()
    else:
        contact_process.genFile(sys.argv[1], 'output.vcf')

        with open('data/omit_names.txt', mode='r') as err_log:
            print('Names not included in the file:')
            lines = err_log.readlines()
            for line in lines:
                print(f'\t{line}')

        err_log.close()


#when script is run
if __name__ == '__main__':
    main()

