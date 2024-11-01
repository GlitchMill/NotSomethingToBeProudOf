# Teacher Binary Tree Visualization

The project requires a `config.json` file to load teacher data. Here is a sample structure for the `config.json`:

```json
{
    "teachers": [
        {
            "name": "Alice Johnson",
            "subject": "Mathematics",
            "subject_code": "MATH101",
            "score": 95
        },
        {
            "name": "Bob Smith",
            "subject": "Science",
            "subject_code": "SCI102",
            "score": 85
        },
        {
            "name": "Charlie Brown",
            "subject": "English",
            "subject_code": "ENG103",
            "score": 90
        }
    ]
}
```

### Fields Explained

- **name**: The name of the teacher.
- **subject**: The subject taught by the teacher.
- **subject_code**: The subject code for the course.
- **score**: The score of the teacher, which is used to determine their ranking.

## Usage

1. Ensure you have Python 3 and `matplotlib` installed on your system.
2. Create a `config.json` file in the same directory as the script with the teacher data.
3. Run the script using the following command:

```bash
python teacher_btree.py
```

4. The script will generate a binary tree visualization and save it as `teacher_ranking_tree.png` in the same directory.

## Example Output

The output will be a PNG image representing the binary tree structure of teachers based on their scores. Each node in the tree includes:

- Teacher's Name
- Subject
- Subject Code
- Score
- Rank

## Troubleshooting

- **If you encounter a "FileNotFoundError" related to `config.json`**:

  - Ensure the file exists in the same directory as the script.
  - Check the file's structure and formatting.
- **If you see a graph that is skewed**:

  - Adjust the parameters in the drawing method of the script, such as the offsets for left and right children.

## License

This project is open-source and available for use under the MIT License.

## Acknowledgments

- This project uses `matplotlib` for visualization.
