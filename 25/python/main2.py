import random

# Initialize counters for each outcome
two_heads = 0
two_tails = 0
one_of_each = 0
odd_count = 0

for _ in range(10000):
    coin1 = random.choice(['H', 'T'])  # 'H' represents heads, 'T' represents tails
    coin2 = random.choice(['H', 'T'])
  

   
    if coin1 == 'H' and coin2 == 'H':
        two_heads += 1
    elif coin1 == 'T' and coin2 == 'T':
        two_tails += 1
    else:
        one_of_each += 1
        
        
for _ in range(10000):
    # Simulate throwing a die
    outcome = random.randint(1, 6)

    # Increment the counter if the outcome is odd
    if outcome % 2 != 0:
        odd_count += 1
        
        

probability_odd = odd_count / 10000
prob_two_heads = two_heads / 10000
prob_two_tails = two_tails / 10000
prob_one_of_each = one_of_each / 10000

# Print the results
print("Probability of getting two heads:", prob_two_heads)
print("Probability of getting two tails:", prob_two_tails)
print("Probability of getting one of each:", prob_one_of_each)
print("Probability of getting an odd number:", probability_odd)

