class HashTable:
    def __init__(self): # initializes the hash table object
        self.collection = {} # the main dictionary to store hashed buckets

    def hash(self, string): # creates a numerical index based on the characters in a string
        hash_sum = 0 # starts the sum at zero
        for char in string: # loops through every character in the word
            hash_sum += ord(char) # adds the numerical Unicode value of the character to the sum
        return hash_sum # returns the final sum as the hash key
        
    def add(self, key, value) -> None: # adds a new key-value pair to the table
        key_hash = self.hash(key) # generates a hash for the provided key
        if key_hash not in self.collection: # check if this hash 'bucket' already exists
            self.collection[key_hash] = {} # if not, create a new dictionary at that hash location
        self.collection[key_hash][key] = value # store the actual key and value inside that hash bucket
        
    def remove(self, key): # removes an entry from the table using its key
        key_hash = self.hash(key) # calculate the hash to find where the key would be stored
        if key_hash in self.collection: # check if the hash bucket exists
            if key in self.collection[key_hash]: # check if the specific key exists in that bucket
                del self.collection[key_hash][key] # delete the key-value pair
        return # exit the function
        
    def lookup(self, key): # finds and returns the value associated with a key
        key_hash = self.hash(key) # calculate the hash to know which bucket to look in
        if key_hash not in self.collection: # if the hash doesn't exist, the key isn't there
            return None
        if key in self.collection[key_hash]: # if the key exists in the bucket
            return self.collection[key_hash][key] # return the stored value

# --- Testing the HashTable ---
hashing = HashTable()

print(hashing.hash('golf')) # prints the numerical hash of 'golf' (432)

hashing.add('golf', 'sport') # adds 'golf' under hash 432
print(hashing.collection)

# 'dear' and 'read' have the same letters, so they will 'collide' at the same hash
hashing.add('dear', 'friend')
hashing.add('read', 'book')
print(hashing.collection) # you will see both stored under the same hash key

print(hashing.lookup('golf')) # searches and returns 'sport'

# 'fcc' and 'cfc' are another example of a collision
hashing.add('fcc', 'coding')
hashing.add('cfc', 'chemical')
print(hashing.collection)

hashing.add('rose', 'flower')
print(hashing.collection)