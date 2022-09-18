import React from 'react'
import './SideButton.css'
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import { colors } from '../colors'

const Button = ({ text, selected, onSelect }) => {
  return (
    <div className={'SideButton' + (selected ? " selected" : "")} onClick={onSelect} >{text}</div>
  )
}

export default Button