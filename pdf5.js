let input = document.createElement(`p`);

function calculateGrade(){
    let charGrade = '';
    const grade = parseInt(document.getElementById("grade").value);

    if (!isNaN(grade)){
        if (grade == 100){
            charGrade = "A+";
        }
        else if (grade <= 99 && grade >= 90){
            charGrade = "A";
        }
        else if (grade <= 89 && grade >= 80){
            charGrade = "B";
        }
        else if (grade <= 79 && grade >= 70){
            charGrade = "C";
        }
        else if (grade <= 69 && grade >= 60){
            charGrade = "D";
        }
        else if (grade <= 59 && grade >= 50){
            charGrade = "E";
        }
        else if (grade < 50 && grade >= 0){
            charGrade = "F";
        }
        else if (grade > 100 || grade < 0){ // input validation - input is less then 0 or more then 100
            input.innerText = "Please Enter A Number Between 0 And 100";
            return;
        }
    }
    else{
        input.innerText = "Please Enter A Number!";

    }

    switch(charGrade){
        case "A+":
            input.innerText = "Perfect!";
            break;
        case "A":
            input.innerText = "Amazing!";
            break;
        case "B":
            input.innerText = "Nicely Done!";
            break;
        case "C":
            input.innerText = "This Is Fine!";
            break;
        case "D":
            input.innerText = "You Can Do Better!";
            break;
        case "E":
            input.innerText = "Moed B Is An Option!";
            break;
        case "F":
            input.innerText = "Moed B Is A Must!";
            break;
    }
    document.getElementById("separator").appendChild(input);
}


let button = document.getElementById("button").addEventListener("click", calculateGrade);
