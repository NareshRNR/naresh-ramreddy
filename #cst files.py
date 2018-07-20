#csv files#cmma separated values#
#it is like a spreadsheet
#teja=open("sample.csv","w")
#teja.close()
import csv
def pen(fileobj,data):
#print(fileobj)
#print(data)
#print(type(fileobj))
#print(type(data))
   csv_writer=csv.writer(fileobj,delimiter=',')  
   for a in data:
      csv_writer.writerow(a) 
if __name__ == '__main__':
   fileobj= open('details.csv','w')
   data=['Name,class,phno,adress'.split(','),
          'batman,python,455535,usa'.split(','),
           'superman,python,78673376,pakistan'.split(','),
             'ironman,iot,5364554,bangladesh'.split(',')]                                                                                          
   pen(fileobj,data)         


#to read the file#
 #def read(fileobj)
      #csv_reader=csv.reader(fileobj,delimiter=','0)
      #for row in csv_reader:
      #	print(row)
      	#fileobj=open('details.csv','r')
      	#read(fileobj)
#dictreader()