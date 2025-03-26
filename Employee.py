#Programmer: Timothy Pickering
#Date: 3/25/25
#Title: Classy employee program

class Employee:
    #Initialize an Employee object with name, ID, department, and job title
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def get_name(self):
        #Return the employee's name
        return self.__name

    def get_id_number(self):
        #Return the employee's ID number
        return self.__id_number

    def get_department(self):
        #Return the employee's department
        return self.__department

    def get_job_title(self):
        #Return the employee's job title
        return self.__job_title

    def display_info(self):
        #Display employee information
        print(f"Name: {self.__name}")
        print(f"ID Number: {self.__id_number}")
        print(f"Department: {self.__department}")
        print(f"Job Title: {self.__job_title}")
        print("-" * 30)  #Separator for readability

#Main program to create and display employee data
def main():
    #Creating three Employee objects with given data
    emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    #Display employee information
    print("Employee Details:\n")
    emp1.display_info()
    emp2.display_info()
    emp3.display_info()

#Run the program
if __name__ == "__main__":
    main()
