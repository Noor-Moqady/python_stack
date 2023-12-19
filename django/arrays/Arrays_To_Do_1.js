
// pushFront /////////////////////

function pushFront(arr, value) {
    for (var i = arr.length; i > 0; i--) {
        arr[i] = arr[i - 1];  /////////////////// Shift elements to the right starting from the end
    }
    arr[0] = value;
    return arr;
}

console.log(pushFront([5, 7, 2, 3], 8)); 
console.log(pushFront([99], 7));        


// ///////////////////////////////////////

// Pop Front

function PopFront(arr){
    var array=arr;
    new_arr=[];
    for(var i=1;i<array.length;i++){
        new_arr.push(array[i])
    }
    return new_arr
}

console.log(PopFront([0,5,10,15]))

// /////////////////////////////////

// Insert At

function insertAt(arr, index, value) {
    for (let i = arr.length; i > index; i--) {
        arr[i] = arr[i - 1]; /////////////////// Shift elements to the right starting from the end
    }
    arr[index] = value; 

    return arr;
}

console.log(insertAt([100, 200, 5], 2, 311)); 
console.log(insertAt([9, 33, 7], 1, 42));   



// -------------------------------------------


// remove duplicate
function remove_duplicate(arr) {
    uniqueElements = [];

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== arr[i - 1]) {
            uniqueElements.push(arr[i]);
        }
    }

    return uniqueElements;
}

console.log(remove_duplicate([-2,-2,3.14,5,5,10])); 
console.log(remove_duplicate([9,19,19,19,19,19,29])); 



