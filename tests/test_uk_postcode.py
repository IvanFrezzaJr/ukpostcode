import pytest
from uk_postcode import postcode


def test_simple():

    data = [
        "EC1A 1BB",
        "W1A 0AX",
        "M1 1AE",
        "B33 8TH",
        "CR2 6XH",
        "DN55 1PT"
    ]

    for s in data:
        assert True == postcode._simple(s)

    data = [
        "DN55 1P",
        "invalid",
    ]
  
    for s in data:
        assert False == postcode._simple(s)

    
    data = [
        False,
        0
    ]

    for s in data:
        with pytest.raises(TypeError):
            postcode._simple(s)



def test_special():

    data = [
        "ASCN 1ZZ",
        "BBND 1ZZ",
        "BIQQ 1ZZ",
        "FIQQ 1ZZ",
        "GX11 1AA",
        "PCRN 1ZZ",
        "SIQQ 1ZZ",
        "STHL 1ZZ",
        "TDCU 1ZZ",
        "TKCA 1ZZ",
    ]

    for s in data:
        assert True == postcode._special(s)

    data = [
        "DN55 1P",
        "invalid",
    ]
  
    for s in data:
        assert False == postcode._special(s)

    
    data = [
        False,
        0
    ]

    for s in data:
        with pytest.raises(TypeError):
            postcode._special(s)

     