const isSufficientFuel = (distance, literPerKm, fuelLeft) => {
    return fuelLeft >= distance / literPerKm
}
