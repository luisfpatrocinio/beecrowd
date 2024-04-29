def main():
    numHumanos, numElfos, numAnoes, numOrcs, numWargs, numAguias = list(map(int, input().split()))

    exercitoBem = numHumanos + numElfos + numAnoes + numAguias
    exercitoMal = numOrcs + numWargs

    b = "Middle-earth is safe."
    a = "Sauron has returned."
    
    if exercitoBem >= exercitoMal:
        print(b)
    else:
        print(a)

main()