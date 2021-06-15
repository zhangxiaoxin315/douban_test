import pytest,os,yaml

@pytest.fixture(scope="session")
def env(request):
    print(request.config.rootdir)
    config_path = os.path.join(request.config.rootdir,
                               "config",
                               request.config.getoption("environment"),
                               "config.yaml")
    with open(config_path,encoding="UTF-8") as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or pre or pro")