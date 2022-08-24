import xml.etree.ElementTree as ET

class Address:
    '''Representation of information about an address.'''
    def __init__(self, street: str, city: str, postal: str) -> None:
        '''Contructor for an address.'''
        self.street = street
        self.city = city
        self.postal = postal

    def add_to_xmltree(self, parent: ET.SubElement) -> None:
        '''Add an address to a XML tree structure.'''
        address_tag = ET.SubElement(parent, 'address')

        street_tag = ET.SubElement(address_tag, 'street')
        street_tag.text = self.street

        city_tag = ET.SubElement(address_tag, 'city')
        city_tag.text = self.city

        postalnumber_tag = ET.SubElement(address_tag, 'postalnumber')
        postalnumber_tag.text = self.postal
