#include <iostream>
#include <cmath>
#include <iomanip> // Incluir iomanip para usar setprecision
using namespace std;

int main() {
    int n;
    cin >> n;

    int sum = 0;
    int count = 0;
    while (true) {
        // Receber valor inteiro
        int x;
        cin >> x;

        // Se for negativo, parar
        if (x < 0) {
            break;
        }

        // Somar valor
        sum += x;
        count++;
    }

    // Calcular média
    double avg = (double) sum / count;
    
    // Garantir que a média seja impressa com duas casas decimais
    cout << fixed << setprecision(2) << avg << endl; // Imprimir a média com duas casas decimais
    
    // Printar média
    return 0;
}

main();