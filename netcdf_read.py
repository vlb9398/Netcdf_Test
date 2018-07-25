from netCDF4 import Dataset
from netCDF4 import MFDataset
import sys
import matplotlib.pyplot as plt

def all_files(group,var):
    f = MFDataset('gui_data_test*nc','r')
    s = f.groups['guiparams']
    t = s.variables['time'][:]
    l = f.groups[group]
    x = l.variables[var][:]
    ''' Note: no attributes have been added to variables/groups yet'''
    # if len(sys.argv) > 4 :
    #     if sys.argv[4] == '--group_att' :
    #         group_att(sys.argv[4],f)
    #     elif sys.argv[4] == '--var_att' :
    #         var_att(sys.argv[4],f)

    print(x[0:10])

def one_file(file,group,var):
    f = Dataset('gui_data_test{num}.nc'.format(num=file),'r')
    s = f.groups['guiparams']
    t = s.variables['time'][:]
    l = f.groups[group]
    x = l.variables[var][:]
    ''' Note: no attributes have been added to variables/groups yet'''
    # if len(sys.argv) > 5 :
    #     if sys.argv[5] == '--group_att' :
    #         group_att(sys.argv[5],f)
    #     elif sys.argv[5] == '--var_att' :
    #         var_att(sys.argv[5],f)

    print(x[0:10])

def group_att(group,f):
    print("Meta Data for the {group} group".format(group=group))
    print(f.groups[group])

def var_att(var,f):
    print("Meta Data for the {var} variable".format(var = var))
    print(f.variables[var])

def file_keys(file):
    f = Dataset('gui_data_test0.nc','r')
    print("Group Keys:")
    print(f.groups.keys())
    print("Variable Keys:")
    for key in f.groups:
        print("For Group {key}:".format(key = key), f.groups[key].variables.keys())

#------------------------------------------------------------------------------
if __name__ == "__main__":
    if sys.argv[1] == 'all' :
        all_files(sys.argv[2],sys.argv[3])
    elif sys.argv[1] == 'one' :
        one_file(sys.argv[2],sys.argv[3],sys.argv[4])
    elif sys.argv[1] == 'keys':
        file_keys(sys.argv[0])
    else:
        print("Error: Invalid Command (check order and names)")
