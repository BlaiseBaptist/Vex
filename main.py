def blaise_drive(throttle, turn):
    v1 = max(abs(throttle), abs(turn))
    v2 = (1 - abs(turn) / 200) * throttle
    if throttle >= 0 and turn >= 0:
        return v1, v2
    if throttle < 0 and turn >= 0:
        return -v1, v2
    if throttle >= 0 and turn < 0:
        return v2, v1
    if throttle < 0 and turn < 0:
        return v2, -v1


print(blaise_drive(50, 50.0))
