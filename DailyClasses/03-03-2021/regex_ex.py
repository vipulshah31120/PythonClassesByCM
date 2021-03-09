import re
import camelcase

a = "I can do this."
x = re.search("^I.*this.$", a)	

if x :
	print("Matched")
else :
	print("No Match")

print(re.search("a.c", " e gc ge f ayc jhajc"))
print(re.findall("a.c", " e gc ge f ayc jhajc"))

y = re.split("\s", a)
print(y)

y = re.split("\s", a, 2)
print(y)

y = re.sub("\s", "-", a)
print(y)

y = re.sub("\s", "-", a, 1)
print(y)

y = re.search(r"\bt\w+", a)
print(y.span())

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

