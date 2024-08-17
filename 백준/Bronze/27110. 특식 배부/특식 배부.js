const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split('\n');
const N = parseInt(input[0]);
const numbs = input[1].split(' ').map(Number);
let res = 0;

for (let i of numbs) {
    if (N >= i) {
        res += i;
    } else {
        res += N;
    }
}

console.log(res);