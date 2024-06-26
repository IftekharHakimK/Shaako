import React from "react";
import { useState, useEffect } from "react";
import LoginScreen from "react-native-login-screen";
import { View, Text, StyleSheet, Image, AppRegistry, ScrollView } from "react-native";
import MaterialButtonViolet from "./../../components/MaterialButtonViolet";
import Navbar from "./../../components/Navbar";
import MaterialCardWithoutImage from "../../components/MaterialCardWithoutImage";
import MaterialButtonWithShadow from "../../components/MaterialButtonWithShadow";
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import { Card, ListItem, Button, Icon, Header } from 'react-native-elements'
import AsyncStorage from '@react-native-async-storage/async-storage'
import MaterialCommunityIconsIcon from "react-native-vector-icons/MaterialCommunityIcons";

const BlogList = ({ navigation }) => {
    let [result, setresult] = useState([]);
    let [sup_image, setsup_image] = useState(null);
    let sup_id = 0;
    // let sup_id = 26;

    useEffect(() => {
        getContents()
    }, [])



    let getContents = async () => {

        let chw_id = await AsyncStorage.getItem('chw_id')
        chw_id = JSON.parse(chw_id)

        sup_id = await AsyncStorage.getItem('sup_id');
        sup_id = JSON.parse(sup_id)

        let tok = await AsyncStorage.getItem('token')
        tok = JSON.parse(tok)

        console.log(tok)
        let response = await fetch(global.ip + '/CHW/getLessonList', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'TOKEN ' + tok
            },
            body: JSON.stringify({ sup_id: sup_id, chw_id: chw_id })
        })
        let d = await response.json()
        setresult([])
        for (let i = 0; i < d.length; i++) {
            let now = d[i]
            console.log(now.id + " " + now.title + " " + now.supervisor_name + " " + now.upload_time + " " + now.is_read)
            setresult(prevArray => [...prevArray, now]);
        }

        console.log("etuku")

        // const nodeFetch = require('node-fetch');
        // global.fetch = nodeFetch;

        let response2 = await fetch(global.ip + '/organization/image/supervisor', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'TOKEN ' + tok
            },
            body: JSON.stringify(sup_id)
        })

        console.log('////////////////////////////////////////////////////')
        console.log("response " + response2)
        //take image respone from bufferIO
        let image = await response2.blob()
        var reader = new FileReader();
        reader.readAsDataURL(image);
        reader.onloadend = function () {
            var base64data = reader.result;
            setsup_image(base64data)
        }
    }

    let click = async (a) => {
        console.log(a.id)
        let chw_id = await AsyncStorage.getItem('chw_id')
        chw_id = JSON.parse(chw_id)

        let tok = await AsyncStorage.getItem('token')
        tok = JSON.parse(tok)

        let response = await fetch(global.ip + '/chw/mark_lesson_read', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'TOKEN ' + tok
            },
            body: JSON.stringify({ lesson_id: a.id, chw_id: chw_id })
        })
        let d = await response.json()
        console.log(d)

        navigation.navigate('BlogPost', { lesson_id: a.id })


    }

    return (
        <View style={styles.container}>
            <Navbar navigation={navigation}></Navbar>
            <ScrollView>

                {result.map(a => {
                    return (
                        <View >
                            <Card>
                                {!a.is_read &&
                                    <View style={styles.circle}></View>
                                }
                                <Card.Title ><Text style={{ fontWeight: 'bold' }}>{a.title}</Text></Card.Title>
                                <Card.Divider />

                                <View style={{ flexDirection: "row", justifyContent: "space-between" }}>


                                    <View style={{ flexDirection: "column"}}>
                                        <View style={{ flexDirection: "row"}}>
                                        <MaterialCommunityIconsIcon
                                            name="lead-pencil"
                                            size={30}                                        
                                        ></MaterialCommunityIconsIcon>
                                                                                
                                        <Text style={{ fontSize: 18, }}>    {a.supervisor_name}{'\n'} </Text>
                                        </View>

                                        <View style={{ flexDirection: "row"}}>
                                        <MaterialCommunityIconsIcon
                                            name="calendar-check"
                                            size={30}                                        
                                        ></MaterialCommunityIconsIcon>                                        
                                        <Text style={{ fontSize: 18, }}>    {a.upload_time}{'\n'} </Text>
                                        </View>
                                        
                                        
                                    </View>
                                    

                                    <View>
                                        <Card.Image style={{ width: 60, height: 60, borderRadius: 60 / 2, alignSelf: 'center' }} source={{ uri: sup_image, scale: 1 }} />
                                    </View>

                                </View>


                                <Button
                                    icon={<Icon name='code' color='#ffffff' />}
                                    buttonStyle={{ borderRadius: 0, marginLeft: 0, marginRight: 0, marginBottom: 0 }}
                                    title='পড়ুন' onPress={() => click(a)} />
                            </Card>
                        </View>);
                })}
            </ScrollView>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: "column",
        backgroundColor: "#41cca6"
    },

    posts: {
        flex: 1,
        flexDirection: "row"
    },
    circle: {
        width: 10, // this should be a "props"-value in future
        height: 10, // this should be a "props"-value in future
        borderRadius: 10 / 2,
        backgroundColor: 'red',
        marginTop: -18,
        marginLeft: -18
    },

});

export default BlogList;