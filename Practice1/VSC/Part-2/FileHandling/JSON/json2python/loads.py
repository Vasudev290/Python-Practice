#Convert into json data to python

import json
emp_json='''{"eid":101,"ename":"Vasu","esal":"45000","avail":true}'''

emp_dict =json.loads(emp_json)
print(emp_json)   #{"eid":101,"ename":"Vasu","esal":"45000","avail":true}
print(emp_dict)   #{'eid': 101, 'ename': 'Vasu', 'esal': '45000', 'avail': True} 