#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ex4.py
#  
#  Copyright 2018 Omer <omer@omer-N56VM>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
## Question No. 1
y = 0
arry = [17,1,12,54,23,9,21]
for x in arry:
	if x >= 3 and x <= 20:
		y +=x




## Question No. 2
bool_var = True
sum1 = []

while bool_var == True:
	user_input = input("enter any number  you can think of ")
	sum1.append(user_input)
	if int(user_input) >= 10:
		bool_var = False
		b =0
		for a in sum1:
			b +=int(a)
		print(b)	
	else:
		c =0
		for d in sum1:
			c +=int(d)
		if c >= 30:
			bool_var = False
			print(c)	
		else:
			continue
		

## Question No. 3
arr_legenth = input("Enter your array length! ") 
s1 = [] * int(arr_legenth)
for arr in  range(int(arr_legenth)):
    ArrVal = input("enter array value! ")
    s1.append(int(ArrVal)) 
z = input("enter another random number! ")
for L in range(3,int(arr_legenth)):
	if int(s1[L]) < 5:
		s1[L]=  int(s1[L]) + int(z)
	elif s1[L] >= 6 and s1[L] <= 10:
		s1[L]=int(s1[L]) * int(z)
	elif s1[L] > 10:
		s1[L]=int(s1[L]) ** int(z)
print(s1)		 	 	 
