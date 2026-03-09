# This setup file is based on the one found here:
# https://towardsdatascience.com/create-your-custom-python-package-that-you-can-pip-install-from-your-git-repository-f90465867893

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='inbreastxmlparser',
    version='0.2.1',
    author='itzorzis',
    author_email='i.n.tzortzis@gmail.com',
    description='INBreast_XML_parser installation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/itzortzis/INBreast_XML_parser',
    project_urls = {
        "Code": "https://github.com/itzortzis/INBreast_XML_parser",
        "Bug Tracker": "https://github.com/itzortzis/INBreast_XML_parser/issues"
    },
    license='GPL-3.0',
    packages=['inbreastxmlparser'],
    install_requires=['numpy', 'polygon'],
)
