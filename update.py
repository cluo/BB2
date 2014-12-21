#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Email: lyleaks@gmail.com

import re
import requests
import sys
import os
import HTMLParser

def down_poc(cookie):
    page = 1
    headers = {'Cookie': cookie}
    while True:
        page_url = 'http://www.beebeeto.com/pdb/?page=%s' % str(page)
        content = requests.get(page_url).content
        current_page = re.search(r'#777777;"\s+href="\?page=(\d+)', content).group(1)
        if str(page) == current_page:
            id_list = re.findall(r'poc-\d+-\d+', content)
            for id in id_list:
                filename = 'poc/%s.py' % id
                if os.path.isfile(filename):
                    pass
                else:
                    poc_url = 'http://www.beebeeto.com/pdb/%s/' % id
                    html = HTMLParser.HTMLParser()
                    r = requests.get(poc_url, headers=headers).content
                    poc_code = re.search(r'<pre\sclass="brush:\spython;">([^<]+)', r)
                    if poc_code:
                        poc = poc_code.group(1)
                        poc = html.unescape(poc.decode('utf-8'))
                        with open(filename, 'w') as fd:
                            fd.write(poc.encode('utf-8').strip())
                            print '[+]%s Succeed' % id
                    else:
                        print '[-]%s Failed' % id
            page += 1
        else:
            print '[+]Done'
            break
def main():
    if len(sys.argv) < 2:
        down_poc(cookie='')
    else:
        down_poc(cookie=sys.argv[1])

if __name__ == '__main__':
    main()