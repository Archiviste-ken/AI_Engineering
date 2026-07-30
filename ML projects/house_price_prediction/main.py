from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parent
    data_path = project_root / "data" / "housing.csv"

    print("House price prediction project scaffold")
    print(f"Expected dataset: {data_path}")


if __name__ == "__main__":
    main()
