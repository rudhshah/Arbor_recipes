
import React from 'react';
import PropTypes from 'prop-types';


class Recipe extends React.Component {
  /* Display number of likes and like/unlike button for one post
   * Reference on forms https://facebook.github.io/react/docs/forms.html
   */

  constructor(props) {
    // Initialize mutable state
    super(props);

  }

  render() {
    // This line automatically assigns this.state.numLikes to the const variable numLikes
    // Render number of likes
    return (
      <div >
        <p>
            Hello world 
        </p>
      </div>
    );
  }
}


export default Recipe;
  