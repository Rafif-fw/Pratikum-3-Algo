# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:06:47 2022

@author: Rafif Fernanda
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:06:47 2022

@author: Rafif Fernanda
"""

s1=int(input("masukan garis satu="))
s2=int(input("masukan garis dua="))
s3=int(input("masukan garis tiga="))

if s1 == s2 == s3 :
    print("segitiga sama sisi")
elif s1 == s2 != s3 or s1 != s2 == s3 or s1 == s3 != s2 :
    print("segitiga sama kaki")
else :
    print("segitiga sembarang")
    

    