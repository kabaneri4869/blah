import pandas as pd
import xml.etree.ElementTree as ET

cols=["name","phone","gender"]
rows=[]

tree=ET.parse('Company.xml')
root=tree.getroot()

for elem in root:
    name = elem.find('name').text

    phone = elem.find('phone').text

    gender = elem.find('gender').text

rows.append({"name":name,"phone":phone,"gender":gender})

df = pd.DataFrame(rows,columns=cols)
df.to_csv('employee.csv',index=False)

print("XML to CSV format")
emp = pd.read_csv('employee.csv')
print(emp)
print('Done')
