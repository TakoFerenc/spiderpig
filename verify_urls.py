import urllib.request as request
from file_handler import FileHandler
from multiprocessing import Pool


class VerifyUrls:

    def __init__(self):
        self.fl = FileHandler()
        self.fl.create_file_temp()

    def verify_each_url(self, url):
        try:
            opened_url = request.urlopen(url)
        except request.HTTPError as error:
            print(error, f'{url} failed', sep='\n')
            self.fl.write_to_file((error, f'{url} failed'))
        except request.URLError as error:
            print(error, f'{url} failed', sep='\n')
            self.fl.write_to_file((error, f'{url} failed'))
        except Exception as error:
            print(f'UNKNOWN ERROR: {error}', f'{url} failed', sep='\n')
            self.fl.write_to_file((error, f'{url} failed'))
        else:
            opened_url.close()
            print(f'{url} worked fine')
        finally:
            print('check complete')

    def verify_urls(self, list_urls):
        p = Pool(processes=10)
        p.map(self.verify_each_url, list_urls, chunksize=20)
        p.close()
        p.join()
        self.fl.rename_file()

# urls = ['http://www.hearthpwn.com/', 'https://stackoverflow.com/derp', 'https://stackoverflow.com/', 'http://www.hearthpwn.com/derp', 'http://www.imdb.com/']
#
# if __name__ == '__main__':
#
#     vf = VerifyUrls()
#     vf.verify_urls(urls)