# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:39:31 2016

@author: Administrator
"""

import cv2
import os
import sys
import numpy as np

def getdata(filepath,size=None):
    #将储存的图片转化为数组。
    x=[]
    y=[]
    count=0
    z=[]
    for dirname,dirnames,filenames in os.walk(filepath):
        for sub_dirname in dirnames:
            sub_path=os.path.join(filepath,sub_dirname)
            for pic_name in os.listdir(sub_path):
                path=os.path.join(sub_path,pic_name)
                img=cv2.imread(path)
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                if not(size is None):
                    gray=cv2.resize(gray,size)
                x.append(np.asarray(gray))
                y.append(count)
            z.append(sub_dirname)
            count+=1
            
    x=np.asarray(x)
    y=np.asarray(y)
    return x,y,z
    
def face_rec(filepath):
    x,y,names=getdata(filepath) 
    print names
    model=cv2.createLBPHFaceRecognizer(1,8,16,16)
    model.train(np.asarray(x),y)
    camera=cv2.VideoCapture(0)
    face_cascade=cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    while (True):
        ret,frame=camera.read()
        faces=face_cascade.detectMultiScale(frame,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            roi=gray[x:x+w,y:y+h]
            try:
                params=model.predict(roi)
                print "姓名:",params[0]
                print '自信度:',params[1]
                if params[0]==-1:
                    pass
                else:
                    cv2.putText(frame,names[params[0]],(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,1,255,2)
            except:
                print sys.exc_info()[0]
        cv2.imshow('camera',frame)
        if cv2.waitKey(1000/12) & 0xff ==ord('q'):
            break
    cv2.destroyAllWindows()
#filepath=r'./test_data'
#face_rec(filepath)             
    
    

    
    
    
    
    