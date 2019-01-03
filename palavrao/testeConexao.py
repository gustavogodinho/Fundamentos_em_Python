import urllib.request as ur
s = ur.urlopen("http://www.wdylike.appspot.com/?q=pussy")
sl = s.read()
print(sl)

d = sl.decode('ASCII')

if "true" in d:
    print("Profanity Alert!!")
elif "false" in d:
    print("This document has no curse words!!!")
else:
    print("Could not scan the document properly.")
