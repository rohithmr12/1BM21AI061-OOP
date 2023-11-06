class StringSlicer:
    def __init__(self, text):
        self.text = text

    def slice(self, start, end):
        return self.text[start:end]

# Create a StringSlicer object
text = "Hello, World!"
slicer = StringSlicer(text)

# Slice the string
sliced_text = slicer.slice(7, 11)
print(sliced_text)  # Output: "World"
