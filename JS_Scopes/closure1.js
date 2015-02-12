var name = "outer";

function one() {
    var name = "middle";
    var other = "findme";

    function two() {
        var name = "inner";
        console.log("1");
        console.dir( {name: name, other: other} );
    }

    two();
    console.log("2");
    console.dir( {name: name, other: other} );
}

one();

console.log("3");
console.dir( {name: name} );


console.log("------------");

function outer(x) {
    return function () { console.log(x) };
}

var foo1 = outer("1");
var foo2 = outer("2");

foo1();
foo2();
