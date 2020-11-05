

class ScoreCalculator:
    def __init__(self, word):
        assert isinstance(word, str)
        self.word = word
    
        self.letter_scores = {
            'aeioulnrst': 1,
            'dg': 2,
            'bcmp': 3,
            'fhvwy': 4,
            'k': 5,
            'jx': 8,
            'qz': 10
        }

    @property
    def score(self):
        score = 0
        for word_letter in self.word:
            score += [letter_value for letters, letter_value in self.letter_scores.items() if word_letter in letters][0]
        return score

if __name__ == "__main__":
    new_word = ScoreCalculator("cat")
    print(new_word.score)