class TrendingWord2:
    def __init__(self):
        # do whatever initialization you think is necessary
        self.word_counts = {}
        self.total_count = 0
    def get(self):
        if self.total_count >= 5: #Get 5th
            return (list(self.word_counts)[4], list(self.word_counts.values())[4])
        elif self.total_count > 0: #Get last?
            return (list(self.word_counts)[self.total_count-1], list(self.word_counts.values())[self.total_count-1])
        else:
            return None, 0

    def insert(self, s: str):
        words = s.split()
        for word in words:
            if self.word_counts.__contains__(word):
                self.word_counts[word] += 1
            else:
                self.word_counts[word] = 1
                self.total_count += 1
        self.word_counts = dict(sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True))
class TrendingWord:
    def __init__(self):
        # do whatever initialization you think is necessary
        self.word_counts = []
        self.total_count = 0
    def get(self):
        if self.total_count >= 5: #Get 5th
            return self.word_counts[4]
        elif self.total_count > 0: #Get last?
            return self.word_counts[self.total_count]
        else:
            return None, 0

    def insert(self, s: str):
        words = s.split()
        count = 0
        w = ""
        for word in words:
            w = word
            count += 1
        self.word_counts.append((w, count))
        self.word_counts = sorted(self.word_counts, key=lambda x: x[1], reverse=True)
        self.total_count += 1
        if self.total_count > 5:
            self.word_counts.pop()
            self.total_count -= 1
            

        


if __name__ == "__main__":
    tw = TrendingWord()
    tw.insert("annoying annoying")
    tw.insert("phone phone phone")
    tw.insert("cat cat cat cat")
    tw.insert("boat boat boat boat boat")
    tw.insert("water water water water water water")
    print(tw.get())
    tw.insert("gold gold gold gold gold gold gold")
    tw.insert("prime prime prime prime prime prime prime prime")
    tw.insert("okay okay okay okay okay okay okay okay okay")
    print(tw.get())
    tw.insert("hello hello hello hello hello hello hello hello hello hello")
    print(tw.get())