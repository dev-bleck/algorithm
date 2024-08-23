const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().trim().split(' ');
const A = parseInt(input[0]), B = parseInt(input[1]), N = parseInt(input[2]);

let remainder = A % B;
let result = 0;

for (let i = 0; i < N; i++) {
  remainder *= 10;
  result = Math.floor(remainder / B);
  remainder %= B;
}

console.log(result);