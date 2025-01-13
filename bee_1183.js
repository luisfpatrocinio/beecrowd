var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

function main() {
  // Leitura da operação
  var op = lines.shift().trim();

  var matriz = [];
  var soma = 0;
  var cont = 0;

  // Leitura da matriz
  for (let i = 0; i < 12; i++) {
    matriz[i] = [];
    for (let j = 0; j < 12; j++) {
      matriz[i][j] = parseFloat(lines.shift());
    }
  }

  // Cálculo da soma ou média dos elementos acima da diagonal principal
  for (let i = 0; i < 12; i++) {
    for (let j = i + 1; j < 12; j++) {
      soma += matriz[i][j];
      cont++;
    }
  }

  // Impressão do resultado
  if (op === "S") {
    console.log(soma.toFixed(1));
  } else if (op === "M") {
    console.log((soma / cont).toFixed(1));
  }
}

main();
