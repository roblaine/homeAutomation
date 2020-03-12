var expect  = require('chai').expect;
var http = require('http');

describe('API Testing', () => {

	describe('Temps endpoints', () => {
		it('Temps endpoint should return JSON with keys: [id, location, temperature, recorded_at]',
		() => {
	    http.get({
				hostname: 'localhost',
				port: 8080,
				path: '/temps',
				agent: false
			}, (res) => {
				let rawData = '';
			  res.on('data', (chunk) => { rawData += chunk; });
			  res.on('end', () => {
					try {
						const parsedData = JSON.parse(rawData);

						expect(parsedData).to.have.all.keys('id', 'location', 'recorded_at', 'temperature');
					} catch (e) {
						return;
					}
				});
	    });
		});
	});

});
