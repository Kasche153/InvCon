from dotenv import load_dotenv, find_dotenv
import os
INVARIANT_STYLE = "VERISOL"
#INVARIANT_STYLE = "DAIKON"

RESULT_DIR = "./sok/result"
ENABLE_CACHE = True
CACHE_DIR = "./sok/cache"

# OPTION FOR ALL Falsified Invariants in the Output
ALLOW_FASIFY_INV = True

# OPTION FOR DISABLE IMPLICATION INVARIANTS
DISABLE_IMPLICATION_INV = True

# OPTION FOR Invariant Reduction with Dependency-based Pruning
ENABLE_INV_REDUCTION = False

# OPTION FOR Matching State Variables with Dynamic Storage Value Update
ENABLE_READ_MODEL_FLATTENVALUE = True
load_dotenv()


ETHERSCAN_API_KEY=os.environ.get("ETHERSCAN_API_KEY")
QUICKNODE_API_KEY=os.environ.get("QUICKNODE_API_KEY")

