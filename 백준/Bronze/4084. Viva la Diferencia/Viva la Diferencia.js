const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split('\n');

for (index of input) {
    if (index === '0 0 0 0') {
        break;
    } else {
        let [a, b, c, d] = index.split(' ').map(Number);
        let count = 0;
        while (true) {
            if (a == b && b == c && c == d && d == a) {
                console.log(count);
                break;
            }
            let list = [];
            list.push(Math.abs(a - b));
            list.push(Math.abs(b - c));
            list.push(Math.abs(c - d));
            list.push(Math.abs(d - a));
            [a, b, c, d] = list;
            count++;
        }
    }
}