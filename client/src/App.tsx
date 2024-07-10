import './App.css';

function App() {
	const test = async () => {
		try {
			const test1 = await fetch('http://127.0.0.1:8000/api/rest');
			if (test1.ok) {
				console.log('Test route is "OK", now converting serialized data to json format');
				const data = await test1.json();

				console.log('test1 response: ', data);
				/** data:
				 * ['/api/test1/', '/api/test2/', '/api/test3/', '/api/test4/', '/api/test5/']
				 */
				return data;
			}
		} catch (e) {
			console.log('Error', e);
		}
	};

	const handleSteamLogin = async () => {
		try {
			const response = await fetch('/steam_login/');
			if (response.redirected) {
				console.log('response', response);

				window.location.href = response.url; // Redirect to the URL provided by the backend
			} else {
				console.log('Response was not a redirect', response);
			}
		} catch (error) {
			console.error('Error during fetch:', error);
		}
	};

	const handlePostLogin = async () => {
		try {
		} catch (e) {
			console.log('Error:', e);
		}
	};

	// Simple working method using window.location.href
	// const handleSteamLogin = async () => {
	// 	try {
	// 		window.location.href = 'http://localhost:8000/steam_login/';
	// 	} catch (e) {
	// 		console.log('Error', e);
	// 	}
	// };

	return (
		<>
			<h1>Dota Pro</h1>
			<div>
				<button onClick={test}>TEST ROUTE: CLICK & CHECK CONSOLE</button>
				<button onClick={handleSteamLogin}>STEAM LOGIN</button>
				<button onClick={handlePostLogin}>HANDLE POST STEAM LOGIN</button>
			</div>
		</>
	);
}

export default App;
