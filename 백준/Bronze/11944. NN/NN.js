let input = require('fs').readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'Algorithm/example.txt').toString().replace(/\r/g, '').trim().split(' ');
let N = parseInt(input[0]), M = parseInt(input[1]);
res = '';

for (i = 0; i < N; i++) {
    res += N;
}

console.log(res.slice(0, M));