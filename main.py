
"""1. Dându-se numărul natural n, determină numerele prime p1 si p2 astfel încât n = p1 + p2 (verificarea conjecturii lui Goldbach), p1 minim și p2 maxim. Pentru ce fel de n există soluție?

2. Execută un număr dat de pași pentru a calcula radicalul unui număr dat folosind metoda lui Newton cu x0=2 și afișează aproximarea obținută.

3. Determină dacă un număr dat este palindrom.
"""

def prim(n):
    """
     Verifica daca un numar e prim
     :param n:
     :return: Bool
    """
    for i in range (2, n-1):
        if n%i == 0 :
            return False
    return True

def get_goldbach(n):
    """
    Verifica conjectura lui Goldbach
    :param n:
    :return: int
    """
    i = 2
    while(i <= n//2):
        if prim(i) == True and prim(n-i) == True:
            return i,n-i
        i=i+1
    return -1

def get_newton_sqrt(n, steps):
    """
    Calculeaza radicalul unui număr dat folosind metoda lui Newton
    :param n, steps:
    :return: float
    """
    x = n
    count = 0
    while (1):
        count = count + 1
        root = 0.5 * (x + (n / x))
        if (abs(root - x) < steps):
            break
        x = root
    return root

def test_get_goldbach():
    #Teste pentru conjectura lui Goldbach
    assert get_goldbach(10)==(3,7)
    assert get_goldbach(7)==(2,5)
    assert get_goldbach(22)==(3,19)

def test_get_newton_sqrt():
    #Teste pentru functia cu radicali ai lui Newton
    assert get_newton_sqrt(327, 0.00001)==18.0831
    assert get_newton_sqrt(49, 2) == 8.474056603773585

def is_palindrome(n):
    """
    Determină dacă un număr dat este palindrom
    :param n:
    :return: Bool
    """
    o = 0
    n2 = n
    while (n != 0):
        o = o * 10 + n % 10
        n = n // 10
    if o == n2:
        return True
    else:
        return False

def test_is_palindrome():
    #Teste pentru functia de palindrom
    assert is_palindrome(1991) == True
    assert is_palindrome(1823) == False
    assert is_palindrome(1725) == False
    assert is_palindrome(3) == True

def main():
    while True:
        print('1. Suma de numere prime')
        print('2. Radical, Newton')
        print('3. Palindrom')
        print('x. Iesire din program')
        optiune=input('Alege optiunea: ')
        if optiune == '1':
            k=int(input('Dati numarul:'))
            p=get_goldbach(k)
            if p==-1 :
                print("Nu exista")
            else:
                print(p)
        elif optiune == '2':
            n=int(input('Dati n:'))
            steps=float(input('Dati steps:'))
            rad=get_newton_sqrt(n,steps)
            print(rad)
        elif optiune == '3':
            c = int(input('Dati valoarea:'))
            if is_palindrome(c) == True:
                print("Este palindrom")
            else:
                print("Nu este palindrom")
        elif optiune == 'x':
            break

if __name__ == '__main__':
    main()