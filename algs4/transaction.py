class Transaction:

    def __init__(self, l):
        who, when, amount = l.split()
        self.who = who
        self.when = when
        self.amount = float(amount)

    def __str__(self):
        return "%-10s %10s %8.2f" % (self.who, self.when, float(self.amount))

    def __lt__(self, other):
        return self.amount < other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def hashcode(self):
        hashcode = 1
        hashcode = 31 * hashcode + hash(self.who)
        hashcode = 31 * hashcode + hash(self.when)
        hashcode = 31 * hashcode + hash(self.amount)
        return hashcode
