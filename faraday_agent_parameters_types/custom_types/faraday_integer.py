from ..faraday_agent_parameters_types import Type


class FaradayInteger(Type):
    def __init__(self, number: 'solo numero entero'):
        """
        Type: Numero enero
        """
        Type.__init__(self, name="int")
        check = self.check_instance(number)
        if check:
            raise TypeError("no es un numero entero")
        else:
            self.number = number

    def __repr__(self):
        return '{0}'.format(self.number)

    def __str__(self):
        return '{0}'.format(self.number)

    @staticmethod
    def check_instance(number):
        if str(number).isnumeric():
            return False
        else:
            return True


