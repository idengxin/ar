import os
def rename_files():
    file_list=os.listdir(r"F:\project\python\prank")#r��������ɶ
    print(file_list)
    saved_path=os.getcwd()
    os.chdir(r"F:\project\python\prank")#����ǰ����Ŀ¼�л�
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"1234567890"))
    os.chdir(saved_path)

rename_files()
