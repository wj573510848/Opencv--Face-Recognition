# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:10:26 2016

@author: Administrator
"""

import cv2
import os

def generate(filepath,size=None):
    #filepath:采集样本放置的目录。size：采集后的图片保存的大小。
    if not os.path.exists(filepath):
        print "目录不存在，创建新目录:%s" % filepath 
        os.mkdir(filepath)        
    
    #定义人脸识别分类器。需要将opencv目录下data/haarcascades复制到当前目录下。
    face_detect=cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    camera=cv2.VideoCapture(0)
    count=0
    while (True):
        ret,frame=camera.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_detect.detectMultiScale(gray,1.3,5)
        
        for (x,y,w,h) in faces:
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            if size is not None:
                f=cv2.resize(gray[y:y+h,x:x+w],size)
            else:
                f=gray[y:y+h,x:x+w]
            cv2.imwrite('{0}\{1}.pgm'.format(filename,str(count)),f)
            count+=1
        
        cv2.imshow('mywindow',frame)
    
        if cv2.waitKey(1000/12) & 0xff==ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    filename=r'./test'
    generate(filename)

        