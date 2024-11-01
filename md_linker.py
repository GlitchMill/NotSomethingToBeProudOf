import os
import re
import networkx as nx
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
folder_path = os.getenv("MARKDOWN_FOLDER")

def find_md_files(folder_path):
    """Find all Markdown files in the given folder."""
    if not os.path.isdir(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return []  # Return an empty list if folder doesn't exist
    return [f for f in os.listdir(folder_path) if f.endswith('.md')]

def extract_links(file_path, folder_path):
    """Extract links from a Markdown file that point to other Markdown files."""
    links = []
    with open(os.path.join(folder_path, file_path), 'r') as file:
        content = file.read()
        # Match links in the format [[other_file.md]] or [link text](other_file.md)
        link_pattern = r'\[\[([^\]]+\.md)\]\]|\[.*?\]\(([^)]+\.md)\)'
        matches = re.findall(link_pattern, content)
        for match in matches:
            # Get the matched link (either in the first or second group)
            linked_file = match[0] if match[0] else match[1]
            links.append(linked_file)
    return links

def create_graph(folder_path):
    """Create a graph from Markdown file links."""
    G = nx.DiGraph()  # Directed graph to show direction of links
    md_files = find_md_files(folder_path)

    if not md_files:
        print("No Markdown files found.")
        return G

    for md_file in md_files:
        G.add_node(md_file)  # Add each markdown file as a node in the graph
        links = extract_links(md_file, folder_path)
        for link in links:
            if link in md_files:  # Only link if target is also in the folder
                G.add_edge(md_file, link)

    return G

def plot_graph(G):
    """Plot the graph using matplotlib."""
    if not G.nodes:
        print("No graph to plot (no Markdown files or links found).")
        return

    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G, seed=42)  # Layout for visual organization

    # Draw the graph
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', edgecolors='black')
    nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

    plt.title("Markdown Files Link Graph")
    plt.axis("off")  # Hide the axes

    # Save the plot as an image file
    plt.savefig("markdown_link_graph.png")
    print("Graph saved as 'markdown_link_graph.png'")


def main():
    if not folder_path:
        print("Please set the MARKDOWN_FOLDER environment variable in your .env file.")
        return

    G = create_graph(folder_path)
    plot_graph(G)

# Run the main function
if __name__ == "__main__":
    main()
