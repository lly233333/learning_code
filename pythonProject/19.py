# 正则表达式的高级应用
import re
s = "我的电话号码：010-89890827 0431-98783265 0432-7654738"
# reg = "0\d{3}-\d{8}"
reg = "0\d{3}-\d{8}|0\d{2}-\d{8}|0\d{3}-\d{7}"
# |或操作符
# 分支条件匹配
# print(re.findall(reg,s))


# 零宽断言
# (?=reg)匹配reg前面的位置
# (?<=reg)匹配reg后面的位置
s = "hellogreedyailove"
reg = "l{2}o(?=greedyai)"
# print(re.findall(reg,s)) #结果llo
reg = "(?<=greedyai)[a-z]*"
print(re.findall(reg,s))