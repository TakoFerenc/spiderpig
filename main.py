from verify_urls import *
from get_urls import *
from database_handler import *
from file_handler import *
from xml_create import *
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('site')
@click.argument('file_name')
def collect_urls_into_file(site, file_name):
    """This script collects urls from SITE and writes them into FILE_NAME."""
    pc = PageContent()
    fl = FileHandler(file_name)
    pc.open_url(site)
    fl.write_to_file(pc.get_urls())
    click.echo('finished')


@cli.command()
@click.argument('site')
@click.argument('db_name')
def collect_urls_into_database(site, db_name):
    """This script collects urls from SITE and writes them into a DATABASE."""
    hd = HandleData(db_name)
    pc = PageContent()
    pc.open_url(site)
    hd.write_data_to_db(pc.get_urls())
    click.echo('finished')


@cli.command()
@click.argument('file_name')
def verify_urls_from_file(file_name):
    """This script verifies urls from a file FILE_NAME outputs the results in a text file."""
    fl = FileHandler(file_name)
    vf = VerifyUrls()
    vf.verify_urls(fl.read_from_file())
    click.echo('finished')


@cli.command()
@click.argument('db_name')
def verify_urls_from_database(db_name):
    """This script verifies urls from a database DB_NAME outputs the results in a text file."""
    hd = HandleData(db_name)
    vf = VerifyUrls()
    vf.verify_urls(hd.read_data_from_db())
    click.echo('finished')


@cli.command()
@click.argument('site')
def verify_urls_from_sitemap(site):
    """This script verifies urls from a sitemap SITE outputs the results in a text file."""
    pc = PageContent()
    vf = VerifyUrls()
    pc.open_url(site)
    vf.verify_urls(pc.get_urls())
    click.echo('finished')


@cli.command()
@click.argument('file_name')
@click.argument('new_file_name')
def create_sitemap_from_file(file_name, new_file_name):
    """This script creates a sitemap form urls from a file FILE_NAME creates xml with NEW_FILE_NAME."""
    fl = FileHandler(file_name)
    xl = CreateXML()
    xl.create_xml(fl.read_from_file(), new_file_name)
    click.echo('finished')


@cli.command()
@click.argument('db_name')
@click.argument('new_file_name')
def create_sitemap_from_database(db_name, new_file_name):
    """This script creates a sitemap form urls from a database DB_NAME creates xml with NEW_FILE_NAME."""
    hd = HandleData(db_name)
    xl = CreateXML()
    xl.create_xml(hd.read_data_from_db(), new_file_name)
    click.echo('finished')


if __name__ == '__main__':

    my_url = 'https://pythonprogramming.net/sitemap.xml'
    my_file_name = 'urls.txt'
    my_db_name = 'database.db'
    my_xml = 'example.xml'
    # collect_urls_into_file(my_url, my_file_name)
    # collect_urls_into_database(my_url, my_db_name)
    # verify_urls_from_file(my_file_name)
    # verify_urls_from_database(my_db_name)
    # verify_urls_from_sitemap(my_url)
    # create_sitemap_from_file(my_file_name, my_xml)
    # create_sitemap_from_database(my_db_name, my_xml)