var expect = require('chai').expect;
var http = require('http');

describe('API Testing', () => {

	describe('Temps endpoints', () => {
		it('Temps endpoint should return JSON with keys: [id, location, temperature, recorded_at]',
		() => {
			expectedKeys = ['id', 'location', 'recorded_at', 'temperature'];
			let parsedData = '';

	    http.get({
				hostname: 'localhost',
				port: 8080,
				path: '/temps',
				agent: false
			}, (res) => {
				let rawData = '';
			  res.on('data', (chunk) => { rawData += chunk; });
			  res.on('end', () => {
					// TODO: Fix this. The test always passes.
					parsedData = JSON.parse(rawData);
					expect(parsedData).to.have.all.keys(expectedKeys);
				});
	    });
		});
	});

});
