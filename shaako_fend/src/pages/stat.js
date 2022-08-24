import man2 from './assets/img/avatars/avatar2.jpg'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import React, { useState, useEffect } from "react";

const Statistics = () => {
    let [result, setresult] = useState([])
    let [search, setsearch] = useState('')
    let organization = localStorage.getItem('organization')
    useEffect(() => {
        getCHW()
    }, [])

    let getCHW = async () => {
        let response = await fetch('http://127.0.0.1:8000/organization/getCHW', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'TOKEN ' + localStorage.getItem('token')
            },
            body: JSON.stringify(organization)
        })
        let d = await response.json()
        setresult([])
        for (let i = 0; i < d.length; i++) {
            let now = d[i]
            // let response2 = await fetch('http://127.0.0.1:8000/organization/image/CHW', {
            //     method: "POST",
            //     headers: {
            //         'Content-Type': 'application/json'
            //     },
            //     body: JSON.stringify(now.id)
            // })
            // //take image respone from bufferIO
            // let image = await response2.blob()
            // //convert to base64
            // let image64 = await image.arrayBuffer()
            // //convert to base64
            // let image64base64 = await btoa(String.fromCharCode.apply(null, new Uint8Array(image64)))
            // //convert to url
            // let imageurl = `data:image/png;base64,${image64base64}`
            // //push to array
            // now.image = imageurl
            setresult(prevArray => [...prevArray, now]);
        }
    }

    let handleChangeSearch = (value) => {
        setsearch(value)
    }

    let handleSubmit = async () => {
        console.log(search)
        let response = await fetch('http://127.0.0.1:8000/organization/searchCHW', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'TOKEN ' + localStorage.getItem('token')
            },
            body: JSON.stringify({ search, organization })
        })
        let d = await response.json()
        setresult([])
        for (let i = 0; i < d.length; i++) {
            let now = d[i]
            // let response2 = await fetch('http://127.0.0.1:8000/organization/image/supervisor', {
            //     method: "POST",
            //     headers: {
            //         'Content-Type': 'application/json'
            //     },
            //     body: JSON.stringify(now.id)
            // })
            // //take image respone from bufferIO
            // let image = await response2.blob()
            // //convert to base64
            // let image64 = await image.arrayBuffer()
            // //convert to base64
            // let image64base64 = await btoa(String.fromCharCode.apply(null, new Uint8Array(image64)))
            // //convert to url
            // let imageurl = `data:image/png;base64,${image64base64}`
            // //push to array
            // now.image = imageurl
            setresult(prevArray => [...prevArray, now]);
        }
    }
    return (
        <div className="container-fluid">
            {!localStorage.getItem('token') && <Navigate to="/login" replace={true} />}
            <br />
            <br />
            <div id="wrapper">
                <div className="d-flex flex-column" id="content-wrapper">
                    <div id="content">
                        <div className="container-fluid">
                            <div className="d-sm-flex justify-content-between align-items-center mb-4"></div>
                            <div className="row">
                                <div className="col">
                                    <div className="card shadow mb-4">
                                        <div className="card-header d-flex justify-content-between align-items-center">
                                            <h6 className="text-primary fw-bold m-0">Earnings Overview</h6>                                
                                        </div>
                                        <div className="card-body">
                                            <div className="chart-area"><canvas data-bss-chart="{&quot;type&quot;:&quot;line&quot;,&quot;data&quot;:{&quot;labels&quot;:[&quot;Jan&quot;,&quot;Feb&quot;,&quot;Mar&quot;,&quot;Apr&quot;,&quot;May&quot;,&quot;Jun&quot;,&quot;Jul&quot;,&quot;Aug&quot;],&quot;datasets&quot;:[{&quot;label&quot;:&quot;Earnings&quot;,&quot;fill&quot;:true,&quot;data&quot;:[&quot;0&quot;,&quot;10000&quot;,&quot;5000&quot;,&quot;15000&quot;,&quot;10000&quot;,&quot;20000&quot;,&quot;15000&quot;,&quot;25000&quot;],&quot;backgroundColor&quot;:&quot;rgba(78, 115, 223, 0.05)&quot;,&quot;borderColor&quot;:&quot;rgba(78, 115, 223, 1)&quot;}]},&quot;options&quot;:{&quot;maintainAspectRatio&quot;:false,&quot;legend&quot;:{&quot;display&quot;:false,&quot;labels&quot;:{&quot;fontStyle&quot;:&quot;normal&quot;}},&quot;title&quot;:{&quot;fontStyle&quot;:&quot;normal&quot;},&quot;scales&quot;:{&quot;xAxes&quot;:[{&quot;gridLines&quot;:{&quot;color&quot;:&quot;rgb(234, 236, 244)&quot;,&quot;zeroLineColor&quot;:&quot;rgb(234, 236, 244)&quot;,&quot;drawBorder&quot;:false,&quot;drawTicks&quot;:false,&quot;borderDash&quot;:[&quot;2&quot;],&quot;zeroLineBorderDash&quot;:[&quot;2&quot;],&quot;drawOnChartArea&quot;:false},&quot;ticks&quot;:{&quot;fontColor&quot;:&quot;#858796&quot;,&quot;fontStyle&quot;:&quot;normal&quot;,&quot;padding&quot;:20}}],&quot;yAxes&quot;:[{&quot;gridLines&quot;:{&quot;color&quot;:&quot;rgb(234, 236, 244)&quot;,&quot;zeroLineColor&quot;:&quot;rgb(234, 236, 244)&quot;,&quot;drawBorder&quot;:false,&quot;drawTicks&quot;:false,&quot;borderDash&quot;:[&quot;2&quot;],&quot;zeroLineBorderDash&quot;:[&quot;2&quot;]},&quot;ticks&quot;:{&quot;fontColor&quot;:&quot;#858796&quot;,&quot;fontStyle&quot;:&quot;normal&quot;,&quot;padding&quot;:20}}]}}}"></canvas></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div className="row">
                                <div className="col">
                                    <div className="card shadow mb-4">
                                        <div className="card-header py-3">
                                            <h6 className="text-primary fw-bold m-0">Projects</h6>
                                        </div>
                                        <div className="card-body">
                                            <h4 className="small fw-bold">Server migration<span className="float-end">20%</span></h4>
                                            <div className="progress mb-4">
                                                <div className="progress-bar bg-danger" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style={{width: "20%"}}><span className="visually-hidden">20%</span></div>
                                            </div>
                                            <h4 className="small fw-bold">Sales tracking<span className="float-end">40%</span></h4>
                                            <div className="progress mb-4">
                                                <div className="progress-bar bg-warning" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style={{width: "40%"}}><span className="visually-hidden">40%</span></div>
                                            </div>
                                            <h4 className="small fw-bold">Customer Database<span className="float-end">60%</span></h4>
                                            <div className="progress mb-4">
                                                <div className="progress-bar bg-primary" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style={{width: "60%"}}><span className="visually-hidden">60%</span></div>
                                            </div>
                                            <h4 className="small fw-bold">Payout Details<span className="float-end">80%</span></h4>
                                            <div className="progress mb-4">
                                                <div className="progress-bar bg-info" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style={{width: "80%"}}><span className="visually-hidden">80%</span></div>
                                            </div>
                                            <h4 className="small fw-bold">Account setup<span className="float-end">Complete!</span></h4>
                                            <div className="progress mb-4">
                                                <div className="progress-bar bg-success" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style={{width: "100%"}}><span className="visually-hidden">100%</span></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div className="col">
                                    <div className="card shadow mb-4">
                                        <div className="card-header d-flex justify-content-between align-items-center">
                                            <h6 className="text-primary fw-bold m-0">Revenue Sources</h6>                                        
                                        </div>
                                        <div className="card-body">
                                            <div className="chart-area"><canvas data-bss-chart="{&quot;type&quot;:&quot;doughnut&quot;,&quot;data&quot;:{&quot;labels&quot;:[&quot;Direct&quot;,&quot;Social&quot;,&quot;Referral&quot;],&quot;datasets&quot;:[{&quot;label&quot;:&quot;&quot;,&quot;backgroundColor&quot;:[&quot;#4e73df&quot;,&quot;#1cc88a&quot;,&quot;#36b9cc&quot;],&quot;borderColor&quot;:[&quot;#ffffff&quot;,&quot;#ffffff&quot;,&quot;#ffffff&quot;],&quot;data&quot;:[&quot;50&quot;,&quot;30&quot;,&quot;15&quot;]}]},&quot;options&quot;:{&quot;maintainAspectRatio&quot;:false,&quot;legend&quot;:{&quot;display&quot;:false,&quot;labels&quot;:{&quot;fontStyle&quot;:&quot;normal&quot;}},&quot;title&quot;:{&quot;fontStyle&quot;:&quot;normal&quot;}}}"></canvas></div>
                                            <div className="text-center small mt-4"><span className="me-2"><i className="fas fa-circle text-primary"></i>&nbsp;Direct</span><span className="me-2"><i className="fas fa-circle text-success"></i>&nbsp;Social</span><span className="me-2"><i className="fas fa-circle text-info"></i>&nbsp;Refferal</span></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><a className="border rounded d-inline scroll-to-top" href="#page-top"><i className="fas fa-angle-up"></i></a>
            </div>
            <br />
            <br />
        </div>
    );
}

export default Statistics;