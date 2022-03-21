
'''
======================================================================================================
In this programming, an object oriented model is designed for a restaurant employee management system.
A restaurant can have cooks, sous-chefs, chefs, servers, janitors, and managers.  Various
abstract data types are created to model the relationships among these occupations. 

======================================================================================================

'''

#create an Empolyee class as a parent class using key word "class":
class Employee:
    def __init__(self,name,address,telephone,ssn,bank_account):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.ssn = ssn
        self.bank_account = bank_account
        
    #setters for each elements in Employee objects:
    def set_name(self,name):
        self.name=name
    def set_address(self,address):
        self.address=address
    def set_telephone(self,telephone):
        self.telephone=telephone
    def set_ssn(self,ssn):
        self.ssn=ssn
    def set_bank_account(self,bank_account):
        self.bank_account=bank_account
        
    #getters for each elements in Employee objects:
    def get_name(self):
        return self.name #Output of print:Liam Cruz
#Note above: return 'name is: ' + self.name -->It also works. Output:name is:  Liam Cruz
#However,    return 'name is: ' , self.name -->It is not good. Output:('name is:  ', 'Liam Cruz')
    def get_address(self):
        return self.address
    def get_telephone(self):
        return self.telephone
    def get_ssn(self):
        return self.ssn
    def get_bank_account(self):
        return self.bank_account

#create a Cook class, Cook class inherits the Employee class and all of its properties and methods.
#To inherits the Employee class, put "Employee" in the parentheses as the argument of Cook.
class Cook(Employee):
    def __init__(self,name,address,telephone,ssn,bank_account,year_of_experience):
        Employee.__init__(self,name,address,telephone,ssn,bank_account)
        self.year_of_experience=year_of_experience
        
    def set_year_of_experience(self,year_of_experience):
        self.year_of_experience=year_of_experience
    def get_year_of_experience(self):
        return self.year_of_experience

'''
Define Sous_Chef class which inherits the Cook class and all of its properties and methods.
In addition, the Sous_Chef class will have the following properties: institution attended and
speciality. Ensure that this class has a constructor and instance methods to get and set these
properties. 
'''
class Sous_Chef(Cook):
    def __init__(self,name,address,telephone,ssn,bank_account,year_of_experience,institution,speciality):
        Cook.__init__(self,name,address,telephone,ssn,bank_account,year_of_experience)
        self.institution=institution
        self.speciality=speciality
    def set_institution(self,institution):
        self.institution=institution
    def set_speciality(self,speciality):
        self.speciality=speciality
    def get_institution(self):
        return self.institution
    def get_speciality(self):
        return self.speciality

'''
Define a Chef class which inherits the Sous_Chef class and all of its properties and methods.
In addition, the Chef class will have the following properties: number of awards and number of
tv shows featured on. Ensure that this class has a constructor and instance methods to get and
set these properties. 
'''
class Chef(Sous_Chef):
    def __init__(self,name,address,telephone,ssn,bank_account,year_of_experience,institution,speciality,number_of_awards,number_of_shows):
        self.number_of_awards=number_of_awards
        self.number_of_shows=number_of_shows
        Sous_Chef.__init__(self,name,address,telephone,ssn,bank_account,year_of_experience,institution,speciality)
    def set_number_of_awards(self,number_of_awards):
        self.number_of_awards=number_of_awards
    def set_number_of_shows(self,number_of_shows):
        self.number_of_shows=number_of_shows
    def get_number_of_awards(self):
        return self.number_of_awards
    def get_number_of_shows(self):
        return self.number_of_awards


#create a Person class as a parent class:
class Person:
    def __init__(self,name,address,telephone,ssn,bank_account):
        self.name=name
        self.address=address
        self.telephone=telephone
        self.ssn=ssn
        self.bank_account=bank_account
    def set_name(self,name):
        self.name=name
    def set_address(self,address):
        self.address=address
    def set_telephone(self,telephone):
        self.telephone=telephone
    def set_ssn(self,ssn):
        self.ssn=ssn
    def set_bank_account(self,bank_account):
        self.bank_account=bank_account
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_telephone(self):
        return self.telephone
    def get_ssn(self):
        return self.ssn
    def get_bank_account(self):
        return self.bank_account    

