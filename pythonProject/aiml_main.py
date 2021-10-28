import aiml

k = aiml.Kernel()
# xml当作语料库
k.learn("std-startup.xml")
# 学习…….xml文件
k.respond("load aiml b")
while True:
    print(k.respond(input("input >>")))