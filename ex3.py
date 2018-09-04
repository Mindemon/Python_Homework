#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ex3.py
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


arry = []
print("enter 1st string!") #User inputs 3 strings
str1 = input()
print("enter 2nd string!")
str2 = input()
print ("enter 3rd string!")
str3 = input()
arry.append(str1)   #input is appended to the list
arry.append(str2)
arry.append(str3)
arry[0] = "replaced"
arry[2] = "abra kadabra"
arry[1] = [1,2,3]
print(arry[1][2]) #second number in the inner arry

