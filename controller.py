"""
Name:           controller.py    
Author:         Randy Runtsch
Date:           April 10, 2021
Description:    Entry point controller. Use class c_e_info to get a 
                list of NIH NCBI Entrez databases and detailed information 
                about the NCBI pubmed database.
"""

from c_e_info import c_e_info

# Get the names of all Entrez databases as XML. Write the XML
# to a file and print it to the screen.

pubmed_db_list = c_e_info()
pubmed_db_list.write_db_xml('c://project_data/c_e_info/entrez_db_list.xml')
print(pubmed_db_list.get_db_xml())

# Get the details of the pubmed database as XML. Write the XML
# to a file and print it to the screen.

pubmed_db_info = c_e_info('pubmed')
pubmed_db_info.write_db_xml('c://project_data/c_e_info/entrez_pubmed_db_info.xml')
print(pubmed_db_info.get_db_xml())



