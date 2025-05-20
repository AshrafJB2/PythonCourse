//Part 1

const people = ["Greg", "Mary", "Devon", "James"];

people.splice(people.indexOf('Greg'),1);

people.splice(people.indexOf('James'),1, "Jason");

people.push("Achraf");

console.log(people.indexOf('Mary'));

let people2 = people.slice(1,people.indexOf("Achraf"));

console.log(people);

console.log(people2);

console.log(people.indexOf("Foo"))

let last = people[people.length-1] 

console.log(last)

//Part 2


for (const person of people) {
   console.log(person)
}


for (const person of people) {
   console.log(person)
   if (person === "Devon") break
}