#current file structure
'''
c_cat_3.jpeg
copy_cat_2.jpeg
cp_cat_1.jpeg
cpy_cat_4.jpeg
'''

import os 
os.chdir('/home/user_name/folder')
for file in os.listdir():
    file_name, file_ext =(os.path.splitext(file))
    f_title, f_common, f_num = file_name.split('_')
    #remove white space
    f_title = f_title.strip()
    f_common = f_common.strip()
    #padding 0's 
    f_num = f_num.strip().zfill(2)
  
    new_file_name = f'{f_num}_{f_common}{file_ext}'
    print(new_file_name)
    ## os.rename(file, new_file_name)

#after script
'''
 01_cat.jpeg
 02_cat.jpeg
 03_cat.jpeg
 04_cat.jpeg
'''