'''
Define a Server class which inherits the Person class and all of its properties and methods.
In addition, the Server class will have the following properties: years of experience,
number of positive feedback, and number of complaints. Ensure that this class has a constructor
and instance methods to get and set these properties. 
'''
class Server(Person):
    def __init__(self,name,address,telephone,ssn,bank_account,year_of_experience,number_of_positive_feedback,number_of_complaints):
        self.year_of_experience=year_of_experience
        self.number_of_positive_feedback=number_of_positive_feedback
        self.number_of_complaints=number_of_complaints
        Person.__init__(self,name,address,telephone,ssn,bank_account)
    def set_year_of_experience(self,year_of_experience):
        self.year_of_experience=year_of_experience
    def set_number_of_positive_feedback(self,number_of_positive_feedback):
        self.number_of_positive_feedback=number_of_positive_feedback
    def set_number_of_complaints(self,number_of_complaints):
        self.number_of_complaints=number_of_complaints
    def get_year_of_experience(self):
        return self.year_of_experience
    def get_number_of_positive_feedback(self):
        return self.number_of_positive_feedback
    def get_number_of_complaints(self):
        return self.number_of_complaints

'''
Define a Janitor class which inherits the Person class and all of its properties and methods.
In addition, the Janitor class will have the following properties: years of relevant experience
and maintenance training. Ensure that this class has a constructor and instance methods to get
and set these properties. 
'''
class Janitor(Person):
    def __init__(self,name,address,telephone,ssn,bank_account,year_of_experience,maintenance_training):
        self.year_of_experience=year_of_experience
        self.maintenance_training=maintenance_training
        Person.__init__(self,name,address,telephone,ssn,bank_account)
    def set_year_of_experience(self,year_of_experience):
        self.year_of_experience=year_of_experience
    def set_maintenance_training(self,maintenance_training):
        self.maintenance_training=maintenance_training
    def get_year_of_experience(self):
        return self.year_of_experience
    def get_maintenance_training(self):
        return self.maintenance_training

'''
Define a Manager class which inherits the Person class and all of its properties and methods.
In addition, the Manager class will have the following properties: years of relevant experience,
tertiary degree, and number of employees managed. Ensure that this class has a constructor and
instance methods to get and set these properties. 
'''
class Manager(Person):
    def __init__(self,name,address,telephone,ssn,bank_account,year_of_experience,tertiary_degree,number_of_employees):
        self.year_of_experience=year_of_experience
        self.tertiary_degree=tertiary_degree
        self.number_of_employees=number_of_employees
        Person.__init__(self,name,address,telephone,ssn,bank_account)
    def set_year_of_experience(self,year_of_experience):
        self.year_of_experience=year_of_experience
    def set_tertiary_degree(self,tertiary_degree):
        self.tertiary_degree=tertiary_degree
    def set_number_of_employees(self,number_of_employees):
        self.number_of_employees=number_of_employees
    def get_year_of_experience(self):
        return self.year_of_experience
    def get_tertiary_degree(self):
        return self.tertiary_degree
    def get_number_of_employees(self):
        return self.number_of_employees



