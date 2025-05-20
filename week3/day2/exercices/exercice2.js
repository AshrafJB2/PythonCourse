const colors = ["blue", "orange", "yellow", "red", "grey"]

for (const key in colors) {
    console.log(`My #${parseInt(key) + 1} choise is ${colors[key]}`)
}