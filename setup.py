from setuptools import setup, find_packages

setup(
    name='spiderpig',
    version='1.0',
    description='URL capturing, verifying and creating sitemap xml',
    classifiers=[
        'Development Status :: Beta',
        'License :: Open source',
        'Programing language :: Python :: 3.6',
        'Topic :: Url parsing :: Url verifying :: Sitemap creating'
    ],
    keywords='url parsing sitemap verify',
    author='Tako Ferenc',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click', 'lxml', 'beautifulsoup4'
    ],
    entry_points='''
        [console_scripts]
        spiderpig=main:cli
    ''',
)