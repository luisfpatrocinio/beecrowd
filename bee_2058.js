var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function main() {
    var numLados = parseInt(lines.shift());
    console.log(numLados - 2);
}

main();
