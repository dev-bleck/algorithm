const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split('\n');
const N = parseInt(input[0]);
const list = input.slice(1, N + 1).sort();
const setList = [...new Set(list)];
let result = 0;
let answer = ''

for (let i = 0; i <= setList.length; i++) {
    let count = 0;
    for (let j = i; j <= N; j ++) {
        if (setList[i] == list[j]) {
            count++;
        }
    }

    if (result < count) {
        result = count;
        answer = setList[i];
    }
}

console.log(answer);