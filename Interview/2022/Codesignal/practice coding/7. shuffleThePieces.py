def shuffleThePieces(arr, pieces):
    pointer = 0
    while pointer < len(arr):
        if not pieces:return False
        cur = None
        for i, piece in enumerate(pieces):
            if piece[0] == arr[pointer]:
                pointer += 1
                cur = piece
                pieces[i], pieces[-1] = pieces[-1], pieces[i]
                pieces.pop()
                break
        if not cur: return False
        for i in range(1, len(cur)):
            if cur[i] != arr[pointer]:return False
            else:
                pointer += 1
    return True

arr = [1, 5, 4, 3, 2, 8]
pieces = [[4, 3], [1, 5], [2]]
print(shuffleThePieces(arr, pieces))