#!/usr/bin/env python
import sys
# -*- coding: utf-8 -*-
#
#  ex2.py
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
#  

print("Enter your 1st String!")
str1 = input()
print("Enter your 2nd String")
str2 = input()
str1 == str2
print("Enter your Num between 1 and 3")      #Aquriring User Input
var1 = input()
if int(var1) > 3:
	print("Number must be between 1 and 3 TERMINATED!")  # The program will terminate if the user inputs a num greater than 3 
	sys.exit()
	
	
if str1 > str2:
	str1 == str2
	print(str1 , "is larger")  
	StrCount = len(str1) #counting the number of chars on the larger string 
	FirstChar = str2[0:1] #First char from the smaller string
	new_str = str1.replace(FirstChar ,"Omer") #Replacing the first char from the smaller string with my name  on the larger string
	MergedStr = str1+str2+str(StrCount) #Merging all 3 strings into 1
	my_count = MergedStr.count('A') #Counting the number of  occurence when the char "A" appears
	
else:
	print (str2, "is larger")
	str1 == str2
	StrCount = len(str2)
	FirstChar = str1[0:1]
	new_str = str1.replace(FirstChar ,"Omer")
	MergedStr = str1+str2+str(StrCount)
	my_count = MergedStr.count('A')
	
