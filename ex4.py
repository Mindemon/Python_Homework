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
user_input = input("enter any number you can think of!" )
if user_input >=10:
	print(user_input)
else:
	i = user_input
	while(i <= 30):
		
		user_input = input("enter any number you can think of! ")
		if user_input > 10:
			print(user_input)
			break
		elif user_input<10:
			i=user_input+i
			continue
   
	print(i)

## Question No. 3
##arr_legenth = input("Enter your array length!")
##s1 = list();
##for arr in range(0,arr_legenth):
	##s1(arr) = input("enter value for item")
										
										
