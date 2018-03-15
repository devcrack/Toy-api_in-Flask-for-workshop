import subprocess

def exe_hard:_sphere:
    print("Ejecutando esferas duras\n")
    hard_sphere_process = subprocess.Popen(['/home/delcracnk/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version/01Hard_Spheere','0.5'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = hard_sphere_process.communicate()
    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())
    if not hard_sphere_process.poll():
        print("Program execute finish")


# if __name__ == "__main__":
#     main()
