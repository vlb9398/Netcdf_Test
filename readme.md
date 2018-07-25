# Author:
  Victoria Butler
  vlb9398@g.rit.edu
  Rochester Institute of Technology

# Purpose :
  This is a test suite to understand the packing and unpacking of TIME data in
  the NETCDF4 file format.

# Required Installations:
  *These instructions assume an installation of Anaconda3*
  *(please believe me that you don't want to try installing netcdf4 pre-reqs
    without it)*
  1. Installing Anaconda3
    Linux:
      download package from https://conda.io/docs/user-guide/install/linux.html
    Mac:
      download package from https://conda.io/docs/user-guide/install/macos.html
    Windows:
      download package from https://conda.io/docs/user-guide/install/windows.html

  2. conda install -c anaconda netcdf4


# File Descriptions :
  *MCE_DATA.py*
    Parses the mce data
    From UBC repository
    DO NOT MODIFY

  *NETCDF_TRIAL.py*
    Responsible for formatting and creating a new file, and also contains
    functions for appending data to existing variables

    Data_all function is used for the full rack of 4 cards in 1 MCE
    data is used for a single readout card

    (Both are not necessary for the final product, but given the RIT/Caltech
      setup differences, this was easier than writing two different scripts.
      Replace the function call in takedata_test as appropriate for your system)

    Both functions are called by takedata_test to append data

  *NETCDF_READ.py*
    Script to parse data from created netcdf files

    Contains functions for reading all or just one file
      (the choice does not affect the speed of reading data)

      Currently prints the first 10 values from the variable selected by the user

    Other functions can print group attributes, variable attributes, and a return
    the full list of groups and variables available in the file

  *TAKEDATA_TEST.py*
    1. Parses the mock mce data file "VLB" using mce_data
    2. Creates a new netcdf file by calling "new_file" function
    3. Appends data to variables in netcdf file after checking current file size
    4. Creates new file once limit is reached

  *SETTINGS.py*
    Stores the global variables used across all scripts


# Activation Commands
  1. (make sure calling anaconda python)
    python takedata_test.py
      #you should now see a file named gui_data_test0 in your directory
  2. To print Keys
    python netcdf_read.py keys
      #you should now see a list of the groups/variables

  3. To print a specific variable
    *One File*
    *python netcdf_read.py one #file_num #group #variable*
    python netcdf_read.py one 0 guiparams datetime
      #will return all of the datetime values stored in the file
    *All Files*
    *python netcdf_read.py all #group #variables*
    python netcdf_read.py all guiparams datetime
      #will return all of the datetime values from all files
    #note this doesn't work in the current version since there is
    only one file
    #you can set the file size limit to smaller if you would like to create
    additional files

    *All returns or prints from netcdf_read.py can be modified to create graphs
    or return different data arrays, or to perform basic math, whatever you want.*

    <!-- 4. *FUTURE FUNCTIONS, NOT READY YET*
      To print group/variable attributes
        add the flag to the end of the previous call commands either
        --group_att
            or
        --var_att -->
