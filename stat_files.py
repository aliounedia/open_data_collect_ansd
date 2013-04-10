import os
for root, dirs, files in os.walk('datas'):
    print  len(files)
