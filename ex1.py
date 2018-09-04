#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ex1.py
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
print ("Input Digit Only!")         
var1 = input()                    ##Requesting User Input type String
print ("Input Digits Only!")
var2 = input()                    ##Requesting User Input type String
print ("Total Sum is:", int(var1)+int(var2)) # Total Sum
print ("Multiplication:" , int(var1)*int(var2)) #Multiply
print ("Division" ,float(var1)/float(var2)) #Devide
if var1 == var2 : #Check if nums are equal
	print("Nums are Equal")
	
elif var1 > var2: #Check if var1 is bigger then var2
	print(var1)
	
else:             #Printing var2 
		print (var2)



