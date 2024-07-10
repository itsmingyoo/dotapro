import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [react()],

	// This option allows Django to properly serve our vite build files.
	base: '/static/',

	server: {
		proxy: {
			// Proxy all requests to the Django backend
			'/': {
				target: 'http://localhost:8000',
				changeOrigin: true,
				rewrite: (path) => path.replace(/^\//, ''),
			},
		},
	},
});
