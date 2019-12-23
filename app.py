import subprocess ,os
dir_path = os.path.dirname(os.path.realpath(__file__))
exepath = dir_path+"/main.exe"
print(exepath)
subprocess.run([exepath])
