# Contact-Maker

A program designed to take the input of a google form and convert the responses into a downloadable contact.vcf file that can easily be imported to a contact application

## Instalation

1. Before trying to download this program, a few prerequisites are required:
- python          (any version newer than 3.0 should suffice)
- git             (any version)
- tkinter         (any version)

   To check for these porgrams, type the following commands into your terminal:

            python3 --version
            git --version
            pip list
   If you have these installed on your computer, a message should be displayed with your version information. For tkinter, your version should appear in the "pip list" output

2. Clone the Repository with the following terminal command:
    
            mkdir contact-maker
            cd contact-maker
            git clone git@github.com/jscruppi/Contack-Maker.git

   Congratulations, you've just installed Contact-Maker!!

## Usage

Contact-Maker was designed with the use of a google form in mind. Chapter members who have access to an already created google form would enter the following information:

- First Name
- Last Name
- Birthday (YYYY-MM-DD)
- Phone Number (###-###-####)
- Link to a photo (_optional_)

In this current version of Contact-Maker, any phone numbers or birthdays not entered in the proper format can be handeled. Any Birthdays or phone numbers not entered in the correct format will be omitted from the output _ENTIRELY_. The order of the questions MUST match the order listed above, or the program could fail.

That being said, Contact-Maker requires this information to be stored in a .csv file. This can be done by downloading the google sheet linked to the google form as a .csv file.
Note that the first kept record in a google form is the response time, Contact-Maker accounts for this in the code, so any attempts to remove the response time column will brick the program.

To run Contact-Maker, you can either launch via the graphical interface or the command line interface. This is done based on the arguments provided at launch.

Launching the command line tool:

        python3 main.py input.csv

Launching the GUI:

        python3 main.py

Contact-Maker will write the results of the program to a .vcf file named "output.vcf" if you launched the command line tool, otherwise it will use the name you selected in the GUI.

## Contributing

For any ATOs who wish to contribute to this code in the future, I don't mind at all! Just make a branch with your new features , push them to the repo, and submit a pull request!