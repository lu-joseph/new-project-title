import React from 'react'
import SideButtons from '../SideButtons/SideButtons'
import './SideBar.css'


const SideBar = () => {
  return (
    <div className='sidebar'>
       <div className='type'>
        <p>Type:</p>
        <div>
        <SideButtons text={"Quick Idea"}/>
        <SideButtons text={"Full DevPost"}/>
        </div>
       </div>

       <div>
       <p> Filter Project Ideas: </p>
       <div className='sidebuttons'>
       <SideButtons text={"Blockchain"}/>
        <SideButtons text={"Hardware"}/>
        <SideButtons text={"NLP"}/>
        <SideButtons text={"IOT"}/>
        <SideButtons text={"AI / ML"}/>
        <SideButtons text={"Computer Vision"}/>
       </div>
       </div>
    </div>
  )
}


export default SideBar