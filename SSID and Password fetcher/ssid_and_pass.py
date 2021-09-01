# This python script will retrieve Wifi ssids stored on a computer along with their security keys
# Author - Bighnesh Sahoo (github - https://github.com/bigsbunny)

import subprocess
import re

# the run method of subprocess module is used to run the system command netsh wlan show profiles, capture_output arg is used to store the stdout of the command, text=True means the output is converted to normal text form.
returned_process = subprocess.run(
    ['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
# print(returned_process.stdout)
ssids_output = returned_process.stdout

pattern = re.compile(r"All User Profile     :.*")
wifi_profiles = pattern.findall(ssids_output)
wifi_ssids = []

for wifi in wifi_profiles:
    wifi_ssids.append(wifi[23:])

final_passwords = []

for wifi in wifi_ssids:
    profile = subprocess.run(['netsh', 'wlan', 'show', 'profiles',
                             wifi, "key=clear"], capture_output=True, text=True)
    pass_part = re.compile(r"Key Content            :.*")
    passwords = pass_part.findall(profile.stdout)

    for password in passwords:
        final_passwords.append(password[25:])

output = list(zip(wifi_ssids, final_passwords))
print(output)
