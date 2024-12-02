import paramiko
from utilities.configurations import *
import csv

username = get_config()['SERVER']['username']
password = get_config()['SERVER']['password']
host = get_config()['SERVER']['host']
port = get_config()['SERVER']['port']


ssh  = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

# Run commands
stdin, stdout, stderr = ssh.exec_command('cat demofile')
lines = stdout.readlines()
print(lines[1])

#Upload files
sftp = ssh.open_sftp()
destinationPath = "script.py"
localPath = "batchFiles/script.py"
sftp.put(localPath, destinationPath)

destinationPath = "loanasa.csv"
localPath = "batchFiles/loanasa.csv"
sftp.put(localPath, destinationPath)

#Trigger the bash commands
stdin, stdout, stderr = ssh.exec_command("python3 script.py")

#Download the file to local system
sftp.get("loanasa.csv", "outputFiles/loanasa.csv")

#Parse output file CSV
with open("outputFiles/loanasa.csv") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    for row in csvReader:
        if row[0] == "32321":
            assert row[1] == "rejected"

ssh.close()