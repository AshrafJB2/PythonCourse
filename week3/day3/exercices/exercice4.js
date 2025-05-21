function hotelCost(nights) {
    return nights * 140;
}

function planeRideCost(destination) {
    destination = destination.trim().toLowerCase();
    if (destination === "london") return 183;
    else if (destination === "paris") return 220;
    else return 300;
}

function rentalCarCost(days) {
    let cost = days * 40;
    if (days > 10) {
        cost *= 0.95;
    }
    return cost;
}

function totalVacationCost() {
    let nights, destination, days;

    while (true) {
        nights = prompt("How many nights will you stay in the hotel?");
        if (!isNaN(nights) && nights !== "" && Number(nights) > 0) {
            nights = Number(nights);
            break;
        }
        alert("Please enter a valid number of nights.");
    }

    while (true) {
        destination = prompt("What is your destination?");
        if (destination && destination.trim() !== "") {
            break;
        }
        alert("Please enter a valid destination.");
    }

    while (true) {
        days = prompt("How many days will you rent the car?");
        if (!isNaN(days) && days !== "" && Number(days) > 0) {
            days = Number(days);
            break;
        }
        alert("Please enter a valid number of days.");
    }

    const hotel = hotelCost(nights);
    const plane = planeRideCost(destination);
    const car = rentalCarCost(days);

    console.log(`The hotel cost: $${hotel}`);
    console.log(`The plane tickets cost: $${plane}`);
    console.log(`The car rental cost: $${car}`);
    console.log(`Total vacation cost: $${hotel + plane + car}`);
}

totalVacationCost();
