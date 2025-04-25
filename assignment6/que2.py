import random,time
class rosk_paper_scissors:
    def __init__(self,rounds):
        self.total_rounds=rounds
        self.current_round=1
        self.player_score=0
        self.computer_score=0
    def start_game(self):
        while(self.current_round<=self.total_rounds):
            print("="*20)
            print("round: ",self.current_round)
            p=int(input("enter \n1.for rock\n2.for paper\n3.for scissor"))
            rps=["rock","papper","scissor"]
            c=random.choice([1,2,3])
            time.sleep(0.5)
            print(f"your choice {rps[p-1]} , computer_choice {rps[c-1]}")
            if(p==c):
                print("draw")
            elif((p==1 and c==3 )or (p==2 and c==1) or (p==3 and c==2)):
                print("you won")
                self.player_score+=1
                self.current_round+=1
            else:
                print(f"you lost")
                self.computer_score+=1
                self.current_round+=1
        print("="*20)
        print(f"final Scores\nyour score :{self.player_score}\ncomputer_score :{self.computer_score}")
        if(self.player_score>self.computer_score):
            print("Bingo you won")
        elif(self.player_score==self.computer_score):
            print("draw")
        else:
            print("you lost,computer is victorious")

game1=rosk_paper_scissors(int(input("enter the number of rounds")))
game1.start_game()