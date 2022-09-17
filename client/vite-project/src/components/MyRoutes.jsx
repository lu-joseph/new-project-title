import React from 'react'
import Home from './Home';
import {
  Routes,
  Route,
} from 'react-router-dom';

const MyRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Home/>}/>
    </Routes>
  )
}

export default MyRoutes