import xml.etree.ElementTree as ET

tree = ET.parse('xml_example.xml')
root = tree.getroot()
print('Root Tag', root.tag)
print('Attribute', root.attrib)
for child in root:
    print('Field:', child.tag)