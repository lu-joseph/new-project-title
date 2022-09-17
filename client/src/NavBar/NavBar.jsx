import React from 'react'
import logo from '../assets/logo.jpg'
import './NavBar.css'

const NavBar = () => {
  return (
    <div className='navBar-container'>
   <div className='navBar-container_title'>
   <div>
        <img src={logo}/>
    </div>
    <div>
        <p>
            New Project Title
        </p>
    </div>
   </div>
    <div>
    
    </div>
    </div>
  )
}

export default NavBar