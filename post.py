#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Dec 2022
# This program formats your adress for post


# This function formats address
def format_address(
    full_name,
    street_number,
    street_name,
    city,
    province,
    postal_code,
    apartment_number=None,
):

    # return proper address

    formatted = full_name + "\n"
    formatted = formatted + str(street_number)
    if apartment_number != None:
        formatted = formatted + "-" + str(apartment_number)
    formatted = formatted + " " + street_name + "\n"
    formatted = formatted + city + " "
    formatted = formatted + province + "  "
    formatted = formatted + postal_code

    return formatted


def main():
    # main function

    # input
    print("This program reformats your address into a mailing address.")
    apartment_number = None

    full_name = input("Enter your full name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question == "y":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name and type: ")
    city = input("Enter your city: ")
    province = input("Enter your province as an abbreviation: ")
    postal_code = input("Enter your postal code: ")

    # process
    try:
        if apartment_number != None:
            apartment_number = int(apartment_number)
        street_number = int(street_number)
        # calls function
        proper_address = format_address(
            full_name,
            street_number,
            street_name,
            city,
            province,
            postal_code,
            apartment_number,
        )
        # output
        print("\n")
        print(proper_address.upper())
    except ValueError:
        print("\nThat is an invalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
