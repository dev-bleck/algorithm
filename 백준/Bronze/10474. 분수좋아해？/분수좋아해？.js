const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split('\n');


for (const numb of input) {
    const [A, B] = numb.split(' ').map(Number);
    
    if (A == 0 && B == 0) {
        break;
    } else {
        console.log(`${Math.floor(A / B)} ${A % B} / ${B}`);
    }
}