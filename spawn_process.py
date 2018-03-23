import json
import os
import subprocess
import convert_json


def exe_hard_sphere(fraction_volumen):
    # path = subprocess.call('cd /home/delcracnk/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version', shell=True)
    path = os.chdir('/home/delcracnk/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version')
    path = os.getcwd()
    print(path)
    hard_sphere_process = subprocess.Popen([path + '/01Hard_Spheere', fraction_volumen.strip()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = hard_sphere_process.communicate()
    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())
    if not hard_sphere_process.poll():
        print("Program execute finish")    
    convert_json.convert_file()
    with open('sk_HSpheere.json') as json_data:
        d = json.load(json_data)
    return d

if __name__ == "__main__":
    exe_hard_sphere('0.8')
