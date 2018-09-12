#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ex5.py
#  
#  Copyright 2018 omer <omer@localhost.localdomain>
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
#  get numbers from the user (one by one) into a collection until the first number that is bigger then 10 . verify that there are no two same numbers at the collection
#remove the numbers one by one and print them
## Question No.1
bolean = True 
num_list= []
while bolean == True:                ## filling the list with values
	num_val = input("enter value! ") 
	num_list.append(int(num_val))
	if int(num_val) > 10:
		bolean = False	
		new_list = set(num_list)     ## Earsing duplicates & and creating set list 
 			

while len(new_list) != 0:
	new_list.pop()              ## Emptying the the set
	print(new_list)
	
	
			
##Question No. 2
Grade_List = {'Omer':100,'Moshe':79,'Jojohalastra':19,'Dubi Zobi':56,'Naor':0} ## creating dictionary list
print(Grade_List.keys())
key_val = input("Enter the student ID from this given list: ")  ## User input the Key
print("The grade for",key_val, "is ",Grade_List[key_val])      ## Displaying the student grade 
for a in range(3):                     ## User inputs new key and values for the dictionary
	keys = input("Enter Student ID ")
	values = input("Enter Student Grade ")
	Grade_List.update({keys:int(values)})

print(Grade_List)   



