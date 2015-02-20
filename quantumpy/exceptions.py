class QuantumPythonError(Exception):
    """ Base exception """

class QuantumError(QuantumPythonError):
    """ Exception for the Quantum API errors """

class HTTPError(QuantumPythonError):
    """ Exception for http errors """
