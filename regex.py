import re

# initializing search patterns
reg_exp ={"mail": r"[\w._-]+@[\w._-]+\.[\w.]+",
          "telephone": r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$",
          "domain": r"",
          "ipv4": r"",
          "mac": r"",
          "ipv6": r"",
          "uri": r"",
          "inn": r""}

#get information from user
filename_input = input("Enter input file: ")
filename_output = input ("Enter output file: ")
search_subject = input ("What do you want to find? Enter one of the options:\nmail, telephone, domain, ipv4, mac, ipv6, uri, inn: ")

file_input = open(filename_input, mode = 'r')
file_output = open(filename_output, mode = 'w')

#Finding information and writing to a file
result = re.findall(reg_exp[search_subject],file_input.read())
for i in result:
    file_output.write(i+"\n")

file_input.close()
file_output.close()