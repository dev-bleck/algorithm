const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split('\n');

for (let i of input.slice(1, parseInt(input[0]) + 1)) {
    if (i.includes('S')) {
        console.log(i);
        break;
    }
}