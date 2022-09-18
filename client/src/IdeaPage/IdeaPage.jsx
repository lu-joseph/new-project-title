import React, { useState } from 'react'
import NavBar from '../NavBar/NavBar'
import SideBar from '../SideBar/SideBar'
import IdeaCards from '../IdeaCards/IdeaCards'
import axios from 'axios'

import './IdeaPage.css'

const serverLocation = "http://localhost:8000/generate"

const IdeaPage = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [postContent, setPostContent] = useState({
    title: "",
    subtitle: "",
    description: ""
  });

  const getIdea = async () => {
    console.log("getIdea")
    setIsLoading(true);

    axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*'

    axios
      .get(serverLocation, {
        headers:{
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

    // setPostContent({
    //   title: "Test Title",
    //   subtitle: "Awesome subtitle",
    //   description: "Descriptions are very long and descsriptive but not too short."
    // })

    // await new Promise(r => setTimeout(r, 2000));
    // setIsLoading(false);
  }

  return (
    <div className='idea-page'>

      <div>
        <SideBar/>
      </div>
      <div>
        <IdeaCards isLoading={isLoading} postContent={postContent} getIdea={getIdea}/>
      </div>
    </div>
  )
}

export default IdeaPage
