from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0'
DESCRIPTION = 'Get information about a twitch channels and streams'

# Setting up
setup(
    name="twitch-info",
    version=VERSION,
    author="Feytus",
    author_email="feytusinho@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['colorama', 'requests', 'datetime', ''],
    keywords=['python', 'stream', 'twitch'],
    classifiers=[
        'Development Status :: 4 - Beta,'
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
