// // Remove Blanks

function removeBlanks(s){
    string=s
    arr=s.split(' ')
    console.log(arr.join(''))
}

removeBlanks("I can not BELIEVE it's not BUTTER")


// Get Digits

function getDigits(str) {
    let digits = '';

    for (let i = 0; i < str.length; i++) {
        if (!isNaN(Number(str[i]))) {
            digits += str[i];
        }
    }

    return Number(digits);
}
console.log(getDigits('0s1a3y5w7h9a2t4?6!8?0'))


// Acronyms

function acronym(str) {
    arr = str.toUpperCase().split(' ');
    list = [];

    for (var i = 0; i < arr.length; i++) {
        if (arr[i] !== '') {
            list.push(arr[i][0]);
        }
    }

    newString = list.join('');
    return newString;
}

console.log(acronym("Live from New York, it's Saturday Night!"));



// Count Non-Spaces

function countNonSpaces(str) {
    let count = 0;

    for (let i = 0; i < str.length; i++) {
        if (str[i] !== ' ') {
            count++;
        }
    }

    return count;
}

console.log(countNonSpaces("Hello world !"))




// Remove Shorter Strings

function removeShorterStrings(arr, value) {
    result = [];

    for (let i = 0; i < arr.length; i++) {
        if (arr[i].length >= value) {
            result.push(arr[i]);
        }
    }

    return result;
}

console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'],4))

