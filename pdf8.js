/*
EX1 :

The difference between arr[index] and arr.at(index) is that arr.at[index] accepts negative integers,
which means we can count back from the last item in the array,
which you can't do in arr[index]
*/


arrTimesTheChar = (charInput, numberInput) => {return Array(numberInput + 1).join(charInput);}


function PutDownFromLast(arrayInput , numberInput){
    if (numberInput > arrayInput.length)
        {
            return "Size Is Bigger Then Array Length!";
        }
        else{
            for (let i = 0; i < numberInput; i++){
                arrayInput.pop(arrayInput.at(i));
            }
        }
        return arrayInput;
}


pushInStart = (arrayInput, numberInput) => {arrayInput.unshift(numberInput);}


twoArraysRoOne = (arrayInput1, arrayInput2) => {newArr = arrayInput1.concat(arrayInput2); return newArr}


toUpperCase = (stringsArrayInput) => {let uppers = stringsArrayInput.map(function(x) { return x.toUpperCase(); }); return uppers}


filterTwoDigit = (numbersArrayInput) => {return numbersArrayInput.filter(function(number) {return number >= 10 && number <= 99;});}


isInArray = (arrayInput, para) => {return arrayInput.includes(para);}


firstCellBiggerThenTen = (numbersArrayInput) => {return numbersArrayInput.find(function(number) {return number > 10;});}


twoFunctionsTogether = (numbersArrayInput) => {
    if (isInArray(numbersArrayInput, firstCellBiggerThenTen(numbersArrayInput))){
        return true
    }
    else{
        return false
    }
}

/*
EX 11:

In default sort() uses alphabetic sorting instead of numeric sort 
if no parameter is defined in the () of the sort() commend  
*/

sortFunction = (arrayToSortInput) => {
    arrayToSortInput.sort(function (a, b){
        return a - b;
    })
    return arrayToSortInput;
}


starsInBetween = (stringsArrayInput) => {return stringsArrayInput.sort().join(" ** ");}


sortAlpabticly = (stringsArrayInput) => {return stringsArrayInput.sort(function(a, b) {
    return a.toLowerCase().localeCompare(b.toLowerCase());});}


isSmallerThenThreshold = (number, threshold) => { return number < threshold;}

isAllNumbersSmallerThenThreshold = (numbersArrayInput, threshold) => {return numbersArrayInput.every(function(number) {
    return isSmallerThenThreshold(number, threshold);});}


isBiggerThenThreshold = (number, element) => { return number < element;}

areThereBiggerThenThreshold = (numbersArrayInput, threshold) => {return numbersArrayInput.some(function(element) {
    return isBiggerThenThreshold(threshold, element);});
}





