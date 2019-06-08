johnsAge = 30
jenniesAge = 30

print(johnsAge, hex(id(johnsAge)))
print(jenniesAge, hex(id(jenniesAge)))

# Copy Operation : Not Data Copy but Reference Copy

jacksAge = johnsAge
print(jacksAge, hex(id(jacksAge)))