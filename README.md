# Package Sorting Automation for Robotic Arm

A Python solution to sort packages into appropriate stacks (STANDARD, SPECIAL, REJECTED) based on their dimensions and mass, designed for Thoughtful’s robotic factory automation.

---

## Features
- Determines if a package is **bulky** (volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm).
- Determines if a package is **heavy** (mass ≥ 20 kg).
- Classifies packages into:
  - `REJECTED`: Both bulky and heavy.
  - `SPECIAL`: Either bulky or heavy.
  - `STANDARD`: Neither bulky nor heavy.

---

## Prerequisites
- Python 3.6 or higher

---

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/package-sorting-automation.git
   cd package-sorting-automation

## Usage
1. Import the `sort` function and call it with package dimensions (in cm) and mass (in kg):

   ```python
   from sorter import sort
   
   # Example 1: Standard package
   print(sort(10, 20, 30, 5))  # Output: "STANDARD"
   
   # Example 2: Bulky package (volume = 1,000,000 cm³)
   print(sort(100, 100, 100, 10))  # Output: "SPECIAL"
   
   # Example 3: Rejected package (bulky and heavy)
   print(sort(200, 150, 180, 25))  # Output: "REJECTED"

## Testing
1. Tests are implemented using `pytest`. To run them, first install the required libraries:

   ```bash
   pip install -r requirements.txt

3. Then run the `test_sorter.py`, as:

   ```python
   pytest test_sorter.py -v

### Test Cases Covered
- Standard packages (not bulky/heavy).
- Bulky packages (volume or dimension thresholds).
- Heavy packages (mass threshold).
- Rejected packages (bulky + heavy).
- Edge cases (e.g., exactly 150 cm dimensions, mass = 20 kg).

