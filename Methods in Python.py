class Calculator:
    brand = 'Casio'

    def add(n1, n2):
        result = n1+n2
        print(result)
    
    def sub(n1, n2):
        if(n1>n2):
            r = n1-n2
        else:
            r = n2-n1
        print(r)

    def multi(n1, n2):
        r = n1*n2
        print(r)

    def div(n1, n2):
        r = n1/n2
        print(r)

Calculator.add(2,3)
Calculator.sub(4,1)
Calculator.multi(3,3)
Calculator.div(99,3)