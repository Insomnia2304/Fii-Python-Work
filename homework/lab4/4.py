def build_xml_element(tag, content, **kwargs):
    attr = ' '.join([f'{key}="{value}"' for key, value in kwargs.items()])
    if attr: attr = ' ' + attr
    return f'<{tag}{attr}> {content} </{tag}>'

print(build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))
