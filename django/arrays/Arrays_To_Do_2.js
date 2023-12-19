// Reverse
function reverseArray(arr) {
    for (let i = 0; i < arr.length / 2; i++) {
        temp = arr[i];
        arr[i] = arr[arr.length - 1 - i];
        arr[arr.length - 1 - i] = temp;
    }
    return arr;
}

    console.log(reverseArray([1,2,3,4,5]))
    // --------------------
    
    // Rotate
    function rotateArray(arr, steps) {
        rotated = [];
        for (let i = 0; i < arr.length; i++) {
            newIndex = (i + (steps % (arr.length))) % arr.length;
            rotated[newIndex] = arr[i];
        }
    
        return rotated;
    }
    
    console.log(rotateArray([1,2,3,4,5,6],2))
    
    // //////////////////////////////

    
    
    // Filter Range
    function filterRange(arr, min, max) {
        new_arr=[]
        for(i=0; i<arr.length ; i++){
            if (arr[i] > min && arr[i] < max) {
                new_arr.push(arr[i])

            }
        }
        return new_arr;
    }

   console.log(filterRange([5, 7, 2, 9, 12, 4], 3, 8))

//////////////////////////////////////////////////////////////////
    
    // Concat
    function arrConcat(arr1, arr2) {
        for (j = 0; j < arr2.length; j++) {
            arr1.push(arr2[j]);
        }
        
        return arr1;
    }
console.log(arrConcat(['a', 'b'], [1, 2]))    