
"""
Module to check for prime numbers.
"""

import math #importer sqrt



def isprime(pr):
    """
    Function to check if a number is prime.

    Args:
        pr (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """


    if pr == 1 :
        return False

    d = int(math.sqrt(pr))

    for i in range (2,d+1) :
        if math.gcd(pr,i) != 1 :
            return False

    return True

#### Fonction principale


def main():

    """
    permet d'executer d'utiliser la fonction isprime
    """

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
