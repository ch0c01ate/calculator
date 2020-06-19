allowedKeys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", ".", "=", "c"]

document.onkeypress = function (e) {
    keyPressed = String.fromCharCode(e.which);
    console.log(keyPressed);
    if (allowedKeys.includes(keyPressed)) {
        console.log("HERE");
        document.getElementById(keyPressed).click();
    }
};