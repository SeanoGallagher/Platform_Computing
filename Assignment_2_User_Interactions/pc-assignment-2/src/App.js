import React from "react"
import './App.css';
import AboutMe from "./AboutMe"
import Blank from "./Blank"

import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

function App() {
  return(
    <Router>
      <Routes>
        <Route path ='/' element={<AboutMe/>}></Route>
        <Route path ='/Blank' element={<Blank/>}></Route>
      </Routes>
    </Router>
  )
}
export default App;
