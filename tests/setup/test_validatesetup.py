def _inc(x):
        return x + 1


def test_pass():
    """Just make sure asserts work."""
    assert _inc(4) == 5


def test_pythonnetworks():
    import clr
    clr.AddReference("System")
    from System import String
    s = String("teststring")
    assert "teststring" == s
