helloWorld = () => {return "Hello World!";}


helloName = (nameInput) => {return `Hello ${nameInput}!`;}


squareThatNumber = (numberInput) => {return numberInput * numberInput;}


areaOfARectangle = (side1, side2) => {return side1 * side2;}


getInfoAboutCircle = (radios) => {arrayCircle = []; arrayCircle[0] = 2 * 3.14 * radios; arrayCircle[1] = 3.14 * radios * radios; return arrayCircle;}


countScoringLetters = (stringInput) => {const vowels = stringInput.match(/[AEIOU]/gi);
return vowels ? vowels.length : 0;}


isSameLength = (array1, array2) => {return array1.length == array2.length;}


convertToArray = (numberInput) => {return String(numberInput).split('');}


booleanArray = (arrayInput) => {return arrayInput.map((item) => Boolean(item));}


