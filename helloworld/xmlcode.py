import xml.etree.ElementTree as ET
 
#XML code embedded in a string format
data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Attribute for tag email:', tree.find('email').get('hide’))
print('Attribute for tag phone:', tree.find('phone').get('type'))