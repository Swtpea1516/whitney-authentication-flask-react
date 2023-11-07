const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			backendURL: process.env.BACKEND_URL,
			token: null,

		},
		actions: {
			login: async (email, password) => {

				let options = {
					method: "POST",
					headers: {
						'Content-Type': 'application/json',
						"Authorization": "Bearer " + store.token
						// 'Authorization': 'Bearer your-access-token'

					},
					body: JSON.stringify({ email: email, password: password })
				}
				try {
					const response = await fetch("https://laughing-telegram-jxp455g57xv3jgx9-3001.app.github.dev/api/token", options)
					if (response.status !== 200) {
						alert("error response code", response.status)
						return false;
					}
					const data = await response.json()
					console.log("access token", data);
					sessionStorage.setItem("token", data.access_token);
					setStore({
						token: data.access_token
					})
					return true;

				}
				catch (error) {
					console.log("login error try again")
				}

				// fetch(store.backendURL + "/api/login", options)
				// 	.then(response => response.json())
				// 	.then(data => {
				// 		sessionStorage.setItem("accessToken", data.access_token)
				// 		console.log(data.access_token)
				// 	})
				// 	.catch(error=>console.log(error))


			},

			signup: (email, password) => {
				let store = getStore()
				let options = {
					method: "POST",
					headers: {
						'Content-Type': 'application/json',
					},
					body: JSON.stringify({ "email": email, "password": password })
				}
				fetch(store.backendURL + "/api/signup", options)
					.then(response => response.json())
					.then(data => {
						console.log(data)
						return true
					}
					)
					.catch(error => console.log(error))

			},
			logout: () => {

			},


		}
	};
};

export default getState;
