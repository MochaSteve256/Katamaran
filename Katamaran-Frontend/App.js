import React, { useState, useEffect } from 'react';
import { StatusBar, StyleSheet, Text, View, Image } from 'react-native';

export default function App() {

  const [imageUri, setImageUri] = useState('');

  useEffect(() => {
    const fetchImage = async () => {
      try {
        const response = await fetch('192.168.178.62:5000/video_feed');
        if (!response.ok) {
          throw new Error('Failed to fetch image');
        }
        const blob = await response.blob();
        const uri = URL.createObjectURL(blob);
        setImageUri(uri);
      } catch (error) {
        console.error('Error fetching image:', error);
      }
    };
  
    // Fetch the initial image when the component mounts
    fetchImage();
  
    // Setup interval to fetch new images
    const interval = setInterval(fetchImage, 1000); // Adjust the interval as needed
  
    return () => clearInterval(interval); // Cleanup interval on unmount
  }, []);
  

  return (
    <View style={styles.container}>
      <StatusBar style="light" />
      <Text style={styles.text}>Katamaran</Text>
      <Image
        style={styles.image}
        source={{ uri: imageUri }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#222222',
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    color: '#ffffff'
  },
  image: {
    width: 200, // Adjust width as needed
    height: 200, // Adjust height as needed
  }
});
