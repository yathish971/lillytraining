unique_visitors = {'John', 'Mary', 'Peter', 'Sara', 'John'}

# Add a new visitor to the set
unique_visitors.add("yathish")

# Remove a visitor from the set

unique_visitors.remove("Sara")
# Check if a visitor is in the set
print(unique_visitors.intersection({"Mary"}))

# Perform set operations
page1_visitors = {'John', 'Mary', 'Sara'}
page2_visitors = {'Peter', 'Sara', 'Emily'}

# Union of visitors across two pages
print(page1_visitors.union(page2_visitors))

# Visitors who visited both pages
print(page2_visitors.intersection(page1_visitors))

# Visitors who visited only one page
print(page1_visitors.symmetric_difference(page2_visitors))
