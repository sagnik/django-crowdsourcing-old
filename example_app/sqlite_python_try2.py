#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import glob
import os

con = None
tnm="crowdsourcing_question"

filelist=[]

for r,d,f in os.walk("example_app/media/imgcxs/"):
    for files in f:
        if files.endswith(".jpeg"):
             filelist.append(files.split('.')[0])

qid=7;
sid="4"
counter=0;
#tnm+="(id,survey_id,fieldname,question,label,help_text,required,order,option_type,numeric_is_int,options,map_icons,answer_is_public,use_as_filter)"

print tnm
try:
    con = lite.connect('dev.db')
    with con:
     for fitem in filelist:
      #insert command start 
      insrtcmd='INSERT INTO '+tnm+' VALUES('

      #increment question id
      qid+=1
      idstr=str(qid)
      insrtcmd+='"'+idstr+'",'

      #surveyid is fixed
      insrtcmd+='"'+sid+'",'

      #field name is similar to qid
      counter+=1
      contstr=str(counter)
      insrtcmd+='"q'+contstr+'",'

      #question is the image file name, barring location (given in forms.py)
      insrtcmd+='"'+fitem+'",'

      #label is the field name
      insrtcmd+='"q'+contstr+'",'

      #help_text is the location of the caption file
      insrtcmd+='"/home/szr163/itagct/caption_'+fitem+'.txt",'
     
      #all questions need to be answered, required 1
      insrtcmd+='"'+'1'+'",'

      #order is same as counter
      insrtcmd+='"'+contstr+'",'

      #option_type is char
      insrtcmd+='"'+'char'+'",'

      #numeric_is_int=1
      insrtcmd+='"'+'1'+'",'

      #options are nothing, NA
      insrtcmd+='"'+'NA'+'",'

      #map_icons are nothing, NA
      insrtcmd+='"'+'NA'+'",'

      #answer_is_public=1
      insrtcmd+='"'+'1'+'",'
      
      #use_as_filter=0 : This is the end of insrtcmd
      insrtcmd+='"'+'0'+'")'
           
      cur = con.cursor()    
#      insertcommand="7","4","q5","a807462c-4","q5","/home/szr163/b206201a-2.txt","1","4","char","1","null","null","1","0")';
      print "executing query number: "+contstr
      cur.execute(insrtcmd)   
#      data = cur.fetchone()
    
    
except lite.Error, e:
    
    print "Error %s: "% e.args[0]
    sys.exit(1)
    



finally:
    
    if con:
        con.close()

