import os, webbrowser
 

class Concept():
# Class structure for the Concept objects.
# Each object(Concepts) will have a title and a description property.
  
  def __init__(self,title,description):
  # Constructor to initialize title and description objects. 
    self.title = title
    self.description = description
 
  def generate_html(self):
  # Generate html for the concepts
  # Function generate_html will be referenced in function generate_all_html
    html_text_1 = '''
    <div class="concept">
      <div class="concept-title">
        ''' + self.title
    html_text_2 = '''
    </div>
      <div class="concept-description"><p>
        ''' + self.description + '</p>'
    html_text_3 = '''
      </div>
     </div>'''
    
    return html_text_1 + html_text_2 + html_text_3


# Wrapper function will add header and footer 
# to complete the HTML code
def wrapper_concept_html(body_html):
    header_html_text = '''
<!DOCTYPE html>
<head> 
   <meta charset="UTF-8">
    <title> Larry's Notes </title>
  <link rel="stylesheet" href="style.css"> 
</head>
<body>
<div class="concept-chapter"> </div> 
'''
    tail_html_text = '''
<div class="concept-chapter"> </div> 
</body>
'''
    full_body = header_html_text + body_html + tail_html_text 
    return full_body

 

def get_title(concept):
# Extract title from a concept text
  start_location = concept.find( TITLE )       
  end_location = concept.find( DESCRIPTION )   
  title = concept[start_location + len(TITLE ): end_location-1]   
  return title

def get_description(concept):
# Extract description from a concept text
  start_location = concept.find( DESCRIPTION )                  
  description = concept[start_location + len( DESCRIPTION ):]   
  return description
 
 
def generate_concept_objects(text):
###################### MAIN FUNCTION #########################
#  Takes the total concepts text, creates Concepts objects,  #
#      and returns a list containing these Concept objects   #
############################################################## 
  concepts = []
  title_con = ''
  desc_con = ''

  while text != '':
    next_concept_start = text.find( TITLE )
    next_concept_end = text.find( TITLE , next_concept_start + 1)
    # concept_str will be the list of concept title and descriptions
    if next_concept_end >= 0:
      concept_string = text[next_concept_start:next_concept_end]
    else:
      concept_string = text[next_concept_start:]
      # else it's the last concept in the text
      
      next_concept_end = len(concept_string)
      # Set next_concept_end to length of the string to properly exit
      # Once this is equal to zero, while loop is done.
      
     
    # from Class Concept, get title and description and return to var concept
    title_con = get_title(concept_string)
    desc_con = get_description(concept_string)
    concept = Concept(title_con, desc_con)
    
    concepts.append(concept)
    # new concept object, append to concepts list
    
    text = text[next_concept_end:]
    # text finished, move on to the next concept
    
  return concepts
 
def generate_all_html(concept_list):
  # all concepts are now stored on the list
 
  all_html = ''
  
  for concept in concept_list:
    all_html += concept.generate_html()

  all_html = wrapper_concept_html(all_html)
   # add html code and add header and style before writing to a file.
  return all_html
  

def main(textstr):
# previous code  
  concepts = generate_concept_objects(textstr)
    
  #print generate_all_html(concepts)
  
  f = open('autocode.html', 'w')
  f.write (generate_all_html(concepts))
  f.close()


# Begin by reading from file 'lesson_notes.txt'  
textstr = ' '
fileo = open("lesson_notes.txt", "r+")
textstr = fileo.read();
fileo.close()

TITLE  = 'TITLE:'
DESCRIPTION  = 'DESCRIPTION:'
 
main(textstr)
#Starts here #
 
# get directory path of file           
from urllib import pathname2url
 
url = 'file:{}'.format(pathname2url(os.path.abspath('autocode.html')))

# After getting the path and filename stored in url, open a 
# web browser with the filename
  
webbrowser.open(url)




