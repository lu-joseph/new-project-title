import React from 'react'
import { Routes, Route } from "react-router-dom";
import Home from './Home';
import IdeaPage from './IdeaPage/IdeaPage';

const MyRouters = () => {
  return (
    <Routes>
        <Route path="/" element ={<Home/>}/>
        <Route path="/ideas" element ={<IdeaPage/>}/>
    </Routes>
  )
}

export default MyRouters