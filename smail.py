import platform
import subprocess

import yagmail


def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '4', host]

    if subprocess.call(command) == 0:
        s1 = str(subprocess.check_output(command))
        offset = s1.find('Average')
        s2 = s1[offset + 10:offset + 15].strip("\ r \\")
        s2 = 'Server ' + host + ' is alive with a timeout of:  ' + s2
    else:
        s2 = 'Server ' + host + ' is dead'
    return s2


# use the following in case of first use
# remeber to generate an app password from google security

# import keyring
# to show the set password
# print(keyring.get_password("yagmail", "your_email"))

# to change to the current password
# keyring.set_password("yagmail", "your_email", "new_password")

print(ping('192.168.1.1'), '/n')

receiver = "smail.mhamed+serverstatus@gmail.com "
body = '<h1> This is a script that I developed in python to check the status of a server </h1> <h3>' + ping(
    '192.168.1.1') + '<br>' + ping('8.8.8.8') + '<br>' + ping('8.8.0.8') + '<br>'

yag = yagmail.SMTP("safa.ahmed.ed@gmail.com")
yag.send(
    to=receiver,
    subject="Server status",
    contents=body
    # attachments=filename,
)
