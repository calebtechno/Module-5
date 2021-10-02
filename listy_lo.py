if __name__ == "__main__":

    food = ['beans', 'rice']
    
    food_addition = ['bread', 'pizza']

    food.append('broccoli')

    food.extend(food_addition)

    print(food[0:2])

    print(food[-1])

    breakfast = "eggs, fruit, orange juice"

    listy = breakfast.split(",")

    print(listy)

    print(len(listy))
    
    try:
        user_numbers = []

        while True:
            user_numbers.append(float(input("Type in number then type stop when finished : ")))
            average = sum(user_numbers) / len(user_numbers)
    except:
                print("Your average is : ", average)
                print("Your minimum is : ", min(user_numbers))
                print("Your maximum is : ", max(user_numbers))