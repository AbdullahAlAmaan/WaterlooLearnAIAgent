/* src/styles/Courses.module.css */
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    padding: 20px;
    background-color: #f9f9f9;
}

.main {
    text-align: center;
    max-width: 800px;
    margin: 0 auto;
}

.title {
    font-size: 2.5rem;
    color: #333;
    margin-bottom: 10px;
}

.description {
    font-size: 1.2rem;
    color: #666;
    margin-bottom: 20px;
}

.courseGrid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    width: 100%;
}
