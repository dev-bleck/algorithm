const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split('\n');
const N = parseInt(input[0]);
const chat = input.splice(1, N + 1);
let count = 0;
let userSet = new Set();

for (let i = 0; i < N; i++) {
    if (chat[i] === 'ENTER') {
        userSet.clear();
    } else { 
        if (!userSet.has(chat[i])) {
            userSet.add(chat[i]);
            count += 1
        }
    }
}

console.log(count);