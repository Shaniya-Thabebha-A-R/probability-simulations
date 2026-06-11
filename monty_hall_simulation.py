import random

def simulate_monty_hall(switch, trials):
    wins = 0
    
    for _ in range(trials):
        # Step 1: randomly place laptop
        car_door = random.randint(1, 3)
        
        # Step 2: you always pick box 1
        your_pick = 1
        
        # Step 3: host opens a phone box
        host_opens = random.choice(
            [d for d in [1, 2, 3] if d != your_pick and d != car_door]
        )
        
        # Step 4: switch or stay
        if switch:
            your_pick = [d for d in [1, 2, 3] if d != your_pick and d != host_opens][0]
        
        # Did you win?
        if your_pick == laptop_box:
            wins += 1
    
    return wins / trials
trials = 100000

stay_wins = simulate_monty_hall(switch=False, trials=trials)
switch_wins = simulate_monty_hall(switch=True, trials=trials)

print(f"Staying wins: {stay_wins:.2f}")
print(f"Switching wins: {switch_wins:.2f}")
