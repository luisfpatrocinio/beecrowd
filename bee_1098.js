function main() {
    let n = parseInt(prompt("Informe o número de entradas:"));
    let cobaias = { 'C': 0, 'R': 0, 'S': 0 };
    let total = 0;

    for (let i = 0; i < n; i++) {
        let input = prompt("Informe a quantidade e o tipo (C/R/S):").split(" ");
        let qtd = parseInt(input[0]);
        let tipo = input[1];
        
        cobaias[tipo] += qtd;
        total += qtd;
    }

    printResults(cobaias, total);
}

function printResults(cobaias, total) {
    console.log(`Total: ${total} cobaias`);
    console.log(`Total de coelhos: ${cobaias["C"]}`);
    console.log(`Total de ratos: ${cobaias["R"]}`);
    console.log(`Total de sapos: ${cobaias["S"]}`);
    console.log(`Percentual de coelhos: ${(cobaias["C"] / total * 100).toFixed(2)} %`);
    console.log(`Percentual de ratos: ${(cobaias["R"] / total * 100).toFixed(2)} %`);
    console.log(`Percentual de sapos: ${(cobaias["S"] / total * 100).toFixed(2)} %`);
}

main();
