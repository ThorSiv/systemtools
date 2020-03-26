#!code='utf-8'



#check server whether is opening 443 port :  nc -w 1 -z domain.com;echo $?
import re
import subprocess
import sys


def main(domain):

    cmd='curl -Ilvs https://{}/'.format(domain)
    sslinfo=subprocess.getstatusoutput(cmd)[1]
    m=re.search('start date:(.*?)\n',sslinfo)
    try:
        if "Mar 23 00:00:00 2020 GMT" not in m.group(1):
            with open("unsecurity.domain","a") as f:
                f.write(domain+'\n')
    except:
            with open("unsecurity.domain","a") as f:
                f.write(domain+'\n')


if __name__ == '__main__':
    domainfile = sys.argv[1]
    with open(domainfile) as f:
        for line in f:
            domain = line.strip().replace("\n",'').replace("\r",'').strip()
            main(domain)

