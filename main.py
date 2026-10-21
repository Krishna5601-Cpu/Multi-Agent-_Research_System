from research_system.pipeline import run_research_pipeline


def main() -> None:
    topic = input("\nEnter a research topic: ")
    run_research_pipeline(topic)


if __name__ == "__main__":
    main()
