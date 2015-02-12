function outer(x) {
    return function () { console.log(x) };
}

var foo1 = outer("1");
var foo2 = outer("2");

foo1();
foo2();

/*

Result of Node.js execution

1
2

*/
