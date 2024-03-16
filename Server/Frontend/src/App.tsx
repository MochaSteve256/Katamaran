import React, { useState } from 'react';
import { Container, Paper, Typography, Slider, Switch } from '@mui/material';
import io from 'socket.io-client';

const socket = io('http://192.168.178.62:5000');  // Adjust the URL as per your Flask-SocketIO server

function App() {
    const [xValue, setXValue] = useState(0);
    const [yValue, setYValue] = useState(0);

    const handleXSliderChange = (_, newValue) => {
        setXValue(newValue);
        socket.emit('slider_data', { x: newValue, y: yValue });
    };

    const handleYSliderChange = (_, newValue) => {
        setYValue(newValue);
        socket.emit('slider_data', { x: xValue, y: newValue });
    };

    return (
        <Container style={{ display: 'flex', flexDirection: 'row', alignItems: 'center' }}>
            <Slider min={-95} max={95} track={false} value={yValue} onChange={handleYSliderChange} orientation='vertical' style={{ marginRight: '16px', height: '480px' }} />
            <Container style={{ display: 'flex', flexDirection: 'column', flex: 1 }}>
                <iframe src="http://192.168.178.62:8000/stream.mjpg" width="640" height="480" style={{ border: 'none' }} loading="lazy" />
                <Slider min={-95} max={95} track={false} value={xValue} onChange={handleXSliderChange} style={{ width: '640px', marginTop: '16px' }} />
            </Container>
        </Container>
    )
}

export default App;