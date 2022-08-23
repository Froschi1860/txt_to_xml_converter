import xml.etree.ElementTree as ET

class Phone:
    def __init__(self, mobile: str, telephone: str) -> None:
        self.mobile = mobile
        self.telephone = telephone

    def add_to_xmltree(self, xml_parent: ET.SubElement):
        phone_tag = ET.SubElement(xml_parent, 'phone')

        mobile_tag = ET.SubElement(phone_tag, 'mobile')
        mobile_tag.text = self.mobile

        telephone_tag = ET.SubElement(phone_tag, 'telephone')
        telephone_tag.text = self.telephone
