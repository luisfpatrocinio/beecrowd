var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var numero = parseInt(lines.pop());

let brancas = Math.floor((numero * numero) / 2);
if (numero % 2 != 0) {
    brancas += 1;
}
let pretas = Math.floor((numero * numero) / 2);
console.log(`${brancas} casas brancas e ${pretas} casas pretas`)
    