import React,{useState} from 'react'
import './SideButton.css'
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import { colors } from '../colors'


const Button = ({text}) => {
  return (
    <div className={`SideButton`} >{text}</div>
  )
}

export default Button