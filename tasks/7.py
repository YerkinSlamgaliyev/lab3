def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

if __name__ == "__main__":
    grams = float(input("Enter the weight: "))
    ounces = grams_to_ounces(grams)
    print(f"{grams} grams = {ounces:.2f} ounces.")