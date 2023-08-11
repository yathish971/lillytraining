import re as reg

a="..thish.*l$"
b="yathish rahul bathish ramesh3"

pattern="ac..ve"
test_string="my activestate platform account is now active"
print(reg.findall(a,b))
print(reg.findall(pattern,test_string))