import React from 'react';
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import Welcome from './Welcome';
import Home from './Home';
// import NotFound from './NotFound';


const Routes = () => (
<Router >
    <Switch>
    <Route exact path="/" component={Welcome}/>
    <Route path="/home" component={Home}/>
    {/* <Route path="*" component={NotFound}/> */}
   </Switch>
</Router>
);
export default Routes;