from __future__ import print_function
import sys

last_category = None
last_uploader=None
for line in sys.stdin:
    try:
        #category, uploader, others = line.split("\t")
        video_id, uploader, age, category, others = line.split("\t", 4)
        if category == last_category:
            if uploader!=last_uploader:
                total_uploader += 1
                last_uploader = uploader
                
        else:
            if last_category :
                print(last_category,total_uploader, sep="\t")
            last_category = category
            last_uploader = uploader
            total_uploader = 1
    except:
        continue
if last_category:
    print(last_category,total_uploader, sep="\t")
    
