import Head from 'next/head';
import Link from 'next/link';
import styles from '../styles/Home.module.css'; // Import CSS module for styling

export default function Home() {
    return (
        <div className={styles.container}>
            <Head>
                <title>Learn Calendar Assistant</title>
                <meta name="description" content="A tool to manage your courses and assignments." />
            </Head>
            <main className={styles.main}>
                <h1 className={styles.title}>Welcome to the Learn Calendar Assistant</h1>
                <p className={styles.description}>Your one-stop solution for managing courses, quizzes, and assignments.</p>
                <nav>
                    <ul className={styles.navList}>
                        <li>
                            <Link href="/courses" className={styles.navLink}>View Courses</Link>
                        </li>
                        <li>
                            <Link href="/quizzes" className={styles.navLink}>Take Quizzes</Link>
                        </li>
                        <li>
                            <Link href="/assignments" className={styles.navLink}>Submit Assignments</Link>
                        </li>
                        <li>
                            <Link href="/notifications" className={styles.navLink}>View Notifications</Link>
                        </li>
                    </ul>
                </nav>
            </main>
        </div>
    );
}