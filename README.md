# JupiTeleApp App

A simple real-time chat application built with Flask and Socket.IO, written by JupiMrNight.

## Features

- Real-time messaging with WebSocket support
- User authentication (username-based)
- Typing indicators
- User join/leave notifications
- Clean and modern UI
- Responsive design

## Project Setup

Create the following directory structure:

```
flask-chat-app/
├── app.py
├── requirements.txt
├── templates/
│   ├── login.html
│   └── index.html
└── README.md
```


## How It Works

- **Flask**: Web framework for routing and session management
- **Flask-SocketIO**: Enables real-time bidirectional communication
- **Socket.IO Client**: JavaScript library for WebSocket connections (loaded from CDN)
- **Sessions**: Store user information securely

## Features Explained

### Real-time Messaging
Messages are sent via WebSocket connections and broadcast to all connected users instantly.

### Typing Indicators
When a user types, other users see a "User is typing..." indicator.

### User Notifications
The chat displays system messages when users join or leave the chat room.

### Online view
The chat room displays when users are online.

## Customization

You can customize the app by:
- Modifying colors in the embedded CSS
- Adding chat rooms in `app.py`
- Implementing message history
- Adding user avatars
- Adding private messaging

## Troubleshooting

**Issue**: "Template not found" error
**Solution**: Make sure `login.html` and `index.html` are in a `templates` folder

**Issue**: WebSocket connection fails
**Solution**: Check that all dependencies are installed correctly

## License

MIT License - Feel free to use and modify!
