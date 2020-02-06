const request = require('supertest')
const app = require('../app.js')

describe('Root path should return 200', () => {
	test('It should respond 200 to GET', () => {
		return request(app).get("/").then(response => {
			expect(response.statusCode).toBe(200)
		});
	}); 
});

