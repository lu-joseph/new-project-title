import React,{useState} from 'react'
import { Button, Card, CardContent, CircularProgress, Typography } from '@mui/material'


const IdeaCards = ({isLoading, postContent, getIdea}) => {
  return (
    <>
      <Card>
        <CardContent>
          {
            isLoading
            ? <CircularProgress />
            : <>
              <Typography variant="h5">{postContent?.title}</Typography>
              <Typography sx={{ mb: 1.5 }} color="text.secondary">{postContent?.subtitle}</Typography>
              <Typography variant="body2">{postContent?.description}</Typography>
            </>
          }
        </CardContent>
      </Card>
      <div className='button-box'>
        <Button onClick={getIdea}>Generate</Button>
      </div>
    </>
  )
}

export default IdeaCards
