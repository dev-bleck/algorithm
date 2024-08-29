const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split('\n');
const M = parseInt(input[0]);
let result = 1;

for (let xy of input.slice(1, M + 1)) {
    const [X, Y] = xy.split(' ').map(Number);

    if (result == Y) {
        result = X;
    } else if (result == X) {
        result = Y;
    }
    
}

console.log(result);