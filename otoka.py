import requests
import subprocess
import sys
f = open('load.txt')
src = f.read()
f.close()
src_s = src.split('\n')
src_g =  ""
for i in range(len(src_s)):
    url = src_s[i]
    try:
        src_site = requests.get(url)
        src_g = src_g + src_site.text
    except:
        try:
            f = open(url)
            src_file = f.read()
            f.close()
            src_g = src_g + src_file
        except:
            print(f"ERROR:URL OR PATH:{url} NOT FOUND")
f = open(sys.argv[1],'w')
f.write(src_g)
f.close()
