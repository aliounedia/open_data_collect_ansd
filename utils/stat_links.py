import os
with open("datas/links/link.txt") as f:
    print 'len', len(set(f.readlines()))
