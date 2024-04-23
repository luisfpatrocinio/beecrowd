def main():
    numCasos = int(input())
    for i in range(numCasos):
        word1, word2 = list(input().split())
        result = ""

        for n in range(max(len(word1), len(word2))):
            if n < len(word1):
                result += word1[n]
            if n < len(word2):
                result += word2[n]
    
        print(result)


main()