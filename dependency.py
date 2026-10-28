class Document:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def get_formatted_text(self) -> str:
        return f"=== {self.title.upper()} ===
{self.content}"


class Printer:
    def __init__(self, model_name: str):
        self.model_name = model_name

    # Dependency: Document is used strictly as a method parameter / temporary resource
    def print_document(self, doc: Document) -> None:
        print(f"[{self.model_name}] Initializing print job...")
        print(doc.get_formatted_text())
        print(f"[{self.model_name}] Print job completed successfully.
")


if __name__ == "__main__":
    printer = Printer("HP LaserJet Pro")
    doc = Document("Quarterly Report", "All metrics exceeded expectations by 15%.")

    printer.print_document(doc)
