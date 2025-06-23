#Regex.py

import re
import pyperclip as py

text =str(py.paste())

phoneRegex = re.compile(r'''(
                        (\d{3}|\(d{3}\))  #Area Code
                        (\s|\.|-)?        #Separator
                        (\d{3})           #First 3 digits
                        (\s|\.|-)?        #Separator
                        (\d{4})           #Last 4 digits
                        )''',re.VERBOSE)
emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+    #username
                        @
                        [a-zA-Z.]+

                        )''',re.VERBOSE)


matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups)

print(matches)

if len(matches) > 0:
    py.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


