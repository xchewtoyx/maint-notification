from setuptools import setup, find_packages
setup(
    name = "xmaintnote",
    version = "0.0.1_rc1",
    packages = find_packages(),
    install_requires=[
        'icalendar>=3.0',
        'simplejson>=2.1.0',
    ],
)
