#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import packages

import pandas as pd
import numpy as np
import math
import datetime
import os

#create a function that can truncate to two decimal places

def truncate(number,decimals):
    '''
    Returns a value truncated to a specific number of decimals
    '''
    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor

#create lists

l_dncb_v = []
l_dncb86_rfi = []
l_dncb_iso = []
l_dncb_86 = []
l_dmso_iso = []
l_dmso_86 = []
l_media_iso = []
l_media_86 = []
l_assay_date = []
l_assay_type = []
l_pass_fail = []
l_start_date = []

#files to read

excel_list = ['K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_081222_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_090922_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_091322A_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_091322B_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_091622_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_092022_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_092322_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_092722_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_100422A_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_100422B_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_110422_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_111122_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_120222A_Analyzed.xlsm',
'K:\lotus22\hCLAT\Analyzed Data 2022\Definitive_120222B_Analyzed.xlsm']


# In[2]:


#iterate through the files

for file in excel_list:
    fd = file

#setup objects to get the file from the file path and convert it to a useable dataframe, count the number of sheets, get date

    df = pd.read_excel(fd, sheet_name = 0, header=9, usecols='G:K')
    nsheets = len(pd.read_excel(fd,sheet_name=None))
    assay_size = nsheets - 3
    date_import = pd.read_excel(fd,sheet_name = 0, header = 3, usecols='D')
    assay_date = date_import.iloc[0,0]
    start_date = assay_date - datetime.timedelta(days=1)
    #assign variables

    dncb_v = df.iloc[22,3]
    dncb86_rfi = truncate(df.iloc[19,3],2)
    dncb_iso = df.iloc[9,0]
    dncb_86 = df.iloc[8,0]
    dmso_iso = df.iloc[6,0]
    dmso_86 = df.iloc[5,0]
    media_iso = df.iloc[3,0]
    media_86 = df.iloc[2,0]
    
    #print assay date

    print(assay_date.strftime('%m-%d-%Y'))
    l_assay_date.append(assay_date.strftime('%m-%d-%Y'))

    #print assay size

    assay_type = 'Definitive '+ str(assay_size) + 'X'

    print(assay_type)
    l_assay_type.append(assay_type)

    #check to see if all criteria passed

    if df.iloc[3,4] == 'Yes' and df.iloc[4,4] == 'Yes' and df.iloc[10,4] == 'Yes' and df.iloc[11,4] == 'Yes'     and df.iloc[12,4] == 'Yes' and df.iloc[13,4] == 'Yes' and df.iloc[18,4] == 'Yes' and df.iloc[19,4] == 'Yes'     and df.iloc[22,4] == 'Yes':
        l_pass_fail.append('Pass')
        print('Pass')
    else:
        l_pass_fail.append('Fail')
        print('Fail')

    #print values of interest and append them to respective lists

    print(dncb_v, ',',dncb86_rfi)
    l_dncb_v.append(dncb_v)
    l_dncb86_rfi.append(dncb86_rfi)

    print(start_date.strftime('%A'))
    l_start_date.append(start_date.strftime('%A'))

    print(dncb_iso,',',dncb_86,',',dmso_iso,',',dmso_86,',',media_iso,',',media_86)
    l_dncb_iso.append(dncb_iso)
    l_dncb_86.append(dncb_86)
    l_dmso_iso.append(dmso_iso)
    l_dmso_86.append(dmso_86)
    l_media_iso.append(media_iso)
    l_media_86.append(media_86)
    
    
    
print(l_assay_date)
print(l_assay_type)
print(l_pass_fail)
print(l_dncb_v)
print(l_dncb86_rfi)
print(l_start_date)
print(l_dncb_iso)
print(l_dncb_86)
print(l_dmso_iso)
print(l_dmso_86)
print(l_media_iso)
print(l_media_86)


# In[3]:


dict1 = {
    'Assay Date' : l_assay_date,
    'Assay Type' : l_assay_type,
    'Pass/Fail' : l_pass_fail,
    'DNCB Viability' : l_dncb_v,
    'DNCB CD86 RFI' : l_dncb86_rfi,
    'MWF' : l_start_date,
    'DNCB Isotype' : l_dncb_iso,
    'DNCB 86' : l_dncb_86,
    'DMSO Isotype' : l_dmso_iso,
    'DMSO 86' : l_dmso_86,
    'Media Isotype' : l_media_iso,
    'Media 86' : l_media_86
}


# In[4]:


#create pd dataframe from dictionary

dfx = pd.DataFrame.from_dict(dict1)


# In[5]:


#write DataFrame to Excel


file_name = "Meganthisissocool.xlsx"
dfx.to_excel(file_name)


# In[ ]:




