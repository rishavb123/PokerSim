from dataclasses import dataclass
from hydra.core.config_store import ConfigStore
from experiment_lab.core import BaseConfig


@dataclass
class PokerConfig(BaseConfig):
    population_size: int = 1
    n_agents: int = 1
    n_iterations: int = 1
    n_children: int = 1
    keep_top_n: int = 0

    def __post_init__(self) -> None:
        return super().__post_init__()


def register_configs():
    cs = ConfigStore.instance()
    cs.store(name="poker_config", node=PokerConfig)