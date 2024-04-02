#include <iostream>
#include <cmath>
using namespace std;

// Rafael
int func_r(int x, int y) {
    return pow(3 * x, 2) + pow(y, 2);
}

// Beto
int func_b(int x, int y) {
    return 2 * pow(x, 2) + pow(5 * y, 2);
}

// Carlos
int func_c(int x, int y) {
    return -100 * x + pow(y, 3);
}

int main() {
    // Número de casos de teste
    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        // Valores de teste
        int x, y;
        cin >> x >> y;

        // Resultados
        int r = func_r(x, y);
        int b = func_b(x, y);
        int c = func_c(x, y);

        // Printar resultados
        if (r > b && r > c) {
            cout << "Rafael ganhou" << endl;
        } else if (b > r && b > c) {
            cout << "Beto ganhou" << endl;
        } else {
            cout << "Carlos ganhou" << endl;
        }
    }

    return 0;
}
