var mysql      = require('mysql');
var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : 'python',
    database : 'python',
    port :  3305
});

connection.connect();

var sql = `select *
                  from emp
`
connection.query(sql, function (err, rows, fields) {

    console.log(err, rows, fields);
});

connection.end();