class CNFClause:
    def __init__(self, literals):
        # Every literal in the clause disjunction with each other
        self.literals = set(literals)

    def satisfy(self, model):
        # If at least one literal is true, the clause is true
        return any(lit in model for lit in self.literals)


class CNFSentence:
    def __init__(self):
        # Every clause in the CNF conjunction with each other
        self.clauses = []

    def add_clause(self, clause):
        self.clauses.append(CNFClause(clause))

    def satisfy(self, model):
        # If at least one clause is false, the CNF is false
        return all(clause.satisfy(model) for clause in self.clauses)
