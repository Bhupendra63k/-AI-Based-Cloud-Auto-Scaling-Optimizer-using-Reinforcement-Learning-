from env import CloudEnv

def make_env(config=None):
    """
    Creates and returns the Cloud Environment.

    Args:
        config (dict, optional): Configuration for environment.

    Returns:
        CloudEnv: Initialized environment
    """
    return CloudEnv()


# Optional: metadata for OpenEnv / HuggingFace
ENV_NAME = "CloudAutoScalingEnv"
ENV_DESCRIPTION = "AI-based cloud auto-scaling environment with cost and latency optimization."