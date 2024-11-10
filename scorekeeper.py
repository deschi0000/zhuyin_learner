class ScoreKeeper:

    total = 0
    correct = 0

    def __init__(self, total_score = 0):
        self.total = total_score        

    def add_to_total(self, num_to_add):
        self.total += num_to_add
        
    def subract_to_total(self):    
        if self.total > 0:
            self.total -= 1
        else:
            self.total = 0

    def add_to_correct(self):
        self.correct += 1

    def __str__(self):
        return f"Total: {self.total} | Correct Answers: {self.correct}"