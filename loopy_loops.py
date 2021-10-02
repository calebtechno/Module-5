if __name__ == "__main__":
    
    
    Pokemon = ( 'Picachu', 'Charmander', 'Bulbasor', )
    print(Pokemon[1])

    starter1, starter2, starter3 = Pokemon

    print(starter1)

myname = 'Caleb'
name_tuple = tuple(myname)
print(name_tuple)

print("i" in myname)

for a in range(2, 11):
    print(a)

b = 2
while b < 11:
    print(b)
    b += 1
pass
simple_string = 'This is a simple string'

for string_b in range(0, len(simple_string)):
    print("\n", simple_string[string_b])

simple_set = ['this', 'is', 'a', 'simple', 'set']

for set_num in range(len(simple_set)):
    for set_num_2 in range(3):
        print(simple_set[set_num])
        
    