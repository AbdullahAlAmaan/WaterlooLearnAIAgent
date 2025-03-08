const QuizCard = ({ quiz }) => {
    return (
        <div className="quiz-card">
            <h2>{quiz.title}</h2>
            <p>Due Date: {quiz.due_date}</p>
            <button>Take Quiz</button>
        </div>
    );
};

export default QuizCard;