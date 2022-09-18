import React from 'react'
import { Link } from 'react-router-dom'
import logo from '../assets/logo.jpg'
import './NavBar.css'

const NavBar = () => {
  return (
    <div className='navBar-container'>
      <div className='navBar-container_title'>
        <div>
          <Link style={{ textDecoration: 'none' }} to='/'>
            <img src={logo} />
          </Link>
        </div>
        <div>
          <p className='title'>
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