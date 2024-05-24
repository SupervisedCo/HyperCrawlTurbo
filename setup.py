from setuptools import setup, find_packages

setup(
    name='hypercrawlturbo',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'hypercrawlturbo=hypercrawlturbo.scraper:main'
        ]
    },
    author='Udit AKhouri',
    description='A turbocharged web scraper for extracting URLs from a webpage. This is the lite version of HyperCrawl',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/uditakhourii/hypercrawlturbo',
)
