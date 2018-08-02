import numpy as np
from os import stat
import os
import sys
import mce_data
import subprocess
import settings as st
import netcdf_trial as nc


def netcdfdata(n_files):
    tempfiledir = ('./netcdffiles')
    if os.path.exists(tempfiledir):
        print('Hello!')
    else:
        print('Making NETCDF File Directory')
        netcdf_dir = ['mkdir netcdffiles']
        subprocess.Popen(netcdf_dir, shell=True).wait()
    #print('HELLO!')
    #n_files = len(os.listdir("/data/cryo/current_data"))
    a = 0
    st.a = a
    mce = 1
    n = 0
    while True:
        mce_file = os.path.exists("/data/cryo/current_data/temp.%0.3i" %(a+1)) #wait to read new file until old file is complete
        if mce_file:
            print(a)
            mce_file_name = "/data/cryo/current_data/temp.%0.3i" %(a)
            a = a + 1
            st.a = a
            f = mce_data.SmallMCEFile(mce_file_name)
            header = read_header(f)
            mce, n = readdata(f, mce_file_name, mce, header, n, a)
            mce_file = os.path.exists("/data/cryo/current_data/temp.%0.3i" %(a+1))
        else:
            pass


def readdata(f, mce_file_name, mce, head, n, a):
    h = f.Read(row_col=True, unfilter='DC').data
    d = np.empty([h.shape[0],h.shape[1]],dtype=float)
    for b in range(h.shape[0]):
        for c in range(h.shape[1]):
            d[b][c] = (np.std(h[b][c][:],dtype=float))

    tempfiledir = ('netcdffiles')
    if a == 1:
    	mce = nc.new_file(n, h.shape, head)
    if os.stat(tempfiledir + "/gui_data_test{n}.nc".format(n=n)).st_size < 20 * 10**6: # of bytes here
        nc.data(h,d,n,a,head)
    else:
        mce.close()
        n = n + 1
        #mce = 'tempfiles/gui_data_test%s.nc' % (n - 1)
        print('----------New File----------')
        mce = nc.new_file(n, h.shape, head)
        nc.data(h,d,n,a,head)

    delete_file = ['rm %s' % (mce_file_name)]
    subprocess.Popen(delete_file, shell=True)
    return mce, n


def read_header(f):
    keys = []
    values = []
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
        keys.append(key)
        values.append(value)
    keys = np.asarray(keys,dtype=object)
    values = np.asarray(values,dtype=object)
    head = np.array((keys,values)).T
    return head

if __name__ == '__main__':
    netcdfdata(sys.argv[1])
