import Head from 'next/head';

export default function Notifications() {
    return (
        <div>
            <Head>
                <title>Notifications</title>
                <meta name="description" content="View your notifications." />
            </Head>
            <main>
                <h1>Notifications</h1>
                <p>Here you can view your notifications for upcoming deadlines.</p>
                {/* Display notifications here */}
            </main>
        </div>
    );
}