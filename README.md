# INBreast_XML_parser
Simple XML parser to create the annotation masks of the INBreast dataset

Required Libraries:

     os, cv2, math, numpy, pydicom, polygon from skimage.draw, xml.etree.ElementTree, pyplot from matplotlib

**Note:** The DICOM files were renamed in order to match the corresponding names in csv

**Example:**

     _Before preprocessing:_
     
     image name in csv: 2234546
     corresponding file: 2234546_hduiu2e8329398021.dcm
     
     _After preprocessing:_
     
     image name in csv: 2234546
     corresponding file: 2234546.dcm
     

Files and description:
----------------------
```
INBreast_XML_parser
│    README.md
│
└─── python
│    │   annotation.py  #The main file containing the Annotation class
│    │   annotation_tb.py #A testbench for the tool
│   
│   
└─── notebook
     │   INbreast_xml_parser.ipynb #Colab/Jupyter notebook version of the tool
```

## Installation

The INBreast_XML_parser can be cloned from here or it can be installed using Python pip tool

- Option 1: Clone the repository and see the demo files in python and notebook folders
- Option 2:
  - Install tool using ```pip3 install git+https://github.com/itzortzis/INBreast_XML_parser.git```
  - Import the needed components ```import annotation```
  
Enjoy!!!
  

INBreast dataset:
-----------------
Inês C. Moreira, Igor Amaral, Inês Domingues, António Cardoso, Maria João Cardoso, Jaime S. Cardoso,
INbreast: Toward a Full-field Digital Mammographic Database,
Academic Radiology,
Volume 19, Issue 2,
2012,
Pages 236-248,
ISSN 1076-6332,
https://doi.org/10.1016/j.acra.2011.09.014.
(https://www.sciencedirect.com/science/article/pii/S107663321100451X)

![parser](https://user-images.githubusercontent.com/105294556/167639632-ff3ab6eb-4c09-46e9-becf-0dad8df639d6.png)
