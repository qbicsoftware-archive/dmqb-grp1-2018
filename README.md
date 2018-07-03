# dmqb-grp1-2018
The project assignment work of group 1 in the lecture DMQB



=======
# valifor 
=======
valifor 
=============================
>>>>>>> 3rd commit

A command line validating tool to parse and validate NGS file formats(fasta and fastq) in their applications.

Motivation
======================

Usually corrupted data creates big problems during analaysis. Reaching the desired result from analaysis is dependent on the quality of data set in the first step. Yet there are not enough tools available to validate the data sets. Although there are some format validators available for some file formats but yet they can not address the issue completely as neither each data format has a validator nor each existing format validator can validate more then one file format. As a good example of already existing validating tools one can name the FastaValidator software; that is designed exactly for fasta files and fastQValidator that can only validate the fastq files.  

In order to address this issue we created the __valifor__ that can validate the NGS file formats; fasta and fastq. Its a command line based tool that can easily varify the quality of data set. Additionaly this tool is designed in a fashion that can be exapanded for more file formats easily. 

Table of Contents
=======================

* The overal design
* Installation
* The command line interface
* Main logic
* Factory
* AbsFormat
    * fasta
    * fastq

The overal design
=======================
The *valifor* design is shown in the following graph: 

![valifor](https://user-images.githubusercontent.com/35918514/42245707-01840510-7f1a-11e8-8860-20ea51f056b9.jpg)

by adding a new format in the list of AbsFormat one can easily add more format to the validator. 

Installation
=======================

The easiest way is to install a stable release of ``valifor`` from PyPi with pip:


    $ pip install valifor

The command-line interface:
========================

Once the *valifor* is installed, it can be called by typing ``--help`` in the command line. It will preview an overview of the subcommands available in *valifor*:

    $ valifor --help
    Usage: parser.py [OPTIONS] [FILES]...

    Options:
    --type [fasta|fastA|fastq]  Type of file
    --help                      Show this message and exit.


in order to validate a file, the user should call the valifor and then type the format that he/she wants to test against and then type the name of file/s. The *--tpye* is optional, the user can either select it or not, but a user can only select from the provided list of data formats listed under type.

    $ valifor fasta example.fasta

    (['example.fasta'], ['fasta'])

if the file does not exist: 

    This file does not exist: example.fasta
    
Main Logic: 
=======================
This part is the main part of the tool. After recieving the input the main logic will check the content of the file/s using the factory and will evaluate the file based on its format using the AbsFormat. 

Factory
=======================
In this part the information that is required for file categorization is stored and once the user inputs the file/s into the valifor the factory will be called by Main logic part to categorize the file to one of the data formats available in valifor. The factory contains specifications that directs the file in a specific direction order to chose its correct data format. 

AbsFormat
=======================
In this part the data formats are specified. Currently the valifor can validate two NGS data formats that are fasta and fastq. But its designed in a way that can let us add more data formats to the AbsFromats part. The specifications for each data format is detailed under the AbsFormat. This part will be called by Main Logic while checking the quality of the file.   


 
