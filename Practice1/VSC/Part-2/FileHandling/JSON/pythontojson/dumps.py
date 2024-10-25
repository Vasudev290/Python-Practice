#Convert python to dict object;
#converting python dict to json data , using dumps method

import json
emp_dict={
    'eid': 101, 
    'ename': 'Vasu', 
    'esal': '45000', 
    'avail': True,
    'discount':None
    }

print(type(emp_dict))  #<class 'dict'>

emp_json=json.dumps(emp_dict)

print(emp_dict)   #{'eid': 101, 'ename': 'Vasu', 'esal': '45000', 'avail': True, 'discount': None}
print(emp_json)   #{"eid": 101, "ename": "Vasu", "esal": "45000", "avail": true, "discount": null}