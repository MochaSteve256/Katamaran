import { useState, useEffect, ChangeEvent } from 'react';
import { Container, Box, Paper, Typography, Slider, Switch, AppBar, Toolbar, FormGroup, FormControlLabel } from '@mui/material';
import { styled } from '@mui/material/styles';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import io from 'socket.io-client';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const lightTheme = createTheme({
  palette: {
    mode: 'light',
  },
});

const MaterialUISwitch = styled(Switch)(({ theme }) => ({
    width: 62,
    height: 34,
    padding: 7,
    '& .MuiSwitch-switchBase': {
      margin: 1,
      padding: 0,
      transform: 'translateX(6px)',
      '&.Mui-checked': {
        color: '#fff',
        transform: 'translateX(22px)',
        '& .MuiSwitch-thumb:before': {
          backgroundImage: `url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" height="20" width="20" viewBox="0 0 20 20"><path fill="${encodeURIComponent(
            '#fff',
          )}" d="M4.2 2.5l-.7 1.8-1.8.7 1.8.7.7 1.8.6-1.8L6.7 5l-1.9-.7-.6-1.8zm15 8.3a6.7 6.7 0 11-6.6-6.6 5.8 5.8 0 006.6 6.6z"/></svg>')`,
        },
        '& + .MuiSwitch-track': {
          opacity: 1,
          backgroundColor: theme.palette.mode === 'dark' ? '#8796A5' : '#aab4be',
        },
      },
    },
    '& .MuiSwitch-thumb': {
      backgroundColor: theme.palette.mode === 'dark' ? '#003892' : '#001e3c',
      width: 32,
      height: 32,
      '&::before': {
        content: "''",
        position: 'absolute',
        width: '100%',
        height: '100%',
        left: 0,
        top: 0,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        backgroundImage: `url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" height="20" width="20" viewBox="0 0 20 20"><path fill="${encodeURIComponent(
          '#fff',
        )}" d="M9.305 1.667V3.75h1.389V1.667h-1.39zm-4.707 1.95l-.982.982L5.09 6.072l.982-.982-1.473-1.473zm10.802 0L13.927 5.09l.982.982 1.473-1.473-.982-.982zM10 5.139a4.872 4.872 0 00-4.862 4.86A4.872 4.872 0 0010 14.862 4.872 4.872 0 0014.86 10 4.872 4.872 0 0010 5.139zm0 1.389A3.462 3.462 0 0113.471 10a3.462 3.462 0 01-3.473 3.472A3.462 3.462 0 016.527 10 3.462 3.462 0 0110 6.528zM1.665 9.305v1.39h2.083v-1.39H1.666zm14.583 0v1.39h2.084v-1.39h-2.084zM5.09 13.928L3.616 15.4l.982.982 1.473-1.473-.982-.982zm9.82 0l-.982.982 1.473 1.473.982-.982-1.473-1.473zM9.305 16.25v2.083h1.389V16.25h-1.39z"/></svg>')`,
      },
    },
    '& .MuiSwitch-track': {
      opacity: 1,
      backgroundColor: theme.palette.mode === 'dark' ? '#8796A5' : '#aab4be',
      borderRadius: 20 / 2,
    },
  }));

const theme = (darkMode: boolean) => (darkMode ? darkTheme : lightTheme);

const socket = io('http://192.168.178.62:5000');

function App() {
  const [darkMode, setDarkMode] = useState(true);
  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  const [xValue, setXValue] = useState<number>(0);
  const [yValue, setYValue] = useState<number>(0);

  useEffect(() => {
    socket.on('slider_data', (data) => {
      setXValue(data.x);
      setYValue(data.y);
    });
  }, []);
  
  const handleXSliderChange = (_: Event, newValue: number | number[]) => {
    setXValue(Array.isArray(newValue) ? newValue[0] : newValue);
    socket.emit('slider_data', { x: newValue, y: yValue });
  };

  const handleYSliderChange = (_: Event, newValue: number | number[]) => {
    setYValue(Array.isArray(newValue) ? newValue[0] : newValue);
    socket.emit('slider_data', { x: xValue, y: newValue });
  };

  const [spotlight, setSpotlight] = useState<boolean>(false);

  const handleSpotlightChange = (_: ChangeEvent<HTMLInputElement>, newValue: boolean) => {
    setSpotlight(newValue);
    socket.emit('spotlight', { on :newValue });
  };

  const [lighting, setLighting] = useState<boolean>(false);

  const handleLightingChange = (_: ChangeEvent<HTMLInputElement>, newValue: boolean) => {
    setLighting(newValue);
    socket.emit('lights', { on :newValue });
  };

  return (
    <ThemeProvider theme={theme(darkMode)}>
      <CssBaseline />
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Katamaran
            </Typography>
            <MaterialUISwitch checked={darkMode} onChange={toggleDarkMode} />
          </Toolbar>
        </AppBar>
      <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 2, m: 2 }}>
        <Paper elevation={10} square sx={{ maxWidth: '750px', margin: '0 auto', p: 4 }}>
          <Container style={{ display: 'flex', flexDirection: 'row', alignItems: 'top' }}>
            <Slider min={-90} max={90} track={false} valueLabelDisplay='auto' value={yValue} onChange={handleYSliderChange} orientation='vertical' style={{ marginRight: '8px', height: '480px', paddingLeft: 0 }} />
            <Container style={{ display: 'flex', flexDirection: 'column', flex: 1 }}>
              <iframe src="http://192.168.178.62:8000/stream.mjpg" width="640px" height="480px" style={{ border: 'none', marginRight: "20"}} loading="lazy" />
              <Slider min={-90} max={90} track={false} valueLabelDisplay='auto' value={xValue} onChange={handleXSliderChange} style={{ width: '640px', marginTop: '16px' }} />
            </Container>
          </Container>
        </Paper >
        <Paper elevation={10} square sx={{ maxWidth: '250px', margin: '0 auto', p: 4 }}>
          <FormGroup>
            <FormControlLabel
              control={<Switch sx={{ m: 1 }} checked={spotlight} onChange={handleSpotlightChange} />}
              label="Scheinwerfer"
            />
            <FormControlLabel
              control={<Switch sx={{ m: 1 }} checked={lighting} onChange={handleLightingChange} />}
              label="Beleuchtung"
            />
          </FormGroup>
        </Paper>
      </Box>
    </ThemeProvider>
  );
}

export default App;
