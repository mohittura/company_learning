course = "NLP intern course of action" 
# length 
print(len(course))

# using dot operator
print(course.upper()) # it doesnt change the original string rather create a new instance
print(course.lower())
print(course.find("N")) # sensitive to upper and lowercase characters
print(course.replace("action", "action kamen"))
print(course.title())

# in operator to return boolean value

print("NLP" in course)