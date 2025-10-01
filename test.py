

def test_escenario():
    from escenario import formar_escenario

    assert formar_escenario("abc") == "abc"
    assert formar_escenario("123") == "123"
    assert formar_escenario("") == ""
    assert formar_escenario("!@#") == "!@#"
    assert formar_escenario("a1b2c3") == "a1b2c3"
