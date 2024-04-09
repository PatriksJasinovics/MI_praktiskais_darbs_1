import random

class AlphaBeta:
    # definē objektu, kas saturēs sakitla virkni, datora un spēlētāja punktus un to, kam ir pirmais gājiens
    def __init__(self, skaitli, datora_punkti, player_punkti, datora_gajiens):
        self.skaitli = skaitli
        self.datora_punkti = datora_punkti
        self.player_punkti = player_punkti
        self.datora_gajiens = datora_gajiens

    # veic spēlētāja vai datora gājienu, kas maina virknes sastāvu
    def make_move(self, move):
        jauna_virkne = self.skaitli.replace(move, '', 1) 
        new_state = AlphaBeta(jauna_virkne, self.datora_punkti, self.player_punkti, not self.datora_gajiens)

        # ja ir datora gājiens, tad punkti tiek atņemt no spēlētāja kopējā punktu skaita
        if self.datora_gajiens:
            if move == '1':
                new_state.datora_punkti -= 1
            elif move == '2':
                new_state.datora_punkti -= 1
                new_state.player_punkti -= 1
            elif move == '3':
                new_state.player_punkti -= 1

            return new_state
        else:
             # ja ir spēlētāja gājiens, tad punkti tiek atņemt no datora kopējā punktu skaita
            if move == '1':
                new_state.player_punkti -= 1
            elif move == '2':
                new_state.player_punkti-= 1
                new_state.datora_punkti -= 1
            elif move == '3':
                new_state.datora_punkti -= 1

            return new_state

# izmanto alpha-beta algoritmu
def alpha_beta(state, depth, alpha, beta):
    # ja tiek sasniegts maksimālais dziļums 
    if depth == 0 or not state.skaitli:
        return state.datora_punkti - state.player_punkti # tiek atgriezts virsotnes heiristiskais novērtējums - punktu starpība
    # starp spēlētājiem attiecīgajā spēles stāvoklī

    # ja ir datora gājiens, tad algoritms mēģina maksimizēt
    if state.datora_gajiens:
        max_eval = float('-inf')
        for move in state.skaitli:
            eval = alpha_beta(state.make_move(move), depth - 1, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else: 
        # ja ir spēlētāja gājiens, tad algoritms mēģina minimizēt
        min_eval = float('inf')
        for move in state.skaitli:
            eval = alpha_beta(state.make_move(move), depth - 1, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# nosaka labāko gājienu datoram
def best_move(state, depth=6):
    best_score = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    for move in state.skaitli:
        eval = alpha_beta(state.make_move(move), depth - 1, alpha, beta)
        if eval > best_score:
            best_score = eval
            best_move = move
        alpha = max(alpha, eval)
    return best_move


######################################################################

# izmanto mini-max algoritmu
def minimax(state, depth):
     # ja tiek sasniegts maksimālais dziļums
    if depth == 0 or not state.skaitli:
        return state.datora_punkti - state.player_punkti # tiek atgriezts virsotnes heiristiskais novērtējums - punktu starpība
    # starp spēlētājiem attiecīgajā spēles stāvoklī

    # ja ir datora gājiens, tad algoritms mēģina maksimizēt
    if state.datora_gajiens:
        max_eval = float('-inf')
        for move in state.skaitli:
            eval = minimax(state.make_move(move), depth - 1)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        # ja ir spēlētāja gājiens, tad algoritms mēģina minimizēt
        min_eval = float('inf')
        for move in state.skaitli:
            eval = minimax(state.make_move(move), depth - 1)
            min_eval = min(min_eval, eval)
        return min_eval

def best_moveM(state, depth=6):
    best_score = float('-inf')
    best_move = None
    for move in state.skaitli:
        eval = minimax(state.make_move(move), depth - 1)
        if eval > best_score:
            best_score = eval
            best_move = move
    return best_move

# ģenerē skaitļu virkni
def virknes_gen(length):
    return ''.join(map(str,[random.randint(1,3) for _ in range(length)]))

# nosaka uzvarētāju
def uzvaretajs(ai, player):
    if ai > player:
        print("AI uzvarēja")
    elif ai < player:
        print("Player uzvarēja")
    else:
        print("It's a tie!")

if __name__ == '__main__':

    garums = 0
    checkVirkne = True
    skaitlu_virkne = 0

    # parbauda vai pareizi ievadīts virknes garums
    while checkVirkne:
        garums = int(input("Ievadiet virknes garumu : "))
        if 15 <= garums <= 25:
            checkVirkne = False
            skaitlu_virkne = virknes_gen(garums)
        else:
            checkVirkne = True

    print(skaitlu_virkne)

    #Izvēlas kurš sāk spēli
    izvele = True

    mini_vai_alpha = False

    # izvelas algortimu mini == true; alpha == false
    if mini_vai_alpha == False:
        print("Tiek izmantots Alpha-Beta algoritms")
        initial_state = AlphaBeta(skaitlu_virkne, 50, 50, izvele) # inicializē objektu, kas satur informāciju par spēli 

        # kamēr skaitļu virknē ir skaitļi veic vaicājumus atkarībā, kam ir gājiens
        while initial_state.skaitli:
            if initial_state.datora_gajiens: # ja ir datora gājiens
                move = best_move(initial_state) # tiek izsaukta labākā gājiena novērtēšanas funkcija
                print(f"AI gājiens: {move}")
            else:
                move = input("Tavs gājiens: ") # spēlētājs izvēlas savu gājienu
                if move not in initial_state.skaitli: # gadījumā, ja spēlētājs ievada skaitļu virknē neesošu skaitli, tiek prasīts ievadīt virknē esošu skaitli
                    while move not in initial_state.skaitli:
                        move = input("Ievadiet skaitli, kas atrodas skaitlu virkne: ")
            
            initial_state = initial_state.make_move(move) # tiek veikts datora vai cilvēka izvēlētais gājiens
            print(f"Current state: {initial_state.skaitli}, AI punkti: {initial_state.datora_punkti}, Tavi punkti: {initial_state.player_punkti}")

        print("Game Over")
        print(f"Rezultāts - AI punkti: {initial_state.datora_punkti}, Tavi punkti: {initial_state.player_punkti}")
        uzvaretajs(initial_state.datora_punkti, initial_state.player_punkti)

    else:
        print("Tiek izmantots Mini-Max algoritms")
        initial_state = AlphaBeta(skaitlu_virkne, 50, 50, izvele) # tiek 

        #kamēr skaitļu virknē ir skaitļi veic vaicājumus atkarībā, kam ir gājiens
        while initial_state.skaitli:
            if initial_state.datora_gajiens:
                move = best_moveM(initial_state) # tiek izsaukta labākā gājiena novērtēšanas funkcija
                print(f"AI gājiens: {move}")
            else:
                move = input("Tavs gājiens: ") # spēlētājs izvēlas savu gājienu
                if move not in initial_state.skaitli:
                    while move not in initial_state.skaitli:
                        move = input("Ievadiet skaitli, kas atrodas skaitlu virkne: ")
            
            initial_state = initial_state.make_move(move)
            print(f"Current state: {initial_state.skaitli}, AI punkti: {initial_state.datora_punkti}, Tavi punkti: {initial_state.player_punkti}")

        print("Game Over")
        print(f"Rezultāts - AI punkti: {initial_state.datora_punkti}, Tavi punkti: {initial_state.player_punkti}")
        uzvaretajs(initial_state.datora_punkti, initial_state.player_punkti)
