a=int(input("Enter first cost"))
b=int(input("Enter second cost"))
c=int(input("Enter third cost"))
cost=a+b+c
if(cost>50):
    cost=cost-cost/10

print(cost)
