# Closest pairs finder

This Python program allows you to find the closest pairs of points in a 2D plane using two modes:
1. **Graphical User Interface (GUI)**: An interactive interface where you can click to add points and find the closest pairs.
2. **Standalone Script**: A non-GUI version that runs directly and computes the closest pairs for predefined points. You can edit the points and number of closest pairs by modifying the script.

## Requirements

Before running the program, make sure to install the required dependencies using `pip`.

### Install Dependencies

```bash
pip install matplotlib numpy tkinter
```

### How to Use the program

There are two ways you can run the program

#### GUI
* From the directory the scripts are located, open a ternminal
* run the script:
```bash
python pairsGUI.py
```
* A window will open where you can click on the graph to add points
* Enter the \( m \leq \binom{m}{2} \) number of closest pairs you want to find in the textbox under the  label: `Enter number of closest pairs`
* The program will find the m closest pairs, show lines between the closest pairs as well as display the coords and distance in a box at the bottom
* You can edit the number of desired pairs to see different amounts of pairs
* You can reset the graph using the `Reset` button to reset everything to start a new session with new points

#### Standalone script (no GUI)
* From the directory the scripts are located, open a ternminal
* run the script:
```bash
python mClosestPairs.py
```
* The script will calculate the \( m \leq \binom{m}{2} \) pairs with the given points and pairs defined inside the `if __name__ == "__main__":` function and log out the closest pairs coordinates and their distance
* To find different points and a different number of pairs, open the `mClosestPairs.py` file in a text editor and modify line 74 and 75.
* Line 74 contains a list labeled: `pairs` which contains a list of points
* Line 75 contains `m`, the number of closest pairs you want to find