const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '');
const N = BigInt(input);

function binarySearch(target) {
    let low = BigInt(0);
    let high = target;
    
    while (low <= high) {
        let mid = (low + high) / BigInt(2);
        let square = mid * mid;
        
        if (square === target) {
            return mid;
        } else if (square < target) {
            low = mid + BigInt(1);
        } else {
            high = mid - BigInt(1);
        }
    }

    return low - BigInt(1);
}

console.log(binarySearch(N).toString());