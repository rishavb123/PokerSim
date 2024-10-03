"""The main experiment entry point."""

from experiment_lab.core import run_experiment

from pokersim.experiment.config import PokerConfig, register_configs
from pokersim.experiment.experiment import PokerExperiment


if __name__ == "__main__":
    run_experiment(
        experiment_cls=PokerExperiment,
        config_cls=PokerConfig,
        register_configs=register_configs,
        config_path=f"./configs",
        config_name="base",
    )