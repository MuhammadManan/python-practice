# Reading file
'''f = open("Manan.txt", "r")
# print(f)

content = f.read()
print(content)

f.close() '''


# Writing to a file
'''f = open("John.txt", "w")
string = '''
# John is a software engineer with over 10 years of experience in the tech industry. He specializes in Python and has worked on various projects ranging from web development to data analysis. In his free time, he enjoys hiking and photography.
# John is passionate about learning new technologies and sharing his knowledge with others. He believes in the power of collaboration and often participates in open-source projects. His goal is to create impactful software that makes a difference in people's lives.
'''
f.write(string)
f.close()'''

# appending to a file
'''f = open ("John.txt", "a")
string = '''
# John is also an advocate for clean code and best practices in software development. He regularly attends tech meetups and conferences to stay updated with the latest trends in the industry. His dedication to continuous learning and improvement has earned him respect among his peers.
# '''
# f.write(string)
# f.close()'''


# Reading a file line by line
'''f = open("John.txt","r")

for line in f:
    print(line)

f.close()'''

# Reading a file using with statement
'''with open("Manan.txt", "r") as f:
    content = f.read()
    print(content)'''


import os
a = os.listdir("dir")
print(a)

print(os.getcwd())
print(os.path.exists("John.txt"))
os.remove("dir/sample1.txt")
