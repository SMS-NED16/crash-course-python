#This block of code will cause a TypeError b/c no typecasting
"""age = 23
message = "Happy " + age + "rd Birthday!"
print(message)"""

#Concatenation with str typecasting - no error
age = 23;
message = "Happy " + str(age) + "rd Birthday"
print(message)