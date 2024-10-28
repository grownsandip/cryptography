
def step(taps,lfsr):
    feedback=0
    for tap in taps:
        feedback^=lfsr[tap]
    output=lfsr[-1]
    lfsr[:]=[feedback]+lfsr[:-1]
    return output
def generate(steps,taps,seed):
    lfsr=list(map(int,bin(seed)[2:]))
    print(f"lfsr initialized with seed{lfsr}")
    sequence=[]
    for _ in range(steps):
        sequence.append(step(taps,lfsr))
    print(sequence)
    
    
def seed_check(bits,seed):
    b=bin(seed)
    if(len(b[2:])>bits):
        raise ValueError("invalid seed length")
    return True
def taps_check(taps,bits):
    for tap in taps:
        if tap>bits:
            raise ValueError("invalid tap positions")
    return True

def main():
    bits=int(input("Enter the number of flopflops in lfsr:"))
    seed=int(input("Enter  the seed value:"))
    seed_check(bits,seed)
    steps=int(input("Enter the steps:"))
    taps=list(map(int,(input(f"Enter the tap postion between (0 to {bits-1}) seperated by space:").split())))
    taps_check(taps,bits)
    generate(steps,taps,seed)
    # print(sequence)
    
if __name__=="__main__":
    main()