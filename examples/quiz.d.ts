type Quizz = {
    language: string,
    title: string,
    questions: Question[]
}

type Component = Component[] | {
    text: string | string[],
    type?: "normal" | "italic" | "bold" | "underlined" | "strikethrough" | "inline-code" | "block-code" | "math"
}

type Question = ChoiceQuestion | TrueFalseQuestion | ShortAnswerQuestion;

// ---------------------------------

type ChoiceQuestion = {
    questionType: "single-choice" | "multiple-choice",
    prompt: Component,
    answers: { 
        content: Component,
        correct?: boolean
    }[]
}

type TrueFalseQuestion = {
    questionType: "true-or-false",
    prompt: Component,
    correct: boolean
}

type ShortAnswerQuestion = {
    questionType: "short-answer",
    prompt: Component,
    correct: string
}
