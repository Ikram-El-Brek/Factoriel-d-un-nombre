def factoriel(n):
    try:
        n = int(n)
        if n < 0:
            raise ValueError("Le nombre doit être positif")
        elif n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result
    except ValueError as e:
        print(f"Erreur : {e}")
        return None
    except TypeError as e:
        print(f"Erreur : {e}")
        return None

# Testez la fonction
nombre = input("Entrez un nombre : ")
resultat = factoriel(nombre)
if resultat is not None:
    print(f"Le factoriel de {nombre} est : {resultat}")