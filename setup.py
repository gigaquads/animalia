#!/usr/bin/env python3
# encoding=utf-8
from setuptools import setup
if __name__ == '__main__':
    setup(
    #package_dir={'animalia': 'animalia'},

    # this works if species.txt is at ./animalia/species.txt
    #package_data={'animalia': ['species.txt']},

    # blah
        include_package_data=True,
    #packages=['find:', 'animalia'],
    #package_dir={'': 'animalia'},
    #package_data={'animalia': ['data/species.txt']},

    #this gets installed in /usr/share/animalia/species.txt
    # animalia-0.0.12.data/data/share/animalia/species.txt
    #    data_files=[('share/animalia', ['data/species.txt'])],
    )
