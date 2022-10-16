#Imports
import re

# Functions

# Searching string using regex
def searchStr(pattern, string):
   patt = re.compile(pattern)
   matches = re.finditer(patt, string)
   return matches

# Coverting into percentage
def convertToPercent(mydict):
   total = 0
   mydict_copy = {}
   for percent_value in mydict.values():
      total += percent_value

   for key2, value2 in mydict.items():
      output1 = value2 * 100
      answer = output1 / total
      mydict_copy[key2] = answer

   print("In Percentage : \n")
   for key, value in mydict_copy.items():
      valueStr = "{0:.3f}".format(value)
      print(f"{key} - {valueStr}")
      
   print("\n")
 

# Analyzing character and main output
def analyzeChars(string):
   string = string.lower()
   matches = searchStr(r".", string)
   matches_chars = []
   matches_chars_set = set()
   output_dict = {}

   for match in matches:
      match_span = match.span()
      matches_chars.append(string[match_span[0]:match_span[1]])
      matches_chars_set.add(string[match_span[0]:match_span[1]])

   for char in matches_chars_set:
      char_count = matches_chars.count(char)
      output_dict[char] = char_count

   output_dict = dict(sorted(output_dict.items()))
   output_dict_percent = output_dict

   print("In Numbers : \n")
   for key, value in output_dict.items():
      print(f"{key} - {value}")

   print("\n")

   convertToPercent(output_dict_percent)


# Driver Code
if __name__ == "__main__":
   string = input("Enter the Sentence or Paragraph : ")
   analyzeChars(string)