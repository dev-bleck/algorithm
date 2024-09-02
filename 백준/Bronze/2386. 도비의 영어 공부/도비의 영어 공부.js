const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split('\n');

for (i of input) {
    if (i === '#') {
        break;
    } else {
        const alphabet = i.slice(0, 1);
        const sentence = i.slice(1, i.length);
        let count = 0;
        for (let i = 0; i <= sentence.length; i++) {
            if (sentence[i] === alphabet.toUpperCase() || sentence[i] === alphabet.toLowerCase()) {
                count++;
            }
        }
        console.log(alphabet, count);
    }
}