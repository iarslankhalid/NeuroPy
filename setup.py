from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'Neural Networks made from scratch'
LONG_DESCRIPTION = 'A package that can be used to make a neural network.'

# Setting up
setup(
    name="NeuroPy",
    version=VERSION,
    author="Arslan Khalid",
    author_email="iarslankhalid@yahoo.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(exclude=["tests", "docs"]),
    install_requires=['numpy'],
    keywords=['python', 'neural network', 'MLP', 'classification'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    url="https://github.com/iarslankhalid/NeuroPy",
    project_urls={
        "Source": "https://github.com/iarslankhalid/NeuroPy",
        "Bug Reports": "https://github.com/iarslankhalid/NeuroPy/issues",
    },
    python_requires=">=3.10",
)
