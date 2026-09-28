"""jgrep's view of the JevKit runtime: the providers it offers, in the order it prefers them."""

from jevkit_runtime import Provider, catalog

# OpenJEV — a free community gateway to the same Jev model (https://openjev.sh).
# TypeSafe stays the default; OpenJEV is picked only when it is the only key set,
# or when the user asks for it explicitly with --api openjev / JEV_API=openjev.
OPENJEV = Provider(
    "openjev",
    "https://api.openjev.sh/v1/systemone",
    "openjev",
    "OPENJEV_API_KEY",
    title="OpenJEV (free community gateway to Jev)",
    max_request_tokens=64_000,
    max_read_tokens=32_000,
)

PROVIDERS = catalog("typesafe", "openrouter", OPENJEV, "gateway", "diffusiongemma", "laya", "gliner")
