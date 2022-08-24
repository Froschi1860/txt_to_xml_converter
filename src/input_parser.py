from address import Address
from family import Family
from person import Person
from phone import Phone

def parse_input_to_persons(lines_in_input: list) -> list:
    '''Convert a list of strings with information into corresponding Person objects.'''
    person = None
    new_person = True
    list_of_people = []
    family_members = []

    for idx in range(len(lines_in_input)):
        if '|' not in lines_in_input[idx]:
            report_input_format_error(idx + 1)
        line = lines_in_input[idx].strip().split('|')

        # Line represents a new person
        if line[0] == 'P':
            if len(line) != 3:
                report_input_format_error(idx + 1)
            if person != None:
                person.add_family(family_members)
                list_of_people.append(person)
            person = Person(line[1], line[2])
            new_person = True
            family_members.clear()

        # Line represents phone numbers of person or family member
        elif line[0] == 'T':
            if len(line) != 3:
                report_input_format_error(idx + 1)
            if new_person:
                person.set_phone(Phone(line[1], line[2]))
                continue
            family_members[-1].set_phone(Phone(line[1], line[2]))

        # Line represents an address of person or family member
        elif line[0] == 'A':
            if len(line) != 4:
                report_input_format_error(idx + 1)
            if new_person:
                person.set_address(Address(line[1], line[2], line[3]))
                continue
            family_members[-1].set_address(Address(line[1], line[2], line[3]))

        # Line represents a family member
        elif line[0] == 'F':
            if len(line) != 3:
                report_input_format_error(idx + 1)
            family_members.append(Family(line[1], line[2]))
            # Indicate that next lines refer to family member
            new_person = False

        else:
            report_input_format_error(idx + 1)

    person.add_family(family_members)
    list_of_people.append(person)

    return list_of_people

def report_input_format_error(line: int) -> None:
    '''Inform user about erroneus format in input and terminate.'''
    print(f'An error occured when reading the file.\nPlease check entry format in line {line}.')
    exit()

def load_infile(filepath: str) -> list:
    '''Open a file for processing. Errors terminate the app.'''
    try:
        with(open(filepath, 'r', encoding='utf-8')) as infile:
            return infile.readlines()
    except IOError:
        print('An error occured when reading the file. Please check provided filepath.')
        exit()
