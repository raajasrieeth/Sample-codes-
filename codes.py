#saving directory:C:\users\kavitha
import json#javascript object notation

data='{"var1":"name","var2":45}'#string in json
#to parse data
parse_ex=json.loads(data)
print(parse_ex)
#as it is now parsed, we can locate variable value with name itself,not possible in var-data,as class=str
print(parse_ex["var1"])
print(type(parse_ex))#dict
#json.load function:
data_ex2={"name1":"example name",
"cars_ex":["bmw","audi","ford"],
"tuple_ex":("item1","item2")
}
#to make this dict to a json,
jscomp=json.dumps(data_ex2)#converts to js compatible object
#learn more about json module,helps in web development
#calc:

 







