NOIR_STYLE_SUFFIX = (
    "film noir style, dramatic black and white, high contrast lighting, "
    "hard venetian blind shadows, rain-slicked streets, cinematic 1940s "
    "detective mood, deep shadows, fog, moody atmosphere"
)


def build_noir_prompt(description: str) -> str:
    description = description.strip()
    if not description:
        raise ValueError("description must not be empty")
    return f"{description}, {NOIR_STYLE_SUFFIX}"
