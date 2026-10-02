from nexora.config import Settings


def test_settings_load_defaults() -> None:
    settings = Settings(_env_file=None)

    assert settings.app_name == "Nexora"
    assert settings.environment == "dev"
    assert settings.log_level == "INFO"
    assert settings.database_url == ""


def test_settings_load_custom_values() -> None:
    settings = Settings(
        _env_file=None,
        app_name="Nexora-Test",
        environment="testing",
        log_level="DEBUG",
        database_url="sqlite:///test.db",
    )

    assert settings.app_name == "Nexora-Test"
    assert settings.environment == "testing"
    assert settings.log_level == "DEBUG"
    assert settings.database_url == "sqlite:///test.db"
