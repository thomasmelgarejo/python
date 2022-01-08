#SET- Er med curly bracket, 
# er uordnet, 
# ikke index, 
# kan ikke ændres,
# alle værdier er unikke 
directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren', 'Bo'} #board
management = {'Tine','Trunte','Rane', 'Bo'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars', 'Bo'}

#who in the board of directors is not an employee?
#MEANING remove employess from directors
directors_employees = directors.difference(employees)

#who in the board of directors is also an employee?
#MEANING keep only fællesmængden
directors_and_employees = set(directors) & set(employees)

#how many of the management is also member of the board?
#MEANING størrelse fællesmængde directors and management
number_directors_and_management = len(set(directors) & set(management))

#All members of the management also an employee
directors_and_employees = set(employees) & set(management)

#All members of the management also in the board?
directors_and_maagement = set(directors) & set(management)

#Who is an employee and member of the management and a member of the board?
directors_management_employee = set(employees) & set(directors) & set(management) 

#Who of the employee is neither a member or the board or management?
only_employee = (employees.difference(management)).difference(directors)


print(only_employee)