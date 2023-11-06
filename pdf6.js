function evalNumbers(inputNumber1, inputNumber2, functionTodO){
    let answer = 0;
    let text = ' '

    switch(functionTodO){
        case "add":
            answer = inputNumber1 + inputNumber2;
            text = `Sum Of ${inputNumber1} and ${inputNumber2} is ${answer}`;
            break;
           
        case "subtract":
            answer = inputNumber1 - inputNumber2;
            text = `Difference Of ${inputNumber1} and ${inputNumber2} is ${answer}`;
            break;

        case "multiply":
            answer = inputNumber1 * inputNumber2;
            text = `Product Of ${inputNumber1} and ${inputNumber2} is ${answer.toFixed(2)}`;
            break;

        case "divide":
            answer = inputNumber1 / inputNumber2;
            text = `Division Of ${inputNumber1} and ${inputNumber2} is ${answer.toFixed(2)}`;
            break;
   
        case "modulus":
            answer = inputNumber1 % inputNumber2;
            text = `Modulus Of ${inputNumber1} and ${inputNumber2} is ${answer.toFixed(2)}`;
            break;
    }
    return text;
}