let sentence = "The movie is not that bad, I like it";
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");
console.log(wordNot);
console.log(wordBad);
let t = sentence.split("");
if (wordNot < wordBad) {
  t.splice(wordNot, wordBad - wordNot + 3, "good");
}

console.log(t.join(""));