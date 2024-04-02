#include <stdio.h>
#include <iostream>
 
using namespace std;

int main() {
    // Ler um valor N
    int n;
    cin >> n;
    
    // Cria um array de numeros inteiros de tamanho N
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Encontrar o menor valor e sua posição
    int menorValor = a[0];
    int posicaoMenorValor = 0;

    for (int i = 1; i < n; ++i) {
        if (a[i] < menorValor) {
            menorValor = a[i];
            posicaoMenorValor = i;
        }
    }

    // Imprimir o menor valor e a posição
    cout << "Menor valor: " << menorValor << endl;
    cout << "Posicao: " << posicaoMenorValor << endl;
 
    return 0;
}