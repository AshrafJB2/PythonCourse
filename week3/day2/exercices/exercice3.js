let num = prompt("Enter a number")
while (Number(num) < 11 || isNaN(num)) {
    num = prompt("Enter a new number")
}
alert("thanks")