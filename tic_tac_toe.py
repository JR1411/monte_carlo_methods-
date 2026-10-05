import numpy as np 

WINNING_LINES = [(0,1,2),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(0,4,8),(2,4,6),(0,3,6)] 

def check_winner(board , player): 
    for a,b,c in  WINNING_LINES: 
        if board[a] == player  and board[b] == player and board[c] == player : 
            return True 
    
    return False 

def gameplay(): 
    board = np.zeros(9 , dtype=int) 

    player = 1 

    for move in range(1,10):  
        available = np.where(board == 0 )[0] 
        field = np.random.choice(available) 

        board[field] = player 
        if check_winner(board , player): 
            return player , move 

        player = 2 if player == 1 else 1 
    return 0 , 9 

def monte_carlo(N): 
    first_wins = 0 
    second_wins = 0 
    draw = 0 

    lengths = np.zeros(N) 
    
    for i in range(N): 
        result , length = gameplay() 

        lengths[i] = length 

        if result ==1 : 
            first_wins += 1

        elif result ==2 : 
            second_wins += 1 

        else : 
            draw += 1 

    p_first = first_wins / N 
    p_second = second_wins / N 
    p_draw = draw / N 

    error_first = np.sqrt(p_first * (1 - p_first)/N ) 
    error_second = np.sqrt(p_second * (1 - p_second) / N ) 
    error_draw = np.sqrt(p_draw * (1 - p_draw) / N ) 

    mean_length = np.mean(lengths) 
    variance_length = np.var(lengths) 

    return p_first , error_first , p_second , error_second , p_draw , error_draw , mean_length , variance_length 

N = 1000000

results = monte_carlo(N) 


print(f"First player wins: {results[0]:.6f} ± {results[1]:.6f}")
print(f"Second player wins: {results[2]:.6f} ± {results[3]:.6f}")
print(f"Draw:               {results[4]:.6f} ± {results[5]:.6f}")

print()
print(f"Mean game length:     {results[6]:.6f}")
print(f"Variance game length: {results[7]:.6f}")
