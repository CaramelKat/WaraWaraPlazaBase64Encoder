# Wara Wara Plaza Base64 Converter
This is a quick Python Script to convert a Base64 string taken from the Wara Wara Plaza XML file to a tga file,(Currently only the <content> string inside <painting>) or convert a tga file to xml
  
  # How do you use it?
  The script is set up by default to convert a tga file to base64, put the runme.py in the same directory as the "input.tga" file, and run it from the terminal, it'll spit out a text file called input2.txt with the string inside. If you want to go from Base64 to tga, just uncomment mv2tga(r'input.txt') and comment out tga2mv(r'input.tga') in runme.py, then save you Base64 string to a text file called input.txt, run the script and you'll get your output.
  
 * Thanks to Ash for figuring out what the file type was like 2 years ago (https://gist.github.com/QuarkTheAwesome/143541120b7e1394c218976b0b330671)
  * Also thanks to my buddy wallefan for writing a better script than me lmao
