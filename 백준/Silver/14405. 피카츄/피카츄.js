const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().trim();

let index = 0;
let flag = 'YES';

while (index < input.length) {
    if (input.slice(index, index + 2) === 'pi' || input.slice(index, index + 2) === 'ka') {
        index += 2;
    } else if (input.slice(index, index + 3) == 'chu') {
        index += 3;
    } else {
        flag = 'NO';
        break;
    }
}

console.log(flag);