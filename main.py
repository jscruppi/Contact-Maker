"""

Script to make the contact .vcf file


Last Updated: October 21, 2024

"""

import csv
import sys

def addContact(f, c):
    #write the header
    f.write('BEGIN:VCARD\n')
    f.write('VERSION:3.0\n')
    print(f"N:{c[2]};{c[1]};;;", file=f)
    print(f"TEL:{c[4]}", file=f)
    print(f"BDAY:{c[3]}", file=f)
    if c[5] != "":
        print(f"PHOTO;VALUE=URL:{c[5]}",file=f)
    f.write('END:VCARD\n')
    f.write('\n')
    
    
    

def main():
    print('in main')
    
    #create vcf file
    out_file = open('output.vcf', mode='w')

    #read through the input file
    with open(sys.argv[1], mode='r') as input_file:
        reader = csv.DictReader(input_file, delimiter=',')
        
        for row in reader:
            #split each current contact
            #contact = row.split(',')
            contact = list(row.values())
            #print(contact, type(contact))
            addContact(out_file, contact)




#when script is run
if __name__ == '__main__':
    main()


