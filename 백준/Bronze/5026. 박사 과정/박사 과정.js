// 제출 코드
let input = require('fs').readFileSync(process.platform === 'linux'? '/dev/stdin' : 'Algorithm/example.txt').toString().replace(/\r/g, '').trim().split('\n');
let N = input[0];
let N_lst = input.slice(1, N + 1);

N_lst.forEach((expression) => {
    if (expression == 'P=NP') {
        console.log('skipped');
    } else {
        let numbers = expression.split('+').map(Number);
        let A = numbers[0], B = numbers[1];
        console.log(A + B);
    }
})

// 리팩토링 코드
// 1. N 자료형 변환
// let N = parseInt(input[0]);

// 2. forEach의 불필요한 파라미터 제거
// 사용되지 않는 '_' 제거 + index 대신 요소 값을 바로 사용
// N_lst.forEach((expression) => {
//     if (expression == 'P=NP') {
//         console.log('skipped');
//     } else {
//         let numbers = expression.split('+').map(Number);

// 3. 조건문을 통한 불필요한 배열 접근 최소화
// else {
//     let [A, B] = expression.split('+').map(Number);
//     console.log(A + B);
// }
