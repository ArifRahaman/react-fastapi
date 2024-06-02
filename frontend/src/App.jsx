import { useState } from 'react'
import { Route,Routes } from 'react-router-dom'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import SignupForm from './SignUpform'
import LoginForm from './Login'
import Homeee from './Homeee'
import Navbar from './Navbar'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
        <Routes>
          <Route path="/signup" element={<SignupForm/>}></Route>
        <Route path="/login" element={<LoginForm />}></Route>
        <Route  path="/home" element ={<Navbar/>}>  </Route>
        </Routes>
    </>
  )
}

export default App
