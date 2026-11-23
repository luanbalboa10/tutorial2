import matplotlib.pyplot as plt
from pathlib import Path

anos = [2021, 2022, 2023, 2024, 2025]
campeoes = ["Palmeiras", "Flamengo", "Fluminense", "Botafogo", "Flamengo"]

cores = {
    "Palmeiras": "#008445",
    "Flamengo": "#C3281E",
    "Fluminense": "#8B1A1A",
    "Botafogo": "#222222",
}

plt.figure(figsize=(9, 5))
plt.bar(
    [str(ano) for ano in anos],
    range(1, 6),
    color=[cores[campeao] for campeao in campeoes],
)

for i, campeao in enumerate(campeoes):
    plt.text(i, i + 1, campeao, ha="center", va="bottom", fontsize=11, fontweight="bold")

plt.title("Últimos 5 campeões da Copa Libertadores")
plt.xlabel("Ano")
plt.ylabel("")
plt.yticks([])
plt.tight_layout()

assets_dir = Path(__file__).parent / "assets"
assets_dir.mkdir(exist_ok=True)
plt.savefig(assets_dir / "campeoes-libertadores.png", dpi=150, bbox_inches="tight")

plt.show()
