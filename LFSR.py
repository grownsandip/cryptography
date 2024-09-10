
class LFSR:
    def __init__(self,seed,bits,taps):
        self.seed=seed
        self.bits=bits
        self.taps=taps
        self.lfsr=self._initialize_lfsr(seed)
        print(f"initialized lfsr with {self.lfsr}")
                   
    def _initialize_lfsr(self, seed):
        #Converts seed into a binary list of length 'bits'.
        lfsr = list(map(int, bin(seed)[2:]))
        return lfsr

    def step(self):
        #Performs one step of LFSR and returns the output bit."""
        feedback = 0
        for tap in self.taps:
            feedback ^= self.lfsr[tap]
        
        output = self.lfsr[-1]  # Collect the last bit as output
        # Shift and update LFSR with feedback
        self.lfsr = [feedback] + self.lfsr[:-1]
        return output

    def generate_sequence(self, steps):
        #Generates a sequence of output bits for the given number of steps.
        sequence = []
        for _ in range(steps):
            sequence.append(self.step())
        return sequence


def seedCheck(seed,bits):
    b=bin(seed)
    if len(b[2:])>bits:
        raise ValueError("The seed's bit length is not according to the number of bit")
    return True
    
def tapsCheck(taps,bits):
    for tap in taps:
      if tap>bits:
        raise ValueError("number of taps cannot be greater than total number of bits")
    return True

def get_inputs():
    bits = int(input("Enter the number of bits in LFSR: "))
    seed = int(input("Enter seed value: "))
    seedCheck(seed, bits)
    
    steps = int(input("Enter the number of steps required: "))
    taps = list(map(int, input(f"Enter the tap positions (0 to {bits - 1}), separated by spaces: ").split()))
    tapsCheck(taps, bits)
    
    return seed, bits, steps, taps
       
    
def main():
    num=int(input("Enter the number of LFSR you would like:"))
    lfsr_list=[]
    for i in range(num):
        print(f"\ncreating #{i+1} LFSR:")
        seed,bits,steps,taps=get_inputs()
        lfsr=LFSR(seed,bits,taps)
        lfsr_list.append((lfsr,steps))
    #Generate print sequences for all lfsrs
    for i,(lfsr,steps) in enumerate(lfsr_list):
        print(f"\nSequence for #{i+1} LFSR:")
        sequence=lfsr.generate_sequence(steps)
        print(sequence)

if __name__=="__main__":
    main()