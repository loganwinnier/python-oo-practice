class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __repr__(self):
        return f"<Serial Number Generator with inital value of {self.start}>"

    def __init__(self, start=100):
        """Creates a inital serial number"""
        self.start = start
        self.number = start

    def generate(self):
        """increments the current serial number by 1 to generate next serial number"""
        self.number += 1
        return self.number - 1

    def reset(self):
        """resets serial number back to initial start value"""
        self.number = self.start
