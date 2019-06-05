def make_shirt(size, style):
    print("Make shirt start")
    print("Shirt size = " + str(size))
    print("Shirt style = " + style)

make_shirt(32, "T-shirt")
        
def make_shirt_with_default(size, style = "I love python"):
    print("Make shirt start")
    print("Shirt size = " + str(size))
    print("Shirt style = " + style)

make_shirt_with_default(20)
