import os
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  filename.py
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

filepath = input("Please enter your new files name ")


filepath = os.path.join('/home/omer/',filepath)
if not os.path.exists('/home/omer/'):
	os.makedirs('/home/omer/')

f =open(filepath , "a")	


with open(filepath , 'a') as file:
	user_input= input("enter your data")
	while user_input != "":
		user_input= input('enter your data ')
		file.write(user_input)
		
	
