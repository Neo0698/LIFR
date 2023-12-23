# LIFR
LIFR is a module that generates an answer, based on a supplied text database and a given answer start. The result can be a generated new sentence or an answer that adapts to the mathematical data supplied.

<p>They are two types of way that the software can be used to answer to a problem.</p>

# search:
use to generate an answer to a question

`ask`: question to be answered by the program<br>
`variable`: list of mathematical variables<br>
`context`: a string of characters that can correspond to the questions and answers before or other content to give a context and help give the most satisfactory answers.<br>
# generate:
use to generate an answer by using multiple phrases that will be given by the client side code

`creative`: to generate sentences based more or less on the given texts.<br>
`data`: list of characheres corresponding to sentences that can be used by the template to generate an answer. ex:[["sentence1"],["sentence2"]...["sentence n"]]<br>
`good`: Example of incorrectly formulated parts of sentences, in the form of a list of character strings.<br>
`bad`: Example of correctly formulated parts of sentences that will be promoted by the system, as a list of strings.<br>
`variable`: Definition of different variables in the form of a dictionary whose key is the variable and whose value is the value of the variable.<br>
