import React from 'react';
import { Pressable, StyleSheet, Text } from 'react-native';

const Button = ({ textInfo }) => {
  return (
    <Pressable style={styles.button}>
      <Text style={styles.text}>{textInfo}</Text>
    </Pressable>
  );
};

const styles = StyleSheet.create({
  button: {
    backgroundColor: '#FF2C55',
    padding: 16,
    borderRadius: 13,
    minWidth: '80%',
  },
  text: {
    fontSize: 16,
    fontWeight: '500',
    lineHeight: 21,
    color: '#FFF5F6',
    textAlign: 'center',
  },
});

export default Button;
