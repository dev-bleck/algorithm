let input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').trim().split('\n');

let [N, M] = input[0].split(' ').map(Number);
let addressPw = input.slice(1, N + 1);
let findAddressPw = input.slice(N + 1, N + M + 1);

let dict = {};
for (let i = 0; i < N; i++) {
    let [address, password] = addressPw[i].split(' ');
    dict[`${address}`] = password;
}


for (let i = 0; i < M; i++) {
    console.log(dict[`${findAddressPw[i]}`])
}