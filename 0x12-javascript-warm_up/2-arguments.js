#!/usr/bin/node
const com_line_Arg = process.argv.length - 2;

if (com_line_Arg === 0)
{
console.log("No argument");
}
else if (com_line_Arg === 1)
{
console.log("Argument found");
}
else
{
console.log("Arguments found");
}
