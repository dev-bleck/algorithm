const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split(' ');

const S = parseInt(input[0]);
const T = parseInt(input[1]);
const D = parseInt(input[2]);

const time = D / (S * 2);

console.log(T * time);