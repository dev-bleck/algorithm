let input = require('fs').readFileSync(process.platform === 'linux'? '/dev/stdin' : 'Algorithm/example.txt').toString().trim().split(' ');
let A = input[0].split('').map(Number);
let B = input[1].split('').map(Number);
let res = '';

if (A.length > B.length) {
    while (A.length != B.length) {
        B.unshift(0);
    }
} else if (A.length < B.length) {
    while (A.length != B.length) {
        A.unshift(0);
    }
}

for (i = 0; i < A.length; i++) {
    res += String(A[i] + B[i]);
}

console.log(res);