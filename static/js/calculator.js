const allowedKeys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", ".", "=", "c"];
const validation = /(?:(?:^|[-+_*/])(?:\s*-?\d+(\.\d+)?(?:[eE][+-]?\d+)?\s*))+$/;
var isEqualed = false;

document.onkeypress = function (e) {
    keyPressed = String.fromCharCode(e.which);
    console.log(keyPressed);
    if (allowedKeys.includes(keyPressed)) {
        console.log("HERE");
        document.getElementById(keyPressed).click(function (event) {
            event.stopPropagation();
        });
    }
};

function calculate(expr) {
    isEqualed = true;
    try {
        return (exprIsValid(expr) ? eval(expr) : "Expression is invalid!");
    } catch (error) {
        return "Expression is invalid!";
    }
}

function exprIsValid(expr) {
    return validation.test(expr);
}

function clickButton(key) {
    isEqualed ? document.calc.txt.value = key : document.calc.txt.value += key;
    isEqualed = false;
}