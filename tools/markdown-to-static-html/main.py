import argparse
import os


def get_args() -> argparse.Namespace:  # Returns the passed arguments
    parser = argparse.ArgumentParser(
        description="A simple markdown to html converter, specific to this project."
    )

    parser.add_argument(
        "filepath", type=str, help="Path pointing to the markdown file."
    )
    parser.add_argument(
        "--outputdir",
        type=str,
        default=".",
        help="The generated html file will be moved to the provided dir.",
    )

    args: argparse.Namespace = parser.parse_args()
    return args


def convert_to_html(filepath: str) -> list[str]:
    with open(filepath) as mdfile:
        mdfile_data: list[str] = mdfile.readlines()

    html_code: list[str] = []
    for mdline in mdfile_data:
        words: list[str] = mdline.strip().split(" ")
        bold_open: bool = False
        italic_open: bool = False
        html_line: str = ""

        # Header: ### Header 3
        if mdline.startswith("#"):
            hastag_count = words[0].count("#")
            header_text = " ".join(words[1:])  # join words to form string
            html_code.append(f"<h{hastag_count}>{header_text}</h{hastag_count}>")

        # List: - List item
        elif mdline.startswith("-"):
            list_text = " ".join(words[1:])
            html_code.append(f"<li>{list_text}</li>")

        else:
            # Subline formatting
            formatted_words = []
            for word in words:

                # Bold: **text**
                if word.startswith("**") and word.endswith("**") and len(word) > 4:
                    formatted_words.append(f"<strong>{word[2:-2]}</strong>")
                elif word.startswith("**"):
                    bold_open = True
                    formatted_words.append(f"<strong>{word[2:]}")
                elif word.endswith("**") and bold_open:
                    bold_open = False
                    formatted_words.append(f"{word[:-2]}</strong>")
                elif bold_open:
                    formatted_words.append(word)

                # Italic: *text*
                elif word.startswith("*") and word.endswith("*") and len(word) > 2:
                    formatted_words.append(f"<em>{word[1:-1]}</em>")
                elif word.startswith("*"):
                    italic_open = True
                    formatted_words.append(f"<em>{word[1:]}")
                elif word.endswith("*") and italic_open:
                    italic_open = False
                    formatted_words.append(f"{word[:-1]}</em>")
                elif italic_open:
                    formatted_words.append(word)

                else:
                    formatted_words.append(word)

            html_line = " ".join(formatted_words)
            if html_line:
                html_code.append(f"<p>{html_line}</p>")

    return html_code


def main():

    # Parse the arguments
    args: argparse.Namespace = get_args()
    md_filepath: str = args.filepath
    md_filename: str = md_filepath.split("/")[-1]
    outputdir: str = args.outputdir

    # HTML
    html_code: list[str] = convert_to_html(md_filepath)

    # Save file
    html_file_path = os.path.join(outputdir, md_filename) + ".html"
    with open(html_file_path, "w") as file:
        file.writelines(html_code)
    print(f"HTML file created at: {html_file_path}")


if __name__ == "__main__":
    main()
