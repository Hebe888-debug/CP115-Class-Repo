num_rounds = int(input())
final_score = 0
rounds_processed = 0

for i in range (num_rounds):
    score = float(input("enter score"))
    if score > 100:
        bonus = 0.20
    else:
        bonus = 0
    num_rounds += 1
 
final_score = score + (score * bonus)

               
print(f"{final_score:.1f}")
print(rounds_processed)
