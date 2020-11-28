import sys

user1 = input("What is your name?: ")
user2 = input("And your name?:")
user1_answer = input("%s, Do you want to choose Rock , paper or scissor?:" % user1)
user2_answer = input("%s, Do you want to choose Rock , paper or scissor?:" % user2)

def compare(u1,u2):
    if u1 == u2:
        return ("Its a Tie")
    elif u1 == 'rock':
        if u2 == 'scissor':
            return(user1,"Wins!")
        else:
            return (user2, "Wins!")
    elif u1 == 'scissor':
        if u2 == 'paper':
            return (user1, "Wins!")
        else:
            return (user2, "Wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return (user1, "Wins!")
        else:
            return (user2, "Wins!")

    else:
        return("Invalid input, Try again")
        sys.exit()

print(compare(user1_answer,user2_answer))
