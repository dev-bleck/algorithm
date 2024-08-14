let input = parseInt(require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').trim());
let sticks = [64];
let sticks_sum = sticks.reduce((acc, cur) => acc + cur, 0);

while (sticks_sum > input) {
    let minimum = sticks.sort((a, b) => a - b).shift();
    minimum = minimum / 2;

    sticks_sum = sticks.reduce((acc, cur) => acc + cur, 0);
    sticks.push(minimum);

    if (sticks_sum + minimum < input) {
        sticks.push(minimum);
    }
    sticks_sum = sticks.reduce((acc, cur) => acc + cur, 0);
}

console.log(sticks.length);