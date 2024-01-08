# MSOFFICE_macro_encoder.py
This script is intentionally crafted with the sole purpose of automating and tackling one of the exercises in PWK-200, Leveraging Microsoft Word Macros. 

Created by windyforce, on 6th November 2023
*Please make sure the .doc format is 97-2003 document !! Newer .docx file type cannot save macros without attaching a containing template

What does this script do?
1. It attempts to get your IP address (with VPN tunneling interface tun0 prioritized)
2. Next, it attempts to download powercat.ps1 from your http server and executes the script.
3. Next, the code is encoded into UTF-16LE and Base64.

Results:
The script prints the original PowerShell command, the Base64-encoded version, and a PowerShell command string containing the Base64-encoded payload.
You just need to copy and paste this payload into your macro and save it together with the document, if the victim attempts to open the infected document and gives
permission to run macros as well, you will get a reverse shell.
