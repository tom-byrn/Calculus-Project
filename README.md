This is the first real project I've made to improve my coding. To use, just run the app.py file.

My idea was to develop an integral calculus web app, as I was learning it in school and found the crossover between maths & physics to be really interesting. The idea was for the user to input a function with upper and lower boundaries, and then the app would return a graph of the function with the upper and lower boundaries defined, alongside a calculation of the boundary area.
I then found that I could calculate the integral with SymPy and display the graph using Matplotlib in Python.


I then drew up a flowchart on how the app would work, and then went onto developing this concept into a full web app using Flask.

<img width="297" alt="Screenshot 2024-03-03 135255" src="https://github.com/tom-byrn/Calculus-Project/assets/137120218/ec07ef14-301a-4c3b-9452-6433b27bf6ed">




I made the calculator interface with JavaScript & html and styled it with CSS. Once the equals sign is clicked, the user is redirected to the /graph page.
The output from the calculator is then sent to app.py and transcribed with regex to be interpretable by SymPy.
Then the function with its integral, differential, and a graph created with Matplotlib is shown on the page. 
I then added a html form to change the boundaries of the graph, which then shows that specific area of the function in the graph image and gives the user the area under that area of the function. 
I then finally added buttons to download the graph image and return back to the calculator.

I hope to add more function to the calculator (e.g. sine, cosine, etc.), improve the styling, and add more graph functionality in the future.