'''
Create one object of each class and initialize the class properties using the constructors.
Then, for each object, call ALL of the getter methods and print the values returned by such. 
Thereafter, for each object, reset the properties using the setter methods and then print them
again using getter methods. 

'''
if __name__=="__main__":
    
    e1=Employee('Liam Cruz','1 Broadway','1234567890','111223333','12334455') 
    print("Employee object before resetting: ")
    print("Name: ", e1.get_name()) # print(e1.get_name()) = print(e1.name)
    print("Address: ",e1.get_address())
    print("telephone number: ",e1.get_telephone())
    print("Social Security Number: ",e1.get_ssn())
    print("Account Number: ",e1.get_bank_account())
    print()
    
    e1.set_name('Noah Cruz')
    e1.set_address('1 Hadson Street')
    e1.set_telephone('2234567890')
    e1.set_ssn('211223333')
    e1.set_bank_account('22334455')
    print("Employee object after resetting:")
    print("Name: ",e1.get_name())
    print("Address: ",e1.get_address())
    print("telephone number: ",e1.get_telephone())
    print("Social Security Number: ",e1.get_ssn())
    print("Bank Account Number: ",e1.get_bank_account())
    print()
    
    
    
    
    
    c1=Cook('Oliver Wu','3 Broadway','3234567890','311223333','32334455','3')
    print("Cook object before resetting: ")
    print("Name: ", c1.get_name())
    print("Address: ",c1.get_address())
    print("telephone number: ",c1.get_telephone())
    print("Social Security Number: ",c1.get_ssn())
    print("Account Number: ",c1.get_bank_account())
    print("Years of experience: ",c1.get_year_of_experience())
    print()
    
    c1.set_name('Elijiah Wu')
    c1.set_address('4 Broadway')
    c1.set_telephone('4234567890')
    c1.set_ssn('411223333')
    c1.set_bank_account('42334455')
    c1.set_year_of_experience('4')
    print("Cook object after resetting:")
    print("Name: ",c1.get_name())
    print("Address: ",c1.get_address())
    print("telephone number: ",c1.get_telephone())
    print("Social Security Number: ",c1.get_ssn())
    print("Bank Account Number: ",c1.get_bank_account())
    print()


    
    
    
    s1=Sous_Chef('Emma Wang','5 Broadway','5234567890','511223333','52334455','5','Apple Company','frying')
    print("Sous_Chef object before resetting: ")
    print("Name: ", s1.get_name())
    print("Address: ",s1.get_address())
    print("telephone number: ",s1.get_telephone())
    print("Social Security Number: ",s1.get_ssn())
    print("Bank Account Number: ",s1.get_bank_account())
    print("Years of experience: ",s1.get_year_of_experience())
    print("Institutions worked: ",s1.get_institution())
    print("Speciality: ",s1.get_speciality())
    print()
    
    s1.set_name('Emma Wu')
    s1.set_address('6 Broadway')
    s1.set_telephone('6234567890')
    s1.set_ssn('611223333')
    s1.set_bank_account('62334455')
    s1.set_year_of_experience('6')
    s1.set_institution('Google Company')
    s1.set_speciality('Steaming')
    print("Sous_Chef object after resetting:")
    print("Name: ",s1.get_name())
    print("Address: ",s1.get_address())
    print("Telephone number: ",s1.get_telephone())
    print("Social Security Number: ",s1.get_ssn())
    print("Bank Account Number: ",s1.get_bank_account())
    print("Years of experience: ",s1.get_year_of_experience())
    print("Institutions worked: ",s1.get_institution())
    print("Speciality: ",s1.get_speciality())
    print()


    
    
    chef1=Chef('Chef Wong','1 Chef Road','chef telephone 1','chef ssn 1','chef bank account 1',15,'Chef Institution 1','Chef speciality 1',12,16)
    print("Chef object before resetting: ")
    print("Name:",chef1.get_name())
    print("Address:",chef1.get_address())
    print("Telephone number",chef1.get_telephone())
    print('Social Security Number:',chef1.get_ssn())
    print('Bank Account Number:',chef1.get_bank_account())
    print('Years of relevant experience: ',chef1.get_year_of_experience())
    print('Institution attended: ',chef1.get_institution())
    print('Speciality: ',chef1.get_speciality())
    print('number of awards: ',chef1.get_number_of_awards())
    print('number of shows: ',chef1.get_number_of_shows())
    print()
    
    chef1.set_name('Chef Wu')
    chef1.set_address('2 Chef Road')
    chef1.set_telephone('chef telephone 2')
    chef1.set_ssn('chef ssn 2')
    chef1.set_bank_account('chef bank account 2')
    chef1.set_year_of_experience(25)
    chef1.set_institution('Chef Institution 2')
    chef1.set_speciality('Chef speciality 1')
    chef1.set_number_of_awards(22)
    chef1.set_number_of_shows(26)
    print("Chef object after resetting: ")
    print("Name:",chef1.get_name())
    print("Address:",chef1.get_address())
    print("Telephone number",chef1.get_telephone())
    print('Social Security Number:',chef1.get_ssn())
    print('Bank Account Number:',chef1.get_bank_account())
    print('Years of relevant experience: ',chef1.get_year_of_experience())
    print('Institution attended: ',chef1.get_institution())
    print('Speciality: ',chef1.get_speciality())
    print('number of awards: ',chef1.get_number_of_awards())
    print('number of shows: ',chef1.get_number_of_shows())
    print()
    
    
    
    
    p1=Person('Person Wong ','1 Person Road','Person telephone 1','Person ssn 1','Person bank account 1')
    print("Person object before resetting: ")
    print("Name:",p1.get_name())
    print("Address:",p1.get_address())
    print("Telephone number:",p1.get_telephone())
    print("Social Security Number:",p1.get_ssn())
    print("Bank Account Number:",p1.get_bank_account())
    print()
    
    p1.set_name('Person Wu')
    p1.set_address('2 Person Road')
    p1.set_telephone('Person telephone 2')
    p1.set_ssn('Person ssn 2')
    p1.set_bank_account('Person bank account 2')
    print("Person object after resetting: ")
    print("Name:",p1.get_name())
    print("Address:",p1.get_address())
    print("telephone number:",p1.get_telephone())
    print("Social Security Number:",p1.get_ssn())
    print("Bank Account Number:",p1.get_bank_account())
    print()
    


    
    s1=Server('Server Wong','1 Server Road','Server telephone 1','Server ssn 1','Server bank account 1',11,12,1)
    print('Server object before resetting: ')
    print('Name:',s1.get_name())
    print('Address:',s1.get_address())
    print('Telephone number:',s1.get_telephone())
    print('Social Security Number:',s1.get_ssn())
    print('Bank Account Number:',s1.get_bank_account())
    print('Years of relevant experience:',s1.get_year_of_experience())
    print('Number of Positive feedback: ',s1.get_number_of_positive_feedback())
    print('Number of complaintslaints:',s1.get_number_of_complaints())
    print()
    
    s1.set_name('Server Wu')
    s1.set_address('2 Server Road')
    s1.set_telephone('Server telephone 2')
    s1.set_ssn('Server ssn 2')
    s1.set_bank_account('Server bank account 2')
    s1.set_year_of_experience(21)
    s1.set_number_of_positive_feedback(22)
    s1.set_number_of_complaints(2)
    print('Server object after resetting: ')
    print('Name:',s1.get_name())
    print('Address:',s1.get_address())
    print('Telephone number:',s1.get_telephone())
    print('Social Security Number:',s1.get_ssn())
    print('Bank Account Number:',s1.get_bank_account())
    print('Years of relevant experience:',s1.get_year_of_experience())
    print('Number of Positive feedback:',s1.get_number_of_positive_feedback())
    print('Number of complaints:',s1.get_number_of_complaints())
    print()
    
    
    
    
    j1=Janitor('Janitor Wong','1 Janitor Road','Janitor telephone 1','Janitor ssn 1','Janitor bank account 1',3,'Yes')
    print('Janitor object before resetting: ')
    print('Name:',j1.get_name())
    print('Address:',j1.get_address())
    print('Telephone number: ',j1.get_telephone())
    print('Social Security Number:',j1.get_ssn())
    print('Bank Account Number:',j1.get_bank_account())
    print('Years of relevant experience:',j1.get_year_of_experience())
    print('Maintenance training:',j1.get_maintenance_training())
    print()
    
    j1.set_name('Janitor Wu')
    j1.set_address('2 Janitor Road')
    j1.set_telephone('Janitor telephone 2')
    j1.set_ssn('Janitor ssn 2')
    j1.set_bank_account('Janitor bank account 2')
    j1.set_year_of_experience(4)
    j1.set_maintenance_training('No')
    print('Janitor object after resetting: ')
    print('Name: ',j1.get_name())
    print('Address: ',j1.get_address())
    print('Telephone number: ',j1.get_telephone())
    print('Social Security Number:',j1.get_ssn())
    print('Bank Account Number:',j1.get_bank_account())
    print('Years of relevant experience:',j1.get_year_of_experience())
    print('Maintenance training:',j1.get_maintenance_training())
    print()
    
    
    
    
    m1=Manager('Manager Wong','1 Manager Road ','Manager telephone 1','Manager ssn 1','Manager bank account 1',5,'Master',66)
    print('Manager object before resetting: ')
    print('Name:',m1.get_name())
    print('Address:',m1.get_address())
    print('telephone number:',m1.get_telephone())
    print('Social Security Number:',m1.get_ssn())
    print('Bank Account Number:',m1.get_bank_account())
    print('Years of relevant experience:',m1.get_year_of_experience())
    print('Tertiary degree:',m1.get_tertiary_degree())
    print('Number of employees managed:',m1.get_number_of_employees())
    print()
    
    m1.set_name('Manager Wu')
    m1.set_address('2 Manager Road')
    m1.set_telephone('Manager telephone 2')
    m1.set_ssn('Manager ssn 2')
    m1.set_bank_account('Manager bank account 2')
    m1.set_year_of_experience(5.5)
    m1.set_number_of_employees(68)
    print('Manager object after resetting: ')
    print('Name:',m1.get_name())
    print('Address:',m1.get_address())
    print('telephone number:',m1.get_telephone())
    print('Social Security Number:',m1.get_ssn())
    print('Bank Account Number:',m1.get_bank_account())
    print('Years of relevant experience:',m1.get_year_of_experience())
    print('Tertiary degree:',m1.get_tertiary_degree())
    print('Number of employees managed:',m1.get_number_of_employees())
    print()
    
