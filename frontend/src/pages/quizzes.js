import Head from 'next/head';
import QuizCard from '../components/QuizCard';

export default function Quizzes({ quizzes }) {
    return (
        <div>
            <Head>
                <title>Quizzes</title>
                <meta name="description" content="List of quizzes." />
            </Head>
            <main>
                <h1>Quizzes</h1>
                <p>Here you can view and take your quizzes.</p>
                <div>
                    {quizzes.map(quiz => (
                        <QuizCard key={quiz.id} quiz={quiz} />
                    ))}
                </div>
            </main>
        </div>
    );
}

// Fetch quizzes from the backend
export async function getStaticProps() {
    const res = await fetch('http://localhost:5000/api/quizzes');

    if (!res.ok) {
        console.error('Failed to fetch quizzes:', res.status, res.statusText);
        return {
            props: {
                quizzes: [],
            },
        };
    }

    const text = await res.text(); // Get the response as text
    console.log('Response text:', text); // Log the response text

    const quizzes = JSON.parse(text); // Parse the text as JSON

    return {
        props: {
            quizzes,
        },
    };
}