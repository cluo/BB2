#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Email: lyleaks@gmail.com

import re
import os
import sys
from optparse import OptionParser
import update

def exploit(target, filter):
    poc_list = os.listdir('poc')
    for poc in poc_list:
        poc_file = 'poc/' + poc
        if poc_file.endswith('.py') and poc_file != 'poc/baseframe.py':
            if filter:
                with open(poc_file, 'r') as fd:
                    if filter.lower() in fd.read().lower():
                        exec_poc(poc, poc_file, target)                 
            else:
                exec_poc(poc, poc_file, target)
                    
def exec_poc(poc, poc_file, target):
    try:
        cmd = 'python %s -v -t %s' % (poc_file, target)
        detail = os.popen(cmd, 'r').read()
        result = re.search(r'{\'[\S\s]+}', detail).group(0)
        result = eval(result)
        print '[*]%s %s' % (os.path.splitext(poc)[0], result['success'])
    except Exception:
        pass   

def main():
    parser = OptionParser()
    parser.add_option('-t', '--target', action='store',
                      type='string', dest='target',
                      default=None,help='the target to be checked.')
    parser.add_option('-f', '--filter', action='store',
                      type='string', dest='filter', default=False,
                      help='filter CMS')
    parser.add_option('--update', action='store',
                      type='string', dest='cookie', default=False,
                      help='update poc')
    (option, args) = parser.parse_args()
    if option.cookie:
        print 'updating...'
        update.down_poc(option.cookie)
        sys.exit()
    elif not option.target:
        parser.print_help()
        sys.exit()
    else:
        exploit(option.target, option.filter)
    
    

    
if __name__ == '__main__':
    main()
