import re
from sys import exception

import openpyxl



def modify_file(input_file, data=None, json_data=None):
    with open(input_file,encoding='utf-8')as file:
        lines=file.readlines()



    in_modifiction_block=False
    modified_lines=[]
    print(len(lines))
    for line in lines:

        if line.startswith('workbook') and 'openpyxl' in line:
            in_modifiction_block=True
            #workbook3 = openpyxl.load_workbook(filename=exel_path+"up lv profile.xlsx")
            new_file=line.split("+")[1].split(")")[0]
            new_value={}



        if in_modifiction_block and line.startswith('sheet') and "workbook" not in line:
            line=line.replace("'","").replace("","")
            key = line.split("[")[1].split("]")[0].replace("'", "")
            value = line.split("=")[1].replace("\n","")
            # match = re.match(r"sheet\d+\['(\w+\d+)'\]\s*=\s*(.*)", line)
            # if match:
            #     cell = match.group(1)
            #     expression = match.group(2)
            #     print(cell, expression)
            #     try:
            #
            #         new_value[cell] = eval(expression)
            #         #new_value[key] = value
            #     except exception as e:
            #         print(f"Error evaluating expression :{expression} - {e}")
            #         continue
            #

            new_value[key] =value
            print(new_value)
            pass



        if in_modifiction_block and '.save(filenam'in line:

            #print(line)
            new_line = """workbook=ExcelUpdater(exel_path+{},{}) \nworkbook.updte() \n""".format(new_file,new_value)
            print(new_line)


            modified_lines.append(new_line)

            in_modifiction_block=False

        # else:
        #  modified_lines.append(line)
    return modified_lines

replacement={
    'old_var':'new_var',
    'old_function()':'new_function()'
}


def modify_file_custom():
    pass


modify_file_custom()
print("file modified successfuly!")

input_file='FINAL_V1.PY'
output_file='modiied_FINAL_V1.PY'

ret=modify_file(input_file)
f = open(output_file, "a")
f.writelines(ret)
f.close()

