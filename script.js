function sequenceA() {
    setTimeout(_ => console.log('Sponge'), 0);
    console.log("Bob");
}

function sequenceB(){
    setTimeout(_ => console.log(`🍅 Timeout at B`), 0);
    Promise.resolve().then(_ => console.log('🍍 Promise at B'));
}

function sequenceC(){
    setTimeout(_ => console.log(`🍅 Timeout at C`), 0);
    Promise.resolve().then(_ => setTimeout(console.log('🍍 Promise at C'), 1000));
}

function sequenceD(){
    console.log('Sponge');
    setTimeout(_ => console.log('Square'), 0);
    Promise.resolve().then(_ => console.log('Pants'));
    console.log('Bob');
}

function questionA(){
    sequenceA();
}

function questionB(){
    sequenceB();
}

function questionC(){
    sequenceC();
}

function questionD(){
    sequenceD();
}

function questionE(){
    sequenceB();
    sequenceC();
}

// questionA();

// bob
// sponge
//in this function, the first that will print is the "bob" and not the "sponge", because the bob is a synchronic method that comes before the async one 

// questionB();
// 🍍 Promise at B
// 🍅 Timeout at B
// in this function, the promise will be printed before the settimeout, even tho the time is 0, 
// because promise has a event loop , that gets priorities from the task queue ( where the  setTimeout() is)

// questionC();
// 🍍 Promise at C
// 🍅 Timeout at C
// same as B , doesn't matter how much time the promise will take, it still will b first


// questionD();
// Sponge
// bob
// Pants
// Square  
// the console.log reads synchronic , so it will read by the lines, line after line , then the promise , then the setTimeOut() ,
// like said in other questions

// questionE();
// 🍍 Promise at C
// 🍍 Promise at B
// 🍅 Timeout at B
// 🍅 Timeout at C
// the promises will come first,in the order of the function calls ( by the lines )
// the setTimeOut() will come after , in the order of the lines 
// like explained in other questions