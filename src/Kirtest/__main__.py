from Kirtest.core.discovery import Discovery


def main():
    discover = Discovery()
    print(f"Discovered tests path: {discover.path}")


if __name__ == "__main__":
    main()
