import urllib.request as request
from bs4 import BeautifulSoup as soup

my_url = 'https://pythonprogramming.net/sitemap.xml'
test_site = 'http://www.yourhtmlsource.com/'


class PageContent:

    page_content = None

    def __init__(self):
        pass

    def open_url(self, url):
        self.url = url
        try:
            page_open = request.urlopen(self.url)
            self.page_content = page_open.read()
        except request.HTTPError as error:
            print(error, f'{url} failed', sep='\n')
        except request.URLError as error:
            print(error, f'{url} failed', sep='\n')
        except Exception as error:
            print(f'UNKNOWN ERROR: {error}', f'{url} failed', sep='\n')
        else:
            page_open.close()

    def get_urls(self):
        content = soup(self.page_content, 'xml')
        for link in content.findAll('loc'):
            yield link.text

    def get_urls_site(self):
        content = soup(self.page_content, 'xml')
        for link in content.findAll('a'):
            try:
                if link.get('href').startswith('/', 0, 1):
                    yield link.get('href')
            except AttributeError:
                continue


# url_list = ['http://www.yourhtmlsource.com/']
# pc = PageContent()
# for url in url_list:
#     pc.open_url(url)
#     for item in pc.get_urls_site():
#         sub_site = item.replace('/', '', 1)
#         new_url = str(url_list[0]) + str(sub_site)
#         url_list.append(new_url)
# print(len(url_list))