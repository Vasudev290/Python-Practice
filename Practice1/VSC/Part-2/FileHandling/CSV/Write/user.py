import csv #firsst step
fp=open('user.csv','w',newline="")
csv_obj=csv.writer(fp)   #second step

csv_obj.writerow(["id","Name","Gender","Email"])
csv_obj.writerow(["101","Vasu","Male","vasu@gmail.com"])
csv_obj.writerow(["102","Chaithanya","Male","Chaithanya@gmail.com"])
csv_obj.writerow(["103","Harish","Male","Harish@gmail.com"])  #Insert data in list method third step
csv_obj.writerow(["104","Siva","Male","siva@gmail.com"])  #Insert data in list method third step



fp.close()