import os
from setuptools import find_packages
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='edc-sync-file-monitor',
    packages=find_packages(),
    include_package_data=True,
    url='http://github.com/botswana-harvard/edc-sync-file-monitor',
    license='GPL license, see LICENSE',
    description='Monitor clients that sync data, collected offline,  with a node by file',
    long_description=README,
    zip_safe=False,
    keywords='edc sync file monitor',
    install_requires=['paramiko'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
