import styles from '../styles/CourseCard.module.css'; // Import CSS module for styling

const CourseCard = ({ course }) => {
    return (
        <div className={styles.card}>
            <h2 className={styles.courseTitle}>{course.name}</h2>
            <p className={styles.courseCode}>Course Code: {course.code}</p>
            <p className={styles.courseDescription}>{course.description}</p>
            <button className={styles.manageButton}>Manage Course</button>
        </div>
    );
};

export default CourseCard;