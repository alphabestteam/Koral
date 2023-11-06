const spnogesFriends = ['Sandy', 'Patrick' , 'Squidward' , 'Ms. Krabs' , 'Gary']
console.log(spnogesFriends)
console.log(spnogesFriends.length)

spnogesFriends.push('Mrs. Puff')
console.log(spnogesFriends)
console.log(spnogesFriends.length)

spnogesFriends[0] = 'PEarl'
console.log(spnogesFriends)

/*
The const before the name of the list does not defines a constant array,
it defines a constant reference to an array,
and thats why we can change the values of the list
*/