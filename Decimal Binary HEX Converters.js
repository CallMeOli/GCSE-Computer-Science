// Binary & Denary
const denaryToBinary = (num, split) => {
    // Convert to binary
    /*
    Denary: 11
             Q | R
    11 / 2 = 5 | 1
    5  / 2 = 2 | 1
    2  / 2 = 1 | 0
    1  / 2 = 0 | 1
    Binary: 1011
    */
    let quotient = Math.floor(num / 2);
    let remainder = num % 2;
    let remainders = [remainder];
    while (quotient >= 1) {
        let prevQuotient = quotient;
        quotient = Math.floor(prevQuotient / 2);
        remainder = prevQuotient % 2;
        remainders.push(remainder);
    };
    // Split binary [ 01010101 -> 0101 0101 ]
    if (split) {
        for (i in remainders) {
            if (i % 4 == 0) {
                remainders[i] = remainders[i].toString() + ' ';
            };
        };
    };
    // Reverse the remainders array and join the values into a string
    remainders = remainders.reverse().join('');
    // Add 0's for readability [ 101011 -> 00101011 ]
    remainders = '0'.repeat(4 - remainders.split(' ')[0].length) + remainders;
    return remainders;
};

const binaryToDenary = binary => {
    // Reverse binary (string or number) as a string
    binary = binary.toString().split('').reverse().join('');
    // Convert to denary
    /*
    Binary: 1010
      Solve right to left (reversed)
        0 * 2^0 = 0
        1 * 2^1 = 2
        0 * 2^2 = 0
        1 * 2^3 = 8
        0 + 2 + 0 + 8 = 10
    Denary: 10
    */
    let sum = 0;
    for (i in binary) {
        sum += binary[i] * 2**i;
    };
    return sum;
};

// Hex & Denary
const denaryToHex = num => {
    // Convert to hexadecimal
    /*
    Denary: 143
               Q | R
    143 / 16 = 8 | 15
    8   / 16 = 0 | 8
    Hexadecimal: 8F
    */
    let quotient = Math.floor(num / 16);
    let remainder = num % 16;
    let remainders = [remainder];
    while (quotient >= 1) {
        let prevQuotient = quotient;
        quotient = Math.floor(prevQuotient / 16);
        remainder = prevQuotient % 16;
        remainders.push(remainder);
    };
    // Convert remainders to hexadecimal values
    const translations = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    };
    for (i in remainders) {
        let num = remainders[i];
        if (num > 9) {
            remainders[i] = translations[num];
        };
    };
    // Reverse the remainders array and join the values into a string
    remainders = remainders.reverse().join('');
    return remainders;
};

const hexToDenary = hex => {
    let numbers = [];
    const translations = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    };
    for (num of hex) {
        if (isNaN(num)) {
            numbers.push(translations[num]);
        } else {
            numbers.push(num);
        };
    };
    numbers = numbers.reverse();
    let sum = 0;
    for (i in numbers) {
        sum += numbers[i] * 16**i
    }
    return sum;
};

// Hex & Binary
const hexToBinary = (hex, split) => {
    const translations = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    };
    const numbers = hex.split('');
    // Convert each hexadecimal digit to binary
    for (i in numbers) {
        let num = numbers[i];
        if (isNaN(num)) {
            num = translations[num];
        };
        let quotient = Math.floor(num / 2);
        let remainder = num % 2;
        let remainders = [remainder];
        while (quotient >= 1) {
            let prevQuotient = quotient;
            quotient = Math.floor(prevQuotient / 2);
            remainder = prevQuotient % 2;
            remainders.push(remainder);
        };
        // Reverse the remainders array and join the values into a string
        remainders = remainders.reverse().join('');
        // Add 0's
        remainders = '0'.repeat(4 - remainders.split(' ')[0].length) + remainders;
        numbers[i] = remainders;
    }
    // Split binary [ 01010101 -> 0101 0101 ]
    if (split) {
        for (i in numbers) {
            if (i % 4 == 0) {
                numbers[i] = numbers[i] + ' ';
            };
        };
    };
    return numbers.join('');
};

const binaryToHex = binary => {
    // Reverse binary (string or number) as a string
    binary = binary.toString().split('').reverse().join('');
    // Convert to denary
    let denary = 0;
    for (i in binary) {
        denary += binary[i] * 2**i;
    };
    // Convert to hex
    let quotient = Math.floor(denary / 16);
    let remainder = denary % 16;
    let remainders = [remainder];
    while (quotient >= 1) {
        let prevQuotient = quotient;
        quotient = Math.floor(prevQuotient / 16);
        remainder = prevQuotient % 16;
        remainders.push(remainder);
    };
    // Convert remainders to hexadecimal values
    const translations = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    };
    for (i in remainders) {
        let denary = remainders[i];
        if (denary > 9) {
            remainders[i] = translations[denary];
        };
    };
    // Reverse the remainders array and join the values into a string
    return remainders.reverse().join('');
};