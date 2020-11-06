# DNA string parsing

class DNA_parser:
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def from_DNA_string(cls, dna_string):
        return cls(dna_string = dna_string.upper())


    def parse_dna(self):
        if not hasattr(self, "dna_string"):
            print("NO DNA STRING CURRENTLY STORED")
            self.dna_string = input("\nPLEASE ENTER ONE NOW\n").upper()

        
        self.a_count = self.dna_string.count('A')
        self.c_count = self.dna_string.count('C')
        self.t_count = self.dna_string.count('T')
        self.g_count = self.dna_string.count('G')

        self.letter_counts = {
            "A": self.a_count,
            "C": self.c_count,
            "G": self.g_count,
            "T": self.t_count
        }
        return self.letter_counts

    



if __name__ == "__main__":
    dna_par_1 = DNA_parser()
    dna_par_2 = DNA_parser.from_DNA_string("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")

    print(dna_par_2.dna_string)
    print(dna_par_1.parse_dna())
