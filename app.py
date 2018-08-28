import pandas as pd
import csv
'''
The initial conditions of the application needs a pre-defines empty csv file named "Student_Data.csv" with column names [name,age,branch,year,semester,prev_sem_score]
'''
def getStudentData():
  student_data = pd.read_csv("Student_Data.csv",index_col = False) 
  if(len(student_data) == 0):
    print("There is no data. Add some data and try again")
  return(student_data)

def addStudentData():
  name = input("Enter name")
  age = int(input("Enter age"))
  branch = input("Enter branch")
  year = int(input("Enter year"))
  semester = int(input("Enter semester"))
  prev_sem_score = float(input("Previous semester Score"))
  
  row = [name,age,branch,year,semester,prev_sem_score]

  with open('Student_Data.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)
  csvFile.close()
  


def filter_score():##Sorting data based on prev_sem_score
  student_data = getStudentData()
  if(len(student_data)!=-1):
    student_data.sort_values('prev_sem_score',ascending = False,axis = 0, inplace = True)
    print(student_data)
  
while(True):
  print("1.Add data")
  print("2.Get data")
  print("3.Show filtered data")
  print("4.Exit")
  choice = int(input("Enter Choice:"))
  if(choice == 1):
    addStudentData()
  elif(choice == 2):
    print(getStudentData())
  elif(choice == 3):
    filter_score()
  elif(choice == 4):
    break
  else:
    print("Enter valid Choice")
