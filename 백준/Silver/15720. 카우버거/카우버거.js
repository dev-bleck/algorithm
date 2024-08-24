const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split('\n');

const burgers = input[1].split(' ').map(Number).sort((a, b) => b - a);
const sides = input[2].split(' ').map(Number).sort((a, b) => b - a);;
const drinks = input[3].split(' ').map(Number).sort((a, b) => b - a);;
let total = 0;
let minTotal = 0;

[burgers, sides, drinks].forEach(array => {
    array.forEach(e => {
        total += e;
    })
});


let tmp = 0;
for (let i = 0; i < Math.min(...input[0].split(' ').map(Number)); i++) {
    tmp += burgers[i] + sides[i] + drinks[i];
    minTotal += burgers[i] * 0.9 + sides[i] * 0.9 + drinks[i] * 0.9;
}
minTotal += total - tmp

console.log(total);
console.log(minTotal);