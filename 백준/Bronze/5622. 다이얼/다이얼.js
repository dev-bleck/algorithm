let input = require('fs').readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'Algorithm/example.txt').toString().trim();

let res = 0;
for (let i of input) {
    let code = i.charCodeAt(0);
    
    if (code < 81) {
        res += Math.floor((code - 65) / 3 + 3);
    } else if (81 <= code && code < 84) {
        res += 8;
    } else if (84 <= code && code < 87) {
        res += 9;
    } else if (87 <= code) {
        res += 10;
    }
}

console.log(res);