const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
const newN = names.sort();
let a = "";
for (let i in newN) {
  a += newN[i][0];
}
console.log(a);