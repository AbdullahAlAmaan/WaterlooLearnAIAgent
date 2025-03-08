import Head from 'next/head';
import CourseCard from '../components/CourseCard';
import styles from '../styles/Courses.module.css'; // Import CSS module for styling

export default function Courses({ courses }) {
    return (
        <div className={styles.container}>
            <Head>
                <title>Courses</title>
                <meta name="description" content="List of courses." />
            </Head>
            <main className={styles.main}>
                <h1 className={styles.title}>Courses</h1>
                <p className={styles.description}>Here you can view and manage your courses.</p>
                <div className={styles.courseGrid}>
                    {courses.map(course => (
                        <CourseCard key={course.id} course={course} />
                    ))}
                </div>
            </main>
        </div>
    );
}

// Fetch courses from the backend
export async function getStaticProps() {
    const res = await fetch('http://localhost:5000/api/courses'); // Correct endpoint for courses

    if (!res.ok) {
        console.error('Failed to fetch courses:', res.status, res.statusText);
        return {
            props: {
                courses: [], // Return an empty array if fetching fails
            },
        };
    }

    const courses = await res.json(); // Parse the response as JSON

    return {
        props: {
            courses, // Return the courses data
        },
    };
}