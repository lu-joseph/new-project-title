import React from 'react'
import illustration from '.././assets/illustration.jpg'
import textImage from '../assets/textImage.jpg'
import Button from '../Button/Button'
import './HomeBody.css'
import { Link } from 'react-router-dom'

const HomeBody = () => {
  return (
    <div className='homeBody'>
        <div className='homeBodyIllustration'>
            <img  src={illustration} />
        </div>
        <div className='homeBodyTextImage'>
            <img  src={textImage} />
           <Link style={{textDecoration: 'none'}} to= '/ideas'>
           <Button/>
           </Link>
        </div>
    </div>

  )
}

export default HomeBody