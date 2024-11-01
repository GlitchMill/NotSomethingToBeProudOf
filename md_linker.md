
# Markdown Link Graph Generator

This project provides a tool to visualize the relationships between Markdown files in a folder by creating a directed graph of links. It is especially useful for exploring interconnected documentation, such as for Data Structures and Algorithms (DSA), knowledge bases, or other projects organized in Markdown files.

## Features

- Automatically detects Markdown files in a specified folder.
- Parses links between Markdown files (e.g., `[[file.md]]` or `[Link](file.md)` formats).
- Generates a directed graph where nodes represent Markdown files, and edges represent links between them.
- Saves the generated graph as an image for easy visualization.

## Example Use Case

If you have Markdown files covering different topics in Data Structures and Algorithms (DSA), such as arrays, linked lists, and graphs, this tool helps you see how each topic links to others, helping you navigate related concepts visually.

## Prerequisites

- Python 3.7 or later
- The following Python libraries:
  - `networkx`
  - `matplotlib`
  - `python-dotenv`

You can install the necessary libraries with:

```bash
pip install networkx matplotlib python-dotenv
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/glitchmill/NotSomethingToBeProudOf.git
   cd NotSomethingToBeProudOf
   ```
2. **Set up the `.env` file**:
   Create a `.env` file in the root directory with the following line:

   ```env
   MARKDOWN_FOLDER=path/to/your/markdown/folder
   ```

   Replace `path/to/your/markdown/folder` with the path to the folder containing your Markdown files.
3. **Add Markdown Files**:
   Place your Markdown files in the specified folder. Ensure they contain links to each other in the format `[[file.md]]` or `[Link](file.md)`.

## Usage

Run the script with:

```bash
python md_linker.py
```

The script will:

- Parse the Markdown files in the specified folder.
- Create a graph of links between the files.
- Save the graph visualization as an image (`markdown_link_graph.png`) in the project directory.

## Example Files

You can use these sample files to test the script. Place them in your Markdown folder.

### `introduction.md`

```markdown
# Introduction to Data Structures and Algorithms
Explore [Arrays](arrays.md), [Linked Lists](linked_lists.md), and [Graphs](graphs.md) as foundational structures in DSA.
```

### `arrays.md`

```markdown
# Arrays
Arrays are contiguous memory structures. Check out [Linked Lists](linked_lists.md) for a more dynamic alternative or proceed to [Graphs](graphs.md).
```

### `linked_lists.md`

```markdown
# Linked Lists
Linked lists allow efficient insertions. Next, explore [Graphs](graphs.md) to see more complex relationships.
```

### `graphs.md`

```markdown
# Graphs
Graphs model pairwise relations. Begin with [Introduction](introduction.md) if you're just starting out.
```

## Output

After running the script, you should see a file called `markdown_link_graph.png` in your project directory. This image shows a graph where each node represents a Markdown file, and each arrow represents a link from one file to another.

## Troubleshooting

- **FileNotFoundError**: Make sure the folder path in your `.env` file is correct and that it contains Markdown files.
- **Empty Graph**: If no links are detected, ensure your files contain links to each other using `[[filename.md]]` or `[Link](filename.md)` syntax.

## Contributing

Feel free to submit issues or pull requests if you'd like to improve the functionality or add new features.

---

## License

This project is licensed under the MIT License.
