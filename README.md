start pg service from services.msc on ctlr + r
open sql shell using `psql -U postgres`
open sql shell and login with default server database port username and your password.
"\l" to check all existing databases. "\l+" for detailed list.
To list only the databases that you have access to, you can use the \du command. This command will show a list of all roles (including databases) and the privileges that each role has.
create new db using CREATE DATABASE name_of_database;

`postgres=# CREATE DATABASE store_monitoring; CREATE DATABASE `
when working with servers that manage multiple databases, you’ll find the need to jump between databases frequently. This can be done with the \connect meta-command or its shortcut \c.

'\c store_monitoring'
postgresql://[user[:password]@][netloc][:port][/dbname]
postgresql://postgres:08031998@localhost:5432/store_monitoring
