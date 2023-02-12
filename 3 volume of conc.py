def concrete(build_type, x_len, y_len):
    dimensions = {
        "residential": 0.25,
        "commercial": 0.5
    }
    return dimensions[build_type] * x_len * y_len


print(concrete(input("build type"), float(input("length of x")), float(input("length of y"))) + "m(cubed)")
