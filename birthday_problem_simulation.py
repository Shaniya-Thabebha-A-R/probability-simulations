import random

def simulate_birthday(people_in_room, trials):
    matches = 0
    my_birthday = 1  # your birthday is just day number 1
    
    for _ in range(trials):
        # generate birthdays for everyone in the room
        room = [random.randint(1, 365) for i in range(people_in_room)]
        
        # check if anyone matches YOUR birthday
        if my_birthday in room:
            matches += 1
    
    return matches / trials

# Test for different room sizes
trials = 100000
for people in [10, 50, 100, 200, 253, 300]:
    probability = simulate_birthday(people, trials)
    print(f"People: {people:3d} → Probability: {probability:.3f}")
