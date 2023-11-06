const spongebob = new Map([
    ["Main Character", "Spongebob"],
    ["Best Friend", "Patrick"],
    ["Pet", "Gary"],
    ["Word Buddy", "Squidward"],
    ["manager", "Mr. Krabs"],
    ["Teacher", "Mrs. Puff"],
    ["Location", "Bikini Bottom"]
]);

console.log(spongebob)


console.log(Array.from(spongebob.keys()))


console.log(spongebob.get("Location"));


console.log(spongebob.size)


spongebob.delete("Location")


console.log(spongebob.size)


console.log(spongebob)


console.log(spongebob.has("Location"))




