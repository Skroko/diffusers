from ...utils import _LazyModule


_import_structure = {}
_import_structure["pipeline_score_sde_ve"] = ["ScoreSdeVePipeline"]

import sys


sys.modules[__name__] = _LazyModule(
    __name__,
    globals()["__file__"],
    _import_structure,
    module_spec=__spec__,
)
