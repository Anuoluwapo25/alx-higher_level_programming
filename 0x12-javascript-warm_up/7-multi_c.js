#!/usr/bin/node
const args = process.argv.slice(2);
let i = 0;
const ifInt = parseInt(args[0]);
if (!isNaN(ifInt))
{
	while (i < ifInt)
	{
		console.log('C is fun');
		i++;
	}
}
else
{
	console.log('Missing number of occurrences');
}

