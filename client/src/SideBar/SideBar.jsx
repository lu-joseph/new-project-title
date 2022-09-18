import React, { useState } from 'react'
import SideButtons from '../SideButtons/SideButtons'
import './SideBar.css'

export default function SideBar({ filterButtons, filter, setFilter }) {

  return (
    <div className='sidebar'>
      <div>
        <p> Filter: </p>
        {
          filterButtons.map((f, i) => <SideButtons
            selected={filter === i}
            onSelect={() => {
              if (filter === i) setFilter(-1)
              else setFilter(i)
            }}
            text={f.display}
            key={i}
          />)
        }
      </div>
    </div>
  )
}


