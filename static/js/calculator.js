const allowedKeys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", ".", "=", "c"];
var isEqualed = false;

document.onkeypress = function (e) {
    keyPressed = String.fromCharCode(e.which);
    console.log(keyPressed);
    if (allowedKeys.includes(keyPressed)) {
        document.getElementById(keyPressed).click(function (event) {
            event.stopPropagation();
        });
    }
};

function calculate(expr) {
    isEqualed = true;
    return evaluate(expr)
}

function clickNumber(key) {
    isEqualed ? document.calc.txt.value = key : document.calc.txt.value += key;
    isEqualed = false;
}

function clickSign(key) {
    isEqualed = false;
    document.calc.txt.value += key;
}

function evaluate(expr) {
    let res = "Server is unresponsive";

    $.ajax({
        url: '/',
        type: 'POST',
        async: false,
        contentType: 'application/json',
        data: JSON.stringify({ "expression": expr }),
        dataType: 'json',
        success: function (response) {
            res = response.result
        }
    });

    return res;
}