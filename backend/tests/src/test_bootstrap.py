from nexora.bootstrap import get_application_name


def test_application_name() -> None:
    assert get_application_name() == "NexoraOS"
