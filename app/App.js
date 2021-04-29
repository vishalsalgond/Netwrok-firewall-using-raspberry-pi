import React,{component} from 'react';
import { StyleSheet, Text, View } from 'react-native';
import * as firebase from 'firebase';
import {firebaseConfig} from './config';
import {Item, Input, Label,Button,List,ListItem } from 'native-base';

firebase.initializeApp(firebaseConfig);

export default class App extends React.Component{
  state={
    text:"",
    list:[]
  }
  
  componentDidMount(){
    const myitems=firebase.database().ref("mywish");
    myitems.on("value",datasnap=>{
      // console.log(datasnap.val());
      if(datasnap.val()){
      this.setState({list:Object.values(datasnap.val()) })
      }
    }
    )
  }
  render(){
    const myitems=this.state.list.map(item=>{
      return(
        <ListItem style={{justifyContent:"space-between"}}>
              <Text>{item.text}</Text>
              <Text>{item.time}</Text>
        </ListItem>
      )
    })
    return(
    <View>
      <List>
            {myitems}
      </List>
    </View>
    )
    }
}
  