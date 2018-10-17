/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import {Grid, Row, Col} from '../lib';

class App extends Component {

    constructor() {
        super();

        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <div>
                <Grid fluid>
                    <Row>
                        <Col xs={6} md={3}>
                            Hello, world!
                        </Col>
                    </Row>
                </Grid>
            </div>
        )
    }
}

export default App;
