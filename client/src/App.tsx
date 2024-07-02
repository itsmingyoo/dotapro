import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  const test = async () => {
    try {
      const test1 = await fetch('http://127.0.0.1:8000/api/rest')
      if (test1.ok) {
        console.log('Test route is "OK", now converting serialized data to json format')
        const data = await test1.json()

        console.log('test1 response: ', data)
        /** data:
         * ['/api/test1/', '/api/test2/', '/api/test3/', '/api/test4/', '/api/test5/']
         */
        return data
      }
    } catch (e) {
      console.log('Error', e)
    }
  }

  return (
    <>
      <div>
        <button onClick={test}>TEST ROUTE: CLICK & CHECK CONSOLE</button>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
