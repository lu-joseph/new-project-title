import React, { useState } from 'react'
import NavBar from '../NavBar/NavBar'
import SideBar from '../SideBar/SideBar'
import IdeaCards from '../IdeaCards/IdeaCards'
import axios from 'axios'

import './IdeaPage.css'

const serverLocation = "http://localhost:5000/generate"

const filters = [
  { text: "Blockchain", display: "Blockchain" },
  { text: "Hardware", display: "Hardware" },
  { text: "NLP", display: "NLP" },
  { text: "IOT", display: "IOT" },
  { text: "AI+ML", display: "AI/ML" },
  { text: "Computer+Vision", display: "Computer Vision" },
]

const idToText = (id) => filters[id].text

const IdeaPage = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [postContent, setPostContent] = useState({
    title: "",
    subtitle: "",
    description: ""
  });
  const [filter, setFilter] = useState(-1);

  const getIdea = async () => {
    console.log("getIdea")
    setIsLoading(true);

    const category = filter !== -1 ? "/" + idToText(filter) : ""

    axios
      .get(serverLocation + category, {
        headers: {
          'Access-Control-Allow-Origin': true
        }
      })
      .then((response) => {
        console.log("response", response)
        setPostContent(response.data);
        setIsLoading(false);
      })
      .catch(e => {
        console.log(e);
        setIsLoading(false);
      })
  }

  return (
    <div className='idea-page'>
      <div>
        <NavBar />
      </div>
      <div>
        <SideBar filter={filter} setFilter={setFilter} filterButtons={filters} />
      </div>
      <div>
        <IdeaCards isLoading={isLoading} postContent={postContent} getIdea={getIdea} />
      </div>
    </div>
  )
}

export default IdeaPage
