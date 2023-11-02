/*
EX 1: 

alert - the "alert" commend is an alert box that pops up when some event happens, for example if the user clicked the "OK" button, an alert box will pop and say something
alert("nice click!");

prompt - the "prompt" commend is an prompt box that allowing the user to insert an input in the alert box.
prompt("Please enter your name")

confirm -the "confirm" commend is an confirm box that used when the developer wants to verify ot accept something. the confirm box lets you click on the "ok" (returns true) or cancel (returns false).

*/
let flag = false;
while (flag == false){
    alert("BobSponge, Patrick Got lost, You Need To Go And Find Him!"); 
    if (confirm("Are You Going To Find Him ? ")) {
        alert("Lets Go On A Trip! ");
        const answer = prompt("Did You Found BobSponge? ");
        if (answer === "yes"){
        flag == true;
        alert("Yay!! BobSponge Found!")
        }  
     }  else {
        flag = false
        }   
}

