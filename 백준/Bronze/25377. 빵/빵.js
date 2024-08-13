let input = require('fs').readFileSync(process.platform === 'linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').trim().split('\n');
let N = input[0];
let N_lst = input.slice(1, N + 1);
let res = 1e9;

for (i of N_lst) {
    let [A, B] = i.split(' ').map(Number);
    if (A <= B) {
        if (B < res) {
            res = B;
        }
    }
}

if (res == 1e9) {
    console.log(-1);
} else {
    console.log(res);
}