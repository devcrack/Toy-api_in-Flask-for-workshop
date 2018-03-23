from shutil import copyfile
import os
# path = '/home/delcracnk/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version/data/sk_HSpheere.dat'

def copy_files(path):
    os.chdir('/home/delcracnk/REPOSITORIES/api_rest_example_Python')    
    copyfile(path, './SKhard_sphere.dat')



if __name__ == "__main__":
    copy_files('/home/delcracnk/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version/data/sk_HSpheere.dat')
