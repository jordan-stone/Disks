#Jordan Stone
#15 Sep 10
#
#
#A Semi-robust data reader?
#
#readcol reads a data file and returns the data.  readcol will attempt to skip
#meta-data lines in any file and will begin reading at the first line it
#encounters with only numbers present.(This could be modified to accept the 
#data type from the user and check for the first line consistent with the 
#supplied data types...future improvement.)  The user can also instruct 
#readcol where to begin reading through the keyword argument skipLines.  
#
import numpy as np
def readcol(filename,delimiter=None,colNames=[],skipLines=0,format=None):
    #open the file and read lines into a list
    f=open(filename,'r')
    lines=f.readlines()
    f.close()
    #Split up lines into their columns
    if delimiter != None:
        lines_split=[line.split(delimiter) for line in lines]
    else:
        lines_split=[line.split() for line in lines]
    #find the first and last lines with data (i.e. find a continuous block of lines with numbers
    if format == None:
        format=[]
        for name in colNames:
            format.append('f')
    elif not isinstance(format,(list,np.ndarray)):
        print 'format keyword must be a list or numpy array'
        return
    elif len(colNames) != len(format):
        print 'the number of entries in colNames and in format must be equal'
        return
    function_list=[]
    for data_type in format:
        if data_type=='f' or data_type=='F' or data_type=='':
            function_list.append(float)
        elif data_type=='i' or data_type=='I':
            function_list.append(int)
        elif data_type=='a' or data_type=='A':
            function_list.append(str)
        else:
            print 'Format not understood.'
            print 'Please provide "f" for float,"i" for int, or "a" for string'
            return
    first_line=skipLines
    while first_line <= len(lines_split):
        try:
            for i in xrange(len(colNames)):
                test=function_list[i](lines_split[first_line][i])
            break
        except:
            first_line+=1
    dat_dict={}
    for name in colNames:
        dat_dict[name]=[]
    line=first_line
    while line <= len(lines_split):
        try:
            for i in xrange(len(colNames)):
                dat_dict[colNames[i]].append(function_list[i](lines_split[line][i]))
            line+=1
        except:
            break
    for key in dat_dict.keys():
        if isinstance(dat_dict[key][0],float): dat_dict[key]=np.array(dat_dict[key],dtype=float)
        if isinstance(dat_dict[key][0],int): dat_dict[key]=np.array(dat_dict[key],dtype=int)
        if isinstance(dat_dict[key][0],str): dat_dict[key]=np.array(dat_dict[key],dtype=str)
    return dat_dict
