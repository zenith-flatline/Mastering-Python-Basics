#python challenge
def pins_totla(pins_digits):
    sum_digits = 0
    for 

    
def pin_is_ok(pins_digits):
    if pins_digits['fifth'] + pins_digits['third'] == 14 and \
        pins_digits['first'] == pins_digits['second'] * 2 - 1 and \
            pins_digits['fourth'] == pins_digits['second'] + 1 and \
                pins_digits['second'] + pins_digits['third'] == 10 and \
                    if pins_total(pins_digits) == 30:
                        return True

for pins in range(0,100000):
    this_pin = str(pins).zfill(5)
    print(this_pin)

    pins_digits = {}
    pins_digits["first"] = int(this_pin[0])
    pins_digits["second"] = int(this_pin[1])
    pins_digits["third"] = int(this_pin[2])
    pins_digits["fourth"] = int(this_pin[3])
    pins_digits["fifth"] = int(this_pin[4])

    if pin_is_ok(pins_digits:)
        print(pins)

