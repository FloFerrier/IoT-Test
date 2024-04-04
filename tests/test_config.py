from config import config_read

def test_Config():
    config = config_read("test_config.yaml")
    assert config is not None
    assert "openweathermap" in config is not None
