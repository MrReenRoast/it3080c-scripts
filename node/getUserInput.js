process.stdout.write("Hello. What is your name? ")

process.stdout.on('data', function(data) {
	console.log("Hello " + data.toString())
});

process.on('exit', function() {
	console.log('Thanks for the info!')
});