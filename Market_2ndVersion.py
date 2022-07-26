import json
f = open('sample/in_01.txt', 'r')
Lines = f.readlines()

List=[]
for line in Lines:	
	company={}
	commands=line.strip().split(" ")
	company['Company Name']=commands[0]
	company['Share']=commands[1]
	company['Percentage']=commands[2]
	company['Value']=100*int(company['Percentage'])/100
	List.append(company)

def test():

	print(Company_Name)
	print()
	print(Shares)
	print()
	print(Share_values)	

def call_print():
	print(json.dumps(List, indent=4))

def output(Missing_shares,var=0.0):
	if Missing_shares: print(Company_Name[0]+" "+"?"+" "+str(int(var)))
	for i,k in zip(Shares,Share_values):
		print(Company_Name[0]+" "+i+" "+str(int(k)))


def search_dictionaries(key, value, list_of_dictionaries):
	return [element for element in list_of_dictionaries if element[key] == value]

Company_Name=[]
Shares=[]
Share_values=[]

def process():

	i=0
	while i<len(List):
		row=List[i]
		if row['Company Name'] not in Company_Name:

			 Company_Name.append(row['Company Name'])

		if row['Company Name']==Company_Name[0]:
		   Shares.append(row['Share'])
		   Share_values.append(row['Value'])
		i+=1
	
  
def process1():	    

	i=0
	while i<len(List):
		row=List[i]
		
		if row['Company Name'] in Company_Name[1:]: 

			if row['Company Name'] not in  Shares: 
				Company_Name[1:].remove(row['Company Name'])
			else:

				var=search_dictionaries("Share",row['Company Name'],List)
				row['Value']=int(var[0]['Value'])*int(row['Percentage'])/100
		
				if len(var) ==1:
					var[0]['Share']=row['Share']
					var[0]['Value']=row['Value']				
		else:
			
			pass		        
			
		i+=1


process()
#call_print()
if len(Company_Name)>1:
	[Company_Name.remove(i) for i in Company_Name[1:] if i not in Shares]

def prefix_output():
		global Missing_shares,var
		if sum(Share_values)==100.0:
			Missing_shares=False
			var=100-sum(Share_values)

		else:
			Missing_shares=True
			var=100-sum(Share_values)


if len(Company_Name)==1:
	prefix_output()
	
else:
	process1()	  
	prefix_output()  

#call_print()  
#test()  



output(Missing_shares,var)		
