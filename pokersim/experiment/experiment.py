from typing import Any
import logging
from experiment_lab.core import BaseExperiment

from pokersim.experiment.config import PokerConfig

logger = logging.getLogger(__name__)

class PokerExperiment(BaseExperiment):

    def __init__(self, cfg: PokerConfig) -> None:
        self.cfg = cfg
        self.initialize_experiment()

    def initialize_experiment(self) -> None:
        super().initialize_experiment()

    def single_run(
        self, run_id: str, run_output_path: str, seed: int | None = None
    ) -> Any:
        logger.info("RUNNING POKER EXPERIMENT")