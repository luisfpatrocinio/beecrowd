# Área: https://www.beecrowd.com.br/judge/pt/problems/view/1012

def main():
    # Entrada:
    a, b, c = map(float, input().split())

    # Processamento:
    area_triangulo = calcular_area_triangulo(a, c)
    area_circulo = calcular_area_circulo(c)
    area_trapezio = calcular_area_trapezio(a, b, c)
    area_quadrado = calcular_area_quadrado(b)
    area_retangulo = calcular_area_retangulo(a, b)
    # Saída:
    print(f"TRIANGULO: {area_triangulo:.3f}")
    print(f"CIRCULO: {area_circulo:.3f}")
    print(f"TRAPEZIO: {area_trapezio:.3f}")
    print(f"QUADRADO: {area_quadrado:.3f}")
    print(f"RETANGULO: {area_retangulo:.3f}")

def calcular_area_triangulo(a, c):
    return (a * c) / 2

def calcular_area_circulo(c):
    return 3.14159 * c ** 2

def calcular_area_trapezio(a, b, c):
    return ((a + b) * c) / 2

def calcular_area_quadrado(b):
    return b ** 2

def calcular_area_retangulo(a, b):
    return a * b

main()
