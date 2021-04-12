
import React from 'react';
import PropTypes from 'prop-types';
import Addbar from './addbar';
import Addbar_1 from './addbar_1';
class App extends React.Component {
  /* Display number of likes and like/unlike button for one post
   * Reference on forms https://facebook.github.io/react/docs/forms.html
   */
    constructor(props){
        super(props);
        this.state = {
          ingredients: [],
          restrictions: [],
          recipelist: []
        }
        this.getRecipe = this.getRecipe.bind(this);
    }

    componentWillMount() {
    this.initialState = this.state
    }

    handleCallback1 = (childData) =>{
      this.setState({ingredients: childData });
    }

    handleCallback2 = (childData) =>{
      this.setState({restrictions: childData });
    }
    
    doreset = () => {
      console.log("IN reset");
      this.setState(this.initialState);
    }



    getRecipe(){
      const { ingredients }  = this.state
      const {restrictions} = this.state
      let url = window.location.href;   
      if(ingredients.length != 0){
        let urlapi = url + `api/i?ingredients=${encodeURIComponent(ingredients.join(','))}&restrictions=${encodeURIComponent(restrictions.join(','))}`;

        //i?ingredients=${encodeURIComponent(ingredients.join(','))}

        console.log("urlapi = ", urlapi)

        fetch(urlapi, { credentials: 'same-origin' })
        .then((response) => {
        if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .then((data) => {
        this.setState({
          recipelist: data["recipe"]
        })
        console.log(this.state.recipelist);
        })
        .catch((error) => console.log(error));
    }
      else{
        console.log("No ingredients");
      }
    }

  render() {
    // This line automatically assigns this.state.numLikes to the const variable numLikes
    // Render number of likes
    const { recipelist } = this.state;
    return (
    //call addbar


        <div>
            <Addbar id = "ingredients_bar" key = "1" parentCallback = {this.handleCallback1} />
            <Addbar_1 id = "restriction_bar" key = "2" parentCallback = {this.handleCallback2} />

                <button className = 'submit-reset-button' type = "button" value ="Submit" onClick = {this.getRecipe}>Search</button>
                <button className = 'submit-reset-button' type = "button" value ="Reset" onClick = {this.doreset}>Reset</button>
                
                <br></br>
                <br></br>
                <br></br>
            {recipelist.map((recipe, index) => (
              <div key ={index.toString()} clas sName = "recipe">
              <b>Recipe: {index + 1}</b>
                <p id="recipeName"classkey = "rname">{recipe["recipe_name"]}</p>
                <p id="prepTime">Preparation time: {recipe["prep_time"]} minutes</p>
                <p id="cookingTime">Cooking time: {recipe["cooking_time"]} minutes</p>


                <p>Ingredients: </p>
                {(recipe["ingredients"]).split(';').map((ingr, ind)=>(

                   <li key = {index.toString()} >{ingr}</li>

                  ))}


                <p>Instruction:  </p>
                {(recipe["instruction"]).split(';').map((instr, ind)=>(

                  <li key = {index.toString()} >{instr}</li>

                ))}
                <br></br>
                <br></br>
                <br></br>
              </div>
            ))}
              
        </div>
    );
  }
}


export default App;
