const details = {
  my: "name",
  is: "Rudolf",
  the: "reindeer",
};
let message = "";
for (let i in details) {
  message += `${i} ${details[i]} `;
}
console.log(message);