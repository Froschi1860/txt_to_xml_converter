import xml.etree.ElementTree as ET

class Phone:
    '''Representation of information about phone numbers.'''
    def __init__(self, mobile: str, telephone: str) -> None:
        '''Constructor for Phone class.'''
        self.mobile = mobile
        self.telephone = telephone

    def add_to_xmltree(self, parent: ET.SubElement) -> None:
        '''Add phone information to a XML tree structure.'''
        phone_tag = ET.SubElement(parent, 'phone')

        mobile_tag = ET.SubElement(phone_tag, 'mobile')
        mobile_tag.text = self.mobile

        telephone_tag = ET.SubElement(phone_tag, 'telephone')
        telephone_tag.text = self.telephone
