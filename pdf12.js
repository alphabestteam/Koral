const isThereVowels = (nameStudent) => {
    const vowels = nameStudent.match(/[AEIOU]/gi);
    if (vowels){
        return 1;
    }
    else{
        return 0;
    }
}

avgGradesCalc = (gradesArr) => {let sum = 0;
    for (let i = 0; i < gradesArr.length; i++) {
      sum += gradesArr[i];
    }
    return  sum / gradesArr.length;
}



let Student1 = 
{
    name : "koral",
    age : 19 , 
    grades : [99,100,98,99,100] ,
    avgGrades : function(){
        return avgGradesCalc(this.grades) + isThereVowels(this.name)
    }
}


let Student2 = 
{
    name : "joi",
    age : 16 , 
    grades : [54,96,35,45,8] ,
    avgGrades : function(){
        return avgGradesCalc(this.grades) + isThereVowels(this.name)
    }
}


let Student3 = 
{
    name : "alma",
    age : 12 , 
    grades : [8,5,6,99,3] ,
    avgGrades : function(){
        return avgGradesCalc(this.grades) + isThereVowels(this.name)
    }
}


let Student4 = 
{
    name : "shrill",
    age : 19 , 
    grades : [85,45,93,62,78] ,
    avgGrades : function(){
        return avgGradesCalc(this.grades) + isThereVowels(this.name)
    }
}


let Student5 = 
{
    name : "amor",
    age : 21 , 
    grades : [89,56,89,55,36] ,
    avgGrades : function(){
        return avgGradesCalc(this.grades) + isThereVowels(this.name)
    }
}



students = [Student1, Student2,Student3, Student4, Student5]


students.forEach((student, index) => {
    console.log(`Student ${student.name} has an index of ${index}`);});


for (let i = 0; i < students.length; i++){
    console.log(`name: ${students[i].name}, age: ${students[i].age}, grades: ${students[i].grades}, average: ${students[i].avgGrades()}`);
}
 

/*
   Adults:
*/

adults = students.filter(student => student.age >= 18)

for (let i = 0; i < adults.length; i++){
    console.log(`name: ${adults[i].name}, age: ${adults[i].age}, grades: ${adults[i].grades}, average: ${adults[i].avgGrades()}`);
}


/*
   Cars:
*/



calculate_age = (dateCar) => {return new Date().getFullYear() - dateCar;}


myCar1 = {
    manufacturerCompany : "Porsche",
    model : "911 Carrera ",
    YearOfManufacture : 1963,
    carAge : function(){
        return calculate_age(this.YearOfManufacture)
    }
}


myCar2 = {
    manufacturerCompany : "Lamborgini",
    model : "Urus ",
    YearOfManufacture : 2018,
    carAge : function(){
        return calculate_age(this.YearOfManufacture)
    }
}


cars = [myCar1, myCar2]


for (let i = 0; i < cars.length; i++){
    console.log(`manufacturerCompany: ${cars[i].manufacturerCompany}, model: ${cars[i].model}, YearOfManufacture: ${cars[i].YearOfManufacture}, carAge: ${cars[i].carAge()}`);
}
