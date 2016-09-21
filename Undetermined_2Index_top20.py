#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys

def searchIndex(f):
    if '.fastq.gz' in f:
        if 'L00' in f:
            os.system("gunzip -c %s | sed -n '/@ST-E/p' | awk -F \":\" '{print $10}' | awk -F \"+\" '{print $1}' > Undetermined_Index" % f)
        else:
            os.system("gunzip -c %s | sed -n '/@NS500713/p' | awk -F \":\" '{print $10}' | awk -F \"+\" '{print $1}' > Undetermined_Index" % f)
    elif '.fastq' in f:
        if 'L00' in f:
            os.system("sed -n '/@ST-E/p' %s | awk -F \":\" '{print $10}' | awk -F \"+\" '{print $1}' > Undetermined_Index" % f)
        else:
            os.system("sed -n '/@NS500713/p' %s | awk -F \":\" '{print $10}' | awk -F \"+\" '{print $1}' > Undetermined_Index" % f)
    os.system("sort -o Undetermined_Index_sort Undetermined_Index")
    os.system("uniq -c Undetermined_Index_sort > Undetermined_Index_sort_uniq")
    os.system("sort -n -r -o Undetermined_Index_sort_uniq_sort Undetermined_Index_sort_uniq")
    os.system("sed -n '1,20p' Undetermined_Index_sort_uniq_sort > %s_Undetermined_Index_top20.txt" % f)

    os.system("rm -rf Undetermined_Index Undetermined_Index_sort Undetermined_Index_sort_uniq Undetermined_Index_sort_uniq_sort ")

def main():
    f = sys.argv[1]
    searchIndex(f)

if __name__ == "__main__":
    main()