import React from 'react'
import illustration from '.././assets/illustration.jpg'
import textImage from '../assets/textImage.jpg'
import Button from '../Button/Button'
import './HomeBody.css'

const HomeBody = () => {
  return (
    <div className='homeBody'>
        <div className='homeBodyIllustration'>
            <img  src={illustration} />
        </div>
        <div className='homeBodyTextImage'>
            I<img  src={textImage} />
            <Button/>
        </div>
    </div>

  )
}

export default HomeBody