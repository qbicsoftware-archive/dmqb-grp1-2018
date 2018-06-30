# dmqb-grp1-2018
The project assignment work of group 1 in the lecture DMQB



=======
# valifor 

A command line validating tool for NGS file formats(fasta and fastq).

## Motivation

Usually corrupted data creates big problems during analaysis. Reaching the desired result from analaysis on the data set is dependent on the quality of data set on the first step. Yet there are not enough tools available to validate the data sets. Although there are some format validators available for some file formats but yet they can not address the issue completely as neither each data format has a validator nor each existing format validator can validate more then one file format. 

In order to address this issue we created the __valifor__ that can validate the NGS file formats; fasta and fastq. Additionaly it could be exapanded easily to the more file formats. 

### Table of Contents
* installation
* The command line interface
* Main logic
* Factory
* AbsFormat
    * fasta
    * fastq

Installation
============

The easiest way is to install a stable release of ``valifor`` from PyPi with pip:


    $ pip install valifor

.. _PyPi: https://pypi.org/
.. _pip: https://pypi.org/project/pip/


The command-line interface:
===========================

Once the *valifor* is installed, it can be called by typing ``--help`` in the command line. It will preview an overview of the subcommands available in *valifor*:

    $ valifor --help
    Usage: parser.py [OPTIONS] [FILES]...

    Options:
    --type [fasta|fastA|fastq]  Type of file
    --help                      Show this message and exit.


in order to validate a file, the user should call the valifor and then type the format that he/she wants to test against and then type the name of file/s. 

    $ valifor fasta example.fasta

    (['example.fasta'], ['fasta'])

if the file does not exist: 
.. code-block:: bash
    This file does not exist: example.fasta


 The overal design
===========================
The *valifor* is designed based on the following structure: 

    .
    ├── file/s
    │   └── input_file/s   // input files
    |   └── output format and path of the file
    ├── main logic       // which format should be called
    ├── factory       // which format should be called
    └── AbsFormats
        └── fasta    // A collection of R scripts
        └── fastq

by adding in the a format in the list of AbsFormat one can add more format to the validator. 

The design of the valifor tool is more visible in the following graph:

![valifor](https://user-images.githubusercontent.com/35918514/42127035-fd59b53c-7c91-11e8-8f96-f229f412b87b.jpg)
