def predict_price():
    print("Enter car details:")

    year = int(input("Year: "))
    present_price = float(input("Present Price: "))
    kms_driven = int(input("KMs Driven: "))
    fuel_type = int(input("Fuel Type (0=Petrol,1=Diesel,2=CNG): "))
    selling_type = int(input("Selling Type (0=Dealer,1=Individual): "))
    transmission = int(input("Transmission (0=Manual,1=Automatic): "))

    input_data = np.array([[year, present_price, kms_driven,
                             fuel_type, selling_type, transmission]])

    prediction = model.predict(input_data)

    print("\n Predicted Car Price:", prediction[0])

# Run prediction
predict_price()
