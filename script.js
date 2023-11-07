const speciesPoints = {
    'pink spotted': 4,
    'blue stinger': 3,
    'green itches': 2
};

const jellyfishDays = [
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'white'},
        { color: 'white'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'green'},
        { color: 'green'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
    ]
];


// SpongeBob's net callback function
function catchJellyfish(jellyfish, identifyJellyfishAndAddPoints) {
    console.log(`Spongebob Caught A ${jellyfish.color} Jellyfish!`);
    identifyJellyfishAndAddPoints(jellyfish, addPoints);
    
}


// Patrick's net callback function
function identifyJellyfishAndAddPoints(jellyfish, addPoints) {
    const specie = identifySpecies(jellyfish.color);
    console.log(`Patrick Identified A ${specie} Jellyfish!`);
    addPoints(specie);
    
}


// Score keeping callback function
function addPoints(species) {
    if(speciesPoints[species]){
        points += 1;
    }
    else{
        points += speciesPoints[species]
    }   
    console.log(`The Score:${score}`)
}


// Helper functions
function identifySpecies(jellyfish) {
    for (let specie in speciesPoints){
        if (jellyfish === specie.split(' ')[0]){
            return specie;
        }
    }
    return "Common";
}


//The Adventure Starts Here! 
for (const day of jellyfishDays){
    console.log("Let's Go Jellyfishing!");

    for (const jellyfish of day){
        catchJellyfish(jellyfish, identifyJellyfishAndAddPoints);
    }

    console.log(`Great Job, Spongebob And Patrick! \nThe Final Score: 15`);
    score = 0;
}