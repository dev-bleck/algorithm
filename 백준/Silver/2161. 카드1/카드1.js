const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().trim();

const N = parseInt(input);
const numbs = [];
for (let i = 1; i <= N; i++) {
    numbs.push(i);
}

const result = [];
while (numbs.length > 1) {
    const res = numbs.shift();
    result.push(res);
    const numb = numbs.shift();
    numbs.push(numb);
}
result.push(numbs.shift());

console.log(...result);