import random
choices=['r','s','p']
moves_count={'r':0,'s':0,'p':0} #keeps track of how many times each move has been played
emoji={'r':'🪨 (Rock)','s':'✂️ (Scissors)','p':'📄 (Paper)'}
user_score=0
computer_score=0
user_last_move=random.choice(choices) # Initially setting the user's last move randomly

def play(user_input,computer_input,user_score,computer_score):
    if (computer_input=='r' and user_input=='s') or (computer_input=='s' and user_input=='p') or (computer_input=='p' and user_input=='r'):
        print('😢 You Lost')
        computer_score+=1
    elif computer_input==user_input:
        print("It's a TIE")
    else:
        print('🎉 YOU WON')
        user_score+=1
    return user_score,computer_score
def counter_move(move):
    if move=='p':
        return 's'
    elif move=='s':
        return 'r'
    else:
        return 'p'
def computer_move(user_last_move,mode):
    if mode=='e': # Easy Mode: 60% counter user's last move, 40% random
        if random.random() < 0.6:
            return counter_move(user_last_move)
        else:
            return random.choice(choices)
    else: # Hard Mode: 70% counter the most frequent move, 30% random
        if random.random() < 0.7:
            max_count=max(moves_count.values())# Get the highest move count
            if max_count==0: # If all moves have 0 count
                return random.choice(choices)
            most_frequent_moves=[move for move,count in moves_count.items() if count==max_count ] # Find all moves with the highest count
            frequent_move=random.choice(most_frequent_moves) # Randomly select one if multiple moves are equally frequent
            return counter_move(frequent_move)
        else:
            return random.choice(choices)

    
mode=''
while mode not in ['e','h']:
    mode=input("Choose difficulty (e = Easy, h = Hard): ").strip().lower()
    if mode not in ['e','h']:
        print("Invalid choice, please enter 'e' for Easy or 'h' for Hard.")
while True:
    user_input=str(input("Enter r for Rock 🪨 , p for Paper 📄, s for Scissors ✂️ (or q to quit):")).lower()
    if user_input=='q':
        break
    if user_input not in choices:
        print("Invalid input,try again!")
        continue
    print("You chose",emoji[user_input])
    computer_input=computer_move(user_last_move,mode)
    moves_count[user_input]+=1 # Update move count after computer picks
    print("Computer chose ",emoji[computer_input])
    user_score,computer_score=play(user_input,computer_input,user_score,computer_score)
    user_last_move=user_input

print("\nGame Over!\nYOUR SCORE:", user_score, "| COMPUTER SCORE:", computer_score)





            

            

