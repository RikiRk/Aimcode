import subprocess
data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1]for i in data if "all user profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles',i,'ket=clear']).decode('utf-8').split('\n')
    results = [b.spilt(":")[1][1:-1]for b in results if "key content" in b]
    try:
        print("{:<30}| {:<}".format(i,results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i,""))
input("")        
    
