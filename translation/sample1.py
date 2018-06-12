import subprocess

print(subprocess.Popen("echo hi", shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8'))