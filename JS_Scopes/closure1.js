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

/*

Result of Node.js execution

1
{ name: 'inner', other: 'findme' }
2
{ name: 'middle', other: 'findme' }
3
{ name: 'outer' } // "other" is undefined

*/
