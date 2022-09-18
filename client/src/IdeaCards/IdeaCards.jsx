import React,{useState} from 'react'
import { Card, CardContent, CircularProgress, Typography } from '@mui/material'
import Button from '../Button/Button'
import './IdeaCards.css'
import { createStyles, makeStyles} from '@material-ui/core';

const CardStyles = makeStyles(() =>
  createStyles({
    card: {
      height: '200px',
      padding: 6,
    },
  })
);

const IdeaCards = ({isLoading, postContent, getIdea}) => {
  const [active, setActive] = useState()
  const classes = CardStyles()
  return (
    <>
    <div className='ideacard'>
      Your idea:
    </div>
      <Card className={classes.card}>
        <CardContent>
          {
            isLoading
            ? <CircularProgress />
            : <div className='ideacard-container'>
              <h2 variant="h5">{postContent.title}</h2>
              <h4 sx={{ mb: 1.5 }} color="text.secondary">{postContent.subtitle}</h4>
              <p variant="body2">{postContent.description}</p>
            </div>
          }
        </CardContent>
      </Card>
      <div className='button-box'>
        <button className='button' onClick={getIdea}>Generate</button>
      </div>
    </>
  )
}

export default IdeaCards
