text = ` Kung Fu Panda is a beloved animated movie about a clumsy, 
food-loving panda named Po who dreams of becoming a kung fu master.\nPo's
dream becomes a reality when he is unexpectedly chosen to become the 
Dragon Warrior and train with the Furious Five to protect the Valley of 
Peace from the evil Tai Lung.\nKung Fu Panda was released on June 6, 2008, 
and grossed over $631 million worldwide, making it the highest-grossing 
non-sequel animated film at the time of its release.\nAlong the way, Po 
learns valuable lessons about inner strength, perseverance, and the 
importance of family and friendship.\nWith stunning animation, a 
heartwarming story, and a star-studded cast including Jack Black, Angelina 
Jolie, and Jackie Chan, Kung Fu Panda has become a timeless classic for 
all ages. `


arrayFullOfParagraphs = (text) => {return Array(text.split(".\n"));}


changeOccurrence = (text) => {return text.replace("movie", "film");}


changeAllOccurrence = (text) => {return text.replaceAll("Panda", "Bear");}


textToUpperCase = (text) => {return text.toUpperCase();}


textToLowerCase = (text) => {return text.toLowerCase();}


findIndexOfPo = (text) => {return text.indexOf("Po");}


slicingToPo = (text) => {return text.slice(findIndexOfPo());}


noWhiteSpaces = (text) => {return text.trim();}


sliceFromPoToEndPara = (text) => {return text.substr(84, text.indexOf("\n", 84) - 84 );}


arrayFullOfWords = (text) => {return Array(noWhiteSpaces(text).split(" "));}


isEndsWithAges = (text) => {return arrayFullOfWords(text)[0][124] == "ages.";}


addString = (text) => {return text + "is one of my favorite movies!";}
