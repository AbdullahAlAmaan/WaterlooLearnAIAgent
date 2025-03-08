import Head from 'next/head';

export default function Assignments() {
    return (
        <div>
            <Head>
                <title>Assignments</title>
                <meta name="description" content="Submit your assignments." />
            </Head>
            <main>
                <h1>Assignments</h1>
                <p>Here you can submit your assignments.</p>
                {/* Add form for submitting assignments */}
            </main>
        </div>
    );
}