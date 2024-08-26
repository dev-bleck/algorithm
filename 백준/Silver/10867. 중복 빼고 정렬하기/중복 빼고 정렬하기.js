const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split('\n');
const numbs = input[1].split(' ').map(Number).sort((a, b) => a - b);

console.log(...new Set(numbs));