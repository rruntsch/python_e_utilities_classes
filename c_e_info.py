import requests

class c_e_info:
    
    """
    Name:           c_e_info.py    
    Author:         Randy Runtsch
    Date:           April 10, 2021
    Description:    Python wrapper class for the NIH NCBI
                    EInfo API used to obtain a list of Entrez databases and statistics
                    for an individual database. 
    References:     Entrez programming utilities - https://www.ncbi.nlm.nih.gov/books/NBK25497/
    """

    def __init__(self, db_name = None):

        # Set the base Entrez API URL and call the appropriate function to return
        # a list of all NIH NCBI Entrez databases or details for a single database.

        self._base_api_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi/'

        if db_name == None:
            # Retrieve a list of all Entrez databases.
            self._db_xml = self.get_db_list()
        else:
            # Retrieve details for a single Entrez database.
            self._db_xml = self.get_db_info(db_name)

    def get_db_xml(self):

        # Return the XML retrieved with the EInfo e-utility.

        return self._db_xml

    def write_db_xml(self, file_nm):

        file = open(file_nm, 'w')

        file.write(self._db_xml)

    def get_db_list(self):

        # Call the Entrez EInfo utility with the base URL to obtain the list of 
        # all Entrez databases.

        response = requests.get(self._base_api_url)

        return response.text

    def get_db_info(self, db_name):

        # Call the Entrez EInfo utility with the base URL and an Entrez database name
        # to obtain statistics and a list of fields and links for the database.

        full_url = self._base_api_url + '?db=' + db_name
        response = requests.get(full_url)

        return response.text














