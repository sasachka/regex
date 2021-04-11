import re

# initializing search patterns
reg_exp ={"mail": r"[\w._-]+@[\w._-]+\.[\w.]+",
          "telephone": r"[0-9]{11}",
          "domain": r"",
          "ipv4": r"",
          "mac": r"",
          "ipv6": r"",
          "uri": r"",
          "inn": r""}

'''reg_tel_number = r"[0-9]{11}"
reg_mail = r"[\w._-]+@[\w._-]+\.[\w.]+"
reg_domain_name = r""
reg_ipv4 = r""
reg_mac = r""
reg_ipv6 = r""
reg_uri = r""
reg_inn = r"" '''

#get filenames from user
filename_input = input("Enter input file: ")
filename_output = input ("Enter output file: ")

file_input = open(filename_input, mode = 'r')
file_output = open(filename_output, mode = 'w')
search_subject = input ("What do you want to find? Enter one of the options:\nmail, telephone, domain, ipv4, mac, ipv6, uri, inn: ")


result = re.findall(reg_exp[search_subject],file_input.read())
for i in result:
    file_output.write(i+"\n")


file_input.close()
file_output.close()