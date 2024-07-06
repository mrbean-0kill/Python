num_sub = int(input("Enter number of subjects in 4th sem:"))
subjects = []
for i in range(num_sub):
    sub = input("Enter subject i: ")
    subjects.append(sub)

print("Subjects in the 4th sem:\n")

print(" Printing all the subjects in the 4th sem:")
for i in range(subjects):
    print(subjects[i])

print("2nd and 5th subjects in 4th sem ",subjects[1],"and",subjects[4])
print("First 4 subjects of 4th sem:",subjects[:3])
print("Last 4 subjects of 4th sem:",subjects[-1:-4])

if "Python Programming Lab" in subjects:
    print("Yes we have")
else:
    print("Nope we don't have")

print("Demonstrating append() and insert() functions:")
new_sub = "XYZ
subjects.append(new_sub)
print("Updates subjects after appending new subject:",subjects)
new_sub1 = "ABC"
subjects.insert(new_sub1,2)
print("After inserting at index 2 updates subjectss list is:",subjects)
print("Demonstrating remove() and pop() function:")
subjects.remove(new_sub)
print("Updated subjects after removing new_subject:",subjects)
subjects.pop()
print("Updated subjects after poping subject:",subjects)