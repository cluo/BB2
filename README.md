BB2
===

一个基于beebeeto的漏洞扫描器

```
$ python bb2.py -h

Usage: bb2.py [options]

Options:
  -h, --help            show this help message and exit
  -t TARGET, --target=TARGET
                        the target to be checked.
  -f FILTER, --filter=FILTER
                        filter CMS
  --update=COOKIE       update poc
```
###示例
```
 $ python bb2.py -t www.victim.com -f wordpress
```
> 不指定-f参数的话就使用所有poc

###更新

带cookie更新
```
 $ python bb2.py --update cookie
```
如果没cookie的话就随便null就行了
```
 $ python bb2.py --update null
```
