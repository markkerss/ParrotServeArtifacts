# Copyright (c) 2023 by Microsoft Corporation.
# Licensed under the MIT license.


# Constants for Parrot

# NOTE(chaofan): All time constansts (with the name of *_TIME, *_INTERVAL) are in seconds.

# ---------- HTTP Server ----------
DEFAULT_SERVER_HOST = "0.0.0.0"
DEFAULT_OS_SERVER_PORT = 9000
DEFAULT_ENGINE_SERVER_PORT = 9001
DEFAULT_OS_URL = f"http://{DEFAULT_SERVER_HOST}:{DEFAULT_OS_SERVER_PORT}"
DEFAULT_ENGINE_URL = f"http://{DEFAULT_SERVER_HOST}:{DEFAULT_ENGINE_SERVER_PORT}"

# ---------- Poll Interval ----------
VM_HEARTBEAT_INTERVAL = 5
ENGINE_HEARTBEAT_INTERVAL = 3
OS_LOOP_INTERVAL = 0.0001
# The engine need a very short interval, prevent it from affecting the performance of LLM
ENGINE_LOOP_INTERVAL = 0.000001

# NOTE(chaofan): HEARTBEAT_INTERVAL + LOOP_INTERVAL < EXPIRE_TIME
VM_EXPIRE_TIME = 999999
ENGINE_EXPIRE_TIME = 999999

# ---------- Chunk Related ----------
FILL_NO_CHUNK = -1
PIPELINE_SEND_CHUNK_NUM = 128
DETOKENIZE_CHUNK_NUM = 256
STREAMING_END_TOKEN_ID = -1

# ---------- Recycle Pool ----------
PROCESS_POOL_SIZE = 4096
THREAD_POOL_SIZE = 4096
CONTEXT_POOL_SIZE = 4096
ENGINE_POOL_SIZE = 4096

# ---------- Engine ----------
LATENCY_ANALYZER_RECENT_N = 20
# EngineType(Enum)
ENGINE_TYPE_BUILTIN = "builtin"
ENGINE_TYPE_OPENAI = "openai"
ENGINE_TYPE_MLCLLM = "mlcllm"
ENGINE_TYPES = [
    ENGINE_TYPE_BUILTIN,
    ENGINE_TYPE_OPENAI,
    ENGINE_TYPE_MLCLLM,
]

# ---------- None Number ----------
NONE_THREAD_ID = -1
NONE_CONTEXT_ID = -1
NONE_PROCESS_ID = -1
UNKNOWN_DATA_FIELD = -1
