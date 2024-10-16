from employee import Employee

first_n = "nikhil"
last_n = "kapoor"
ann_sal = 30_000

my_employee = Employee(first_n, last_n, ann_sal)

my_employee.print_employee()

my_employee.give_raise(90_000)

my_employee.print_employee()

