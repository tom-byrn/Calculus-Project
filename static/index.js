//Setup Display & Cursor
const display = document.getElementById("display");
const cursor = document.getElementById("cursor");


let cursorPosition = display.selectionStart;

function stopKeyboardInput(event) {
  event.preventDefault();
}
document.addEventListener("keydown", stopKeyboardInput);
document.addEventListener("keyup", stopKeyboardInput);
document.addEventListener("keypress", stopKeyboardInput);


function appendToDisplay(input) {
  let newValue;
  newValue = display.value + input;
  display.value = newValue;
}

// Delete & Clear
function Delete() {
  let length = display.value.length;
  if (length > 0) {
    let lastChar = display.value.charAt(length - 1);
    if (lastChar === "g") {
      display.value = display.value.slice(0, -3);
      cursorPosition -= 3;
    } else {
      display.value = display.value.slice(0, -1);
      cursorPosition -= 1;
    }
  }
}

function clearDisplay() {
  display.value = "";
  cursorPosition = 0;
}

//Send string to python to be calculated
function calculate() {
  equation = display.value;

  fetch("/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ equation: equation })
  })
  .then(response => {
    if (response.ok) {
      // Redirect to /graph after successful fetch
      window.location.href = "/graph";
    } else {
      // Handle errors if needed
      console.error('Failed to fetch');
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

document.getElementById("equation") = equation;

