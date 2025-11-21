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
    in_code_block: bool = False
    code_block_lines: list[str] = []

    for mdline in mdfile_data:
        mdline = mdline.rstrip("\n")
        words: list[str] = mdline.strip().split(" ")
        bold_open: bool = False
        italic_open: bool = False
        html_line: str = ""

        # Code block: ``` ... ```
        if mdline.startswith("```"):
            in_code_block = not in_code_block
            if not in_code_block:
                # Closing code block
                html_code.append('<pre class="md-code"><code>')
                html_code.extend(code_block_lines)
                html_code.append("</code></pre>")
                code_block_lines = []
            continue
        if in_code_block:
            code_block_lines.append(mdline)
            continue

        # Horizontal rule: ---
        if mdline.startswith("---") or mdline.startswith("***"):
            html_code.append('<hr class="md-hr">')
            continue

        # Header: # Header 1, ## Header 2, etc.
        if mdline.startswith("#"):
            hastag_count = words[0].count("#")
            header_text = " ".join(words[1:])
            html_code.append(
                f'<h{hastag_count} class="md-header md-h{hastag_count}">{header_text}</h{hastag_count}>'
            )
            continue

        # Blockquote: > Quote
        if mdline.startswith(">"):
            quote_text = " ".join(words[1:])
            html_code.append(
                f'<blockquote class="md-blockquote">{quote_text}</blockquote>'
            )
            continue

        # List: - item or * item
        if mdline.startswith("-") or mdline.startswith("*"):
            list_text = " ".join(words[1:])
            html_code.append(f'<li class="md-list-item">{list_text}</li>')
            continue

        # Inline formatting
        formatted_words = []
        for word in words:
            # Bold: **text**
            if word.startswith("**") and word.endswith("**") and len(word) > 4:
                formatted_words.append(f'<strong class="md-bold">{word[2:-2]}</strong>')
            elif word.startswith("**"):
                bold_open = True
                formatted_words.append(f'<strong class="md-bold">{word[2:]}')
            elif word.endswith("**") and bold_open:
                bold_open = False
                formatted_words.append(f"{word[:-2]}</strong>")
            elif bold_open:
                formatted_words.append(word)

            # Italic: *text*
            elif word.startswith("*") and word.endswith("*") and len(word) > 2:
                formatted_words.append(f'<em class="md-italic">{word[1:-1]}</em>')
            elif word.startswith("*"):
                italic_open = True
                formatted_words.append(f'<em class="md-italic">{word[1:]}')
            elif word.endswith("*") and italic_open:
                italic_open = False
                formatted_words.append(f"{word[:-1]}</em>")
            elif italic_open:
                formatted_words.append(word)

            # Inline code: `code`
            elif word.startswith("`") and word.endswith("`") and len(word) > 2:
                formatted_words.append(
                    f'<code class="md-inline-code">{word[1:-1]}</code>'
                )
            else:
                formatted_words.append(word)

        # Links: [text](url)
        html_line = " ".join(formatted_words)
        import re

        html_line = re.sub(
            r"\[([^\]]+)\]\(([^)]+)\)",
            r'<a class="md-link" href="\2">\1</a>',
            html_line,
        )

        # Images: ![alt](url)
        html_line = re.sub(
            r"!\[([^\]]*)\]\(([^)]+)\)",
            r'<img class="md-image" src="\2" alt="\1">',
            html_line,
        )

        # Paragraphs
        if html_line:
            html_code.append(f'<p class="md-paragraph">{html_line}</p>')

    return html_code


def main():
    # Parse arguments
    args = get_args()
    md_filepath = args.filepath
    outputdir = args.outputdir

    # Convert markdown to HTML
    html_code = convert_to_html(md_filepath)

    # Prepare output filename
    md_basename = os.path.basename(md_filepath)
    html_filename = os.path.splitext(md_basename)[0] + ".html"
    html_file_path = os.path.join(outputdir, html_filename)

    # Save file
    with open(html_file_path, "w") as f:
        f.write("""<link rel="stylesheet" href="md.css">""")
        f.write("\n".join(html_code))

    print(f"HTML file created: {html_file_path}")


if __name__ == "__main__":
    main()
