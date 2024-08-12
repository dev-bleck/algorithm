let input = require('fs').readFileSync(process.platform === 'linux'? '/dev/stdin' : 'Algorithm/example.txt').toString().replace(/\r/g, '').trim().split('\n');

let N = parseInt(input[0]);
let N_lst = input.slice(1, N + 1);
let winA = 0, winB = 0;

for (numbers of N_lst) {
    let [A, B] = numbers.split(' ').map(Number);
    if (A > B) {
        winA++;
    } else if (A < B) {
        winB++;
    }
}

console.log(winA, winB);