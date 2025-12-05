def Constructor(pieces: int, people: int, cars: int, trees: int) -> int:
    piece = pieces//72
    peopl = people//4
    car = cars//2
    tree = trees//7
    return min(piece, peopl, car, tree) 
