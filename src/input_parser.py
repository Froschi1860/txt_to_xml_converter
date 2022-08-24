import sys
from address import Address
from family import Family

from person import Person
from phone import Phone

def parse_input(file_as_list: list):
    person = None
    person_or_family = 'p'
    list_of_people = []
    family_list = []

    for i in file_as_list:
        if '|' not in i:
            report_input_format_error(i + 1)

        line_as_list = i.split('|')

        if line_as_list[0] == 'P':
            if len(line_as_list) != 3:
                report_input_format_error(i + 1)

            if person != None:
                person.add_family(family_list)
                list_of_people.append(person)

            person = Person(line_as_list[1], line_as_list[2])
            person_or_family = 'p'
            family_list.clear()
        elif line_as_list[0] == 'T':
            if len(line_as_list) != 3:
                report_input_format_error(i + 1)
            
            if person_or_family == 'p':
                person.set_phone(Phone(line_as_list[1], line_as_list[2]))
            elif person_or_family == 'f':
                family_list[-1].set_phone(Phone(line_as_list[1], line_as_list[2]))

        elif line_as_list[0] == 'A':
            if len(line_as_list) != 4:
                report_input_format_error(i + 1)
            
            if person_or_family == 'p':
                person.set_address(Address(line_as_list[1], line_as_list[2], line_as_list[3]))
            elif person_or_family == 'f':
                family_list[-1].set_address(Address(line_as_list[1], line_as_list[2], line_as_list[3]))
    
        elif line_as_list[0] == 'F':
            if len(line_as_list) != 3:
                report_input_format_error(i + 1)

            family_list.append(Family(line_as_list[1], line_as_list[2]))
            person_or_family = 'f'
        else:
            report_input_format_error(i + 1)

    person.add_family(family_list)
    list_of_people.append(person)

    return list_of_people


def report_input_format_error(line: int):
    print(f'An error occured when reading the file.\nPlease check entry format in line {line}.')
    exit()

def load_infile():
    filepath = sys.argv[1]
    try:
        with(open(filepath), 'r') as infile:
            return infile.readlines()
    except IOError:
        print('An error occured when reading the file. Please check provided filepath.')
        exit()
