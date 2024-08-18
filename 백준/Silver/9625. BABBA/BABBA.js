const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '');

const N = parseInt(input);
let countA = 1;
let countB = 0;

for (let i = 0; i < N; i++) {
    const nextA = countB;
    const nextB = countA + countB;

    countA = nextA;
    countB = nextB;
}

console.log(countA, countB);