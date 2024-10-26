"""

Scripts for the Contact-Maker Application
IE - The methods that make the Contact-Maker work but don't necessarily belong to the Window / Main files

Last Updated: Oct 22, 2024
Authors: Joe Scruppi

"""

import csv
import re

def isFormatted(c):
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    number_pattern = r'\d{3}-\d{3}-\d{4}'

    #check to make sure both birthday and number match required pattern
    if re.fullmatch(date_pattern, c[3]) and re.fullmatch(number_pattern, c[4]):
        return True
    else:
        print(f"{c[2]}, {c[1]}'s information is unformattted. Will be excluded")
        return False


def addContact(f, c):
    #write the header
    f.write('BEGIN:VCARD\n')
    f.write('VERSION:3.0\n')

    #write the contact contents
    print(f"N:{c[2]};{c[1]};;;", file=f)
    print(f"TEL:{c[4]}", file=f)
    print(f"BDAY:{c[3]}", file=f)
    if c[5] != "":
        print(f"PHOTO;VALUE=URL:{c[5]}",file=f)

    #write the footer
    f.write('END:VCARD\n')
    f.write('\n')

def genFile(vcf_file, csv_file):
    #create vcf file
    out_file = open(vcf_file, mode='w')

    #read through the input csv file
    with open(csv_file, mode='r') as input_file:
        reader = csv.DictReader(input_file, delimiter=',')

        for row in reader:
            #split each current contact row into their attributes
            contact = list(row.values())

            #check for formatting issues
            if isFormatted(contact):
                #write the data to the file
                addContact(out_file, contact)



