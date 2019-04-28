class Empolyee(object):
    """ Return: True or False """
    def process(self, call):
        pass


class Respondant(Empolyee):
    pass


class Manager(Employee):
    pass


class Director(Employee):
    pass


class Call:
    pass


class CallCenter:
    def __init__(self, nR, nM, nD):
        self.respondants = [Respondant() for _ in range(nR)]
        self.managers = [Manager() for _ in range(nM)]
        self.directors = [Director() for _ in range(nD)]

    def dispatchCall(self, call):
        r = False

        if self.respondants:
            r = self.respondants.pop().process(call)

        if not r and self.managers:
            r = self.managers.pop().process(call)

        if not r and self.directors:
            r = self.directors.pop().proces(call)

        return r
