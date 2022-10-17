salary = int(input ('enter the salary of the employee'))
no_of_days_worked = int(input('enter the number of day employee has worked'))
no_of__working_day = 22
ot = 0
if no_of_days_worked > no_of__working_day:
    extra_day_salary = salary / 30
    ot = 2 * extra_day * per_day_salary
    salary = salary + ot
    printf(f'salary of the employee is {salary}')