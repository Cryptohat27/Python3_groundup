def exceptionhandling():

    car = {
        "make": "Subaru",
        "model": "WRX",
        "year": 2013,
        #"color": "blue"
}

    try:
        print(car["color"])

    except:
        print("There is no key of this value")

    finally:
        print("yay you printed something")

exceptionhandling()
