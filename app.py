from flask import Flask, render_template, request, jsonify
from googleapiclient.discovery import build
from textblob import TextBlob
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# YouTube API configuration
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def get_video_comments(video_id, max_results=100):
    """Fetch comments from a YouTube video."""
    comments = []
    try:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=max_results
        )
        response = request.execute()
        
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
            
    except Exception as e:
        print(f"Error fetching comments: {str(e)}")
    
    return comments

def analyze_sentiment(comments):
    """Analyze sentiment of comments using TextBlob."""
    sentiments = []
    for comment in comments:
        analysis = TextBlob(comment)
        sentiments.append(analysis.sentiment.polarity)
    
    return sentiments

def get_video_details(video_id):
    """Get video details from YouTube."""
    try:
        request = youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        )
        response = request.execute()
        
        if response['items']:
            video = response['items'][0]
            return {
                'title': video['snippet']['title'],
                'channel': video['snippet']['channelTitle'],
                'views': video['statistics']['viewCount'],
                'likes': video['statistics']['likeCount']
            }
    except Exception as e:
        print(f"Error fetching video details: {str(e)}")
    
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video_url = request.form.get('video_url')
    
    # Extract video ID from URL
    video_id = None
    if 'youtube.com' in video_url:
        video_id = video_url.split('v=')[1].split('&')[0]
    elif 'youtu.be' in video_url:
        video_id = video_url.split('/')[-1]
    
    if not video_id:
        return jsonify({'error': 'Invalid YouTube URL'})
    
    # Get video details
    video_details = get_video_details(video_id)
    if not video_details:
        return jsonify({'error': 'Could not fetch video details'})
    
    # Get and analyze comments
    comments = get_video_comments(video_id)
    sentiments = analyze_sentiment(comments)
    
    # Calculate statistics
    avg_sentiment = np.mean(sentiments) if sentiments else 0
    sentiment_counts = pd.Series(sentiments).value_counts().to_dict()
    
    return jsonify({
        'video_details': video_details,
        'total_comments': len(comments),
        'average_sentiment': avg_sentiment,
        'sentiment_distribution': sentiment_counts,
        'comments': comments[:10]  # Return first 10 comments
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
