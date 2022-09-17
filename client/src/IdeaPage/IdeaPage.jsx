import React from 'react'
import NavBar from '../NavBar/NavBar'
import SideBar from '../SideBar/SideBar'
import ideaCards from '../ideaCard/ideaCards'

const IdeaPage = () => {
  return (
    <div>
      <div>
        <NavBar/>
      </div>
      <div>
      <div>
        <SideBar/>
      </div>
      <div>
        <ideaCards/>
      </div>
      </div>
    </div>
  )
}

export default IdeaPage