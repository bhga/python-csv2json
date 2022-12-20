import csv
import json

inputpath=input("Enter the input path file:")
outputpath=input("Enter the output path file:")
dlm=input("Enter delimiter(must be a 1-character string):")

schemabody = {}

with open(inputpath,'r') as file:
    csvreader = csv.DictReader(file,delimiter=dlm)
    print("Successfully read the input file")
    print(csvreader)
    columns=[]
    for r in csvreader:
        columns.append(r)


schemabody['schema'] = columns
jsonstring=json.dumps(schemabody,indent=4)

with open(outputpath,'w') as outfile:
    outfile.write(jsonstring)

print("Successfully created the output file!!!")
