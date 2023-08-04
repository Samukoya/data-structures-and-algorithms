import logging
logging.basicConfig(level=logging.INFO)
def min_max(S):
    """Returns the minimum and maximum values in a sequence S of length n"""
    max_val = min_val = S[0]
    n = len(S)
    
    def find_min_max(S, n, min_val, max_val,i):
        if S[i]>max_val:
            max_val = S[i]
        elif S[i] < min_val:
            min_val = S[i]
        
        if i == n-1:
            return (max_val, min_val)
        else:
            return find_min_max(S, n, min_val, max_val, i+1)
    return find_min_max(S, n, max_val, min_val, 0)

def recursive_product(m, n):
    """Finds the product of two numbers m and n using only addition"""
    if n==0:
        return 0
    else:
        cum_prod = m + recursive_product(m, n-1)
    return cum_prod

def towers_of_hanoi(n_disks: int)-> int:
    """Attempts to solve the towers of hanoi challenge using three pegs for n_disks number of disks
    Returns:
        steps: number of steps
    """
    # initializes the source peg
    source = [i for i in range(1, n_disks+1)]
    source.reverse()
    dest = [] # destination peg
    aux = [] # auxillary peg
    steps = 0 # Number of pegs
    logging.info("Starting function")
    logging.info(f"Source : {source}\tDestination : {dest}\tAuxiliary : {aux}\tSteps : {steps}")

    def solve(source, dest, aux, n_disks, steps):
        """Moves n_disks from one peg to source to dest"""
        if n_disks == 1:
            # move disk from source to destination
            dest.append(source.pop())
            logging.info(f"Source : {source}\tDestination : {dest}\tAuxiliary : {aux}\tSteps : {steps}")
            return steps + 1
        
        else:
            # move n_disks-1 from source to destination.
            steps = solve(source, aux, dest, n_disks-1, steps)
            logging.info(f"Source : {source}\tDestination : {dest}\tAuxiliary : {aux}\tSteps : {steps}")
            # move last disk from source to destination
            dest.append(source.pop())
            steps += 1
            # move disks from aux to dest
            steps = solve(aux, dest, source, n_disks-1, steps)
            logging.info(f"Source : {source}\tDestination : {dest}\tAuxiliary : {aux}\tSteps : {steps}")
            return steps
    
    return solve(source, dest, aux, n_disks, steps)

def is_palindrome(S, ind_1, ind_2):
    """Checks whether a string is a palindrome"""
    if ind_1 == ind_2:
        # if the remaining letter is one
        return True 
    elif ind_1 - ind_2 == 1:
        if S[ind_1] == S[ind_2]:
            return True
        else: 
            return False
    else:
        if S[ind_1] == S[ind_2]:
            return is_palindrome(S, ind_1+1, ind_2-1)
        else: 
            return False


        
