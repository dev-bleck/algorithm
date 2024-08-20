const input = require('fs').readFileSync(process.platform==='linux'?'dev/stdin':'Algorithm/example.txt').toString().replace(/\r/g, '');

function findFraction(X) {
    let diagonal = 1;
    let sum = 0;

    // X가 속하는 대각선 찾기
    while (sum + diagonal < X) {
        sum += diagonal;
        diagonal++;
    }

    // 대각선에서의 위치 찾기
    let positionInDiagonal = X - sum;

    // 분자와 분모 계산
    let numerator, denominator;

    if (diagonal % 2 === 0) {
        // 짝수 대각선: 분자가 증가, 분모가 감소
        numerator = positionInDiagonal;
        denominator = diagonal - positionInDiagonal + 1;
    } else {
        // 홀수 대각선: 분자가 감소, 분모가 증가
        numerator = diagonal - positionInDiagonal + 1;
        denominator = positionInDiagonal;
    }

    return `${numerator}/${denominator}`;
}

console.log(findFraction(input));