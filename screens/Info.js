import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { useFonts } from 'expo-font';
import Button from '../components/button';

export default function Info() {
  const [loaded] = useFonts({
    DINRoundPro: require('../assets/fonts/DINRoundPro.woff2'),
  });

  if (!loaded) {
    return null;
  }
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Your Personal Vocabulary</Text>
      <Text style={styles.textInfo}>
        Play cards with memorization of words, make a challenge to yourself and
        play with friends. And let the strongest defeat 💪
      </Text>
      <View style={{ marginBottom: '6%', width: '100%' }}>
        <Button textInfo="Start" />
      </View>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#22252C',
    alignItems: 'center',
    justifyContent: 'center',
    color: '#fff',
    padding: '7.5%',
  },
  title: {
    fontWeight: '900',
    fontSize: 66,
    lineHeight: 73,
    color: '#ffffff',
    marginBottom: '3%',
    marginTop: '35%',
    fontFamily: 'DINRoundPro',
  },
  textInfo: {
    color: '#8F9BA8',
    lineHeight: 21,
    fontWeight: '500',
    fontSize: 16,
    marginBottom: '19%',
    fontFamily: 'DINRoundPro',
  },
});
