class Symbol:

    def __init__(self, statement):
        self.statement = statement

    def evaluate(self, model):
        if self.statement in model:
            return model[self.statement]

        else :
            raise Exception(f"{self.statement} not in model")
        
    def symbols(self):
        return {self.statement}
        
class Not :

    def __init__(self, operand):
        self.operand = operand

    def evaluate(self, model):
        
        return not self.operand.evaluate(model)
    
    def symbols(self):
        return self.operand.symbols()
    
class And :

    def __init__(self,operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def evaluate(self, model):
        return self.operand1.evaluate(model) and self.operand2.evaluate(model)
    
    def symbols(self):
        return self.operand1.symbols().union(self.operand2.symbols())

class Or :

    def __init__(self,operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def evaluate(self, model):
        return self.operand1.evaluate(model) or self.operand2.evaluate(model)
    
    def symbols(self):
        return self.operand1.symbols().union(self.operand2.symbols())

class Implication :

    def __init__(self,operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def evaluate(self, model):
        return not self.operand1.evaluate(model) or self.operand2.evaluate(model)
    
    def symbols(self):
        return self.operand1.symbols().union(self.operand2.symbols())

class Biconditional :

    def __init__(self,operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def evaluate(self, model):
        first = self.operand1.evaluate(model)
        second = self.operand2.evaluate(model)
        return (not first or second ) and  (first or not second)
    
    def symbols(self):
        return self.operand1.symbols().union(self.operand2.symbols())

def check_all(kb, query, symbols, model):

    if len(symbols) == 0 :

        if kb.evaluate(model) :
            ans = query.evaluate(model)
            print(f"{model} : {ans}")
            return ans
        
        else :
            print(f"{model} : True")
            return True
 
    else :
        symbol = symbols[0]
        remaining = symbols[1:]

        model_true = model.copy()
        model_false = model.copy()

        model_true[symbol] = True
        model_false[symbol] = False

        return check_all(kb, query, remaining, model_true) and check_all(kb, query, remaining, model_false)


def model_check(kb, query):
    symbols = list(kb.symbols().union(query.symbols()))
    return check_all(kb, query, symbols, {})

P = Symbol("P")
Q = Symbol("Q")

kb = And(Implication(P, Q), Q)

print(model_check(kb, P))