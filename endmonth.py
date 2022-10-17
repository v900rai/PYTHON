salary = int(input('enter the salary of the employee'))
no_of_days_worked = int(input('enter the no day employee has worked'))
no_of_days_working_days=22
per_day_salary=salary/30
ot=0
lop=0
if (no_of_days_working_days -2) > no_of_days_worked:
    no_of_day_not_worked = (no_of__working_day - 2) - no_of_days_worked
    lop = no_of_day_not_worked * per_day_salary

elif no_of_days_worked > no_of_days_working_days:
    extra_day =   no_of_days_worked - no_of_days_working_days
    ot = 2 * extra_day * per_day_salary
    
salary = salary + ot - lop
print(f'salary of the employee is{salary}')