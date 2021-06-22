# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import pymysql

# Create your views here.
def display(request):
	return render(request,'form.html')

def user(request):
	db = pymysql.connect(host='0.0.0.0',user='root',password='G0d!sgreat',database='nodejs')
	cur = db.cursor()
	name = request.GET['name']
	email = request.GET['email']
	dob = request.GET['dob']
	phone = request.GET['phone']
	q = "insert into user values (%s,%s,%s,%s)"
	t = (name,email,dob,phone,)
	cur.execute(q,t)
	db.commit()
	q1 = "select * from user"
	cur.execute(q)
	data = cur.fetchall()
	
	return render(request,'user.html',{"data":data})
