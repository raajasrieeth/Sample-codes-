#saving directory:C:\users\kavitha
import json#javascript object notation
with open("txt.json","w") as f:
	f.write("The previous data has been overwritten")
data='{"var1":"name","var2":45}'#string in json
#to parse data
parse_ex=json.loads(data)#converts json form to python
print(parse_ex)
#as it is now parsed, we can locate variable value with name itself,not possible in var-data,as class=str
print(parse_ex["var1"])
print(type(parse_ex))#dict
#json.load function:
data_ex2={"name1":"example name",
"cars_ex":["bmw","audi","ford"],
"tuple_ex":("item1","item2")
}
#note load method loads a file into a python obj,'loads' loads a string to an object
#similarly,'dumps 'method converts to a json string, 'dump ' to a json file
with open('txt.json') as f:
    data=json.load(f)    #loads file
print(file_data)
#modify the files:
for i in file_data:
	del  file_data["cars_ex"]
f.close()
#dump it in 
with open("txt.json",'w') as f:
	json.dump(data)#input to dump method
#to make this dict to a json,
jscomp=json.dumps(data_ex2,indent=1,sort_keys=True)#converts to js compatible object from python.
#'indent' method provides indentation,'sort_keys' sorts the keys of the dictionary alphbetically
print(jscomp)

#learn more about json module,helps in web development
"""table of json types to python types:
JSON:				PYTHON:
object				dict
array				list
string				str
number(int) 		int
number(real)		float
true				True
false				False
null				none
"""





