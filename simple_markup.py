import sys,re
from util import *

print '<html><head><title>this is my first substring document</title><boby>'

title=True
for block in blocks(sys.stdin):
    blocks=re.sub(r'\*(.+?)\*',r'<em>\l</em>',block)
    if title:
        print '<hl>'
        print block
        print '</hl>'
        title=False
    else:
        print'<p>'
        print block
        print '</p>'
print '</boby><html>'