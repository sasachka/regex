import re

# initializing search patterns
reg_exp ={"mail": r"[\w._-]+@[\w._-]+\.[\w.]+",
          "telephone": r"[78]\d{10}",
          "domain": r"[a-z0-9_-]+(?:\.[a-z0-9_-]+)*\.[a-z]{2,6}",
          "ipv4": r"(?:(?:25[0-5]|2[0-4]\d|1?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|1?\d\d?)",
          "mac": r"(?:[a-f0-9A-F]{2}:){5}[a-f0-9A-F]{2}",
          "ipv6": r"(?:[0-9a-fA-F]{0,4}:){2,7}(?:[0-9a-fA-F]{0,4})?",
          "uri": r"https?://[0-9a-zA-Z-_]+\.[0-9a-zA-Z-_]+[^\s]*"}

try:
# get information from user:
    filename_input = input("Enter input file: ")
    filename_output = input ("Enter output file: ")
    search_subject = input ("What do you want to find? Enter one of the options:\nmail, telephone, domain, ipv4, mac, ipv6, uri: ")

    file_input = open(filename_input, mode = 'r')
    file_output = open(filename_output, mode = 'w')

#Finding information and writing to a file
    result = re.findall(reg_exp[search_subject],file_input.read())
    for i in result:
        file_output.write(i+"\n")
        print(i+"\n")
except:
    print ("!!! Please, check the input and try again !!!")

file_input.close()
file_output.close()