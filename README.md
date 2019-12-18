# config tool
A tool help you to create config and load in an easy way

## Usage

### Define and Writing Config to toml

In Python Code
```python
from typing import NamedTuple
import gxconfig

class DataConfig(NamedTuple):
    root:str = "/home/gawainx/data"
    chkp:str = "chkp"

class ModelConfig(NamedTuple):
    embd_dim:int = 768
    hidden_dim:int = 5

class Config(NamedTuple):
    dataConfig:DataConfig = DataConfig()
    modelConfig:ModelConfig = ModelConfig()

cfg = Config()
gxconfig.save_toml(cfg, "config.toml")
```

Then you can get a toml
```toml
[DataConfig]
root = "/home/gawainx/data"
chkp = "chkp"

[ModelConfig]
embd_dim = 768
hidden_dim = 5
```

### Load from Toml

```python
import gxconfig
from typing import NamedTuple
class DataConfig(NamedTuple):
    root:str = "/home/gawainx/data"
    chkp:str = "chkp"

class ModelConfig(NamedTuple):
    embd_dim:int = 768
    hidden_dim:int = 5

class Config(NamedTuple):
    dataConfig:DataConfig = DataConfig()
    modelConfig:ModelConfig = ModelConfig()

cfg = gxconfig.load_toml("config.toml", Config)
```