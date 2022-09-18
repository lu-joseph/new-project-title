import React, { useState } from 'react'
import { Button, Card, CardContent, CircularProgress, Typography } from '@mui/material'


const IdeaCards = ({ isLoading, postContent, getIdea }) => {
  return (
    <>
      <Card>
        <CardContent>
          {
            isLoading
              ? <CircularProgress />
              : <>
                <Typography variant="h5">{postContent ? postContent.title : null}</Typography>
                <Typography sx={{ mb: 1.5 }} color="text.secondary">{postContent ? postContent.subtitle : null}</Typography>
                <Typography variant="body2">{postContent ? postContent.description : null}</Typography>
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
