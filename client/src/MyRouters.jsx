import React from 'react'
import { Routes, Route } from "react-router-dom";
import Home from './Home';
import IdeaPage from './IdeaPage/IdeaPage';
import NavBar from './NavBar/NavBar';

const MyRouters = () => {
  return (
    <>
    <NavBar/>
    <Routes>
      <Route path="/" element ={<Home/>}/>
      <Route path="/ideas" element ={<IdeaPage/>}/>
    </Routes>
    </>
  )
}

export default MyRouters
