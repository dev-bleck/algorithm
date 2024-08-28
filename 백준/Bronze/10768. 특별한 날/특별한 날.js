const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split('\n');

const month = parseInt(input[0]);
const day = parseInt(input[1]);
let result = '';

if (month < 2) {
    result = 'Before';
} else if (month == 2) {
    if (day == 18) {
        result = 'Special';
    } else if (day < 18) {
        result = 'Before';
    } else {
        result = 'After';
    }
} else {
    result = 'After';
}

console.log(result);