"""
Write a library that supports validating and formatting post codes for UK. 
The details of which post codes are valid and which are the parts they consist of can be found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting. 
The API that this library provides is your choice.
"""
    
import argparse
import postcode


def main(args: argparse.Namespace) -> None:
    """ gets the argument and send to the function to print
    """
    ukpostcode = args.ukpostcode

    ukpostcode_sanitised = str.upper(ukpostcode.replace(" ", ""))


    check = postcode.validate(ukpostcode_sanitised)

    if not check:
        raise ValueError("UK Postcode not valid")

    ukpostcode_formatted = postcode.format_(ukpostcode_sanitised)

    print(f"UK postcode {ukpostcode_formatted} was validated and formatted successfully")
    return ukpostcode_formatted


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Library to validating and formatting post codes for UK.')
    parser.add_argument('-c', '--ukpostcode', 
                        type=str, 
                        required=True,
                        help='UK postcode')

    args = parser.parse_args()
  
    main(args)