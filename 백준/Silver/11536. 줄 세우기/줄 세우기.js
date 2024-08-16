// 백준 11536번 문제를 fs 모듈을 사용하면 에러 발생함
// readline 사용
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function(line) {
    input.push(line);
}).on('close', function() {
    let N = parseInt(input[0]);
    let list = input.slice(1, N + 1);
    let ansList = JSON.stringify(list);
    // toSorted()로 제출하면 TypeError
    let incList = JSON.stringify([...list].sort());
    let decList = JSON.stringify([...list].sort((a, b) => b.localeCompare(a)));
    
    if (ansList === incList) {
        console.log('INCREASING');
    } else if (ansList === decList) {
        console.log('DECREASING');
    } else {
        console.log('NEITHER');
    }
});
