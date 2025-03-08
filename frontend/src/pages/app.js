import '../styles/globals.css'; // Import global styles
import Header from '../components/Header'; // Import the Header component

function MyApp({ Component, pageProps }) {
    return (
        <>
            <Header />
            <Component {...pageProps} />
        </>
    );
}

export default MyApp;