# 1. Import necessary libraries
# 2. Define a function `simulate_galton_board(rows, balls)`
#    - Create an empty list to store bin counts
#    - Iterate through each ball:
#       - Simulate its movement row-by-row
#       - Each row, randomly decide left (0) or right (1)
#       - Track final bin position based on total right movements
#       - Update the bin counts accordingly
# 3. Save results as a CSV file in `outputs/galton_simulation_results.csv`
# 4. Allow user to specify rows and balls via `config.json`
# 5. If run as a script, execute `simulate_galton_board`