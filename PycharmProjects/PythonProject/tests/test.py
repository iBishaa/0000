from backend.filter import apply_filter_cpp
result = apply_filter_cpp([0, 0, 0, 255], 1, 1, "invert")
print(result)  # Має вивести [255, 255, 255, 255]