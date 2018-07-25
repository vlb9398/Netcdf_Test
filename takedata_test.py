import mce_data
import netcdf_trial as nct
import numpy as np
import os
import settings as st
import datetime as now
import json
import sys

''' Add your mce file path below '''
#--------------------------------------------------------------#
path = '/Users/vlb9398/Dropbox/NetCDF_Test/VLB'
sys.path.append(path)
#--------------------------------------------------------------#

def readdata(f,mce_file_name,h):
    d = np.empty([h.shape[0],h.shape[1]],dtype=float)
    for b in range(h.shape[0]):
        for c in range(h.shape[1]):
            d[b][c] = (np.std(h[b][c],dtype=float))
    #ADDING DATA TO NETCDF/CHECK FOR CETCDF FILE SIZE-------------------------------
    if os.stat("gui_data_test{n}.nc".format(n=st.n)).st_size < 5*10**6 : # of bytes here
        nct.data(h,d,st.n,st.a)
    else:
        st.n = st.n + 1
        nct.mce.close()
        nct.new_file(st.n)
        nct.data(h,d,st.n,st.a)

def read_header(f):
    for key,value in f.header.items():
        if key == '_rc_present':
            for i in range(len(value)):
                if value[i] == True:
                    value[i] = "1"
                elif value[i] == False:
                    value[i] = "0"
                else:
                    print("I don't know what I am...")
            value = ''.join(map(str,value))
        value = str(value)
        st.keys.append(key)
        st.values.append(value)
    # keys,values = zip(*f.header.items())
    st.keys = np.asarray(st.keys,dtype=object)
    st.values = np.asarray(st.values,dtype=object)
    st.head = np.array((st.keys,st.values)).T
    #-------------------------------------------------------------------------------

if __name__ =="__main__":
    st.init()
    mce_file_name = path
    f = mce_data.SmallMCEFile(mce_file_name)
    h = f.Read(row_col=True, unfilter='DC').data
    read_header(f)
    st.h_size = h.shape[2]
    nct.new_file(st.n)
    readdata(f,mce_file_name,h)
