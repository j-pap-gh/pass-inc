from src.pass_inc.main import run


def test_placeholder(capsys):
    """
    Simple test to verify the project wiring works.
    """
    run()
    captured = capsys.readouterr()
    assert "pass-inc is running!" in captured.out
