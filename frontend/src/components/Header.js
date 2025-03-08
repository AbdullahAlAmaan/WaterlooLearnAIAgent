import Link from 'next/link';

const Header = () => {
    return (
        <header>
            <nav>
                <ul>
                    <li>
                        <Link href="/">Home</Link>
                    </li>
                    <li>
                        <Link href="/courses">Courses</Link>
                    </li>
                    <li>
                        <Link href="/quizzes">Quizzes</Link>
                    </li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;