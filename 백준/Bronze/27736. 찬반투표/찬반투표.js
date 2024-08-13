let input = require('fs').readFileSync(process.platform === 'linux' ? 'dev/stdin' : 'Algorithm/example.txt').toString().replace(/\r/g, '').trim().split('\n');
let N = parseInt(input[0]);
let numbList = input[1].split(' ').map(Number);
let vote = 0;
let invalid = 0;

numbList.forEach((i) => {
    if (i == 1) {
        vote++;
    } else if (i == -1) {
        vote--;
    } else {
        invalid++;
    }
});

if (invalid >= Math.ceil(N / 2)) {
    console.log('INVALID');
} else {
    if (vote > 0) {
        console.log('APPROVED');
    } else if (vote <= 0) {
        console.log('REJECTED');
    } else {
        console.log('INVALID');
    }
}