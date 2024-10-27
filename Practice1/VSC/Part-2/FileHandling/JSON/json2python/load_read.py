#load -file handlig converting json file to python file
#read emp.json data from json, print all employee names


import json
fp=open('emp.json','r')   #for handling text files, we use read modules;
emp_dict=json.load(fp)

print(emp_dict)
'''
[
{'id': 1, 'name': 'Korella', 'email': 'kballister0@xinhuanet.com', 'gender': 'Female'}, 
{'id': 2, 'name': 'Shaughn', 'email': 'sabele1@globo.com', 'gender': 'Male'}, 
{'id': 3, 'name': 'Elsy', 'email': 'efooter2@surveymonkey.com', 'gender': 'Female'}, 
{'id': 4, 'name': 'Dorita', 'email': 'dtarpey3@ameblo.jp', 'gender': 'Female'}, 
{'id': 5, 'name': 'Clim', 'email': 'cclaeskens4@mit.edu', 'gender': 'Male'}, 
{'id': 6, 'name': 'Idell', 'email': 'isimkin5@yahoo.co.jp', 'gender': 'Female'}, 
{'id': 7, 'name': 'Dane', 'email': 'dmattimoe6@howstuffworks.com', 'gender': 'Male'}, 
{'id': 8, 'name': 'Agace', 'email': 'aboules7@macromedia.com', 'gender': 'Female'}, 
{'id': 9, 'name': 'Chaim', 'email': 'ccroad8@hp.com', 'gender': 'Male'}, 
{'id': 10, 'name': 'Krishnah', 'email': 'kkingsnod9@icio.us', 'gender': 'Male'}, 
{'id': 11, 'name': 'Abagael', 'email': 'ahafnera@spiegel.de', 'gender': 'Female'}, 
{'id': 12, 'name': 'Bertha', 'email': 'braitieb@discovery.com', 'gender': 'Female'}, 
{'id': 13, 'name': 'Lynde', 'email': 'lbeavingtonc@wordpress.com', 'gender': 'Female'}, 
{'id': 14, 'name': 'Austine', 'email': 'amellingd@craigslist.org', 'gender': 'Female'}, 
{'id': 15, 'name': 'Ryon', 'email': 'rdarmodye@ihg.com', 'gender': 'Male'}, 
{'id': 16, 'name': 'Gigi', 'email': 'gsigsworthf@google.it', 'gender': 'Female'}, 
{'id': 17, 'name': 'Eben', 'email': 'ewackleyg@netscape.com', 'gender': 'Male'}, 
{'id': 18, 'name': 'Morris', 'email': 'mkopmanh@plala.or.jp', 'gender': 'Male'}, 
{'id': 19, 'name': 'Essy', 'email': 'echillingsworthi@blogs.com', 'gender': 'Female'}, 
{'id': 20, 'name': 'Dunn', 'email': 'dpalaj@bloomberg.com', 'gender': 'Male'}, {'id': 21, 'name': 'Sully', 'email': 'sbollandk@google.ca', 'gender': 'Male'}, {'id': 22, 'name': 'Immanuel', 'email': 'idamiatal@sina.com.cn', 'gender': 'Male'}, {'id': 23, 'name': 'Valera', 'email': 'vsilkstonm@ihg.com', 'gender': 'Polygender'}, {'id': 24, 'name': 'Erich', 'email': 'estronachn@telegraph.co.uk', 'gender': 'Agender'}, {'id': 25, 'name': 'Veronique', 'email': 'vbrennono@biblegateway.com', 'gender': 'Female'}, {'id': 26, 'name': 'Camella', 'email': 'cswindellsp@zdnet.com', 'gender': 'Female'}, {'id': 27, 'name': 'Alexei', 'email': 'asayesq@g.co', 'gender': 'Male'}, {'id': 28, 'name': 'Celia', 'email': 'ccharlestonr@discuz.net', 'gender': 'Female'}, {'id': 29, 'name': 'Reinaldos', 'email': 'rlaurensons@nytimes.com', 'gender': 'Male'}, {'id': 30, 'name': 'Lyn', 'email': 'lhaught@yellowpages.com', 'gender': 'Male'}, {'id': 31, 'name': 'Maureene', 'email': 'mpumfreyu@nba.com', 'gender': 'Female'}, {'id': 32, 'name': 'Bentley', 'email': 'balldisv@sbwire.com', 'gender': 'Male'}, {'id': 33, 'name': 'Dawna', 'email': 'dgrimstonw@nature.com', 'gender': 'Female'}, {'id': 34, 'name': 'Corbett', 'email': 'cgrinstonx@typepad.com', 'gender': 'Male'}, {'id': 35, 'name': 'Liliane', 'email': 'lzapatay@chicagotribune.com', 'gender': 'Female'}, {'id': 36, 'name': 'Catie', 'email': 'cvossgenz@ning.com', 'gender': 'Female'}, {'id': 37, 'name': 'Aubree', 'email': 'agottelier10@java.com', 'gender': 'Female'}, {'id': 38, 'name': 'Tandy', 'email': 'toliveira11@canalblog.com', 'gender': 'Female'}, {'id': 39, 'name': 'Tomkin', 'email': 'twallwork12@google.ca', 'gender': 'Male'}, {'id': 40, 'name': 'Rolf', 'email': 'rmalt13@technorati.com', 'gender': 'Male'}, {'id': 41, 'name': 'Gayelord', 'email': 'glyes14@home.pl', 'gender': 'Male'}, {'id': 42, 'name': 'Pail', 'email': 'peminson15@altervista.org', 'gender': 'Genderqueer'}, {'id': 43, 'name': 'Gennie', 'email': 'gforre16@thetimes.co.uk', 'gender': 'Female'}, {'id': 44, 'name': 'Rasla', 'email': 'rscandrett17@google.it', 'gender': 'Female'}, {'id': 45, 'name': 'Fonsie', 'email': 'fbandy18@miitbeian.gov.cn', 'gender': 'Male'}, {'id': 46, 'name': 'Meggi', 'email': 'mrobertot19@trellian.com', 'gender': 'Female'}, {'id': 47, 'name': 'Oona', 'email': 'okidstoun1a@slashdot.org', 'gender': 'Genderfluid'}, {'id': 48, 'name': 'Hailey', 'email': 'hgoudman1b@booking.com', 'gender': 'Male'}, {'id': 49, 'name': 'Moira', 'email': 'mmccaghan1c@cbslocal.com', 'gender': 'Female'}, {'id': 50, 'name': 'Glenna', 'email': 'gtatam1d@ucsd.edu', 'gender': 'Female'}]
'''

#print all employee names or print all employee ids,name;
for emp in emp_dict:
    print(emp['id'])
    print(emp['name'])