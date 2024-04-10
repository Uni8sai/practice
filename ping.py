# %%
import subprocess

cmd = "ping 10.10.10.3 >> /var/log/ping_log/ping_in_`date +\%Y\%m\%d`"
subprocess.call(cmd.split())
print('Hello GitHub')
print('create new branch')