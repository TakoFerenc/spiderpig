from lxml import etree
from lxml import objectify
import datetime


class CreateXML:

    def __init__(self):
        xml = '''
            <urlset>
            </urlset>
            '''
        self.root = objectify.fromstring(xml)
        self.root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    @staticmethod
    def create_tree(data):
        url = objectify.Element('url')
        url.loc = data['loc']
        url.lastmod = data['lastmod']
        return url

    def create_xml_obj(self, data_url):
        date = datetime.date.today()
        url = self.create_tree({'loc': data_url,
                                'lastmod': date
                                })
        self.root.append(url)
        objectify.deannotate(self.root)
        etree.cleanup_namespaces(self.root)

    def create_xml_file(self, filename):
        obj_xml = etree.tostring(self.root, encoding='utf-8', pretty_print=True, xml_declaration=True, )
        try:
            with open(filename, "ab") as xml_writer:
                xml_writer.write(obj_xml)
        except IOError as error:
            print(error)

    def create_xml(self, all_urls, file_name):
        for url in all_urls:
            self.create_xml_obj(url)
        self.create_xml_file(file_name)

# all_urls = ['http://www.hearthpwn.com/', 'https://stackoverflow.com/derp', 'https://stackoverflow.com/']
#
# if __name__ == "__main__":
#     xml_o = CreateXML()
#     for item in all_urls:
#         xml_o.create_xml_obj(item)
#     xml_o.create_xml_file('example.xml')