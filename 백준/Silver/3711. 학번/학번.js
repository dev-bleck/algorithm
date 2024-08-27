const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '').split('\n');
const T = parseInt(input[0]);

for (let i = 0; i < T; i++) {
    const N = parseInt(input[1]);
    const numbs = input.slice(2, N + 2).map(Number);
    input.splice(1, N + 1); // 이미 처리한 input 부분을 삭제

    let res = Infinity;

    for (let index = 1; ; index++) {
        let remainder = new Set();
        let flag = true;

        for (let e of numbs) {
            const mod = e % index;
            if (remainder.has(mod)) {
                flag = false;
                break;
            }
            remainder.add(mod);
        }

        if (flag) {
            res = index;
            break;
        }
    }
    console.log(res);
}