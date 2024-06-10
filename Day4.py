# Lists 
# List Methods:

companies = ["Google", "Facebook", "Meta", "Netflix"]

# Append 
companies.append("Apple")
print(f"Append: {companies}")

# Insert 
companies.insert(2, "CISCO")
print(f"Insert: {companies}")

# Remove
companies.remove("Facebook")
print(f"Remove: {companies}")

# Copy
# Shallow Copy
shallow_copy = companies.copy()
shallow_copy[0] = "OpenAI"
print(f"Shallow Copy: {shallow_copy}, Original: {companies}")

# Deep Copy
import copy
deep_copy = copy.deepcopy(companies)
deep_copy[0] = "IBM"
print(f"Deep Copy: {deep_copy}, Original: {companies}")

# Count
companies.append("Google")
googleCount = companies.count("Google")
print(f"Google Count: {googleCount}")

# Extend
more_companies = ["Tesla", "SpaceX", "Twitter"]
companies.extend(more_companies)
print(f"Extending: {companies}")

# Index
openAiIndex = companies.index("Tesla")
print(f"Index of OpenAI: {openAiIndex}")

# Sort
companies.sort
print(f"Sort: {companies}")

# Reverse
companies.reverse()
print(f"Reverse: {companies}")

# Clear 
companies.clear()
print(f"Clear: {companies}")

# Pop
removed_company = more_companies.pop()
print(f"Pop: {removed_company}, Remainings: {more_companies}")