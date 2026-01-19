import sys
if len(sys.argv)<4:
    print("\n usage:python salary_caluculator.py <name> <basicsalary> <bonus in percentage> <tax percentage> \n")
    sys.exit() # to terminate program exeuction safely

name=sys.argv[1]
basic=float(sys.argv[2])
bonus_percent=float(sys.argv[3])
tax_percent =float(sys.argv[4])

bonus=(bonus_percent/100) * basic
tax=(tax_percent/100) * basic
net_salary=basic + bonus - tax

print("Employee name :",name)
print("basic salary :",basic)
print("bonus(%) :",bonus_percent)
print("Tax(%) :",tax_percent)
print("Take home salary",net_salary)




