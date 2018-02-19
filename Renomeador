import os

def rename_files():
    #(1) procura os nomes dos arquivos na pasta
    file_list = os.listdir(r."C:\OOP\Prank")
    #print(file_list)
    saved_path = os.getcwd()
    
    #(2) para cada arquivo, renomeia o nomearquivo
    for file_name in the file_list:
      print("Old Name - " +file_name)
      print("New name - " +file_name.translate(None, "0123456789"))
      os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    
rename_files()    
