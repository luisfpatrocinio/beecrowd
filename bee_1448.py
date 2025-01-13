def checarAcertos(original: str, time: str) -> int:
    acertos = 0
    for i in range(len(original)):
        if original[i] == time[i]:
            acertos += 1
    return acertos
    

def main():
    t = int(input())
    for i in range(t):
        original = input()
        time1 = input()
        time2 = input()
        
        print(f"Instancia {i+1}")

        if checarAcertos(original, time2) == checarAcertos(original, time1):
            print("empate")
            continue

        if checarAcertos(original, time1) > checarAcertos(original, time2):
            print("time 1")
        elif checarAcertos(original, time2) > checarAcertos(original, time1):
            print("time 2")
        
        if i < t - 1:
            print()
main()