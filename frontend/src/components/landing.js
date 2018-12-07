import React, {Component} from 'react'
import {Avatar} from 'evergreen-ui'
import '../styles/styles.css'

class landing extends Component {

    redirect(url) {
        window.location.replace(url)
    }

    render() {
        return (
            <div className={'apps'}>
                <h1>Apps that we offer:</h1>
                <a href = {'https://limitless-citadel-11410.herokuapp.com/'}>
                    <Avatar
                        size={150}
                        src={'https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Tic_tac_toe.svg/300px-Tic_tac_toe.svg.png'}
                    />
                    </a>
                <a href= {'https://infinite-tor-85455.herokuapp.com/'}>
                <Avatar
                    size={150}

                    src={'https://quizlet.com/a/i/brandmark/1024.TGu7.png'}
                />
                </a>
                <a href= {'https://infinite-tor-85455.herokuapp.com/'}>
                <Avatar
                    size={150}

                    src={'https://gamesrob.com/res/hangman.png'}
                />
                    </a>
            </div>
        );
    }
}

export default landing;