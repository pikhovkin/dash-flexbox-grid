import React, {Component} from 'react';
import {Grid, Row, Col} from '../src';


class Demo extends Component {
    constructor() {
        super();
        this.state = {
            value: ''
        }
    }

    render() {
        return (
            <div>
                <h1>dash-flexbox-grid Demo</h1>

                <hr/>
                <h2>Grid, Row, Col</h2>
                <Grid fluid>
                    <Row>
                        <Col xs={6} md={3}>
                            Hello, world!
                        </Col>
                    </Row>
                </Grid>
                <hr/>
            </div>
        );
    }
}

export default Demo;
